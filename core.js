/* Núcleo sem dependência de DOM: eventos imutáveis, diagnóstico e backup. */
(function(root){'use strict';
const C=root.JarvisContent||(typeof require!=='undefined'?require('./content.js'):null);
const allLessons=C.allLessons||C.lessons;
const lessonMap=new Map(allLessons.map(l=>[l.id,l]));
const questionMap=new Map(allLessons.flatMap(l=>l.questions.map(q=>[q.id,{...q,topic:l.id}])));
const ROUND_SIZE=4;
const KEY='jarvis.estudante.v1',DRAFT='jarvis.estudante.draft.v1';
const uid=()=>globalThis.crypto?.randomUUID?.()||('j-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2));
const fresh=()=>({schema:1,created:new Date().toISOString(),events:[],prefs:{name:'',theme:'dark',font:16,goal:30},revision:0});
const ev=(type,payload={},cycle='inicial')=>({id:uid(),at:new Date().toISOString(),type,cycle,...payload});
const types=new Set(['read','attempt','note','evidence','session','cycle','review','coverage','diagnosis','rubric','gap','audit','sim-evaluation']);
function validate(v){
 if(!v||v.schema!==1||!Array.isArray(v.events)||v.events.length>100000)throw Error('Formato de backup incompatível.');
 const ids=new Set();for(const e of v.events){if(!e||typeof e.id!=='string'||ids.has(e.id)||!types.has(e.type)||!Number.isFinite(Date.parse(e.at))||typeof e.cycle!=='string')throw Error('Histórico inválido ou duplicado.');ids.add(e.id);
 if(['read','attempt','note','evidence','review','gap','audit'].includes(e.type)&&!lessonMap.has(e.topic))throw Error('Assunto desconhecido no backup.');
 if(e.type==='attempt'&&(!questionMap.has(e.qid)||![true,false,null].includes(e.answer)||!['seguro','duvida','chute'].includes(e.confidence)))throw Error('Resposta inválida.');
 if(e.type==='attempt'&&questionMap.get(e.qid).topic!==e.topic)throw Error('Resposta vinculada ao tópico errado.');
 if(e.type==='attempt'&&e.questionSnapshot){const q=e.questionSnapshot;if(q.id!==e.qid||typeof q.answer!=='boolean'||!['text','explanation'].every(k=>typeof q[k]==='string'&&q[k].length<=20000)||!Number.isInteger(q.version)||q.version<1)throw Error('Versão histórica da questão inválida.');}
 if(e.type==='cycle'&&typeof e.next!=='string')throw Error('Ciclo inválido.');
 if(e.type==='evidence'&&(!Array.isArray(e.checks)||e.checks.length!==4||!e.checks.every(x=>typeof x==='boolean')))throw Error('Evidências inválidas.');
 if(e.type==='session'&&(!Number.isFinite(e.seconds)||e.seconds<0||typeof e.title!=='string'))throw Error('Sessão inválida.');
 if(e.type==='coverage'&&(typeof e.item!=='string'||typeof e.done!=='boolean'))throw Error('Registro de aprofundamento inválido.');
 if(e.type==='attempt'&&(typeof e.round!=='string'||typeof e.reason!=='string'||typeof e.cause!=='string'))throw Error('Diagnóstico inválido.');
 if(e.type==='diagnosis'&&(typeof e.attempt!=='string'||typeof e.cause!=='string'))throw Error('Diagnóstico inválido.');
 if(e.type==='rubric'&&(typeof e.attempt!=='string'||!Array.isArray(e.checks)||e.checks.length!==4||!e.checks.every(v=>typeof v==='boolean')))throw Error('Rubrica inválida.');
 if(e.type==='gap'&&(typeof e.key!=='string'||typeof e.open!=='boolean'||typeof e.text!=='string'))throw Error('Lacuna inválida.');
 if(e.type==='audit'&&(!C.realIndex?.some(r=>r.id===e.ref)||!['ensinada','parcial','lacuna'].includes(e.coverage)||typeof e.reason!=='string'||![true,false,null].includes(e.answer)))throw Error('Auditoria de questão real inválida.');
 if(e.type==='sim-evaluation'&&(typeof e.session!=='string'||![1,2,3,4,5].includes(e.fatigue)||![1,2,3,4,5].includes(e.concentration)))throw Error('Análise de simulado inválida.');
 if(e.type==='note'&&typeof e.text!=='string')throw Error('Nota inválida.');
 }
 const p=v.prefs||{};return{schema:1,created:typeof v.created==='string'?v.created:new Date().toISOString(),events:JSON.parse(JSON.stringify(v.events)),prefs:{name:String(p.name||'').slice(0,80),theme:p.theme==='light'?'light':'dark',font:[16,18,20].includes(p.font)?p.font:16,goal:[15,30,45,60,90].includes(p.goal)?p.goal:30},revision:Number(v.revision)||0};
}
function merge(a,b){const map=new Map(a.events.map(e=>[e.id,e]));for(const e of b.events)if(!map.has(e.id))map.set(e.id,e);return{...a,events:[...map.values()].sort((x,y)=>x.at.localeCompare(y.at)||x.id.localeCompare(y.id)),revision:Math.max(a.revision,b.revision)+1};}
function cycle(db){return db.events.filter(e=>e.type==='cycle').at(-1)?.next||'inicial';}
function active(db){return db.events.filter(e=>e.cycle===cycle(db));}
function needsNewCurriculumCycle(db,hasDraft=false){const es=active(db);return C.version>=2&&!hasDraft&&es.some(e=>lessonMap.get(e.topic)?.legacy&&!e.methodVersion)&&!es.some(e=>lessonMap.get(e.topic)?.planId);}
function question(id,attempt=null){return attempt?.questionSnapshot||questionMap.get(id);}
function stats(db,topic){const es=active(db),ats=es.filter(e=>e.type==='attempt'&&(!topic||e.topic===topic));const answered=ats.filter(e=>e.answer!==null);const right=answered.filter(e=>question(e.qid,e)?.answer===e.answer);return{total:ats.length,answered:answered.length,right:right.length,wrong:answered.length-right.length,blank:ats.length-answered.length,accuracy:ats.length?Math.round(right.length/ats.length*100):0,attempts:ats};}
function gaps(db,id){const map=new Map();for(const e of active(db).filter(e=>e.type==='gap'&&(!id||e.topic===id)))map.set(e.key,e);return [...map.values()].filter(e=>e.open);}
function topicState(db,id){const es=active(db).filter(e=>e.topic===id),s=stats(db,id),l=lessonMap.get(id);const seen=es.some(e=>e.type==='read');const evidence=es.filter(e=>e.type==='evidence').at(-1)?.checks||[false,false,false,false];const rubrics=new Map(active(db).filter(e=>e.type==='rubric').map(e=>[e.attempt,e.checks]));const legacy=l?.legacy||!l?.planId;
 const secure=s.attempts.filter(e=>question(e.qid,e)?.answer===e.answer&&e.confidence==='seguro'&&(legacy?e.reason.trim().length>=20:rubrics.get(e.id)?.every(Boolean)));
 const unique=new Set(secure.map(e=>e.qid)).size,rounds=new Set(secure.map(e=>e.round)).size;
 const coverage=(l?.subtopics||[]).map((_,i)=>active(db).filter(e=>e.type==='coverage'&&e.item===id+':sub:'+i).at(-1)?.done===true);
 const covered=legacy||coverage.length>0&&coverage.every(Boolean),openGaps=gaps(db,id);
 const required=legacy?4:Math.min(8,l?.questions.filter(q=>q.mode!=='reserva').length||4);
 const eligible=seen&&unique>=required&&rounds>=2&&s.accuracy>=80&&covered&&!openGaps.length;const mastered=eligible&&evidence.every(Boolean);
 return{...s,seen,evidence,eligible,mastered,status:mastered?'dominado':s.total?'consolidacao':seen?'visto':'novo',unique,rounds,required,coverage,covered,openGaps};}
function errors(db){const map=new Map();for(const e of active(db).filter(x=>x.type==='attempt')){const q=question(e.qid,e);if(e.answer!==q?.answer)map.set(e.qid,{...e,resolved:false});else if(map.has(e.qid)&&e.confidence==='seguro')map.get(e.qid).resolved=true;}return [...map.values()].reverse();}
function dueDate(db,id){const es=active(db).filter(e=>e.topic===id),last=es.filter(e=>['attempt','review'].includes(e.type)).at(-1);if(!last)return null;const rounds=new Set(es.filter(e=>e.type==='attempt').map(e=>e.round)).size;const st=stats(db,id),days=st.accuracy<70?1:rounds<2?1:rounds<3?3:rounds<5?7:14;return new Date(Date.parse(last.at)+days*86400000);}
function recommend(db,now=new Date()){const pending=gaps(db).find(g=>C.lessons.some(l=>l.id===g.topic));if(pending)return{lesson:lessonMap.get(pending.topic),reason:'Ensine e recupere a lacuna registrada antes de avançar.',mode:'recover'};const due=C.lessons.filter(l=>{const d=dueDate(db,l.id);return d&&d<=now;});if(due.length)return{lesson:due.sort((a,b)=>dueDate(db,a.id)-dueDate(db,b.id))[0],reason:'Revisão vencida: recupere antes de avançar.',mode:'review'};
 const es=active(db),recent=es.filter(e=>e.type==='session').slice(-3);const lastTopics=recent.map(e=>C.lessons.find(l=>l.id===e.topic)?.d);const weak=C.lessons.filter(l=>{const s=topicState(db,l.id);return s.total&&s.accuracy<70&&!s.mastered;});if(weak.length)return{lesson:weak.sort((a,b)=>stats(db,a.id).accuracy-stats(db,b.id).accuracy)[0],reason:'Recuperação: há dificuldade registrada neste assunto.',mode:'recover'};
 let d='prev';if(lastTopics.length&&lastTopics.at(-1)==='prev')d='const';else if(lastTopics.length>=2&&lastTopics.at(-2)==='prev'&&lastTopics.at(-1)==='const'){const order=['port','adm','rlm','info','etica'];d=order[Math.floor(es.filter(e=>e.type==='session').length/3)%order.length];}
 const pool=C.lessons.filter(l=>l.d===d),next=pool.find(l=>topicState(db,l.id).seen&&!topicState(db,l.id).mastered)||pool.find(l=>topicState(db,l.id).status==='novo')||C.lessons.find(l=>!topicState(db,l.id).mastered)||C.lessons[0];return{lesson:next,reason:d==='prev'?'Prioridade máxima: construa sua base previdenciária.':d==='const'?'Reforço estratégico: mantenha Constitucional no ciclo.':'Equilibre o ciclo sem abandonar as outras disciplinas.',mode:'learn'};
}
function pick(db,ids,count,random=Math.random,mode='learn'){const last=new Map();for(const e of active(db).filter(e=>e.type==='attempt'))last.set(e.qid,e.at);const pool=allLessons.filter(l=>ids.includes(l.id)).flatMap(l=>l.questions.filter(q=>mode==='sim'||q.mode!=='reserva'||last.has(q.id)).map(q=>({...q,topic:l.id})));const scores=new Map(pool.map(q=>[q.id,random()]));const level=new Map(ids.map(id=>[id,stats(db,id).total<4?0:stats(db,id).accuracy<70?0:stats(db,id).total<8?1:2]));const rank=q=>Math.abs(({'basico':0,'intermediario':1,'avancado':2}[q.difficulty]||0)-(level.get(q.topic)||0));pool.sort((a,b)=>{const x=last.get(a.id),y=last.get(b.id);if(!x&&y)return -1;if(x&&!y)return 1;if(mode!=='sim'&&rank(a)!==rank(b))return rank(a)-rank(b);return !x&&!y?scores.get(a.id)-scores.get(b.id):x.localeCompare(y)||scores.get(a.id)-scores.get(b.id);});return pool.slice(0,count);}
function simPlan(db){const es=active(db),last=es.filter(e=>e.type==='session'&&e.mode==='sim').at(-1);if(!last)return{count:40,reason:'Comece com até 40 itens inéditos elegíveis; use diagnóstico menor se o banco estudado não permitir.'};const ats=es.filter(e=>e.type==='attempt'&&e.round===last.round),right=ats.filter(e=>question(e.qid,e).answer===e.answer).length,review=es.filter(e=>e.type==='sim-evaluation'&&e.session===last.id).at(-1),base=Math.max(40,Math.min(120,Math.floor(ats.length/10)*10));const advance=ats.length>=40&&right/ats.length>=.8&&review?.fatigue<=2&&review?.concentration>=4;return{count:advance?Math.min(120,base+10):base,reason:advance?'Desempenho e autoavaliação permitem experimentar mais 10 itens. Aumento opcional.':'Mantenha o volume e recupere os pontos frágeis. Registre fadiga e concentração após o simulado.'};}
const weekly=[['Segunda','Previdenciário — aprender','Português'],['Terça','Administrativo','Previdenciário — consolidar'],['Quarta','Raciocínio Lógico','Previdenciário — aplicar'],['Quinta','Constitucional','Administrativo'],['Sexta','Português','Informática e Ética'],['Sábado','Simulado cumulativo','Análise e planejamento'],['Domingo','Descanso','Recuperação']];
function summary(db){const s=stats(db),next=recommend(db);return{methodVersion:'1.7',contentVersion:C.version,cycle:cycle(db),at:new Date().toISOString(),sessions:active(db).filter(e=>e.type==='session').length,answered:s.answered,right:s.right,wrong:s.wrong,seen:C.lessons.filter(l=>topicState(db,l.id).seen).map(l=>l.id),mastered:C.lessons.filter(l=>topicState(db,l.id).mastered).map(l=>l.id),gaps:gaps(db).map(g=>({topic:g.topic,text:g.text})),next:{topic:next.lesson.id,reason:next.reason}};}
class Store{
 constructor(storage){this.storage=storage;this.error=null;this.db=fresh();try{const raw=storage?.getItem(KEY);this.originalRaw=raw;if(raw)this.db=validate(JSON.parse(raw));}catch(e){this.error='Não foi possível ler os dados. O conteúdo original foi preservado; exporte antes de continuar.';this.readBlocked=true;}}
 async commit(events=[],prefs=null){const run=()=>{if(this.readBlocked)throw Error(this.error);let latest=fresh();const raw=this.storage?.getItem(KEY);if(raw)latest=validate(JSON.parse(raw));const combined=merge(latest,this.db);combined.events=merge(combined,{events,revision:combined.revision}).events;if(prefs)combined.prefs={...this.db.prefs,...prefs};else combined.prefs=this.db.prefs;combined.revision++;
 this.db=combined;try{if(!this.storage)throw Error('Armazenamento indisponível');this.storage.setItem(KEY,JSON.stringify(combined));this.error=null;}catch(e){this.error='Não foi possível salvar neste navegador. Exporte seu backup agora.';throw Error(this.error);}return combined;};
 if(globalThis.navigator?.locks)return navigator.locks.request(KEY,async()=>run());return run();}
 async restore(v){const parsed=validate(v);return this.commit(parsed.events);}
 export(){if(this.readBlocked&&this.originalRaw)return this.originalRaw;return JSON.stringify({...this.db,exportedAt:new Date().toISOString(),app:'JARVIS Estudante'},null,2);}
}
const api={C,KEY,DRAFT,ROUND_SIZE,weekly,lessonMap,questionMap,uid,ev,fresh,validate,merge,cycle,active,needsNewCurriculumCycle,question,stats,topicState,errors,gaps,dueDate,recommend,pick,simPlan,summary,Store};root.Jarvis=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
