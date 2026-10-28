# Instruções obrigatórias do JARVIS Estudante

Leia `CODEX.md` antes de alterar este projeto. Ele é o registro operacional de contexto; o Git contém o histórico exato de alterações. Leia também o código diretamente afetado: o documento não substitui verificar a implementação.

- Trabalhe somente em `andersonx553-beep/Jarvis-estudante`. O `Almox.aqua` foi referência de instruções, somente leitura. Não o modifique nem copie credenciais, dados, regras ou configurações de seu banco.
- Faça apenas o pedido autorizado. Evite refatorações, dependências e mudanças de arquitetura sem necessidade. Preserve interface, rotas e funções já testadas.
- Use português do Brasil. Ícones em SVG, sem emojis na interface. Preserve os tokens de cores e os layouts aprovados.
- Não apague histórico, respostas, notas ou ciclos para facilitar uma correção. Não altere identificadores existentes de tópicos ou questões. Alterações significativas de conteúdo exigem versão e preservação da interpretação anterior.
- Não substitua o banco inteiro em uma sincronização. Eventos históricos são imutáveis; correções e diagnósticos geram novos eventos. Mudanças de esquema exigem migração versionada, backup e testes.
- Não publique backups, dados reais, credenciais, chaves administrativas, `.env` ou tokens no Git. Nada de Firebase/Cloudflare é herdado de outro projeto.
- O modo local deve continuar operando sem conta, internet ou IA. Nuvem é uma camada futura opcional, não condição para estudar.
- Questões de aprendizagem em rodadas de quatro; gabarito apenas após as quatro respostas. Rascunhos legados em duplas são preservados até a conclusão. Itens autorais não são questões reais CEBRASPE. Simulados cumulativos não devem repetir itens para preencher tamanho.
- Visto não é dominado. Não invente desempenho, percentuais de edital, notícias ou fontes. Novo ciclo começa zerado e preserva os anteriores.
- Rode `npm test` e `npm run build`. Confira as telas em 390×844, 768×1024 e 1366×900 e verifique ausência de rolagem horizontal. Verifique teclado, foco, temas e backups conforme a mudança.
- Antes de entregar, atualize o histórico no `CODEX.md`: pedido, arquivos, decisões, testes realmente executados, resultados e limitações. Não afirme testes ou publicações que não ocorreram.
- Escopo aprovado já autoriza implementação e correções necessárias. Peça confirmação somente para nova decisão material ou ação destrutiva fora do pedido; não bloqueie trabalho reversível por burocracia.

- Método vigente: v1.7 Cara a Cara com a Banca. Teoria antes da cobrança, auditoria por questões reais, lacunas por subtema e domínio funcional com rubrica de autocorreção. Nunca inferir compreensão só pela extensão da justificativa.
- Conteúdo v2: editar assets JSON em data/ e validar com python3 tools/compile_content.py. Não editar content.js gerado nem alterar content-legacy.js. Scripts editoriais organizam textos autorais; não devem multiplicar templates para inflar o banco.

- Firebase v1.8: ler docs/FIREBASE.md e testar npm run test:firebase em projeto demo com Java21+. Nunca usar produção nos testes. Preservar separação por UID, transferência explícita e eventos somente criação; a configuração Web pública não é credencial administrativa. Não afirmar ativação remota sem verificação.
