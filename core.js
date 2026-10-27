/* Núcleo sem dependência de DOM: eventos imutáveis, diagnóstico e backup. */
(function(root){'use strict';
const C=root.JarvisContent||(typeof require!=='undefined'?require('./content.js'):null);
const KEY='jarvis.estudante.v1',DRAFT='jarvis.estudante.draft.v1';
const uid=()=>globalThis.crypto?.randomUUID?.()||('j-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2));
const fresh=()=>({schema:1,created:new Date().toISOString(),events:[],prefs:{name:'',theme:'dark',font:16,goal:30},revision:0});
const ev=(type,payload={},cycle='inicial')=>({id:uid(),at:new Date().toISOString(),type,cycle,...payload});
const types=new Set(['read','attempt','note','evidence','session','cycle','review','coverage','diagnosis']);
function validate(v){
 if(!v||v.schema!==1||!Array.isArray(v.events)||v.events.length>20000)throw Error('Formato de backup incompatível.');
 const ids=new Set();for(const e of v.events){if(!e||typeof e.id!=='string'||ids.has(e.id)||!types.has(e.type)||!Number.isFinite(Date.parse(e.at))||typeof e.cycle!=='string')throw Error('Histórico inválido ou duplicado.');ids.add(e.id);
 if(['read','attempt','note','evidence','review'].includes(e.type)&&!C.lessons.some(l=>l.id===e.topic))throw Error('Assunto desconhecido no backup.');
 if(e.type==='attempt'&&(!C.lessons.some(l=>l.questions.some(q=>q.id===e.qid))||![true,false,null].includes(e.answer)||!['seguro','duvida','chute'].includes(e.confidence)))throw Error('Resposta inválida.');
 if(e.type==='attempt'&&!C.lessons.find(l=>l.id===e.topic).questions.some(q=>q.id===e.qid))throw Error('Resposta vinculada ao tópico errado.');
 if(e.type==='cycle'&&typeof e.next!=='string')throw Error('Ciclo inválido.');
 if(e.type==='evidence'&&(!Array.isArray(e.checks)||e.checks.length!==4||!e.checks.every(x=>typeof x==='boolean')))throw Error('Evidências inválidas.');
 if(e.type==='session'&&(!Number.isFinite(e.seconds)||e.seconds<0||typeof e.title!=='string'))throw Error('Sessão inválida.');
 if(e.type==='coverage'&&(typeof e.item!=='string'||typeof e.done!=='boolean'))throw Error('Registro de aprofundamento inválido.');
 if(e.type==='attempt'&&(typeof e.round!=='string'||typeof e.reason!=='string'||typeof e.cause!=='string'))throw Error('Diagnóstico inválido.');
 if(e.type==='diagnosis'&&(typeof e.attempt!=='string'||typeof e.cause!=='string'))throw Error('Diagnóstico inválido.');
 if(e.type==='note'&&typeof e.text!=='string')throw Error('Nota inválida.');
 }
 const p=v.prefs||{};return{schema:1,created:typeof v.created==='string'?v.created:new Date().toISOString(),events:JSON.parse(JSON.stringify(v.events)),prefs:{name:String(p.name||'').slice(0,80),theme:p.theme==='light'?'light':'dark',font:[16,18,20].includes(p.font)?p.font:16,goal:[15,30,45,60,90].includes(p.goal)?p.goal:30},revision:Number(v.revision)||0};
}
function merge(a,b){const map=new Map(a.events.map(e=>[e.id,e]));for(const e of b.events)if(!map.has(e.id))map.set(e.id,e);return{...a,events:[...map.values()].sort((x,y)=>x.at.localeCompare(y.at)||x.id.localeCompare(y.id)),revision:Math.max(a.revision,b.revision)+1};}
function cycle(db){return db.events.filter(e=>e.type==='cycle').at(-1)?.next||'inicial';}
function active(db){return db.events.filter(e=>e.cycle===cycle(db));}
function question(id){return C.lessons.flatMap(l=>l.questions).find(q=>q.id===id);}
function stats(db,topic){const es=active(db),ats=es.filter(e=>e.type==='attempt'&&(!topic||e.topic===topic));const answered=ats.filter(e=>e.answer!==null);const right=answered.filter(e=>question(e.qid)?.answer===e.answer);return{total:ats.length,answered:answered.length,right:right.length,wrong:answered.length-right.length,blank:ats.length-answered.length,accuracy:ats.length?Math.round(right.length/ats.length*100):0,attempts:ats};}
function topicState(db,id){const es=active(db).filter(e=>e.topic===id),s=stats(db,id);const seen=es.some(e=>e.type==='read');const evidence=es.filter(e=>e.type==='evidence').at(-1)?.checks||[false,false,false,false];const secure=s.attempts.filter(e=>question(e.qid)?.answer===e.answer&&e.confidence==='seguro'&&e.reason.trim().length>=20);const unique=new Set(secure.map(e=>e.qid)).size,rounds=new Set(secure.map(e=>e.round)).size;
 const eligible=seen&&unique>=4&&rounds>=2&&s.accuracy>=80;const mastered=eligible&&evidence.every(Boolean);
 return{...s,seen,evidence,eligible,mastered,status:mastered?'dominado':s.total?'consolidacao':seen?'visto':'novo',unique,rounds};}
function errors(db){const map=new Map();for(const e of active(db).filter(x=>x.type==='attempt')){const q=question(e.qid);if(e.answer!==q?.answer)map.set(e.qid,{...e,resolved:false});else if(map.has(e.qid)&&e.confidence==='seguro')map.get(e.qid).resolved=true;}return [...map.values()].reverse();}
function dueDate(db,id){const es=active(db).filter(e=>e.topic===id),last=es.filter(e=>['attempt','review'].includes(e.type)).at(-1);if(!last)return null;const rounds=new Set(es.filter(e=>e.type==='attempt').map(e=>e.round)).size;const st=stats(db,id),days=st.accuracy<70?1:rounds<2?1:rounds<3?3:rounds<5?7:14;return new Date(Date.parse(last.at)+days*86400000);}
function recommend(db,now=new Date()){const due=C.lessons.filter(l=>{const d=dueDate(db,l.id);return d&&d<=now;});if(due.length)return{lesson:due.sort((a,b)=>dueDate(db,a.id)-dueDate(db,b.id))[0],reason:'Revisão vencida: recupere antes de avançar.',mode:'review'};
 const es=active(db),recent=es.filter(e=>e.type==='session').slice(-3);const lastTopics=recent.map(e=>C.lessons.find(l=>l.id===e.topic)?.d);const weak=C.lessons.filter(l=>{const s=topicState(db,l.id);return s.total&&s.accuracy<70&&!s.mastered;});if(weak.length)return{lesson:weak.sort((a,b)=>stats(db,a.id).accuracy-stats(db,b.id).accuracy)[0],reason:'Recuperação: há dificuldade registrada neste assunto.',mode:'recover'};
 let d='prev';if(lastTopics.length&&lastTopics.at(-1)==='prev')d='const';else if(lastTopics.length>=2&&lastTopics.at(-2)==='prev'&&lastTopics.at(-1)==='const'){const order=['port','adm','rlm','info','etica'];d=order[Math.floor(es.filter(e=>e.type==='session').length/3)%order.length];}
 const pool=C.lessons.filter(l=>l.d===d),next=pool.find(l=>topicState(db,l.id).status==='novo')||pool.find(l=>!topicState(db,l.id).mastered)||C.lessons.find(l=>!topicState(db,l.id).mastered)||C.lessons[0];return{lesson:next,reason:d==='prev'?'Prioridade máxima: construa sua base previdenciária.':d==='const'?'Reforço estratégico: mantenha Constitucional no ciclo.':'Equilibre o ciclo sem abandonar as outras disciplinas.',mode:'learn'};
}
function pick(db,ids,count,random=Math.random){const pool=C.lessons.filter(l=>ids.includes(l.id)).flatMap(l=>l.questions.map(q=>({...q,topic:l.id})));const last=new Map();for(const e of active(db).filter(e=>e.type==='attempt'))last.set(e.qid,e.at);const scores=new Map(pool.map(q=>[q.id,random()]));pool.sort((a,b)=>{const x=last.get(a.id),y=last.get(b.id);return !x&&!y?scores.get(a.id)-scores.get(b.id):!x?-1:!y?1:x.localeCompare(y)||scores.get(a.id)-scores.get(b.id);});return pool.slice(0,count);}
class Store{
 constructor(storage){this.storage=storage;this.error=null;this.db=fresh();try{const raw=storage?.getItem(KEY);this.originalRaw=raw;if(raw)this.db=validate(JSON.parse(raw));}catch(e){this.error='Não foi possível ler os dados. O conteúdo original foi preservado; exporte antes de continuar.';this.readBlocked=true;}}
 async commit(events=[],prefs=null){const run=()=>{if(this.readBlocked)throw Error(this.error);let latest=fresh();const raw=this.storage?.getItem(KEY);if(raw)latest=validate(JSON.parse(raw));const combined=merge(latest,this.db);combined.events=merge(combined,{events,revision:combined.revision}).events;if(prefs)combined.prefs={...this.db.prefs,...prefs};else combined.prefs=this.db.prefs;combined.revision++;
 this.db=combined;try{if(!this.storage)throw Error('Armazenamento indisponível');this.storage.setItem(KEY,JSON.stringify(combined));this.error=null;}catch(e){this.error='Não foi possível salvar neste navegador. Exporte seu backup agora.';throw Error(this.error);}return combined;};
 if(globalThis.navigator?.locks)return navigator.locks.request(KEY,async()=>run());return run();}
 async restore(v){const parsed=validate(v);return this.commit(parsed.events);}
 export(){if(this.readBlocked&&this.originalRaw)return this.originalRaw;return JSON.stringify({...this.db,exportedAt:new Date().toISOString(),app:'JARVIS Estudante'},null,2);}
}
const api={C,KEY,DRAFT,uid,ev,fresh,validate,merge,cycle,active,question,stats,topicState,errors,dueDate,recommend,pick,Store};root.Jarvis=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
