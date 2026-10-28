# JARVIS Estudante • INSS / CEBRASPE

Aplicativo responsivo com modo local independente e conta opcional Firebase Authentication/Firestore (v1.8). Método v1.7 Cara a Cara com a Banca, catálogo de 290 pontos em 42 blocos e banco de 3.200 questões autorais. Interface em HTML/CSS/JavaScript; Python organiza e valida os assets editoriais.

## Começar

1. Abra a versão publicada ou execute por servidor estático.
2. Toque em **Começar estudo**, leia a teoria e os exemplos.
3. Registre a leitura e responda **quatro questões juntas**. Gabarito somente após o conjunto.
4. Corrija, confira a rubrica da justificativa e classifique as causas dos erros.
5. Confronte a base com as referências reais em **Cara a Cara com a Banca**. Registre e aprofunde lacunas.
6. Encerre a sessão; histórico e resumo ficam no aparelho. Exporte uma cópia em **Configurações e backup**.

Todos os pontos da nova trilha começam pendentes. Marcas de estudo dos PDFs não são importadas. O catálogo introdutório anterior permanece em arquivo para que backups, rascunhos e respostas antigos continuem legíveis. Um novo ciclo preserva todo o histórico.

## Executar e validar

Node22+ e Python3 para preparação. Para testes Firebase, execute npm ci e use Java21+. O build precisa de npm ci para empacotar o SDK Firebase junto ao app; os testes do núcleo não precisam dessas dependências; nada disso é necessário no celular.

```sh
npm ci
npm run content
npm test
npm run build
npm run test:dist
python3 -m http.server 8080 --directory dist
```

O compilador valida quotas, IDs, enunciados únicos, gabaritos booleanos e presença de fontes; não cria enunciados nem substitui revisão editorial. Os scripts em tools/editorial reconstroem assets a partir de textos redigidos individualmente. Depois de editar um asset, compile antes do build.

Use localhost:8080 ou o HTML independente gerado em dist/jarvis-estudante.html. No celular, prefira uma origem HTTPS estável: dados do navegador não ficam embutidos no HTML e não migram entre endereços sem backup.

## Conteúdo e método

- Previdenciário1.800; Português360; Administrativo320; Constitucional320; Informática160; RLM120; Ética120.
- 800 itens de fixação,1.600 de treino e800 reservados para avaliação. A reserva fica fora do treino até exposição em avaliação.
- 360 referências reais INSS2016,2022 e Guarulhos, com links para cadernos, microtemas e gabarito histórico. Não são reprodução integral de questões, nem declaração de gabarito atual.
- Cada ponto inclui teoria, exemplos, diferenças, limites, fontes e questões. Os temas amplos seguem exigindo aprofundamento e auditoria pela cobrança real.
- MicrosoftOffice no núcleo do edital-base retificado; LibreOffice preservado como repertório suplementar histórico.
- Rodadas de quatro na aprendizagem; simulados navegam em pares e só corrigem ao encerrar.
- Visto, consolidação e domínio funcional separados. A rubrica é autoavaliação: caracteres digitados não provam compreensão.
- Revisões1/3/7/14dias e recuperação de lacunas. Sábado com simulado e análise; domingo descanso na referência semanal.
- Progressão opcional40–120 considera desempenho, fadiga e concentração registrados; não cresce pelo calendário.

## Preservação e limites

Respostas novas guardam texto, gabarito, explicação e versão respondida. O conteúdo legado permanece imutável para interpretar eventos antigos. Notas, diagnósticos, auditorias e rubricas geram eventos, sem apagar respostas. Backups JSON são mesclados porID; preferências locais são mantidas.

O banco passou por preparação editorial porIA e checagem de fontes; não foi auditado por revisor jurídico independente. A base curricular é o edital histórico2022 retificado e o PDF fornecido, não uma afirmação sobre novo edital. Anulações e mudanças legislativas exigem cuidado nos itens reais; sua auditoria não gera automaticamente pontuação com gabarito histórico.

O app não pesquisa notícias nem atualiza leis sozinho. Não há agente deIA online. Firebase permite conta e sincronização opcionais após habilitar Authentication/Firestore e publicar as regras do projeto. O estudo local funciona sem esses serviços. Justificativas não recebem análise semântica automática. A teoria inicial de um ponto não é promessa de esgotar todas as nuances jurídicas.

LocalStorage tem limites e pode ser apagado pelo navegador. Falhas de gravação são informadas e os eventos em memória permanecem exportáveis. Exporte backups regularmente. Cronômetro mede tempo decorrido, inclusive pausas. Instalação PWA e armazenamento em file:// dependem do navegador.

## Hospedagem e continuidade

A pasta dist é estática e compatível com hospedagem HTTPS. A navegação usa hash. O service worker só armazena arquivos públicos. Respostas/notas são enviadas ao Firestore apenas no espaço da conta conectado. GitHubPages não está automaticamente habilitado.

Leia AGENTS.md e a atualização vigente no começo de CODEX.md. Veja docs/FIREBASE.md para ativação, regras, comandos, transferência do progresso e limites. PROMPT_CODEX_BACKEND.md registra o contrato de preservação para próximas evoluções. Não copiar a identidade .openai da demonstração para outro projeto.

## Conta opcional

Em Configurações e backup, conecte ao Firebase e crie/entre na sua conta por e-mail e senha. Cada conta tem um espaço separado no navegador. Transfira o histórico local somente após conferir o e-mail e baixar backup. A conta mantém uma cópia no aparelho e retoma o envio após reconexão. As regras precisam ser publicadas no projeto jarvis-estudante; esta configuração não é automática só por informar a chave pública.

Correção v1.8.1: o SDK12.11.0 é instalado por npm e incorporado no cliente pelo esbuild, servido pela própria hospedagem. O app não importa módulos de gstatic.com. As APIs de Authentication/Firestore ainda exigem internet quando conectadas; o modo local permanece independente.
