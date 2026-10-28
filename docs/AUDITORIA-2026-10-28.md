# Auditoria técnica e funcional — JARVIS Estudante

Data:28/10/2026. Runtime examinado:v1.8.1, commits6d887b3396af95b36df5e308af42e9dfe0f01aba e5214364e3fa41da5ba0a67ddb6f9a84988414a4b (o segundo acrescenta o workflow Pages/documentação, sem alterar o runtime). Escopo: código, estrutura integral dos assets, testes, reprodução de casos com dados fictícios e resultado das publicações. A auditoria é feita porIA; não representa revisão jurídica independente nem certificação de segurança. Não foram usados dados ou credenciais reais de estudo.

## Resultado

O aplicativo tem uma base funcional de estudos e integração opcional Firebase. Ainda há problemas reproduzíveis de continuidade e método que precisam de correção antes de considerá-lo concluído para todos os cenários. O endereço GitHub Pages existente está desatualizado; a nova preparação/build passou, mas a implantação falhou. A sincronização da conta real do proprietário não foi confirmada nesta auditoria.

Os44testes existentes passam:33núcleo/método/sync,3distribuição e8regras/integração em emuladores. Isso não cobre todos os cenários: cinco casos adicionais abaixo foram reproduzidos fora dessas suítes e revelam lacunas. O script tools/audit_app.cjs e docs/audit-evidence-2026-10-28.json permitem repetir a verificação sem acessar produção.

## O que foi conferido no conteúdo

| Disciplina | Pontos | Itens autorais |
|---|---:|---:|
| Previdenciário |130|1.800|
| Constitucional |26|320|
| Português |27|360|
| Administrativo |54|320|
| Raciocínio Lógico |18|120|
| Informática |23|160|
| Ética |12|120|
| Total |290|3.200|

São42pares disciplina/bloco. Há41títulos distintos de bloco porque um título se repete entre disciplinas; isso não é falta de um bloco. O mapa tem2.324entradas de subtemas, que são uma decomposição pedagógica, não2.324itens literais do edital.

O compilador confirmou:290IDs de aula,3.200IDs de questão,3.200enunciados normalizados distintos, quotas por ponto, gabaritos booleanos, explicações, fontes HTTPS e localizadores. Modos:800fixação,1.600treino,800reserva. O catálogo legado39aulas/156questões está preservado. Existem360referências reais com links e identificação de item, não360enunciados integrais hospedados.

Essa conferência não prova ausência de duplicação semântica, veracidade de cada gabarito, vigência integral de cada fundamento nem profundidade suficiente de cada aula. A base continua sendo edital histórico2022retificado e os documentos fornecidos, com revisão editorial porIA. Falta revisão de mérito por assunto/questão, com vigência e identificação do revisor. A dificuldade é classificação editorial, sem calibração estatística. O volume de texto não foi usado como prova de ensino suficiente.

## Problemas reproduzidos e prioridade

| ID | Prioridade | Achado e efeito | Onde | Correção necessária |
|---|---|---|---|---|
| A01 | Alta | Um ciclo criado em outra aba do mesmo espaço pode tornar-se ativo enquanto o rascunho da primeira aba mantém o ciclo anterior. Novas respostas usam event(), que consulta o ciclo atual; há risco de atribuição ao ciclo errado. Não foi constatado apagamento de dados reais. | app.js:event e listener storage; core.js:Store.commit/cycle | Conferir mudança de ciclo entre abas; impedir envio de respostas para ciclo divergente da sessão; preservar e recuperar o rascunho. |
| A02 | Alta | Um ciclo recebido da nuvem fica em meta.pendingCycles, mas Store.export exporta só db. Um backup feito enquanto esse ciclo aguarda conferência pode conter leituras do ciclo remoto sem seu evento de ciclo. Ao restaurar, o ciclo ativo fica inicial. A nuvem ainda conserva o evento; o backup isolado não está completo nesse estado. | cloud-core.js:splitRemote/checkpoint; core.js:Store.export | Exportar ciclos pendentes em envelope versionado ou exportação própria, sem aplicá-los silenciosamente; testar restauração offline completa. |
| A03 | Média | Treino misto verifica lacunas só no primeiro tópico selecionado. Pode iniciar itens de outro tópico com lacuna aberta, contrariando a recuperação antes da cobrança. | app.js:beginQuiz | Avaliar todos os tópicos elegíveis e excluir/encaminhar os que possuem lacuna antes de montar a rodada. Simulado diagnóstico deve continuar com regra própria explícita. |
| A04 | Média | Importação de backup com mesmo ID e payload diferente mantém o original sem alertar conflito. É preservação contra sobrescrita, mas a mensagem de sucesso pode ocultar que a outra versão foi ignorada. A sincronização cloud já rejeita esse conflito. | core.js:merge/Store.restore | Aplicar verificação de conflito também à importação e mostrar prévia/resultado; nunca substituir o original automaticamente. |
| A05 | Média | Snapshot importado aceita sourceRef.url com protocolo não HTTPS; source() escapa caracteres, mas não restringe protocolo antes de criar href. A reprodução usou javascript:void(0) inerte e não executou código no navegador. Trata-se de falta comprovada de validação, não de exploração demonstrada. | core.js:validate; app.js:source | Validar formato e protocolo de fontes importadas e renderizar somente URLs permitidas, preservando o texto histórico como dado quando inválido. |

Nenhum desses cinco pontos foi corrigido silenciosamente durante a auditoria. São pendências registradas para uma alteração específica, com migração/compatibilidade quando necessária. O pedido de auditoria não foi usado para reescrever o banco ou alterar o histórico.

## Publicação GitHub Pages

