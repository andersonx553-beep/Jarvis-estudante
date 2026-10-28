# Validação da expansão v1.7

Data da entrega:27/10/2026. Conferência estrutural e funcional; não é revisão jurídica independente.

## Conteúdo

- 290aulas/pontos,42blocos,3.200questões autorais,IDs e textos normalizados únicos.
- Quotas exatas:Prev1.800;Português360;Const320;Adm320;Info160;RLM120;Ética120.
- Runtime distribui800fixação,1.600treino,800reserva, mantendo≥4itens não reservados por ponto.
- 39aulas/156itens legados preservados e360referências de provas oficiais, com15anulações sinalizadas.
- Seis scripts editoriais reproduzem os assets usando manifesto local. RLM tem79verificações computacionais vinculadas a itens.
- Compilador valida fontesHTTPS/localizadores,IDs,duplicatas exatas,booleanos,campos teóricos e versões. Não certifica veracidade jurídica nem diversidade conceitual por si só.

## Testes

22testes Node passaram: catálogo,persistência,backup inválido,mesclagem,novo ciclo,falhas de gravação,dados corrompidos,recomendação,rubrica,cobertura,lacunas,reserva,snapshot histórico,auditoria real,progressão do simulado e ausência de repetição.

Build gera site eHTMLindependente sem npm install. Scripts de sintaxe foram conferidos. Dados dos testes ficaram somente no navegador/local deQA, fora do repositório.

## Fluxos observados no navegador

- Início zerado:0/290vistos,0respostas,0sessões; prioridadePrev.
- Botão de questões bloqueou cobrança antes do registro da leitura; exemplos e quatro itens exibidos. Correção desabilitada com respostas faltantes e sem gabarito antecipado.
- Quatro respostas,3acertos/1erro,justificativas,diagnósticoAtenção,rubrica com4critérios e encerramento da sessão.
- Uma falha de referência à lista causes na correção foi identificada e corrigida. Recarregar recuperou as4respostas gravadas e sua correção; o fluxo completo foi concluído depois do ajuste.
- Auditoria real registrou lacuna sem converter gabarito histórico em nota; referência anulada claramente sinalizada.
- Simulado40itens,20páginas,correção só ao final,40em branco preservados; fadiga2/concentração4 registradas.
- Download JSON real:55eventos,44tentativas com snapshots,2sessões com resumo,4rubricas,1diagnóstico,1auditoria,1lacuna,1avaliação e1leitura. Importação do mesmo arquivo mesclou sem duplicar; dashboard continuou2sessões/44itens.
- HTMLindependente abriu corretamente na mesma origem deQA; tema claro inspecionado e tema escuro preservado.
- Menu móvel:aberto sem inert;fechado com inert. Tab no último botão do modal retornou ao botãoFechar;Escape fechou. Tema e preferências continuam locais.

## Responsividade

Conferidas as telas início,plano,catálogoPrev,aula,banca real,questões,banco de erros,simulado,mapa,fontes,configurações em iframes390×844,768×1024e1366×900. Nenhuma rolagem horizontal no documento interno:scrollWidth igualclientWidth. Larguras úteis375/753/1351quando há scrollbar;768/1366nas telas sem scrollbar vertical. Inspeção visual feita no navegador; não equivale a teste físico Android/iOS.

A prévia teve conexão recusada por serviço antigo. O serviço gerenciado foi parado/reiniciado e voltou a responder. Um timeout de carregamento do mapa nos três iframes simultâneos foi observado; a página carregou sem erro de aplicação e a medição foi concluída.

## Limites

Dificuldade é editorial, rubrica é autodeclarada e notícias não são pesquisadas automaticamente. IA online/Firebase/sincronização não estão implementados. LocalStorage tem quota do navegador e requer backups. O conteúdo usa fontes oficiais e checagem de elaboração porIA, sem certificação jurídica independente.
