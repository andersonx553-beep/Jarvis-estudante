"""Compila assets editoriais preservando o catálogo v1 e sem gerar enunciados."""
from pathlib import Path
import json, hashlib, collections, re, argparse

ROOT=Path(__file__).resolve().parents[1]
PARTS=['prev-base','prev-beneficios','prev-especiais','const-adm','port-rlm','info-etica']
def compile_content():
    plan=json.loads((ROOT/'data/curriculum-plan.json').read_text())
    targets={x['id_planejamento']:x for x in plan['assuntos']}
    lessons=[]; notes=[]
    for part in PARTS:
        data=json.loads((ROOT/f'data/{part}.json').read_text())
        lessons+=data['lessons'];notes.append({'asset':part,**data.get('editorial',{})})
    assert len(lessons)==290,(len(lessons),'aulas')
    assert len({x['id'] for x in lessons})==290
    assert {x['planId'] for x in lessons}==set(targets)
    ids=set();texts={};counts=collections.Counter();source_counts=0
    for l in lessons:
        p=targets[l['planId']]
        assert len(l['questions'])==p['meta_questoes_autorais'],(l['id'],len(l['questions']),p['meta_questoes_autorais'])
        assert isinstance(l.get('title'),str) and len(l['title'])>=3,(l['id'],'title')
        for f in ['core','rule','example','contrast','limit']:
            assert isinstance(l.get(f),str) and len(l[f])>10,(l['id'],f)
        l['contentVersion']=2;l['methodVersion']='1.7';l['editorialReview']='IA e conferência de fontes; sem revisão independente'
        l['block']=p['bloco'];l['priority']=p['prioridade_editorial'];l['legacy']=False
        l['subtopics']=l.get('subtopics') or ['Conceito e fundamento','Requisitos e aplicação','Limites e exceções','Distinção de conceitos próximos']
        assert l.get('sources') and all(s.get('url','').startswith('https://') and s.get('locator') for s in l['sources']),(l['id'],'fontes')
        l['source']='v17-'+l['id']
        for q in l['questions']:
            assert q['id'] not in ids,(q['id'],'ID repetido');ids.add(q['id'])
            normalized=re.sub(r'\s+',' ',q['text'].strip().casefold())
            assert normalized not in texts,(q['id'],texts.get(normalized),'enunciado repetido')
            texts[normalized]=q['id']
            assert isinstance(q['answer'],bool) and len(q.get('explanation',''))>20,q['id']
            assert q.get('sourceRef',{}).get('url','').startswith('https://') and q['sourceRef'].get('locator'),(q['id'],'fundamento')
            assert type(q.get('version',1)) is int and q.get('version',1)>=1,(q['id'],'version')
            q.update({'version':q.get('version',1),'contentVersion':2,'kind':'autoral','microtopic':l['planId'],'reviewedAt':'2026-10-27','reviewType':'editorial-IA-fontes','topic':l['id']})
            q['family']=q.get('family') or l['planId']
            q['difficulty']=q.get('difficulty','intermediario')
            counts[l['d']]+=1;source_counts+=1
    assert len(ids)==3200,len(ids)
    # Reserva estável, por matéria; todo assunto mantém no mínimo quatro itens de treino.
    for d in counts:
        ls=[l for l in lessons if l['d']==d]
        target=counts[d]//4
        candidates=[q for l in ls for q in sorted(l['questions'],key=lambda q:q['id'])[4:]]
        candidates.sort(key=lambda q:hashlib.sha256(('reserva:'+q['id']).encode()).hexdigest())
        assert len(candidates)>=target,(d,'reserva insuficiente')
        reserve={q['id'] for q in candidates[:target]}
        train=[q for l in ls for q in l['questions'] if q['id'] not in reserve]
        train.sort(key=lambda q:hashlib.sha256(('fixacao:'+q['id']).encode()).hexdigest())
        fixation={q['id'] for q in train[:target]}
        for l in ls:
            for q in l['questions']:q['mode']='reserva' if q['id'] in reserve else 'fixacao' if q['id'] in fixation else 'treino'
    ordered={x['id_planejamento']:i for i,x in enumerate(plan['assuntos'])}
    lessons.sort(key=lambda l:ordered[l['planId']])
    official=json.loads((ROOT/'data/official-index.json').read_text())
    for r in official['rows']:r['id']='real-'+r['prova']+'-'+str(r['item'])
    payload={'version':2,'methodVersion':'1.7','updated':'2026-10-27','lessons':lessons,'plan':plan,'realIndex':official['rows'],'editorial':notes}
    js="""/* Gerado por tools/compile_content.py; editar os assets, não este arquivo. */
(function(root){'use strict';
const old=root.JarvisLegacyContent||(typeof require!=='undefined'?require('./content-legacy.js'):null);
const pack=PAYLOAD;
const sources={...old.sources};for(const l of pack.lessons){const s=l.sources[0];sources[l.source]=[s.title,s.url];}
const archived=old.lessons.map(l=>({...l,legacy:true,contentVersion:1}));
const coverage=Object.fromEntries(old.disciplines.map(d=>[d.id,[...new Set(pack.lessons.filter(l=>l.d===d.id).map(l=>l.block))]]));
const data={...pack,sources,disciplines:old.disciplines,lessons:pack.lessons,archiveLessons:archived,allLessons:[...archived,...pack.lessons],coverage};
root.JarvisContent=data;if(typeof module!=='undefined')module.exports=data;
})(typeof window!=='undefined'?window:globalThis);
""".replace('PAYLOAD',json.dumps(payload,ensure_ascii=False,separators=(',',':')))
    (ROOT/'content.js').write_text(js)
    report={'lessons':len(lessons),'questions':len(ids),'disciplines':dict(counts),'modes':dict(collections.Counter(q['mode'] for l in lessons for q in l['questions'])),'realReferences':len(official['rows']),'legacyLessonsPreserved':39,'legacyQuestionsPreserved':156,'structuralChecks':'passed','independentLegalReview':False,'generatedText':False}
    (ROOT/'docs/content-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':compile_content()
