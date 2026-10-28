# Firebase do JARVIS Estudante

Projeto exclusivo: `jarvis-estudante`. Configuração pública fornecida pelo proprietário em 28/10/2026. Não usar credenciais ou banco do Almox. Não há conta administrativa autorizada no ambiente de desenvolvimento; implementação e testes em emulador não equivalem a ativação em produção.

## Ativar no console

1. No console do projeto, abra Authentication e habilite **E-mail/senha**. A interface desta entrega utiliza esse provedor; Google ainda não foi implementado.
2. Crie o Firestore **Standard**, banco `(default)`, em **modo de produção**. A localização é uma decisão do proprietário na criação. Não abrir regras globais de teste.
3. Publique o conteúdo integral de `firestore.rules` em Firestore → Regras, ou execute a implantação abaixo. As regras são específicas deste app, cujo espaço `users/{uid}` deve ser novo. Se já houver outras aplicações/regras nesse projeto, revise a combinação antes de implantar: a CLI substitui o conjunto de regras, não o mescla.
4. Authentication → Configurações → Domínios autorizados: confira o domínio final de hospedagem. Para a demonstração existente, o hostname é `jarvis-estudante-inss.sageflea1025.chatgpt.site`. Adicione apenas os domínios utilizados. O acesso privado do Site é uma camada distinta do login Firebase. `localhost`, quando necessário para desenvolvimento, deve ser configurado explicitamente nos projetos novos.
5. Abra Configurações e backup no JARVIS → Conectar ao Firebase → Criar conta/Entrar. Cadastre a própria senha na interface; nunca envie senha ou conta de serviço por chat.
6. Para trazer dados antigos: **Trazer progresso do modo local**, confira o e-mail e a quantidade e confirme **Baixar backup e transferir**. O download é solicitado antes da mesclagem; confira se o navegador realmente salvou o arquivo. A cópia de origem não é removida. Para dados de outro domínio, exporte nessa origem e importe no espaço desejado do novo domínio.

## Comandos

Preparação: Node22+, npm e Java21+ para os emuladores. Java/Python/npm não são necessários no celular. O SDK12.11.0 é carregado da CDN oficial apenas ao conectar à conta; o modo local não depende dele.

```sh
npm ci
npm test
npm run test:firebase
npm run build
npx firebase login
npm run deploy:rules
```

`deploy:rules` publica as regras e a isenção de índice do payload dos eventos. Não publica o site nem cria usuários. O terminal precisa estar autenticado na conta com permissão nesse projeto. A chave pública do SDK não dá permissão de administração.

Hospedar no Firebase é opcional. O app estático pode usar Cloudflare/Sites e conectar aos mesmos Auth/Firestore. Se o proprietário quiser Firebase Hosting, o comando já está preparado:

```sh
npm run deploy:hosting
```

Isso publica `dist/` no Hosting do projeto. O comando **não foi executado nesta entrega**; o acesso do Firebase Hosting deve ser avaliado separadamente do acesso privado do Site atual.

## Dados e sincronização

- Modo local mantém `jarvis.estudante.v1` e o rascunho originais, schema1.
- Cada conta usa cópias `jarvis.account.{uid}.jarvis.estudante.v1` e `.draft.v1`. Trocar de conta não carrega nem envia eventos de outra conta. O modo local fica separado e não é enviado automaticamente.
- `jarvis.cloud.active.v1` lembra o espaço selecionado. A conta é revalidada ao conectar; offline é possível estudar na cópia do espaço já aberto. Não é criptografia contra quem usa o mesmo perfil do navegador: saia e proteja o aparelho em dispositivos compartilhados.
- `users/{uid}/events/{id}`: `{schema:1,event,receivedAt}`. O servidor atribui `receivedAt`; dados históricos mantêm seus IDs, datas, tipos e snapshots. Eventos são somente criação; update/delete são negados mesmo ao dono.
- Transações de10eventos leem os IDs antes de criar; repetições idênticas não gravam de novo. Mesmo ID com payload diferente bloqueia a sincronização e pede investigação/backup, sem escolher silenciosamente uma versão.
- Download incremental em páginas de200, cursor por timestamp do servidor+ID. Eventos recebidos são validados pelo app antes de mesclar. O índice do mapa `event` é dispensado; `receivedAt` continua indexado.
- Fila deriva de eventos locais sem confirmação de recebimento. Checkpoints e ciclos pendentes em `jarvis.cloud.{uid}.sync.v1`. Falhas mantêm os dados locais e tentam novamente com backoff deaté5min; sincronização normala cada30s, ao reconectar, ao voltar à aba e pelo botão. Não há listener contínuo; mudanças podem levar esse intervalo. Há leituras faturáveis; observar as cotas do projeto.
- Preferências em `users/{uid}/settings/preferences`, campos limitados. Última gravação vence nesse documento. Uma preferência local ainda não enviada tem prioridade sobre o download da preferência remota. Eventos/respostas nunca usam essa política.
- Mudança de ciclo remoto fica pendente para conferência. Aplicá-la exige encerrar a sessão neste aparelho. Migração/importação explícita informa que o ciclo mais recente poderá tornar-se ativo. Sessões em andamento/rascunhos não são enviados à nuvem.
- O frontend usa cache de memória do Firestore; a fila durável é a cópia local existente. O service worker só armazena arquivos públicos da interface. Notas e respostas são transmitidas ao Firestore apenas no espaço de conta conectado.

## Validação e limites

Testes de unidade cobrem migração repetida, falha remota, offline/reload, conflito, troca de conta em operação, ciclo pendente, concorrência de dois aparelhos e preferências. Testes no Emulator Suite cobrem acesso negado sem login/cruzado, eventos imutáveis, esquema, snapshots,13tipos de eventos, cadastro/login/recuperação e o adaptador real paginando205registros em dois clientes SDK.

O teste executa os arquivos de modo sequencial, pois a suíte de regras limpa o banco **demo** entre casos. Nunca apontar esses testes para produção. Os dados e usuários de teste permanecem apenas no emulador, sem envio ao projeto real.

LocalStorage ainda tem quota e depende do navegador; exporte backups. Evite sessões paralelas em abas do mesmo espaço, pois o rascunho é compartilhado nessa origem. Não há Google Sign-in, IA online, apagamento de conta/dados, sync de rascunho, notificações ou certificação de produção. Não criar conta real automaticamente para testar. O banco editorial de3.200itens continua estático e não é copiado integralmente para o Firestore.
