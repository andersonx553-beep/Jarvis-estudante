# CODEX.md — memória operacional do JARVIS Estudante

Última atualização: 27/10/2026. Repositório autorizado: `andersonx553-beep/Jarvis-estudante`.

Este arquivo preserva contexto, decisões, arquitetura e evidências de entrega. O histórico exato de diffs e commits continua no Git. Ele não substitui ler os trechos de código afetados antes de mudar uma função. Novas conversas devem começar por `AGENTS.md` e este documento.

## Estado vigente da expansão v1.7

Atualização autorizada em 27/10/2026: o usuário aprovou integrar o planejamento completo ao aplicativo, usar Python, abrir PR e fazer merge no GitHub. O DOCX JARVIS_Metodo_Modelo_Estrategias_Oficial_v1.7_Cara_a_Cara_com_a_Banca.docx é a fonte principal do método. O PDF Assuntos_vistos_INSS_atualizado_Dia16(1).pdf fornece matérias/blocos; todas as marcas de progresso são ignoradas para o novo ciclo. Os dois anexos foram lidos integralmente. Trechos históricos abaixo descrevem a v1 inicial e não prevalecem sobre este estado.

- Método atual: teoria suficiente e mapa de subtemas → exemplos → quatro questões juntas na aprendizagem → correção das quatro → diagnóstico → questões reais → auditoria da teoria → lacunas → aprofundamento → consolidação. Duplas só permanecem na navegação de simulado ou em rascunho legado recuperado.
- Catálogo v2: 290 pontos principais em42blocos, plano data/curriculum-plan.json, todos inicialmente pendentes;3.200itens autorais com quota por assunto. O catálogo de285pontos anterior ganhou seis detalhamentos líquidos em delegação e deslocou LibreOffice para suplemento. Não são290itens literalmente numerados no edital.
- Distribuição: Previdenciário1.800; Português360; Constitucional320; Administrativo320; Informática160; RLM120; Ética120. Fixação800, treino1.600, reserva800. Todo assunto mantém≥4itens de treino. Reserva só entra no treino após exposição em avaliação. O banco não é uma meta diária e não prevê a distribuição de prova futura.
- Cada aula tem mapa, teoria, exemplo, comparação, limites e fontes; as explicações das questões ampliam a teoria. Dificuldade é editorial provisória. Há conferência porIA e fontes primárias; não existe auditoria jurídica independente ou promessa de esgotamento do direito vigente.
- data/official-index.json preserva360referências de INSS2016,2022 e Guarulhos,15anuladas. Gabarito histórico não é silenciosamente tratado como regra atual. O app linka cadernos e registra auditoria; não hospeda reprodução integral dessas provas. A reaplicação não é um terceiro concurso independente.
- Respostas novas armazenam questionSnapshot com texto/gabarito/explicação/versão. content-legacy.js mantém39aulas/156itens originais sem mudarIDs ou respostas. O catálogo ativo usa IDs v17 distintos; progresso antigo não preenche a trilha nova. Ao abrir a expansão com eventos apenas legados e sem sessão em andamento, é acrescentado um evento de novo ciclo autorizado, preservando todos os anteriores; rascunho legado adia essa transição. Nenhum dado pessoal ou backup foi enviado aoGitHub.
- Tipos novos de evento: rubric,gap,audit,sim-evaluation. Esquema de backup continua1com validação ampliada aditiva, teto de100.000eventos e importação de até64MB. A quota efetiva de localStorage continua dependendo do navegador. Nenhum evento antigo é apagado. Marcações de rubrica e cobertura são autodeclaradas, não avaliação semântica porIA. Extensão de justificativa deixou de servir de evidência de domínio na trilha nova. Regra antiga permanece apenas na interpretação legada.
- Domínio funcional novo usa leitura, até8itens distintos conforme disponibilidade de treino, pelo menos2rodadas,80%auxiliar, rubricas completas, cobertura dos subtemas, ausência de lacunas abertas e quatro evidências finais. São heurísticas transparentes; memorização de pares pode enganar métricas, portanto não afirmar domínio objetivo certificado.
- Sábado:simulado cumulativo; domingo:descanso. Plano semanal em #plan, com Previdenciário aprender/consolidar/aplicar em três dias, Português/Administrativo e reforçoConstitucional. Sugestão automática40–120 só aumenta10quando simulado anterior≥40teve80%+, fadiga≤2e concentração≥4nas escalas1–5; ausência de autoavaliação mantém volume. Critérios auxiliares são propostas pedagógicas configuráveis futuras, não regras da banca.
- Pesquisador offline não executa busca. O app diz “não verificado nesta sessão” em vez de inventar notícias. AgenteIA online, análise semântica, Firebase e sincronização permanecem fora desta entrega; modo local é independente desses serviços.
- Fontes recentes conferidas durante produção incluem alterações em salário-maternidade, pensãoZika,SeguroDefeso,acumulação de cargos e vencimentoDAE. Fontes e limites específicos ficam nos metadados dos assets. Não generalizar além do dispositivo e da vigência descritos.

