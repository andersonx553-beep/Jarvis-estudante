/* Cache apenas dos arquivos públicos do app; respostas e backups nunca vão à rede. */
const VERSION='jarvis-shell-v1.0.0';
const FILES=['./','./index.html','./styles.css','./content.js','./core.js','./app.js','./assets/icon.svg','./manifest.webmanifest'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(FILES)));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('jarvis-shell-')&&k!==VERSION).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;const url=new URL(e.request.url),known=FILES.some(path=>new URL(path,self.registration.scope).pathname===url.pathname);if(!known&&!e.request.mode.includes('navigate'))return;e.respondWith(fetch(e.request).then(async response=>{if(response.ok&&known){const c=await caches.open(VERSION);await c.put(e.request,response.clone());}return response;}).catch(async()=>{const cached=await caches.match(e.request);return cached||(e.request.mode==='navigate'?caches.match('./index.html'):Response.error());}));});
