/* Adaptador do SDK, compartilhado pela aplicação e pelos testes em emulador. */
(function(root){'use strict';const CC=root.JarvisCloudCore||(typeof require!=='undefined'?require('./cloud-core.js'):null);
function create(F,firestore,uid,guard=fn=>fn()){
 const events=F.collection(firestore,'users',uid,'events'),prefs=F.doc(firestore,'users',uid,'settings','preferences');return{
  pull:cursor=>guard(async()=>{const clauses=[F.orderBy('receivedAt'),F.orderBy(F.documentId())];if(cursor)clauses.push(F.startAfter(new F.Timestamp(cursor.seconds,cursor.nanoseconds),cursor.id));clauses.push(F.limit(200));const page=await F.getDocsFromServer(F.query(events,...clauses));const last=page.docs.at(-1),stamp=last?.data().receivedAt;if(last&&!stamp)throw Error('Registro remoto sem data de recebimento.');return{events:page.docs.map(d=>{const data=d.data();if(data.schema!==1||data.event?.id!==d.id)throw Error('Registro remoto incompatível.');return data.event;}),cursor:last?{seconds:stamp.seconds,nanoseconds:stamp.nanoseconds,id:last.id}:cursor,more:page.size===200};}),
  push:batch=>guard(()=>F.runTransaction(firestore,async tx=>{const refs=batch.map(e=>F.doc(events,e.id));const existing=await Promise.all(refs.map(r=>tx.get(r)));existing.forEach((snap,i)=>{if(snap.exists()){if(CC.canonical(snap.data().event)!==CC.canonical(batch[i]))throw Error('Conflito de histórico na nuvem. Exporte o backup; nenhuma versão foi substituída.');}else tx.set(refs[i],{schema:1,event:batch[i],receivedAt:F.serverTimestamp()});});})),
  getPrefs:()=>guard(async()=>{const snap=await F.getDocFromServer(prefs);return snap.exists()?snap.data().prefs:null;}),
  setPrefs:value=>guard(()=>F.setDoc(prefs,{schema:1,prefs:value,updatedAt:F.serverTimestamp()}))
 };}
const api={create};root.JarvisFirestoreTransport=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
