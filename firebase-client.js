/* SDK carregado somente ao solicitar a conexão. O estudo local funciona sem Firebase. */
(function(){'use strict';
const VERSION='12.11.0';let loading;
const messages={
 'auth/invalid-credential':'E-mail ou senha inválidos.', 'auth/email-already-in-use':'Este e-mail já possui cadastro. Entre ou recupere a senha.',
 'auth/weak-password':'Escolha uma senha mais forte, com pelo menos 6 caracteres.', 'auth/password-does-not-meet-requirements':'A senha não atende à política configurada no Firebase.',
 'auth/invalid-email':'Confira o endereço de e-mail.', 'auth/too-many-requests':'Muitas tentativas. Aguarde antes de tentar novamente.',
 'auth/operation-not-allowed':'Ative o provedor E-mail/senha no Authentication do projeto jarvis-estudante.',
 'auth/configuration-not-found':'O Authentication ainda precisa ser ativado no projeto jarvis-estudante.',
 'auth/unauthorized-domain':'Adicione o domínio deste aplicativo aos domínios autorizados do Firebase Authentication.',
 'auth/network-request-failed':'Sem conexão com a autenticação. Seu estudo local continua disponível.',
 'permission-denied':'O Firestore recusou o acesso. Confira se as regras firestore.rules foram publicadas neste projeto.',
 'failed-precondition':'O Firestore ainda precisa de configuração. Confira o banco (default) e as regras do projeto.',
 'unavailable':'Firestore indisponível. As alterações continuam salvas no aparelho para nova tentativa.'
};
function friendly(error){return messages[error.code]||error.message||'Não foi possível conectar. Tente novamente.';}
async function load(){if(location.protocol==='file:')throw Error('Para usar a conta, abra o aplicativo em uma hospedagem HTTPS. O arquivo HTML continua funcionando no modo local.');if(loading)return loading;loading=(async()=>{
 const base='https://www.gstatic.com/firebasejs/'+VERSION+'/';
 const [A,H,F]=await Promise.all([import(base+'firebase-app.js'),import(base+'firebase-auth.js'),import(base+'firebase-firestore.js')]);
 const emulator=window.JarvisFirebaseEmulators;const local=['localhost','127.0.0.1','terminal.local'].includes(location.hostname);
 if(emulator&&!local)throw Error('Emuladores só podem ser usados na prévia local.');
 const config=emulator?{...window.JarvisFirebaseConfig,projectId:'demo-jarvis-estudante',apiKey:'demo-api-key',authDomain:'localhost'}:window.JarvisFirebaseConfig;
 const app=A.initializeApp(config);const auth=H.getAuth(app);auth.languageCode='pt-BR';const firestore=F.initializeFirestore(app,{localCache:F.memoryLocalCache()});
 if(emulator){H.connectAuthEmulator(auth,'http://'+emulator.host+':9099',{disableWarnings:true});F.connectFirestoreEmulator(firestore,emulator.host,8080);}
 await H.setPersistence(auth,H.browserLocalPersistence);await auth.authStateReady();
 const guard=async fn=>{try{return await fn();}catch(e){throw Error(friendly(e));}};

 return{get user(){return auth.currentUser;},watch:fn=>H.onAuthStateChanged(auth,fn),
  login:(email,password)=>guard(()=>H.signInWithEmailAndPassword(auth,email,password)),
  register:(email,password)=>guard(()=>H.createUserWithEmailAndPassword(auth,email,password)),
  reset:email=>guard(()=>H.sendPasswordResetEmail(auth,email)),logout:()=>guard(()=>H.signOut(auth)),
  verify:()=>guard(()=>H.sendEmailVerification(auth.currentUser)),transport:uid=>window.JarvisFirestoreTransport.create(F,firestore,uid,guard)};
})();try{return await loading;}catch(e){loading=null;throw Error(friendly(e));}}
window.JarvisFirebase={load,friendly};
})();