### Arquivos da expansão

- data/{prev-base,prev-beneficios,prev-especiais,const-adm,port-rlm,info-etica}.json: assets editoriais, cada enunciado e correção redigidos; fontes e localizadores. tools/editorial/*.py reconstroem esses assets e validam suas quotas; não são geradores de milhares por troca de nomes.
- tools/compile_content.py:confere integralidade,quotas,IDs,textos exatos únicos,tipos,fontes e reserva; gera content.js e docs/content-validation.json. Não altera o legado nem produz novas assertivas.
- core.js:índices emMap,compatibilidade de backup,snapshot,domínio por rubrica,cobertura,lacunas,reserva,dificuldade e sugestão de volume de simulado.
- app.js:#plan,#real,quatro itens,modo de auditoria real,rubrica,diagnóstico de fadiga/concentração e resumo de sessão; interface e ações existentes preservadas.
- index.html/build/sw:carregamento do legado antes de conteúdov2,HTMLindependente e novo cacheversionado. styles.css:adições responsivas sem trocar tokens.
- AGENTS.md,README.md,PROMPT_CODEX_BACKEND.md e este arquivo:regras atuais e instruções de execução. GitHub não recebe .openai/hosting.json.
- .github/workflows/checks.yml:CI de leitura, compilação determinística, testes e build em PR e pushmain, sem acesso a segredos nem publicação automática.

### Execução e evidências desta expansão

```sh
npm run content
npm test
npm run build
```

Validações locais concluídas:catálogo integral3.200/290,22testesNode passaram,compilação ebuild concluídos. QA de navegador:rodada de quatro,correção,rubrica,diagnóstico,encerramento,auditoria real,lacuna,simulado40itens,fadiga/concentração,backup real55eventos e reimportação sem duplicação. Telas conferidas nos3tamanhos com scrollWidth==clientWidth. Falha inicial causesundefined corrigida e recuperação verificada sem perda de respostas. Evidências e limites em docs/qa-v1.7.md. PR,merge e publicação serão registrados após confirmação. Os blocos abaixo preservam o histórico da implementação original.

## 1. Objetivo e decisão atual do usuário

Criar um aplicativo profissional de preparação INSS, foco CEBRASPE, fiel às dez pranchas visuais aprovadas, responsivo no celular/tablet/computador e funcional com progresso local. O usuário autorizou implementar também as funções viáveis sem backend, pediu código no GitHub, contexto em CODEX.md e um prompt separado para backend futuro. Novo ciclo começa do zero. Não restaurar nem pré-preencher o Dia 16.

Firebase e Cloudflare serão usados posteriormente. Não há credencial de Firebase nem projeto remoto configurado. A implementação atual não exige login ou IA. Nenhuma ação foi feita em bancos externos.

## 2. Histórico de requisitos e fontes

- Foram anexados `JARVIS_Contexto_Continuacao_INSS_CEBRASPE_2026-10-27.pdf` e `Mapa_Estudos_INSS_CEBRASPE_Completo_2026-10-27.pdf` (também cópias com `(1)`). Ambos foram lidos integralmente quando o executor voltou a funcionar. Os PDFs são uma especificação de continuidade e um mapa, não apostilas exaustivas.
- Houve falhas iniciais de acesso ao ambiente. Não se inventou leitura ou progresso. A leitura posterior recuperou o método; o usuário depois escolheu explicitamente um novo ciclo.
- Os documentos mencionavam Dia 16 confirmado e referência incompleta ao Dia 17. Esse histórico NÃO é importado como progresso do app; foi substituído, por decisão do usuário, pelo início zerado. Não reabrir essa discussão sem pedido.
- Dez pranchas de prévia visual foram geradas e aprovadas: início/menu; conteúdos/plano; aula/raciocínio; questões/correção; banco de erros; revisões/simulados; resultados/evolução; mapa/histórico; configurações/backup; componentes/estados.
- O usuário pediu preservar cores, movimentos, CSS e botões, adaptando os layouts a telas reais. As imagens são referências de composição, não conteúdo jurídico validado nem números reais. Não copiar erros de texto presentes nas imagens.
- `Almox.aqua/CLAUDE.md` foi consultado SOMENTE PARA LEITURA como provável projeto citado verbalmente como “Moxiaco”. Regras reaproveitadas conceitualmente: PT-BR, SVG sem emojis, alterações pequenas, modo sem IA, testes móveis e desktop, auditoria e preservação de histórico. Não se copiou código de banco, domínio, credenciais, dados pessoais ou regras de segurança do outro aplicativo. Nada foi alterado nele.

## 3. Método preservado

Prioridade máxima: Previdenciário. Constitucional recebe reforço estratégico. Português e Administrativo têm prioridade alta. RLM, Informática e Ética entram progressivamente.

Aula: teoria → exemplos → raciocínio → 2 itens juntos → correção → diagnóstico → registro → recuperação/avanço. O desempenho orienta o ritmo; não há obrigação de avançar por calendário. As oito etapas de raciocínio são núcleo, elementos, limites, fronteiras, caso, formulação, recuperação ativa e transferência.

Itens autorais são rotulados “estilo CEBRASPE”, nunca “QUESTÃO REAL”. Gabarito aparece somente após as duas respostas no treino. Confiança e justificativa são registradas, sem avaliação semântica automática. O simulado revela gabarito somente ao encerrar e mistura todo o banco selecionado sem repetir itens para completar quantidade. Tamanhos 40–120 são referência, não obrigação.

Estados: não iniciado, visto, consolidação, dominado. Domínio exige leitura, quatro itens distintos corretos com confiança, justificativas de 20+ caracteres, pelo menos duas rodadas, 80%+ no tópico e quatro evidências declaradas pelo estudante. É uma aproximação transparente, não avaliação semântica de domínio. Repetir de memória quatro itens não garante transferência real: novos itens e revisão editorial são um aprofundamento futuro.

Revisões usam 1/3/7/14 dias conforme rodadas e resultado, com dificuldade retomada antes de avanço. Domingo é referência de revisão sem bloqueio do calendário. A recomendação é determinística, por revisão vencida/dificuldade/prioridade/alternância; não é um agente de IA.

## 4. Implementação e arquivos

Site estático sem frameworks, sem CDN e sem instalação de dependências. HTML, CSS e JavaScript puro. Java ou Python não são exigidos pela aplicação; Python é apenas uma opção de servidor de desenvolvimento.

| Arquivo | Responsabilidade |
|---|---|
| `index.html` | Entrada sem scripts inline; carregamento content → core → app |
| `styles.css` | Tokens, tema escuro/claro, layouts, estados, foco, impressão e movimento reduzido |
| `content.js` | 7 disciplinas, 39 módulos introdutórios, 156 itens autorais, fontes e checklist de aprofundamentos |
| `core.js` | Eventos, armazenamento, validação, mesclagem, status, erros, revisão, recomendação e seleção |
| `app.js` | Ícones, rotas hash, telas, modais, ações, formulários, downloads e retomada |
| `assets/icon.svg` | Marca original em SVG, sem dependências externas |
| `manifest.webmanifest`, `sw.js` | Manifesto e cache dos arquivos públicos do app |
| `tools/build.mjs` | Gera `dist/` e `dist/jarvis-estudante.html` independente |
| `tests/core.test.cjs` | Onze testes do contrato de conteúdo e persistência/método |
| `AGENTS.md` | Instruções de execução e proteção do escopo/dados |
| `PROMPT_CODEX_BACKEND.md` | Prompt completo para integração futura de nuvem |
| `docs/design.md` | Referência de aparência e mapeamento das telas |
| `README.md` | Uso, execução, limitações e hospedagem futura |
| `.openai/hosting.json` | Identidade da publicação de demonstração; nunca copiar essa identidade para outro Site |

Rotas: `#home`, `#courses`, `#courses/{disciplina}`, `#lesson/{topico}`, `#questions`, `#errors`, `#reviews`, `#sim`, `#result/{rodada}`, `#map`, `#history`, `#sources`, `#settings`, `#more`.

Responsividade: sidebar a partir de 901 px; navegação inferior e menu móvel até 900 px; cards e formulários em coluna no celular; conteúdo sem largura mínima rígida. Modo foco das questões não entrega tema/pegadinha no cabeçalho. SVG, contraste, rótulos, teclado, foco de modal, `inert` no menu móvel fechado e preferência de movimento reduzido.

## 5. Dados e proteção

Chave `localStorage`: `jarvis.estudante.v1`, schema 1. Sessão em andamento em `jarvis.estudante.draft.v1`. Estrutura principal: `{schema, created, events, prefs, revision}`.

Eventos: `read`, `attempt`, `note`, `evidence`, `session`, `cycle`, `review`, `coverage`, `diagnosis`. Todo evento tem id, data, tipo e ciclo. Tentativas têm tópico, qid, resposta, confiança, justificativa, rodada, sessão e versão de conteúdo. Resposta original não é editada para registrar causa: `diagnosis` referencia o evento original. Notas geram versões; não sobrescrevem notas antigas.

Seletores recalculam mapa/erros/resultados a partir dos eventos do ciclo atual. Novo ciclo adiciona evento e arquiva o anterior sem apagar. Histórico e backup incluem todos os ciclos. Importação valida schema, tópicos, questões, vinculação, tipos e identificadores; mescla sem duplicar ou excluir. Preferências atuais ficam mantidas. O ciclo mais recente entre os eventos mesclados pode tornar-se ativo; futura sincronização deve definir uma política explícita de conflito.

Gravações usam Web Locks quando disponível, releem o armazenamento e mesclam IDs antes de salvar. Há atualização entre abas pelo evento `storage`. Navegadores sem Web Locks têm menor proteção a escritas rigorosamente simultâneas: resolver no adaptador futuro. Uma sessão em andamento tem uma chave compartilhada entre abas; evitar estudar duas sessões paralelas na mesma origem.

Falha de gravação mantém o estado em memória para exportar e exibe erro. JSON corrompido não é sobrescrito: o original permanece e é exportável. Não criar reset automático para “resolver” corrupção. O limite da importação é 8 MB e 20 mil eventos; ampliar de forma versionada se necessário, preferindo IndexedDB e paginação para grande volume.

O HTML não contém o progresso pessoal. Limpeza de dados pode apagar o localStorage. Domínios/arquivos diferentes não migram localStorage automaticamente. Exportar/importar ao trocar de origem. Modo `file://` depende do navegador. Cache do service worker não guarda backups ou respostas em servidor. Não há telemetria nem envio de notas a terceiros.

## 6. Conteúdo e limites editoriais

São 39 INTRODUÇÕES estruturadas, não uma apostila integral do edital. Há checklist explícito de aprofundamentos. Não declarar 100% de cobertura do edital vigente; a referência recuperada é 2022. Valores anuais, prazos específicos, regras de benefícios, transições, jurisprudência, subitens de gramática e versões de software exigem aprofundamento e atualização editorial.

Fontes primárias de referência: Constituição, Leis 8.212/8.213/8.742/8.112/9.784, Decretos 3.048/1.171/6.029, STF Tema 532, Manual de Redação da Presidência, CERT.br e ajuda oficial do LibreOffice. O aplicativo não alega pesquisa automática de leis ou notícias. A voz depende de suporte/vozes do navegador.

Numa mudança de gabarito ou texto, preservar versão histórica. A primeira versão registra `contentVersion: 1`, mas usa o catálogo atual para leitura dos resultados. Antes de mudanças editoriais substanciais, implementar catálogo histórico de versões. Isso está especificado no prompt de backend.

## 7. Como executar e validar

```sh
npm test
npm run build
python3 -m http.server 8080 --directory dist
```

Sem `npm install`. Abrir `http://localhost:8080`, ou `dist/jarvis-estudante.html` independente. Em ambiente Sites gerenciado usar `sites-preview start <checkout>`; não iniciar outro servidor paralelo. `dist/` é gerado e ignorado no Git. A hospedagem GitHub Pages não está automaticamente habilitada.

Testes efetivamente executados nesta entrega:

- Sintaxe: `node --check app.js`, `core.js`, `content.js`.
- Onze testes Node passaram: catálogo; leitura/acerto isolado sem domínio; critérios de domínio; validação/união; novo ciclo; preservação de erro; seleção sem repetição; persistência/importação; quota; armazenamento corrompido; recomendação.
- Browser: início → primeira aula → registro de leitura → exemplos → rodada de dois itens → correção com um erro e um acerto → diagnóstico “Interpretação” → encerramento → sessão no histórico. Gabarito ausente antes da correção, botão desativado com resposta faltante.
- Browser: simulado pediu 40, limitou-se a 4 disponíveis, navegou em duplas, confirmou quatro em branco e mostrou resultado/registro correto ao finalizar.
- Browser: download real do JSON com dez eventos de teste, importação do mesmo arquivo e confirmação de mesclagem sem exclusão/duplicação.
- Layout em iframes com viewport de 390×844, 768×1024, 1366×900. Larguras úteis medidas (descontada a barra): 375/753/1351; `scrollWidth === clientWidth` nas três. Inspeção visual móvel e desktop realizada. Isso é QA de navegador, não teste físico de aparelho Android/iPhone.
- Ajustes durante teste: callback assíncrono do Web Lock para liberar corretamente após falha; referência explícita `window.history` para não conflitar com função de histórico; guard de leitura de voz; exportação do JSON original em caso de corrupção; menu móvel fechado sem foco por `inert`.

Não alegar que toda combinação possível de navegador, instalação PWA, quota, dispositivo e versão legal foi testada. O cronômetro mede tempo decorrido, inclusive intervalos entre acessos. A meta é preferência de referência, sem notificações push.

## 8. Pendências e próxima etapa

O frontend e a lógica local são a entrega atual. Firebase/Auth, Firestore, sincronização entre aparelhos, regras testadas em emulador e configuração de Cloudflare ficam para a próxima etapa. O prompt está em `PROMPT_CODEX_BACKEND.md`. Ele exige preservar o modo local, IDs, histórico, interface e migração com backup, sem modificar bancos de outros projetos.

Ainda são evoluções editoriais: aprofundar o edital por subitem, ampliar banco de itens com casos novos, catálogo versionado de conteúdos, auditoria jurídica por dispositivo/data e eventual comparação de edital novo. Não apresentar funcionalidades futuras como implementadas.

## 9. Registro de alterações desta entrega

27/10/2026 — Implementação inicial autorizada. Arquivos de entrada, conteúdo, núcleo, UI, CSS, ícone, manifesto, cache, build, testes e documentação criados em repositório vazio. Visual dark navy/ciano/azul e estado inicial zerado; progressão guiada pelos registros locais. Backend deliberadamente não simulado. Documentação foi adaptada de princípios do Almox, sem alterações no projeto de referência.

Publicação e sincronização: ver seção final de verificação de entrega, acrescentada após retorno dos serviços.

## 10. Verificação final de entrega

27/10/2026 — Código completo salvo na branch `main` do GitHub. Commit inicial da implementação: `e1f0c66bbac03057bbd987f09df65dac5dc6a59d` (após bootstrap de README). Sincronização feita pela API de Git, com verificação do SHA esperado, sem force push. O contexto final é acrescentado em commit separado de documentação.

Publicação privada confirmada pelo serviço com status `succeeded`: https://jarvis-estudante-inss.sageflea1025.chatgpt.site . O endereço exige entrar com a conta proprietária do ChatGPT; a tela de acesso foi observada no navegador de QA. Não se mudou o público para contornar o acesso. O HTML independente continua disponível sem login e pode ser servido em outra hospedagem. Dados locais não migram entre essas origens sem backup.

Identificadores de publicação: projeto `appgprj_6ae0e8f23d988191ad105974fcc97b43`; versão `appgprj_6ae0e8f23d988191ad105974fcc97b43~appgver_335f41211bec819197ee4f55c52a4a4f`; deploy `appgdep_6ae0eeb4f85c81919a5d68f42c763cf5`. Commit de fonte da publicação: `f51a9aa7c9dbbf8dce7fb807b1a0a922a30c4b50`. Esses IDs são da hospedagem de demonstração, não Firebase/Cloudflare do usuário. Não modificar ou reutilizar em outro projeto.

A fonte da hospedagem contém o mesmo runtime da entrega GitHub. O bloco final deste documento é posterior ao deploy e não muda o runtime. Backend remoto e expansão editorial continuam pendentes conforme seções 6 e 8.

QA complementar concluído após a publicação: novo ciclo confirmado digitando NOVO; dashboard voltou ao Dia 1 com zero sessões/respostas, e o histórico mostrou as duas sessões anteriores arquivadas (zero no ciclo atual, duas no arquivo completo). O HTML independente foi aberto pelo servidor de prévia e renderizou corretamente o dashboard, sem dependências externas de CSS/JS. O teste físico de `file://` no celular continua dependente do navegador.

Observação de distribuição: `.openai/hosting.json` pertence à cópia local e ao repositório da hospedagem de demonstração. Não foi copiado para o GitHub do usuário, para não vincular indevidamente futuros projetos a essa identidade. A branch GitHub contém o código estático, os testes e as instruções de build; a configuração Cloudflare futura será própria.
