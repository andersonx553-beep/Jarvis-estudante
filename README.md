# JARVIS Estudante • INSS / CEBRASPE

Aplicativo responsivo, sem dependências, com conteúdo introdutório autoral e estudo orientado por evidências. Funciona no navegador, com dados locais. O código usa HTML, CSS e JavaScript; Java e Python não são necessários para executar o aplicativo.

## Começar

1. Abra o endereço publicado ou execute o projeto por um servidor estático.
2. Toque em **Começar Dia 1**, leia a aula, avance aos exemplos e responda às duas questões.
3. Corrija, classifique erros e encerre a sessão para registrar o fechamento.
4. Exporte o backup em **Configurações e backup** regularmente.

O aplicativo inicia com zero respostas, sessões e tópicos vistos. Não carrega progresso histórico do candidato. Os PDFs originais forneceram o método e a estrutura curricular, não resultados pré-preenchidos.

## Executar e verificar

Requer Node 18+ somente para build e testes. Não é necessário `npm install`.

```sh
npm test
npm run build
python3 -m http.server 8080 --directory dist
```

Abra `http://localhost:8080`. Para usar sem servidor, abra `dist/jarvis-estudante.html`, que reúne tudo em um arquivo. A disponibilidade de armazenamento em `file://` depende do navegador: prefira uma origem HTTPS estável e use backup para trocar de endereço ou aparelho. O progresso não fica embutido no HTML.

## Funções

- Dashboard sem números fictícios; trilha das sete disciplinas.
- 39 módulos introdutórios, 156 itens autorais, fontes e checklist de aprofundamentos.
- Teoria, exemplos, comparações, limites, oito passos de raciocínio e notas versionadas.
- Questões em duplas, confiança, justificativa, correção e diagnóstico.
- Banco de erros, revisões em 1/3/7/14 dias e recomendação por prioridade/desempenho.
- Simulados cumulativos, cronômetro, itens em branco, pontuação simples ou líquida configurável.
- Mapa de evidências, histórico entre ciclos, preferências e leitura em voz alta quando suportada.
- Exportação JSON, importação por mesclagem sem exclusão e resumo Markdown de continuidade.
- Temas, ajuste de texto, navegação por teclado e cache offline após acesso inicial em origem compatível.

## Limites reais

Os módulos são introduções autorais; não são uma apostila exaustiva, nem reprodução de questões oficiais. A referência é o edital histórico de 2022. A lista de aprofundamentos registra o restante a estudar; não inventa cobertura integral de edital vigente. Consulte o texto legal e as versões dos programas aplicáveis. O aplicativo não pesquisa notícias nem atualiza legislação automaticamente. Justificativas são guardadas, mas não avaliadas semanticamente por IA.

Dados do navegador podem ser apagados pelo usuário ou pelo sistema; exporte backups. Preferências são locais e mantidas ao importar. Uma importação mescla eventos e pode selecionar o ciclo mais recente importado. Não há Firebase, login, sincronização ou backend remoto nesta versão. O cronômetro mede tempo decorrido da atividade, incluindo eventual pausa entre acessos.

## Hospedar depois

`dist/` é a pasta estática pronta para Cloudflare Pages, Workers Assets ou GitHub Pages. Não há rotas de servidor: a navegação usa hash. O service worker só funciona em contextos permitidos pelo navegador. O ícone SVG é fornecido; a oferta de instalação varia por plataforma. Não há implantação automática no GitHub Pages nesta versão.

Leia `CODEX.md`, `AGENTS.md` e `PROMPT_CODEX_BACKEND.md` para continuidade e regras de preservação.