O endereço fornecido é https://andersonx553-beep.github.io/Jarvis-estudante/ . A leitura HTTP retornou index911bytes, Last-Modified28/10/202600:17:49UTC; firebase-client.js retornou404. Portanto, o endereço não entregava a correção Firebase atual.

PR#4 mesclado: https://github.com/andersonx553-beep/Jarvis-estudante/pull/4 . Commit89b1f1e40682efb17bd021dba46364bc8e1ad4ea; merge5214364e3fa41da5ba0a67ddb6f9a84988414a4b. Workflow .github/workflows/pages.yml instala dependências, testa, compila e sobe dist/ como artefato oficial.

Execução40690929936: build/job122825214408 concluído com sucesso, incluindo npm ci/test/build/test:dist/upload. Deploy/job122825388815 falhou antes de executar steps e não disponibilizou logs (404BlobNotFound). A causa detalhada não foi obtida pelo conector; não afirmar que se trata de uma proteção específica. Não houve rejeição de aprovação automática nesta ação: foi uma falha de execução no GitHub Actions.

A configuração mostrada pelo usuário ainda utiliza publicação por branch. Próximo ajuste administrativo: Settings→Pages→Build and deployment→Source→GitHub Actions, conforme o mecanismo que agora compila dist/. Depois, Actions→Publicar JARVIS no GitHub Pages→Run workflow na main. Se a execução continuar falhando, consultar a mensagem do job deploy/ambiente github-pages e corrigir a causa; não remover proteções indiscriminadamente. O conector do repositório não tem administração para alterar essa configuração.

O Site privado anterior está publicado separadamente com a v1.8.1. Isso não significa que o endereço GitHub Pages foi atualizado. Nunca confundir merge, CI aprovada, upload de artefato e implantação concluída.

## O que já funciona e seus limites

| Área | Estado conferido | Limite ou falta |
|---|---|---|
| Método | Teoria/exemplos, quatro itens juntos, correção após completar, confiança, causa, rubrica e evidências. | Entendimento autodeclarado; não há avaliação semântica de justificativas. Treino misto precisa A03. |
| Progresso | Novo ciclo sem importar marcas antigas; visto/consolidação/domínio separados; erros/notas/revisões e snapshots históricos. | A01/A02/A04; evitar sessões paralelas em abas até correção. |
| Simulados | Seleção sem repetição, pontuação simples/líquida, volume40–120 condicionado a desempenho/fadiga/concentração. | Progressão é heurística; dificuldade e resistência não têm calibração independente. |
| Planejamento | Referência semanal e recomendação por lacunas, revisões, dificuldade, prioridade Previdenciário/reforço Constitucional. | Não é agenda que redistribui automaticamente horários pessoais/atrasos; não cresce por mês. |
| Auth | E-mail/senha, cadastro/login/saída/recuperação; SDK servido pelo próprio app. Conta real apareceu no print do proprietário. | Não foi feito login com a senha do usuário. Google Sign-in não implementado. |
| Firestore | Separação por UID, eventos imutáveis, transações/deduplicação, paginação, fila offline e conflitos testados no emulador. | Regras publicadas foram relatadas pelo usuário; falta confirmar sessão real em dois aparelhos, resposta→sync→reabrir. |
| Backups | JSON validado/mesclado e exportação de continuidade. Quebras de linha do resumo foram verificadas e estão corretas. | A02/A04; quota localStorage e downloads dependem do navegador. Não há backup externo agendado. |
| Fontes | Referências oficiais e índice histórico de provas. | Não existe pesquisa automática de leis/notícias nem revisão jurídica independente de todo o banco. |
| JARVIS agente | Recomendador e diagnóstico por regras locais. | Não existe agente deIA conversacional, pesquisador online ou geração de conteúdo em tempo real no app. |
| Segurança | Regras por proprietário e negação de update/delete dos eventos, sem senha administrativa no frontend. | A05; limites/proteções de produção e AppCheck/cotas/alertas não foram auditados no console. Não declarar aplicação blindada. |
| Distribuição | SDK local, HTML independente e cache público da interface. | GitHub Pages ainda depende da implantação; HTML file:// permanece local; dados não migram sozinhos entre origens. |

## Ordem prática para concluir

1. Finalizar GitHub Pages e confirmar os arquivos corretos servidos no endereço público; autorizar o hostname andersonx553-beep.github.io no Firebase Auth, se necessário.
2. Corrigir A01 eA02 antes de depender de várias abas e de backup completo durante recebimento de novo ciclo.
3. Corrigir A03–A05 com testes que reproduzam os casos registrados, sem alterar IDs/respostas existentes.
4. Validar produção com a conta do proprietário: um registro de estudo, sincronização, reabertura e leitura em outro aparelho. Confirmar que outra conta não acessa os dados; testes destrutivos continuam só em emuladores.
5. Revisar conteúdo por matéria e vigência, começando Previdenciário e Constitucional; calibrar variações e dificuldade; aprofundar lacunas apontadas por provas reais.
6. Se desejado, implementar o agente online em etapa própria, com backend para credenciais, limites/custos e revisão de fontes. Isso não é requisito para continuar o estudo local.

## Repetir a auditoria técnica

```sh
npm ci
npm test
npm run build
npm run test:dist
npm run test:firebase
node tools/audit_app.cjs
```

A suíte Firebase precisa de Java21+ e usa somente demo-jarvis-estudante. O script de auditoria não acessa rede, arquivos de progresso do navegador nem produção. A evidência inclui hashes dos arquivos examinados; uma correção posterior exige repetir os casos e atualizar seus estados, sem apagar esta versão histórica do relatório.
