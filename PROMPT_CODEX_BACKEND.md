# Prompt de continuação: backend opcional e integração de nuvem

Trabalhe exclusivamente no repositório `andersonx553-beep/Jarvis-estudante`. Leia `AGENTS.md`, `CODEX.md`, `README.md`, `core.js` e os fluxos afetados antes de alterar. O frontend funcional já existe e foi aprovado visualmente: preserve-o. O projeto de referência `Almox.aqua` é somente leitura e está fora do escopo.

Objetivo: adicionar, em etapa separada, Firebase Auth/Firestore e hospedagem Cloudflare, mantendo o modo local sem conta e sem IA. Não recrie o frontend nem substitua botões por placeholders. Primeiro verifique a implementação atual e descreva o plano técnico; execute o que estiver autorizado e mantenha credenciais/configuração ausentes como pendências explícitas. Não invente contas, projetos, chaves ou domínios.

## Preservação

1. Não altere IDs existentes de módulos, questões, eventos ou ciclos. Não apague dados reais, históricos ou regras existentes. Não inicialize banco remoto com um objeto vazio. Não publique backups de teste nem históricos no Git.
2. Mantenha `jarvis.estudante.v1`, seu schema e todos os eventos; migre apenas com cópia de segurança e rotina versionada, idempotente, reversível e testada. Eventos de resposta são imutáveis. Diagnósticos e correções geram novos eventos.
3. Não copie Firebase, domínios ou dados de outros repositórios. Nunca grave credencial administrativa no cliente. A configuração pública do SDK não é autorização: regras do servidor devem isolar usuários.
4. Interface azul/ciano em fundo navy, modo claro, layouts móveis, navegação, fontes e acessibilidade devem ser preservados. Use os SVG existentes. Não adicione Java, Python ou um framework sem necessidade concreta.

## Contrato e arquitetura

- Isole a persistência atrás de um adaptador compatível com `Store`. Os seletores e cálculos locais precisam continuar funcionando.
- Login opcional. Usuário sem login continua com dados locais. Exiba estado real: local, sincronizando, sincronizado, offline ou falha.
- Firestore em `users/{uid}/events/{eventId}` com eventos imutáveis e documentos separados para preferências, versão e metadados. Regras negam acesso cruzado, validam esquema/tipos/tamanho e impedem update/delete de eventos. Use Firebase Emulator Suite e testes de segurança.
- Migração local → nuvem explícita com exportação anterior, prévia da quantidade, confirmação, checkpoints e deduplicação por ID. Repetir a importação não deve duplicar respostas. Cancelar/falhar não pode apagar nada. Não use última gravação do banco inteiro como estratégia de conflito.
- Sincronização incremental, filas locais, repetição com backoff e paginação; não recarregue todo histórico a cada render. Teste duas abas/dispositivos, offline/online e escrita concorrente.
- Preserve ciclo ativo e sessões em andamento; um evento de outro aparelho não deve trocar silenciosamente o ciclo. Defina e documente a política de conflito.
- Guarde a versão do conteúdo de cada resposta. Antes de mudar gabaritos ou textos, implemente um catálogo versionado que permita explicar respostas antigas com seu conteúdo original.
- Backend não deve depender de IA para corrigir itens C/E. Avaliação semântica de justificativas só se expressamente solicitada e com dados/limites transparentes.
- Fontes oficiais e notícias não devem ser inventadas. Se houver atualização automatizada de conteúdo, projetar revisão editorial, fonte, vigência e histórico antes de ativar.

## Cloudflare

Prepare `dist/` para Pages ou Worker Assets, com HTTPS, manifesto e cache versionado. Não coloque tokens no Git. Domínio final depende da conta do proprietário. Configure domínio autorizado no Firebase Auth quando conhecido. A mudança de origem exige orientar exportação/importação; `localStorage` não migra sozinho entre domínios. Não mude compartilhamento/acesso do site atual sem pedido.

## Entrega e testes

Rode `npm test` e `npm run build`, acrescente testes de adaptador/migração/regras de segurança e confira 390×844, 768×1024 e 1366×900. Verifique rodadas de quatro na aprendizagem (rascunhos legados em duplas devem continuar recuperáveis), simulados sem repetição, banco de erros, notas, revisão, evidências, histórico, exportação/importação, falha de armazenamento e manutenção do modo local. Documente o que foi realmente executado.

Atualize `CODEX.md` a cada entrega com objetivo, arquivos, decisões, esquema, migração, testes, resultado e pendências. Encerre com o que funciona, o que exige configuração e os comandos exatos para continuar. Não declare Firebase ou Cloudflare publicados sem confirmação do serviço.


Atualização v1.7: preservar o catálogo ativo de290 pontos/3200itens, os156itens legados e snapshots históricos, tipos de evento rubric/gap/audit/sim-evaluation, reserva de inéditas e referências reais. Não substituir a autoavaliação por IA silenciosamente. Pesquisador online e análise semântica exigem fontes, custos/limites transparentes e chaves somente no backend.
