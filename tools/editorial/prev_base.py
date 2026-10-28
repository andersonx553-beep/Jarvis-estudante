"""Assets autorais: regras, contrastes e casos distintos, sem reprodução de provas.

O script organiza itens escritos explicitamente. Não expande nomes ou números para
inflar o banco. Texto legal pode mudar: a revisão registrada não é parecer jurídico.
"""
from pathlib import Path
import json, re, collections
ROOT=Path(__file__).resolve().parents[2]
PLAN=json.loads((ROOT/'data/curriculum-plan.json').read_text())
rows=[r for r in PLAN['assuntos'] if r['disciplina']=='Previdenciário e legislação social' and int(r['id_planejamento'].split('-')[1][1:])<=7]
S={
'cf':('Constituição Federal','https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm'),
'c':('Lei 8.212/1991 — texto atualizado Câmara','https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.pdf'),
'p':('Lei 8.213/1991 — texto atualizado Câmara','https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.pdf'),
'r':('Decreto 3.048/1999','https://www.planalto.gov.br/ccivil_03/decreto/d3048.htm'),
'h':('INSS — histórico institucional','https://www.gov.br/inss/pt-br/acesso-a-informacao/institucional/institucional'),
'lin':('LINDB','https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm'),
'ctn':('Código Tributário Nacional','https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm'),
'lc':('Lei Complementar 150/2015','https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp150.htm'),
'rfb':('Lei 11.457/2007 — texto atualizado Câmara','https://www2.camara.leg.br/legin/fed/lei/2007/lei-11457-16-marco-2007-552186-normaatualizada-pl.html'),
'ec':('EC 103/2019','https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm'),
'lc187':('Lei Complementar 187/2021','https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp187.htm'),
'l9430':('Lei 9.430/1996','https://www.planalto.gov.br/ccivil_03/leis/l9430.htm')}
D={}
def add(key,source,locator,core,example,contrast,limit,text):
 qs=[]
 for line in text.strip().splitlines():
  line=line.strip()
  if not line:continue
  assert line[0] in '+-',(key,line)
  statement,why=line[1:].split('¦',1)
  qs.append((statement.strip(),line[0]=='+',why.strip()))
 D[key]=(source,locator,core,example,contrast,limit,qs)

add('B01-S01','h','Breve Histórico; O INSS',
'A evolução passou de proteção vinculada a empresas e categorias para um sistema constitucional integrado. Linha do tempo: Lei Eloy Chaves (1923), IAPs (anos 1930), LOPS (1960), INPS (1966), SINPAS (1977), Constituição (1988) e INSS (1990).',
'Uma questão que atribua a criação do INSS à Constituição de 1988 mistura a integração constitucional da seguridade com a criação administrativa de uma autarquia, ocorrida em 1990.',
'CAPs se vinculavam a empresas; IAPs, a categorias. A LOPS uniformizou legislação; o INPS unificou institutos. INSS não é o nome de todo o sistema de seguridade.',
'Marco histórico não significa que inexistiam quaisquer mecanismos de proteção anteriores.', '''
+A Lei Eloy Chaves é marco de 1923 ligado às caixas das empresas ferroviárias.¦O marco de 1923 se relaciona às CAPs ferroviárias, não à criação do INSS.
-As CAPs nasceram como institutos nacionais organizados por categoria profissional.¦A organização por categoria caracteriza os IAPs; as CAPs se vinculavam a empresas.
+A expansão dos IAPs ocorreu na década de 1930, por categorias profissionais.¦A mudança ampliou o modelo anterior, ainda com segmentação profissional.
-A LOPS de 1960 criou imediatamente o INSS pela fusão do INPS com o IAPAS.¦A LOPS unificou legislação; o INSS resultou da fusão de 1990.
+A unificação dos IAPs no INPS foi estabelecida em 1966.¦O Decreto-Lei 72/1966 é o marco da unificação institucional.
-SINPAS e INPS eram apenas duas siglas para a mesma autarquia.¦O SINPAS era um sistema de integração de entidades e funções, criado em 1977.
+A Constituição de 1988 integrou saúde, previdência e assistência na seguridade social.¦A integração constitucional ampliou a visão de proteção social para três áreas.
-A previdência brasileira surgiu apenas com a Constituição de 1988.¦Existiam instituições anteriores; 1988 marca a concepção constitucional integrada.
+O INSS foi criado em 1990 mediante a fusão do INPS com o IAPAS.¦A criação da autarquia é posterior à Constituição de 1988.
-O INSS foi formado pela fusão do SUS com os IAPs na década de 1930.¦SUS não foi uma das entidades da fusão; foram INPS e IAPAS em 1990.
+Uma linha cronológica que situe os IAPs antes do INPS respeita a evolução institucional.¦O INPS unificou os institutos existentes e, portanto, é posterior a eles.
-O caráter universal da seguridade atual torna historicamente incorreta a existência de cobertura segmentada por profissão.¦O modelo atual não apaga as fases históricas de segmentação.
''')
add('B01-S02','cf','arts. 194, 196, 201 e 203',
'Seguridade é o conjunto integrado de ações destinado a saúde, previdência e assistência. A saúde tem acesso universal; a assistência independe de contribuição e atende requisitos de necessidade; o RGPS tem caráter contributivo e filiação obrigatória nas hipóteses legais.',
'Uma pessoa sem contribuições pode utilizar o SUS. Para receber uma aposentadoria do RGPS, deve preencher requisitos previdenciários próprios; o mesmo fato não é exigido para toda prestação assistencial.',
'Assistência não é previdência sem desconto: são políticas distintas. Universalidade não equivale a benefício incondicional.',
'Seguro-desemprego e previdência não devem ser equiparados automaticamente: examine a prestação e seu regime jurídico.', '''
+A seguridade abrange ações dos poderes públicos e da sociedade.¦O art. 194 não limita as iniciativas ao Estado.
-Saúde e assistência são excluídas do conceito constitucional de seguridade.¦As duas áreas integram a seguridade juntamente com a previdência.
+O acesso ao SUS não depende de filiação prévia ao RGPS.¦Saúde é direito de todos; filiação previdenciária não é condição geral de acesso.
-O BPC é aposentadoria contributiva concedida pelo simples recolhimento mensal.¦O BPC é assistencial e depende de seus requisitos específicos.
+A assistência social é prestada independentemente de contribuição à seguridade.¦A ausência de contribuição não dispensa os demais requisitos legais da prestação.
-A filiação obrigatória ao RGPS é incompatível com seu caráter contributivo.¦Obrigatoriedade da filiação e financiamento contributivo coexistem.
+Atender uma pessoa pelo SUS não lhe concede, por si só, direito a pensão por morte.¦Cada área possui prestações e requisitos próprios.
-Toda pessoa pobre pode escolher qualquer benefício do RGPS sem satisfazer requisitos.¦Necessidade social não substitui requisitos de benefício previdenciário.
+A sociedade participa tanto do financiamento quanto das iniciativas de proteção social.¦A organização constitucional combina ações públicas e sociais.
-O pagamento de contribuição ao RGPS é requisito constitucional de todo serviço de saúde.¦A saúde é universal, sem essa exigência contributiva prévia.
+O INSS pode operacionalizar benefício assistencial sem alterar a natureza dessa prestação.¦Órgão pagador e natureza jurídica são critérios distintos.
-A Constituição reserva a proteção social exclusivamente aos empregados com carteira assinada.¦O sistema protege públicos distintos e possui categorias previdenciárias além do empregado.
''')
add('B01-S03','cf','arts. 194, parágrafo único, VII, 198, III, e 204, II',
'A gestão da seguridade é democrática e descentralizada, com participação quadripartite de trabalhadores, empregadores, aposentados e governo nos órgãos colegiados. Participação social, descentralização e integração não significam ausência de competências legais.',
'Um conselho que reúna os quatro segmentos exemplifica participação quadripartite; isso não transforma todos os usuários do sistema em servidores do INSS.',
'Participação da sociedade não é privatização obrigatória. Descentralização não equivale à inexistência de coordenação nacional.',
'Não transponha a composição de um conselho específico para todos os colegiados sem consultar sua lei.', '''
+A participação quadripartite inclui aposentados.¦Os aposentados aparecem expressamente ao lado dos demais três segmentos.
-A gestão constitucional da seguridade deve ser exclusivamente empresarial.¦O modelo exige participação de trabalhadores, empregadores, aposentados e governo.
+Descentralização e integração são compatíveis na organização da seguridade.¦A distribuição de gestão não elimina a articulação do sistema.
-Democracia administrativa dispensa a observância das competências dos órgãos.¦Participação não afasta legalidade ou competência.
+Órgãos colegiados são o espaço indicado no art. 194 para a gestão quadripartite.¦O dispositivo especifica participação nos colegiados.
-Contribuintes individuais não podem ser considerados trabalhadores na representação da seguridade.¦A Constituição não restringe o segmento trabalhador a empregados celetistas.
+A Constituição admite participação social no controle das ações de assistência.¦O art. 204 prevê participação da população na formulação e controle.
-A descentralização elimina a obrigação de financiamento pela União.¦Gestão descentralizada não elimina responsabilidades de financiamento.
+A participação da comunidade é diretriz da organização do SUS.¦O art. 198 inclui participação comunitária no sistema de saúde.
-Todo ato de concessão de aposentadoria exige votação dos quatro segmentos.¦Gestão colegiada não converte cada ato administrativo de benefício em votação quadripartite.
+Representação de trabalhadores e empregadores não substitui a presença do governo no modelo quadripartite.¦Os quatro segmentos são distintos no texto constitucional.
-A organização integrada exige que saúde, previdência e assistência tenham sempre a mesma autoridade executora.¦Integração não significa identidade de órgãos executores ou de competências.
''')
add('B01-S04','cf','arts. 194, parágrafo único, I, 196, 201 e 203',
'Universalidade da cobertura se relaciona aos riscos e contingências protegidos; universalidade do atendimento, ao alcance pessoal da proteção. O princípio orienta expansão e inclusão, mas opera junto à seletividade e aos requisitos específicos.',
'A proteção à maternidade trata de contingência; alcançar públicos urbanos e rurais trata de pessoas e grupos. Não se conclui daí que qualquer cidadão já tenha direito a toda prestação.',
'Cobertura olha o que se protege; atendimento olha quem é alcançado. As duas dimensões não eliminam a contributividade do RGPS.',
'Universalidade é objetivo da seguridade; não atribua automaticamente a todos os regimes idênticas regras de acesso.', '''
+A universalidade da cobertura se relaciona às contingências sociais protegidas.¦Ela examina os eventos e riscos que o sistema busca alcançar.
-Universalidade do atendimento significa dispensar carência em todas as aposentadorias.¦Objetivo constitucional não revoga requisitos legais de cada benefício.
+A dimensão pessoal da universalidade é destacada pela expressão atendimento.¦Atendimento trata da abrangência subjetiva da proteção.
-A universalidade torna inconstitucional o caráter contributivo do RGPS.¦A própria Constituição prevê simultaneamente universalidade e previdência contributiva.
+A proteção a novos riscos pode ampliar a cobertura do sistema.¦Cobertura corresponde ao conjunto de contingências alcançadas.
-Como o SUS é universal, todo beneficiário da saúde é segurado obrigatório do RGPS.¦Direito à saúde não define filiação previdenciária.
+Um sistema pode buscar universalidade e ainda selecionar prestações por critérios legais.¦Universalidade e seletividade devem ser interpretadas conjuntamente.
-Atendimento universal permite conceder pensão por morte sem a ocorrência de morte.¦A universalidade não elimina o fato gerador de cada benefício.
+Incluir grupos antes desprotegidos está relacionado à ampliação do atendimento.¦O foco é a extensão pessoal da proteção social.
-Universalidade da cobertura e do atendimento são expressões sem qualquer diferença de enfoque.¦A doutrina distingue a dimensão objetiva da subjetiva.
+A necessidade assistencial deve ser examinada segundo os requisitos da política correspondente.¦Atendimento amplo não se confunde com concessão indiscriminada.
-O princípio da universalidade autoriza o administrador a criar benefício sem lei.¦A expansão depende do regime normativo e do custeio constitucionalmente exigido.
''')
add('B01-S05','cf','arts. 194, parágrafo único, II, e 201, § 2º',
'Uniformidade e equivalência impedem proteção social inferior apenas pela condição rural. Uniformidade relaciona-se ao conjunto de prestações; equivalência à proteção proporcional e adequada. Não exigem igualdade absoluta de todas as formas de contribuição ou dos valores individuais.',
'Dois segurados, um urbano e outro rural, podem ter formas legais diferentes de comprovar atividade e contribuir. Isso não autoriza excluir o rural da proteção por pertencer ao campo.',
'Igual dignidade e equivalência protetiva não significam identidade de requisitos em toda hipótese.',
'Diferenciações legais justificadas devem ser analisadas no contexto constitucional, sem generalização de privilégio ou de exclusão.', '''
+O objetivo alcança populações urbanas e rurais.¦A Constituição menciona expressamente os dois grupos.
-Equivalência obriga todos os benefícios rurais a terem exatamente o valor de qualquer benefício urbano.¦Valores individuais dependem de regras de cálculo; não há identidade absoluta.
+A residência rural, isoladamente, não autoriza suprimir proteção social constitucional.¦O princípio combate desigualdade de proteção fundada apenas na condição rural.
-Uniformidade determina contribuição idêntica de todas as categorias de segurados.¦O princípio se refere à proteção; existem formas de custeio diferenciadas.
+Requisitos legais próprios da atividade rural podem coexistir com equivalência protetiva.¦Igualdade material admite tratamento conforme diferenças relevantes.
-A uniformidade permite criar assistência apenas para moradores urbanos, excluindo rurais por sua residência.¦A condição rural não legitima essa exclusão geral.
+Uniformidade e equivalência são objetivos da organização da seguridade.¦Não se limitam a um único benefício ou categoria de segurado.
-O princípio exige que toda pessoa rural seja classificada como segurada especial.¦O enquadramento exige requisitos legais da atividade e do regime de trabalho.
+Empregado rural e segurado especial não são categorias intercambiáveis.¦O princípio de proteção equivalente não apaga categorias jurídicas distintas.
-A existência de regras rurais específicas demonstra, por si só, violação da uniformidade.¦A especificidade justificada não equivale a proteção indevidamente inferior.
+Benefícios substitutivos do rendimento do trabalho submetem-se ao piso constitucional nas hipóteses legais.¦A garantia constitucional não depende de o segurado ser urbano ou rural.
-A equivalência dispensa o trabalhador rural de comprovar qualquer requisito do benefício.¦Ela assegura proteção, mas não suprime os requisitos aplicáveis.
''')
add('B01-S06','cf','arts. 194, parágrafo único, III, e 195, § 5º',
'Seletividade orienta a escolha das contingências e prestações cobertas; distributividade orienta a destinação social da proteção, buscando reduzir desigualdades. Esses objetivos convivem com universalidade e com a exigência de custeio.',
'Ao priorizar determinada prestação para quem apresenta maior necessidade social, o desenho legal pode materializar distributividade; não se trata de livre escolha pessoal do servidor.',
'Selecionar prestações não é discriminar arbitrariamente pessoas. Distribuir proteção não significa repartir igualmente todo benefício entre contribuintes.',
'Seleção e distribuição dependem dos critérios legais e constitucionais, não da preferência do agente público.', '''
+A seletividade relaciona-se à escolha das prestações que compõem a proteção social.¦O sistema seleciona legalmente contingências e instrumentos de proteção.
-Distributividade significa restituir a cada segurado exatamente tudo o que contribuiu.¦A proteção solidária não opera como simples devolução de poupança individual.
+A distributividade orienta a proteção para redução de desigualdades sociais.¦Seu enfoque é a função social da distribuição de benefícios e serviços.
-Seletividade autoriza o servidor a negar benefício previsto em lei por preferência pessoal.¦A seleção ocorre no desenho normativo, respeitada a legalidade administrativa.
+Universalidade e seletividade não são necessariamente incompatíveis.¦A universalidade é buscada mediante organização racional de prestações.
-A seletividade elimina o dever de financiar benefício recém-criado.¦A Constituição exige fonte de custeio total para criação, majoração ou extensão.
+Critérios legais de vulnerabilidade podem expressar distributividade em prestações assistenciais.¦A distribuição considera necessidades e finalidades da política social.
-Distributividade determina o mesmo pagamento a todas as pessoas, sem considerar requisitos.¦Não se trata de igualdade aritmética incondicional.
+Escolher quais riscos serão protegidos é enfoque distinto de definir a distribuição social da proteção.¦O primeiro destaca seletividade; o segundo, distributividade.
-A escassez de recursos autoriza excluir livremente os requisitos de proteção definidos pela Constituição.¦Limitações orçamentárias não conferem poder ilimitado de afastar direitos.
+A seletividade precisa ser aplicada sem discriminação arbitrária.¦O objetivo constitucional se submete à igualdade e às finalidades da seguridade.
-Um benefício criado por decisão individual do atendente atende à seletividade mesmo sem previsão normativa.¦Objetivo organizacional não concede competência legislativa ao atendente.
''')
add('B01-S07','cf','arts. 194, parágrafo único, IV, 201, § 4º',
'Irredutibilidade do valor dos benefícios é objetivo da seguridade. Na previdência há garantia específica de reajustamento para preservar o valor real conforme critérios legais. Não confunda valor nominal, poder de compra, aumento real e vinculação automática a determinado índice.',
'Manter o mesmo valor monetário em período inflacionário pode preservar o nominal e reduzir poder de compra. O reajuste legal busca enfrentar a perda real, sem prometer aumento real anual.',
'Proteção contra redução não significa incorporação definitiva de pagamento indevido nem impossibilidade de cessação legal do benefício.',
'A comparação deve considerar o direito à prestação e os critérios legais; não presuma imunidade a revisão de ilegalidade.', '''
+A irredutibilidade do valor dos benefícios integra os objetivos da seguridade.¦A garantia está expressa no art. 194.
-Irredutibilidade assegura aumento real anual obrigatório acima de qualquer inflação.¦Preservação de valor não equivale a ganho real obrigatório.
+Valor nominal e poder de compra são conceitos diferentes.¦Uma quantia monetária constante pode perder valor real pela inflação.
-A Constituição exige que todo benefício seja reajustado sempre pelo mesmo percentual do salário mínimo.¦O reajustamento deve observar os critérios legais aplicáveis.
+O art. 201 prevê reajustamento para preservar o valor real dos benefícios previdenciários.¦Há garantia específica no regime previdenciário.
-A irredutibilidade impede cessar benefício quando desaparece legalmente a condição que o sustentava.¦A garantia do valor não elimina hipóteses legais de cessação.
+A mera manutenção nominal não garante, por si só, preservação do poder aquisitivo.¦A inflação pode reduzir a quantidade de bens adquiridos.
-Todo erro de cálculo favorável ao segurado fica protegido contra revisão pela irredutibilidade.¦O princípio não transforma pagamentos ilegais em direitos definitivos automaticamente.
+Reajuste inflacionário e aumento real não são expressões equivalentes.¦O primeiro recompõe perda; o segundo acresce poder de compra.
-Benefício pago acima do mínimo deve necessariamente permanecer ligado ao número original de salários mínimos.¦Não existe vinculação constitucional geral a uma quantidade fixa de mínimos.
+A forma de reajuste deve ser identificada na legislação da prestação.¦Não se transporta automaticamente a regra de um benefício para todos os outros.
-A existência da garantia nominal afasta a regra previdenciária de preservação do valor real.¦As garantias coexistem, com alcance e fundamentos próprios.
''')
add('B01-S08','cf','arts. 194, parágrafo único, V e VI, e 195',
'Equidade no custeio procura repartir encargos de modo adequado às diferenças relevantes dos sujeitos. Diversidade da base distribui financiamento entre várias fontes. O financiamento constitucional envolve recursos públicos e contribuições de distintos agentes, com identificação contábil das receitas e despesas das áreas.',
'A contribuição do trabalhador e uma contribuição empresarial sobre receita possuem sujeitos e bases diferentes. Isso exemplifica diversidade, não pagamento duplo do mesmo tributo por uma única pessoa.',
'Equidade não é igualdade de alíquota para todos; diversidade não é liberdade para inventar tributos sem competência ou lei.',
'A seleção de base, alíquota e sujeito exige a norma pertinente e suas regras temporais.', '''
+A diversidade reduz a dependência do sistema de uma única fonte de receitas.¦A Constituição prevê financiamento por várias bases e sujeitos.
-Equidade exige necessariamente a mesma alíquota para empregado e empresa em qualquer situação.¦Equidade considera diferenças relevantes, sem igualdade aritmética obrigatória.
+Recursos orçamentários e contribuições sociais podem coexistir no financiamento.¦O art. 195 combina financiamento direto e indireto.
-Diversidade autoriza uma autarquia a criar livremente nova contribuição por portaria.¦Competência e legalidade tributárias continuam exigidas.
+A remuneração do trabalho não é a única base constitucional de financiamento.¦Receita, lucro e outras bases também aparecem no desenho constitucional.
-Diversidade da base significa que cada prestação é financiada por um só contribuinte identificado.¦O financiamento do sistema é social e plural, não individualização absoluta.
+A organização deve identificar receitas e despesas vinculadas às áreas da seguridade.¦A Constituição associa diversidade à identificação em rubricas contábeis específicas.
-O trabalhador sem remuneração contributiva no mês passa a dever automaticamente toda contribuição patronal.¦Sujeitos, fatos geradores e responsabilidades são definidos em lei.
''')
add('B01-S09','cf','art. 194, parágrafo único, VII',
'O caráter democrático e descentralizado é associado à gestão quadripartite nos órgãos colegiados. Memorize os quatro segmentos pelo papel: trabalhadores, empregadores, aposentados e governo. O modelo refere-se à administração da seguridade, não a um sistema de quatro poderes.',
'Excluir os aposentados de uma descrição dos quatro segmentos torna a descrição incompleta. Acrescentar Judiciário e Ministério Público como segmentos substitutos também altera a regra.',
'Quadripartite descreve representação social; não se confunde com os três Poderes ou com os entes federativos.',
'A expressão constitucional não fixa, sozinha, o número de cadeiras de cada conselho concreto.', '''
+Governo e aposentados são dois dos segmentos da gestão quadripartite.¦Os outros são trabalhadores e empregadores.
-Gestão quadripartite é a divisão entre União, estados, Distrito Federal e municípios.¦A regra enumera segmentos sociais, e não os quatro tipos de entes federativos.
+Trabalhadores e empregadores integram a representação constitucional.¦Ambos participam juntamente com aposentados e governo.
-O Ministério Público substitui os aposentados entre os quatro segmentos expressos.¦O art. 194 não enumera o Ministério Público nessa composição.
+O princípio é incompatível com gestão necessariamente fechada à participação social.¦A democracia administrativa exige abertura aos segmentos previstos.
-Quadripartição significa que todo conselho terá exatamente quatro membros.¦A Constituição enumera segmentos, não um número universal de cadeiras.
+Descentralização não retira dos agentes o dever de prestar contas.¦A distribuição de gestão deve preservar controle e responsabilidade.
-A gestão democrática torna facultativo obedecer às leis de benefícios.¦Participação social não afasta a legalidade.
''')

add('B02-S01','c','ementa, arts. 1º, 10 a 12; Lei 8.213/1991, ementa',
'O direito previdenciário disciplina proteção, beneficiários, financiamento e relações jurídicas previdenciárias. Constituição, leis, regulamentos e atos administrativos possuem funções e hierarquias diferentes. A autonomia didática não rompe a relação com direito constitucional, tributário, administrativo e processual.',
'Para contribuição, identifique a regra de custeio; para concessão de aposentadoria, identifique a regra de benefícios e eventuais normas constitucionais e transitórias.',
'Lei de custeio e lei de benefícios se complementam, mas não são sinônimos. Regulamento detalha execução sem contrariar a lei.',
'Uma lista de fontes não dispensa observar validade, vigência e competência de quem editou o ato.', '''
+A Lei 8.212 organiza a seguridade e institui o plano de custeio.¦Seu objeto central distingue-se do plano de benefícios da Lei 8.213.
-A Lei 8.213 é apenas um regulamento administrativo da Lei 8.212.¦As duas são leis ordinárias com objetos diferentes e complementares.
+A Constituição é fonte central das regras previdenciárias.¦Define estrutura, direitos e limites para legislação inferior.
-A autonomia didática permite ao direito previdenciário ignorar garantias constitucionais.¦A autonomia não rompe a submissão à Constituição.
+O regulamento auxilia a execução das leis previdenciárias.¦Seu papel executivo não o autoriza a revogar comandos legais válidos.
-Uma instrução normativa tem hierarquia superior à lei porque é mais específica.¦Especialidade não inverte a hierarquia normativa.
+Normas de custeio dialogam com o direito tributário.¦Contribuições sociais possuem regime jurídico tributário e regras próprias.
-Toda notícia de portal substitui o texto normativo como fonte vinculante.¦Notícia pode informar, mas não equivale à norma competente.
+Atos administrativos normativos precisam respeitar a competência do órgão editor.¦A validade do ato depende também de autoridade competente e fundamento legal.
-O direito previdenciário trata exclusivamente do valor de aposentadorias.¦Abrange vínculos, financiamento, benefícios, serviços e relações correlatas.
+A fonte aplicável deve ser vinculada ao problema concreto.¦Enquadramento, custeio e benefício podem exigir normas diferentes.
-A existência de uma cartilha oficial dispensa consultar a lei quando há divergência de conteúdo.¦Material explicativo não prevalece sobre norma hierarquicamente superior.
''')
add('B02-S02','lin','arts. 1º e 2º; CF, arts. 5º, XXXVI, e 195, § 6º',
'Validade, vigência e eficácia não são a mesma coisa. A norma pode prever entrada em vigor futura. Lei posterior revoga expressamente, por incompatibilidade ou por disciplinar inteiramente a matéria anterior, observadas as regras de convivência normativa. Hierarquia e competência precedem especialidade e cronologia.',
'Uma lei publicada hoje pode ter vigência futura. Uma portaria posterior não passa a prevalecer sobre lei apenas por ser mais nova.',
'Publicação não é necessariamente início imediato de todos os efeitos. Norma especial não é automaticamente revogada por toda norma geral posterior.',
'Contribuições sociais possuem regra constitucional de noventena; isso não autoriza generalizar o regime temporal a todo ato previdenciário.', '''
+A lei pode indicar uma data futura para entrar em vigor.¦A vigência depende da cláusula legal ou da regra supletiva da LINDB.
-Uma portaria posterior revoga lei anterior sempre que forem incompatíveis.¦A norma inferior não afasta a lei válida por simples posterioridade.
+Revogação pode ser expressa ou decorrer de incompatibilidade normativa.¦A LINDB reconhece diferentes formas de revogação.
-Validade e vigência são conceitos necessariamente idênticos.¦Validade se refere à conformidade jurídica; vigência, à inserção temporal da norma.
+A mera edição de norma geral não elimina automaticamente toda norma especial anterior.¦É preciso analisar compatibilidade e disciplina da matéria.
-O texto original de uma lei é suficiente mesmo quando há alterações vigentes.¦A aplicação exige identificar a redação pertinente ao período.
+A eficácia de determinada regra pode estar sujeita a uma condição temporal específica.¦Início de vigência e produção de todos os efeitos podem não coincidir.
-A noventena das contribuições sociais corresponde a noventa meses.¦O prazo constitucional é de noventa dias da publicação da lei que institui ou modifica a contribuição.
+A Constituição ocupa posição superior aos regulamentos administrativos.¦O regulamento deve respeitar limites constitucionais e legais.
-A norma mais conveniente ao servidor prevalece na solução de antinomia.¦Antinomias exigem critérios jurídicos, não conveniência individual.
+A revogação da lei revogadora não restaura automaticamente a primeira lei.¦A repristinação depende de disposição em contrário, conforme a LINDB.
-Toda cláusula de vigência dispensa o respeito às limitações constitucionais de cobrança.¦A norma inferior não pode afastar limitações temporais da Constituição.
''')
add('B02-S03','lin','arts. 4º e 5º; CTN, art. 108',
'Interpretar é determinar o sentido de norma existente. Integrar é suprir lacuna pelos instrumentos juridicamente admitidos. A LINDB menciona analogia, costumes e princípios gerais; no campo tributário, o CTN impõe limites próprios, inclusive vedação de exigir tributo não previsto em lei por analogia.',
'Aplicar uma regra de contribuição a situação diferente apenas porque parece parecida não autoriza criar incidência tributária sem base legal.',
'Interpretação não equivale a criação livre do direito; analogia não pode superar limitações específicas de legalidade.',
'Na questão, identifique se há dúvida de sentido ou lacuna, e se a matéria envolve contribuição, benefício ou sanção.', '''
+A interpretação pode considerar o contexto sistemático da norma.¦O dispositivo deve ser lido em conjunto com as normas pertinentes.
-Analogia autoriza exigir contribuição sobre fato não previsto em lei.¦O CTN veda que analogia resulte na exigência de tributo não previsto em lei.
+A integração pressupõe lacuna a ser enfrentada juridicamente.¦Não se confunde com simples identificação do sentido de texto existente.
-Costume contrário à Constituição sempre revoga o texto constitucional.¦Prática social não revoga norma constitucional válida.
+A LINDB indica analogia, costumes e princípios gerais do direito diante de omissão da lei.¦São instrumentos de integração, respeitados os limites do ordenamento.
-Interpretar literalmente é suficiente para ignorar finalidade e sistema em qualquer hipótese.¦A interpretação jurídica não se reduz universalmente à leitura isolada de palavras.
+A finalidade social e o bem comum são referências de aplicação na LINDB.¦O art. 5º orienta a aplicação da lei por essas finalidades.
-O recurso à equidade pode dispensar o pagamento de tributo devido.¦O CTN estabelece que a equidade não pode resultar nessa dispensa.
+No custeio, a integração deve respeitar a legalidade tributária.¦Instrumentos integrativos não autorizam criar obrigação tributária sem suporte legal.
-Interpretar uma palavra e preencher lacuna são sempre a mesma operação.¦Interpretação e integração possuem enfoques diferentes.
+Princípios auxiliam a compreensão de regras previdenciárias sem eliminar requisitos legais.¦A atuação principiológica deve considerar a estrutura normativa.
-Uma analogia favorável permite conceder qualquer benefício sem fonte de custeio.¦A criação, majoração ou extensão de benefício está sujeita ao art. 195, § 5º.
''')
add('B02-S04','cf','art. 5º, XXXVI; Lei 8.212/1991, art. 85-A; LINDB, art. 6º',
'A regra aplicável depende da data do fato e da situação jurídica formada. Direito adquirido, ato jurídico perfeito e coisa julgada recebem proteção constitucional. A aplicação territorial admite particularidades e acordos internacionais; territorialidade não significa proibição absoluta de efeitos no exterior.',
'Quem já preencheu todos os requisitos legais para determinada aposentadoria deve ter sua situação distinguida daquela de quem apenas iniciou contribuições sob regra antiga.',
'Expectativa de direito e direito adquirido não se confundem. Residir no exterior não decide sozinho a filiação ou a proteção por acordo.',
'Acordos internacionais têm objeto e condições próprias; não presume contagem automática de qualquer período estrangeiro.', '''
+A identificação da data do fato relevante pode alterar a norma de benefício aplicável.¦Direito intertemporal exige observar o momento de formação dos requisitos.
-O início das contribuições garante que todas as regras futuras permaneçam para sempre inalteradas.¦O início do vínculo não equivale a direito adquirido a todo regime jurídico.
+Direito adquirido e mera expectativa devem ser distinguidos.¦A proteção depende da situação já consolidada segundo os requisitos legais.
-Uma lei nova desfaz automaticamente coisa julgada anterior apenas por ser mais recente.¦A Constituição protege a coisa julgada, observadas as vias jurídicas próprias.
+A Constituição protege o ato jurídico perfeito.¦A proteção integra o art. 5º, XXXVI, juntamente com direito adquirido e coisa julgada.
-A norma previdenciária brasileira jamais produz efeitos para pessoa no exterior.¦Há hipóteses legais extraterritoriais e acordos internacionais.
+Acordos internacionais previdenciários exigem leitura de suas condições específicas.¦Países envolvidos, prestações e procedimentos não são presumidos.
-Todo tempo trabalhado no exterior deve ser somado automaticamente, mesmo sem base normativa.¦A contagem depende do regime aplicável e dos instrumentos admitidos.
+A lei em vigor tem efeito imediato e geral, respeitadas as proteções da LINDB.¦Efeito imediato não significa retroatividade ilimitada.
-A norma nova sempre se aplica retroativamente por beneficiar o interessado.¦Não existe regra geral de retroatividade irrestrita para todo benefício previdenciário.
+Cumprir todos os requisitos de um direito antes da mudança é relevante para examinar direito adquirido.¦A análise não pode ser substituída pela simples data do requerimento.
-A territorialidade é argumento suficiente para ignorar qualquer acordo internacional previdenciário.¦Acordos integram a disciplina jurídica pertinente e têm tratamento específico.
''')

add('B03-S01','p','arts. 11 a 13; Decreto 3.048/1999, arts. 9º a 11',
'Filiação obrigatória decorre de atividade remunerada legalmente enquadrada. As categorias são empregado, doméstico, contribuinte individual, avulso e especial. A realidade da atividade é decisiva. Uma pessoa pode ter múltiplos vínculos; o aposentado que exerce atividade abrangida volta a ser contribuinte obrigatório nessa atividade.',
'Quem trabalha subordinadamente para uma loja não vira facultativo por escolher esse código na guia. Um aposentado que retoma atividade remunerada abrangida também não fica dispensado do custeio.',
'Pessoa física segurada não é a mesma coisa que empresa responsável pelo recolhimento. Categoria decorre de fatos, não de escolha livre.',
'Ausência de remuneração e trabalho voluntário exigem análise própria; nem toda atividade humana gera filiação obrigatória.', '''
+O exercício de atividade abrangida pode gerar filiação antes do cadastro administrativo.¦Para o obrigatório, o vínculo jurídico decorre do exercício da atividade enquadrada.
-Uma empresa com personalidade jurídica é segurada empregada do RGPS.¦As categorias de segurados obrigatórios referem-se a pessoas físicas.
+O aposentado que retorna a atividade sujeita ao RGPS é segurado obrigatório em relação a ela.¦A aposentadoria não afasta a contribuição sobre a nova atividade abrangida.
-O trabalhador pode escolher ser facultativo mesmo exercendo atividade que o enquadre como obrigatório.¦A opção não elimina o enquadramento imposto pelos fatos e pela lei.
+Empregado doméstico é categoria própria de segurado obrigatório.¦Seu vínculo não se confunde com o empregado de empresa.
-Toda pessoa rural é necessariamente segurada especial.¦O enquadramento depende dos requisitos específicos da atividade rural.
+A atividade por conta própria pode enquadrar a pessoa como contribuinte individual.¦Há diversas hipóteses legais dessa categoria.
-A existência de remuneração basta para transformar todo trabalhador em empregado.¦Subordinação e demais requisitos distinguem empregado de outras categorias.
+O enquadramento precisa considerar como o serviço é prestado.¦Rótulo contratual não substitui a situação real.
-Uma declaração privada pode dispensar permanentemente a filiação obrigatória prevista em lei.¦A vontade das partes não afasta obrigação legal de enquadramento.
+Quem mantém duas atividades abrangidas é filiado em relação a cada uma delas.¦A lei disciplina filiação em cada atividade, observados os limites contributivos aplicáveis.
-O trabalhador avulso deixa de ser obrigatório porque não possui vínculo permanente com um tomador.¦Ausência desse vínculo é compatível com a categoria de avulso.
+A pessoa que passa a atividade remunerada obrigatória deve adequar sua categoria contributiva.¦Não pode continuar tratada como facultativa em relação à atividade.
-O RGPS admite apenas empregados urbanos como segurados obrigatórios.¦O regime abrange outras categorias e atividades urbanas e rurais.
+Um prestador autônomo não se torna pessoa jurídica apenas por contribuir ao RGPS.¦Natureza do sujeito e enquadramento previdenciário são análises distintas.
-A falta de recolhimento pelo empregador impede sempre a filiação do empregado.¦A filiação obrigatória não nasce do ato de recolhimento patronal.
+A categoria do segurado influencia base e responsabilidade pelo custeio.¦Regras de contribuição variam segundo o enquadramento legal.
-A inscrição equivocada em uma categoria torna corretos os fatos de enquadramento.¦O cadastro deve refletir a atividade, podendo exigir correção.
+Uma atividade voluntária sem remuneração não se confunde automaticamente com trabalho segurado obrigatório.¦É preciso verificar a existência dos requisitos legais da atividade remunerada.
-A filiação obrigatória é sempre resultado de aprovação em concurso público.¦O RGPS abrange atividades privadas e vínculos públicos previstos em lei.
''')
add('B03-S02','p','art. 11, I; Lei 8.212/1991, art. 12, I',
'Empregado presta serviço urbano ou rural à empresa de modo não eventual, subordinado e remunerado. A categoria alcança hipóteses especiais previstas em lei, como trabalho temporário e diretor empregado. A inscrição ou o nome do contrato não prevalecem contra os fatos.',
'Uma pessoa cumpre ordens e jornada não eventual em empresa, mediante remuneração. Chamá-la de consultora não encerra o exame do vínculo.',
'Empregado e contribuinte individual diferem pela relação de trabalho. Diretor empregado não é o mesmo que diretor não empregado.',
'Os casos internacionais e de agentes públicos dependem dos requisitos específicos das alíneas legais.', '''
+O empregado pode exercer atividade rural.¦A definição legal abrange serviço urbano ou rural.
-A condição de empregado exige serviço eventual como requisito central.¦A definição exige caráter não eventual, além de subordinação e remuneração.
+A subordinação é um elemento do enquadramento como empregado.¦Ela distingue essa categoria de várias formas de trabalho autônomo.
-O diretor empregado deve ser necessariamente contribuinte individual.¦A lei o inclui entre empregados quando presentes os requisitos dessa condição.
+O trabalhador contratado por empresa de trabalho temporário pode ser empregado para fins previdenciários.¦A hipótese é expressamente prevista na categoria.
-Empregado recebe benefício de filiação somente após o empregador optar por cadastrá-lo.¦A atividade enquadrada gera filiação obrigatória.
+Contrato denominado autônomo não impede o reconhecimento do enquadramento real como empregado.¦A análise depende das características concretas da relação.
-Quem trabalha por conta própria sem subordinação é sempre empregado por receber pagamento.¦Remuneração isolada não satisfaz todos os requisitos do emprego.
+O salário pago por tempo à disposição pode integrar a relação remunerada de emprego.¦O trabalho subordinado não se reduz às horas de produção material efetiva.
-Empregado da iniciativa privada passa ao RPPS porque presta serviço em prédio público terceirizado.¦O local da prestação não o torna titular de cargo efetivo amparado por RPPS.
+Serviço não eventual em loja pode configurar emprego ainda que a remuneração inclua comissões.¦A forma variável de remuneração não afasta, sozinha, a categoria.
-A falta de assinatura da carteira elimina definitivamente a condição previdenciária de empregado.¦O vínculo pode ser comprovado pelos meios legalmente admitidos.
+O brasileiro ou estrangeiro domiciliado e contratado no Brasil para sucursal nacional no exterior tem hipótese legal de emprego no RGPS.¦A lei contempla esse enquadramento extraterritorial específico.
-A definição previdenciária de empregado se limita ao trabalhador industrial.¦Ela abrange diferentes setores e hipóteses legais.
+A empresa tem obrigações contributivas relativas aos empregados a seu serviço.¦O enquadramento implica deveres de arrecadação e custeio nos termos da lei.
-O empregado pode afastar sua contribuição assinando renúncia particular à aposentadoria.¦A contribuição decorre de lei e não de opção por benefício futuro.
''')
add('B03-S03','lc','art. 1º; Lei 8.213/1991, art. 11, II',
'O emprego doméstico exige prestação contínua, subordinada, onerosa e pessoal, de finalidade não lucrativa, à pessoa ou família no âmbito residencial, por mais de dois dias por semana. A mesma atividade material pode ter categoria diferente conforme o tomador e a finalidade.',
'Limpar uma residência familiar em três dias semanais, presentes os demais requisitos, pode caracterizar emprego doméstico. Limpar quartos de hotel é atividade prestada a empresa com finalidade econômica.',
'Doméstico e diarista por conta própria não se distinguem apenas pelo nome escolhido. Residência usada como atividade lucrativa exige examinar os fatos.',
'A frequência é requisito importante, mas não substitui pessoalidade, subordinação, onerosidade e finalidade não lucrativa.', '''
+O serviço doméstico é prestado à pessoa ou família para finalidade não lucrativa.¦A finalidade da atividade e o tomador compõem a definição legal.
-Uma pessoa contratada para limpar hotel comercial é doméstica apenas porque executa limpeza.¦Limpeza em empreendimento econômico não se torna doméstica pela tarefa material.
+Mais de dois dias por semana integra a definição da LC 150.¦A continuidade doméstica possui esse critério legal.
-Dois dias semanais bastam, em qualquer caso, para satisfazer o requisito legal de mais de dois dias.¦A expressão legal exige frequência superior a dois dias na semana.
+O empregado doméstico é segurado obrigatório do RGPS.¦A categoria possui previsão específica na legislação previdenciária.
-O trabalho doméstico é facultativo para fins previdenciários porque ocorre em residência.¦Local residencial não afasta a filiação obrigatória quando preenchidos os requisitos.
+Cuidador contratado por família pode se enquadrar como doméstico se presentes os requisitos.¦A categoria não se limita à função de limpeza.
-Todo prestador que entra em residência particular é empregado doméstico.¦Prestação autônoma e eventual não satisfaz automaticamente a definição.
+O vínculo doméstico exige pessoalidade.¦O serviço deve ser pessoalmente prestado nos termos da relação de emprego.
-Finalidade lucrativa é requisito indispensável do emprego doméstico.¦A definição doméstica exige finalidade não lucrativa da prestação ao tomador.
+O empregador doméstico possui obrigações próprias no sistema de arrecadação.¦A natureza familiar não elimina os encargos legais.
-Um contrato chamado de diarista impede o exame de subordinação e frequência.¦O nome contratual não afasta análise dos fatos.
+A onerosidade diferencia o emprego doméstico de ajuda familiar gratuita.¦A relação empregatícia pressupõe remuneração.
-O doméstico é considerado trabalhador avulso porque atende necessidade familiar.¦São categorias distintas com requisitos próprios.
+A exclusividade em uma única residência não é, por si só, o critério legal completo.¦O vínculo depende do conjunto de requisitos, não apenas do número de tomadores.
-A pessoa pode ser doméstica mesmo quando presta serviços diretamente a uma sociedade empresarial com fins econômicos.¦O tomador doméstico é pessoa ou família na hipótese legal não lucrativa.
''')
add('B03-S04','p','art. 11, V; Lei 8.212/1991, art. 12, V',
'Contribuinte individual reúne hipóteses variadas de atividade remunerada sem enquadramento em outra categoria obrigatória: trabalho por conta própria, prestação eventual a empresas, ministro de confissão religiosa e diretor não empregado, entre outras situações legais. Autonomia não significa ausência de contribuição.',
'Uma profissional autônoma pode prestar serviços a pessoas físicas e a empresas. A categoria pode ser a mesma, mas responsabilidade por retenção e recolhimento varia conforme o tomador e a norma.',
'Contribuinte individual não é facultativo. Diretor não empregado não se confunde com diretor empregado.',
'O regime do MEI e as formas simplificadas possuem condições próprias; não generalize seus percentuais a todos os contribuintes individuais.', '''
+A pessoa que exerce atividade econômica por conta própria pode ser contribuinte individual.¦A lei inclui trabalho autônomo nas hipóteses dessa categoria.
-O contribuinte individual só se filia se desejar receber aposentadoria no futuro.¦A atividade remunerada enquadrada gera filiação obrigatória.
+O ministro de confissão religiosa integra hipótese legal de contribuinte individual.¦A categoria está expressamente contemplada na legislação.
-Todo contribuinte individual é empresário constituído como pessoa jurídica.¦O segurado é pessoa física e a categoria inclui diferentes atividades.
+Diretor não empregado e diretor empregado podem ter enquadramentos distintos.¦A presença ou ausência de relação empregatícia altera a classificação.
-Quem presta serviço eventual a empresa jamais pode ser segurado obrigatório.¦A prestação eventual pode enquadrar-se como contribuinte individual.
+A autonomia na prestação não dispensa obrigações previdenciárias.¦O trabalho por conta própria possui disciplina contributiva.
-A contratação por pessoa física torna qualquer profissional empregado doméstico.¦Exigem-se os requisitos específicos do vínculo doméstico.
+A mesma pessoa pode ter atividade de contribuinte individual e outra de empregado.¦Atividades concomitantes são examinadas individualmente.
-Um recolhimento como facultativo corrige automaticamente a categoria de quem trabalha por conta própria.¦É necessário identificar e, se pertinente, regularizar a categoria correta.
+Prestação remunerada sem vínculo de emprego pode gerar contribuição mesmo sem salário mensal fixo.¦Remuneração variável não exclui a atividade da disciplina previdenciária.
-O aposentado que atua como autônomo fica sempre dispensado das contribuições dessa atividade.¦O retorno a atividade abrangida gera obrigatoriedade contributiva.
+A forma de arrecadação pode variar conforme o serviço seja prestado a empresa ou a pessoa física.¦Categoria e responsável pelo recolhimento não são análises idênticas.
-Ser contribuinte individual garante automaticamente toda prestação sem carência ou demais requisitos.¦O enquadramento não dispensa os requisitos próprios dos benefícios.
+O empresário que trabalha remuneradamente pode se enquadrar como contribuinte individual nas hipóteses legais.¦A atuação pessoal remunerada precisa ser distinguida da titularidade puramente patrimonial.
-A mera propriedade de ações, sem exercício de atividade remunerada, prova sempre filiação obrigatória como contribuinte individual.¦A condição de investidor não equivale automaticamente ao exercício de atividade enquadrada.
''')
add('B03-S05','p','art. 11, VI; Decreto 3.048/1999, art. 9º, VI',
'Trabalhador avulso presta serviços a diversas empresas sem vínculo empregatício, com intermediação legal do sindicato ou órgão gestor de mão de obra, conforme a atividade. A categoria alcança hipóteses portuárias e não portuárias disciplinadas em lei; não equivale a qualquer bico autônomo.',
'A intermediação do OGMO em trabalho portuário sem vínculo empregatício pode caracterizar avulso. Um prestador autônomo contratado diretamente não se torna avulso apenas por trabalhar para muitos clientes.',
'Ausência de vínculo com o tomador não elimina proteção obrigatória. Avulso e contribuinte individual não são sinônimos.',
'A intermediação e as atividades admitidas devem ser confirmadas no regime legal correspondente.', '''
+O avulso integra as categorias de segurados obrigatórios.¦Não depende de filiação facultativa para a atividade enquadrada.
-A falta de vínculo empregatício torna o avulso estranho ao RGPS.¦A categoria possui cobertura obrigatória própria.
+Intermediação legal é elemento relevante para diferenciar avulso de autônomo comum.¦O enquadramento não resulta apenas de atender vários clientes.
-Qualquer profissional que faça trabalho eventual é automaticamente avulso.¦É preciso observar intermediação e hipóteses legais.
+O trabalho avulso pode abranger hipóteses não portuárias previstas em lei.¦A categoria não é universalmente limitada aos portos.
-OGMO é o órgão de concessão de aposentadorias do RGPS.¦O órgão gestor de mão de obra exerce funções relacionadas ao trabalho portuário, não substitui o INSS.
+O avulso pode prestar serviços a diversos tomadores.¦Isso é compatível com a estrutura da categoria.
-A intermediação por sindicato transforma necessariamente o avulso em empregado do sindicato.¦Intermediação não significa, por si só, vínculo de emprego com a entidade.
+A responsabilidade de arrecadação do avulso tem disciplina própria.¦A legislação atribui deveres aos sujeitos envolvidos na intermediação e contratação.
-Trabalhador com emprego permanente em empresa portuária é avulso apenas por trabalhar no porto.¦Local de trabalho não substitui os requisitos da categoria.
+Trabalhador avulso e empregado podem ter enquadramentos diferentes apesar de realizar tarefas semelhantes.¦A relação jurídica e a forma de contratação são decisivas.
-O avulso pode renunciar à filiação obrigatória por declaração ao OGMO.¦A filiação decorrente da atividade legal não é afastada por renúncia privada.
+A ausência de contrato individual permanente com um tomador é compatível com a categoria.¦O trabalho é organizado conforme a intermediação prevista em lei.
-Atender diretamente três clientes por conta própria basta para provar trabalho avulso.¦A multiplicidade de clientes não dispensa os demais elementos legais.
+O enquadramento do avulso exige examinar a atividade efetivamente exercida.¦Não basta o uso da palavra avulso em recibo ou contrato.
-A remuneração do avulso nunca integra base contributiva porque não se chama salário.¦A legislação previdenciária disciplina salário de contribuição dessa categoria.
''')
add('B03-S06','p','art. 11, VII e §§ 1º, 6º a 12',
'Segurado especial exige enquadramento legal em atividade rural ou pesca artesanal, individualmente ou em regime de economia familiar, conforme requisitos. Economia familiar envolve trabalho indispensável à subsistência e ao desenvolvimento socioeconômico do núcleo, em mútua dependência e colaboração. Nem todo trabalhador rural é especial.',
'Produtor que explora área rural deve ser analisado quanto à atividade, área, mão de obra e demais condições legais. Apenas declarar-se agricultor não substitui esse exame.',
'Empregado rural, produtor contribuinte individual e segurado especial são categorias diferentes. Participação familiar não equivale a filiação de qualquer parente sem atividade.',
'A lei admite exceções e condições específicas para receitas e atividades paralelas; não use a fórmula toda renda externa exclui em qualquer caso.', '''
+O regime de economia familiar exige colaboração e dependência entre os membros que exercem a atividade.¦O conceito está vinculado à atividade indispensável do grupo familiar.
-Toda pessoa que reside em imóvel rural é segurada especial.¦Residência isolada não comprova atividade e requisitos legais.
+O pescador artesanal pode se enquadrar como segurado especial.¦É uma das hipóteses legais, atendidas suas condições.
-Empregado rural é sempre segurado especial por trabalhar na agricultura.¦O vínculo empregatício gera categoria própria de empregado.
+A lei disciplina limites e condições para uso de mão de obra no enquadramento especial.¦Não se pode afirmar que qualquer contratação é irrelevante.
-A mera propriedade de terreno rural garante, sem atividade, a condição de especial.¦O enquadramento depende do exercício da atividade legal.
+O trabalho do membro familiar deve ser examinado, e não apenas seu parentesco.¦A filiação não decorre automaticamente da relação familiar.
-Toda renda de origem externa exclui invariavelmente a categoria, sem exceções legais.¦A lei prevê hipóteses de renda e atividades que não descaracterizam, respeitadas condições.
+O produtor rural pode ser contribuinte individual quando não atende às condições do especial.¦Trabalho rural não implica enquadramento único.
-Ter inscrição no cadastro basta para afastar a prova das condições de segurado especial.¦Cadastro e requisitos materiais são dimensões distintas.
+O grupo familiar pode exercer a atividade em mútua colaboração.¦Essa estrutura é característica da economia familiar definida em lei.
-O segurado especial é uma pessoa jurídica rural distinta dos membros da família.¦O segurado obrigatório é pessoa física.
+A exploração individual pode ser compatível com o enquadramento especial.¦A lei admite exercício individual e em economia familiar.
-Um agricultor com empregados permanentes ilimitados deve ser considerado especial sem examinar condições legais.¦A mão de obra e demais requisitos precisam ser confrontados com os limites normativos.
+A prova da atividade e do período importa para os direitos vinculados à condição especial.¦O enquadramento não dispensa comprovação juridicamente adequada.
-A designação comercial de pequeno produtor substitui todos os requisitos previdenciários.¦Expressões informais não definem sozinhas a categoria legal.
''')
add('B03-S07','r','art. 11 e §§; CF, art. 201, § 5º',
'Facultativo é pessoa com idade mínima admitida de 16 anos que não exerce atividade que a enquadre como segurada obrigatória e se filia mediante contribuição. A inscrição formalizada com primeiro recolhimento válido produz o vínculo; não admite retroação livre. Participante de RPPS não pode, em regra, filiar-se facultativamente ao RGPS.',
'Estudante sem trabalho remunerado pode optar pela filiação facultativa se preencher as condições. Ao iniciar atividade remunerada obrigatória, deve adequar o enquadramento.',
'Facultatividade é da adesão de quem não está obrigado; não é liberdade para trocar a categoria de atividade remunerada.',
'A contribuição de baixa renda possui condições específicas e não se confunde com a definição geral do facultativo.', '''
+A filiação facultativa exige ausência de atividade que gere filiação obrigatória.¦Quem exerce atividade abrangida deve observar a categoria obrigatória correspondente.
-Qualquer empregado pode optar por facultativo para reduzir a contribuição do emprego.¦A vontade individual não substitui o enquadramento obrigatório.
+Estudante sem atividade remunerada pode ser facultativo se preencher os requisitos legais.¦Estudar não impede a adesão de quem não está obrigatoriamente filiado.
-A inscrição do facultativo, isoladamente e sem primeiro recolhimento válido, basta em toda hipótese para filiação.¦O regulamento vincula a formalização ao primeiro recolhimento.
+A idade mínima operacional de filiação facultativa é 16 anos.¦A disciplina regulamentar deve ser lida com a Constituição e a proteção do trabalho do adolescente.
-A pessoa de dez anos pode filiar-se facultativamente apenas com autorização dos pais.¦A autorização não afasta a idade mínima aplicável.
+A participação em RPPS impede, em regra, a filiação facultativa ao RGPS.¦A vedação tem fundamento constitucional e deve ser observada.
-O facultativo pode escolher livremente qualquer data passada para início de filiação, mesmo sem recolhimento.¦Não há retroação irrestrita do vínculo facultativo.
+A dona de casa sem atividade remunerada pode estar entre os possíveis facultativos.¦A adesão depende dos requisitos da filiação facultativa.
-Ser facultativo concede imediatamente todos os benefícios sem carência.¦A filiação não dispensa carência ou demais requisitos das prestações.
+O exercício posterior de atividade remunerada abrangida pode mudar o enquadramento contributivo.¦O vínculo obrigatório deve refletir a atividade efetiva.
-Contribuição facultativa de baixa renda é permitida a qualquer pessoa independentemente de renda e cadastro.¦A forma reduzida possui requisitos próprios que devem ser verificados.
+A contribuição facultativa é uma forma de ingresso voluntário no sistema contributivo.¦A voluntariedade se refere à adesão de quem não é obrigatório.
-A falta de emprego formal prova, sozinha, ausência de atividade remunerada obrigatória.¦Trabalho por conta própria e outras atividades também podem gerar obrigatoriedade.
+O primeiro pagamento deve respeitar as condições legais para produzir os efeitos pretendidos.¦Pagamento inválido ou inadequado não deve ser tratado automaticamente como filiação regular.
-Receber ajuda financeira familiar transforma necessariamente o estudante em empregado.¦Ajuda sem prestação remunerada subordinada não constitui automaticamente vínculo de emprego.
''')
add('B03-S08','r','arts. 18 a 20; Lei 8.213/1991, art. 17',
'Filiação é vínculo jurídico; inscrição é cadastro. Para obrigatório, o vínculo nasce da atividade remunerada enquadrada. Para facultativo, depende de inscrição e primeiro recolhimento válido. O NIT é identificador cadastral; não é benefício nem certificado de cumprimento de todos os requisitos.',
'Um empregado pode já estar filiado mesmo antes de regularizar seu cadastro. Já o facultativo não cria cobertura de qualquer evento passado apenas obtendo um número.',
'Ter cadastro não é ter carência; filiação não é concessão de benefício.',
'Regularização cadastral e comprovação de atividade devem seguir os procedimentos e provas pertinentes.', '''
+O vínculo de filiação obrigatória pode anteceder a regularização da inscrição.¦A atividade enquadrada, e não o cadastro, é o fato constitutivo geral desse vínculo.
-O NIT é o nome de uma aposentadoria do RGPS.¦É um identificador cadastral, não uma prestação previdenciária.
+Inscrição e filiação são conceitos distintos.¦Uma é cadastramento; a outra é vínculo jurídico com o regime.
-O empregado não é filiado enquanto a empresa não recolher a primeira contribuição.¦A filiação do obrigatório decorre do exercício da atividade.
+A filiação facultativa apresenta requisito de recolhimento que não define da mesma forma o início do vínculo do empregado.¦A categoria do segurado altera a formação do vínculo.
-A obtenção de cadastro comprova automaticamente cumprimento da carência de todo benefício.¦Carência exige exame das contribuições e regras próprias.
+Uma inconsistência cadastral pode exigir regularização sem apagar atividade comprovada.¦Defeito de registro e inexistência da atividade não são equivalentes.
-Qualquer pessoa com número de inscrição é segurada especial, independentemente de trabalho rural.¦Identificador não define categoria material.
+A inscrição permite organizar informações pessoais e vínculos do segurado.¦Sua finalidade cadastral não substitui o enquadramento jurídico.
-Filiação significa concessão automática de aposentadoria na mesma data.¦Concessão depende de requisitos específicos de benefício.
+A categoria correta deve refletir a atividade real na inscrição.¦O registro administrativo precisa corresponder aos fatos.
-Um código de recolhimento incorreto transforma legalmente empregado em facultativo.¦A realidade do vínculo não é substituída pelo código escolhido.
+A filiação ao RGPS pode coexistir com mais de uma atividade remunerada abrangida.¦A legislação prevê vínculo em relação a cada atividade.
-O primeiro cadastro de facultativo autoriza sempre recolher qualquer período anterior como facultativo.¦Não existe autorização geral de retroação irrestrita.
+A prova do trabalho pode ser relevante para reconhecer filiação de obrigatório.¦É o exercício da atividade que deve ser juridicamente demonstrado.
-Inscrição é necessariamente renovada a cada troca de empregador, com novo vínculo facultativo.¦Mudança de emprego não transforma o segurado em facultativo nem exige esse efeito jurídico.
''')
add('B03-S09','p','arts. 16 e 17; Decreto 3.048/1999, art. 18',
'Dependente possui relação derivada com o segurado e não se confunde com sua categoria contributiva. A inscrição do dependente ocorre no requerimento do benefício, conforme a disciplina legal. Inscrição posterior ao óbito e comprovação da atividade pretérita de obrigatório não equivalem à criação de filiação facultativa depois da morte.',
'Ao pedir pensão, a pessoa demonstra sua condição de dependente e demais requisitos. A ausência de cadastro antecipado de dependente não se confunde com inexistência da relação protegida.',
'Inscrição de dependente não é contribuição própria. Cadastro post mortem não pode ser usado para inventar atividade ou vínculo inexistente.',
'Cada reconhecimento exige documentação e requisitos pertinentes; não presumir dependência econômica em todas as classes.', '''
+A qualidade de dependente é distinta da condição de segurado contribuinte.¦O direito do dependente deriva da relação legal com o segurado.
-O dependente precisa contribuir pessoalmente ao RGPS para existir como dependente.¦Contribuição própria não é requisito geral dessa condição derivada.
+A inscrição de dependente pode ocorrer por ocasião do requerimento de benefício.¦A disciplina legal não exige cadastro antecipado universal como condição de existência da dependência.
-A falta de cadastro prévio impede qualquer pedido de pensão por morte, sem exame dos fatos.¦É necessário examinar dependência e demais requisitos legais, e não apenas cadastro anterior.
+A prova da condição de dependente deve observar a classe e os requisitos aplicáveis.¦Não há presunção econômica universal para qualquer parente.
-Qualquer parente distante é dependente previdenciário apenas por comprovar parentesco.¦A lei enumera classes e requisitos de dependência.
+Reconhecer atividade pretérita de obrigatório falecido é diferente de criar atividade inexistente após a morte.¦O reconhecimento deve se apoiar nos fatos e na prova admitida.
-A morte permite iniciar livremente filiação facultativa retroativa sem recolhimentos anteriores.¦Não existe criação irrestrita de vínculo facultativo post mortem.
+O pedido de pensão exige analisar a situação jurídica do instituidor.¦A existência do benefício não depende somente dos documentos do requerente.
-Inscrição administrativa torna dispensável qualquer requisito material da pensão.¦Cadastro não substitui óbito, qualidade protegida e dependência conforme a hipótese.
+As classes de dependentes têm efeitos na preferência entre possíveis beneficiários.¦A lei organiza classes e regras de exclusão entre elas.
-A inscrição de dependente transforma o segurado falecido em contribuinte individual.¦Os cadastros e as categorias possuem finalidades jurídicas distintas.
+A documentação apresentada após o óbito pode se referir a fatos ocorridos antes dele.¦Momento da prova não é necessariamente o momento de constituição do fato provado.
-Toda prova produzida depois do óbito cria automaticamente novo vínculo facultativo anterior.¦Prova de fato pretérito e constituição de filiação facultativa não são a mesma operação.
+A decisão deve distinguir dependência, filiação e inscrição.¦Confundir os institutos leva a negar ou conceder direitos por critério inadequado.
-A mera informação de dependente em formulário é prova absoluta de todos os requisitos.¦Declaração cadastral está sujeita a exame e comprovação juridicamente pertinente.
''')
add('B03-S10','p','arts. 11, § 2º, e 12; CF, art. 201, § 5º',
'Quem exerce atividades concomitantes abrangidas pelo RGPS é filiado relativamente a cada uma. Servidor amparado por RPPS pode ter atividade privada abrangida pelo RGPS, com filiação obrigatória por essa atividade. Isso é diferente de adesão facultativa de quem já participa do regime próprio.',
'Servidor efetivo vinculado a RPPS que exerce licitamente atividade autônoma remunerada pode ser obrigatório do RGPS nessa atividade; não é facultativo apenas por já ter RPPS.',
'Concomitância não significa contagem em dobro do mesmo período em uma única aposentadoria. Teto de contribuição do segurado não é teto de remuneração recebida.',
'Compatibilidade de cargos e contagem recíproca possuem requisitos próprios; não deduza autorização funcional da regra previdenciária.', '''
+Uma pessoa pode ser empregada em uma atividade e contribuinte individual em outra.¦O enquadramento é realizado em relação a cada atividade.
-Participar de RPPS afasta toda filiação obrigatória ao RGPS por atividade privada.¦A atividade abrangida pode gerar filiação obrigatória própria.
+Filiação obrigatória por atividade privada difere de filiação facultativa ao RGPS.¦A vedação ao facultativo de RPPS não elimina o vínculo obrigatório pela atividade.
-Dois vínculos de emprego garantem contagem de dois meses para cada mês civil no mesmo regime.¦Concomitância não transforma o mesmo tempo cronológico em tempo dobrado automaticamente.
+Remunerações de atividades concomitantes exigem coordenação do limite contributivo do segurado.¦O teto se refere à base contributiva segundo as regras aplicáveis.
-O teto do salário de contribuição impede o trabalhador de receber remuneração acima dele.¦Limite previdenciário da base não é proibição geral de remuneração maior.
+Servidor com RPPS deve ter sua atividade adicional examinada segundo os fatos e a lei.¦O regime do cargo público não define sozinho a natureza da atividade paralela.
-Qualquer vínculo adicional é sempre facultativo quando o primeiro já é obrigatório.¦Cada atividade legalmente abrangida pode gerar obrigatoriedade.
+O vínculo de empregado não elimina automaticamente a contribuição de atividade autônoma concomitante.¦Devem ser observadas regras da categoria e limite contributivo.
-A filiação previdenciária regular autoriza, por si só, acumular qualquer cargo público.¦Acumulação funcional tem disciplina constitucional própria.
+A prova de vínculos distintos é relevante para regularizar informações contributivas.¦A apuração precisa considerar todas as atividades envolvidas.
-O segurado pode omitir livremente uma atividade para escolher apenas a categoria de menor custo.¦A obrigatoriedade não é opção para afastar atividade abrangida.
+A contagem recíproca exige observar vedações de aproveitamento duplicado.¦Ter dois regimes não permite usar indevidamente o mesmo tempo já aproveitado.
-O reconhecimento de um RPPS converte todo trabalho privado do servidor em cargo efetivo.¦Natureza funcional e atividade privada são relações distintas.
+O aposentado pode exercer atividade concomitante sujeita ao custeio, observadas as regras legais.¦A condição de aposentado não elimina obrigatoriedade da atividade abrangida.
-Os regimes RGPS e RPPS são apenas nomes diferentes de uma mesma relação contributiva.¦São regimes com estruturas e requisitos próprios.
''')
add('B03-S11','p','art. 12; CF, arts. 40 e 201',
'O servidor civil titular de cargo efetivo e o militar são excluídos do RGPS nas condições legais de amparo por regime próprio. A exclusão é relativa ao vínculo coberto: atividade adicional abrangida pelo RGPS pode gerar filiação obrigatória. Empregado público e ocupante exclusivamente de cargo em comissão não se equiparam automaticamente ao titular efetivo com RPPS.',
'Um empregado celetista de empresa estatal não passa ao RPPS só porque seu empregador é público. Um servidor efetivo amparado por regime próprio tem situação diversa.',
'Trabalhar para o poder público não define um único regime para todo agente. Examine natureza do vínculo e cobertura legal.',
'Regime próprio não é criado por escolha pessoal do servidor; exige suporte jurídico do ente competente.', '''
+A exclusão legal do servidor efetivo depende de sua condição e do amparo pelo regime próprio pertinente.¦Não basta o nome servidor em sentido amplo.
-Todo trabalhador de empresa pública é titular de cargo efetivo amparado por RPPS.¦Emprego público e cargo efetivo são vínculos distintos.
+Atividade privada abrangida pode gerar RGPS para quem já tem vínculo público com RPPS.¦A exclusão relativa ao cargo não abrange automaticamente toda outra atividade.
-A nacionalidade estrangeira exclui toda possibilidade de filiação ao RGPS.¦Existem hipóteses de segurado estrangeiro previstas em lei.
+O ocupante exclusivamente de cargo em comissão tem disciplina previdenciária distinta do efetivo amparado por RPPS.¦Não se pode inferir RPPS apenas da natureza pública do órgão.
-Qualquer pessoa pode escolher entre RGPS e RPPS sem relação com seu vínculo funcional.¦O regime decorre da Constituição e da legislação aplicável.
+O empregado público celetista pode ser segurado do RGPS.¦O poder público também mantém vínculos sujeitos ao regime geral.
-A existência de atividade rural exclui o trabalhador do RGPS porque existe apenas previdência urbana.¦O RGPS protege também trabalhadores rurais nas categorias legais.
+A análise da exclusão deve identificar o vínculo específico abrangido.¦Uma pessoa pode manter relações sujeitas a regimes diferentes.
-O servidor efetivo vinculado ao RGPS pode criar seu próprio RPPS mediante requerimento pessoal.¦Regime próprio exige estrutura normativa do ente competente.
+O art. 12 da Lei 8.213 não autoriza omitir atividade privada obrigatória.¦A própria disciplina preserva filiação pela atividade abrangida pelo RGPS.
-Quem não possui emprego formal é sempre excluído do RGPS.¦Há outras categorias obrigatórias e possibilidade legal de filiação facultativa.
+O aposentado em atividade remunerada abrangida continua submetido às regras de custeio dessa atividade.¦A aposentadoria não representa exclusão geral de toda atividade futura.
-O benefício assistencial recebido por alguém prova sua exclusão eterna de qualquer filiação previdenciária.¦A natureza assistencial do benefício não decide de forma absoluta toda atividade futura.
+A natureza estatutária ou celetista deve integrar a análise do regime aplicável.¦A expressão genérica agente público não basta.
-A exclusão de um vínculo específico permite concluir que a pessoa nunca poderá receber prestação do RGPS sob qualquer hipótese.¦É necessário examinar outros vínculos, períodos e requisitos legais.
''')

add('B04-S01','c','art. 15, I',
'Empresa, para os fins da Lei de Custeio, inclui firma individual ou sociedade que assume risco de atividade econômica urbana ou rural, com ou sem finalidade lucrativa, e órgãos e entidades da Administração Pública direta, indireta e fundacional. A definição previdenciária é mais ampla que a ideia coloquial de negócio com lucro.',
'Uma associação sem fins lucrativos com empregados não se livra dos deveres previdenciários apenas porque não distribui lucro.',
'Empresa, contribuinte individual e segurado são conceitos relacionados, mas distintos. Órgão público pode ter deveres de empresa na legislação de custeio.',
'A definição de empresa não resolve automaticamente benefícios fiscais, imunidades ou alíquotas de cada situação.', '''
+A definição previdenciária de empresa abrange atividade econômica rural.¦O art. 15 não limita a empresa ao meio urbano.
-Somente sociedades com finalidade lucrativa são empresas para o custeio.¦A lei inclui atividades com ou sem fins lucrativos.
+Órgãos e entidades públicas estão incluídos na definição legal pertinente.¦A inclusão abrange Administração direta, indireta e fundacional.
-A empresa só tem obrigações previdenciárias se obter lucro no mês.¦Lucro não é condição universal dos deveres relativos à remuneração do trabalho.
+Uma sociedade sem fins lucrativos pode ter responsabilidade previdenciária sobre seus empregados.¦A ausência de finalidade lucrativa não afasta, sozinha, o enquadramento.
-Firma individual é sempre excluída do conceito previdenciário de empresa.¦O art. 15 a inclui expressamente.
+O conceito legal deve ser distinguido da linguagem comum de empresa comercial.¦A lei adota alcance próprio para suas finalidades de custeio.
-Ser empresa significa ser uma pessoa física segurada empregada.¦Responsável empresarial e segurado empregado são posições jurídicas diferentes.
+A assunção dos riscos da atividade integra a definição da firma individual ou sociedade.¦O conceito examina o empreendimento e seus riscos econômicos.
-Uma entidade pública nunca pode ser responsável por desconto previdenciário de trabalhadores.¦A natureza pública não elimina obrigações legais de arrecadação.
+Definição de empresa e concessão de imunidade contributiva exigem análises separadas.¦A existência de benefício fiscal depende de fundamento e requisitos específicos.
-A lei de custeio usa empresa e empregador doméstico como termos inteiramente intercambiáveis.¦O art. 15 os define separadamente.
''')
add('B04-S02','c','art. 15, parágrafo único',
'A lei equipara sujeitos à empresa para fins previdenciários, como o contribuinte individual em relação a segurado que lhe presta serviço e outros sujeitos enumerados, incluindo cooperativa e representação estrangeira. A equiparação é finalística: atribui deveres no âmbito normativo, sem necessariamente criar personalidade empresarial geral.',
'Um profissional liberal que contrata empregado precisa examinar seus deveres previdenciários como equiparado, embora sua própria categoria de segurado continue sendo analisada separadamente.',
'Equiparação previdenciária não é transformação de pessoa física em sociedade comercial. Nem toda relação civil equivale a contratação de segurado.',
'A enumeração legal e a situação concreta delimitam o alcance da equiparação.', '''
+O contribuinte individual pode ser equiparado à empresa em relação ao segurado que lhe presta serviço.¦A lei atribui deveres previdenciários nessa relação específica.
-A equiparação cria automaticamente uma sociedade anônima para a pessoa física.¦Seus efeitos são finalísticos para o regime jurídico de custeio.
+Cooperativa está entre os sujeitos legalmente equiparados para os efeitos da lei.¦É necessário observar a definição do art. 15.
-Missão diplomática jamais pode ter obrigações previdenciárias no Brasil.¦A lei contempla representação estrangeira na equiparação pertinente.
+O profissional que contrata empregado deve distinguir sua contribuição pessoal dos deveres relativos ao contratado.¦São posições jurídicas e fatos geradores distintos.
-Equiparação torna facultativa a contribuição do empregado contratado.¦A categoria e a filiação obrigatória do empregado permanecem regidas pela lei.
+A equiparação tem alcance definido pela finalidade da legislação previdenciária.¦Não se estende automaticamente a todo ramo do direito.
-Toda contratação de pessoa jurídica prova, sem análise adicional, vínculo de segurado empregado da contratante.¦A natureza da relação e os fatos devem ser examinados.
+A ausência de sociedade comercial não basta para afastar dever de custeio como equiparado.¦A lei pode atribuir obrigações a outros sujeitos.
-Equiparado à empresa fica dispensado de prestar quaisquer informações previdenciárias.¦A equiparação pode justamente trazer deveres legais de custeio e informação.
+A situação do trabalhador contratado deve ser analisada segundo sua categoria.¦Equiparação do tomador não define por si só todos os vínculos.
-As equiparações do art. 15 permitem escolher livremente entre cumprir ou não a legislação de custeio.¦Dever legal não se torna opcional pelo nome equiparação.
''')
add('B04-S03','c','art. 15, II; LC 150/2015, art. 1º',
'Empregador doméstico é a pessoa ou família que admite a seu serviço, sem finalidade lucrativa, empregado doméstico. A definição depende da relação doméstica, não apenas de o contratante ser pessoa física. Obrigações de cadastro, declaração e recolhimento devem ser cumpridas nos meios próprios.',
'Família contrata cuidador com os requisitos de emprego doméstico. Um médico pessoa física que contrata recepcionista para seu consultório tem finalidade profissional distinta e não deve presumir relação doméstica.',
'Pessoa física pode ser tomador empresarial por equiparação ou empregador doméstico, conforme os fatos.',
'Contratação em residência não basta se a prestação servir diretamente a atividade econômica do tomador.', '''
+O empregador doméstico pode ser uma família.¦A definição legal não se limita a empresa ou pessoa jurídica.
-Toda pessoa física contratante é empregador doméstico, independentemente da finalidade do serviço.¦A finalidade não lucrativa e a relação doméstica precisam estar presentes.
+A prestação doméstica não possui finalidade lucrativa para a pessoa ou família tomadora.¦Esse é elemento central da definição legal.
-Uma sociedade empresarial pode ser empregadora doméstica apenas por manter um apartamento.¦A categoria doméstica pressupõe pessoa ou família na hipótese legal.
+A contratação de cuidador familiar pode gerar deveres de empregador doméstico.¦A função pode integrar emprego doméstico quando presentes seus requisitos.
-Recepcionista de consultório particular é doméstica necessariamente porque o médico é pessoa física.¦O serviço atende atividade profissional, não a finalidade doméstica não lucrativa.
+Cadastro e recolhimento domésticos têm disciplina própria.¦A natureza familiar não elimina obrigações legais.
-A inexistência de finalidade lucrativa elimina automaticamente todas as contribuições do doméstico e do empregador.¦O vínculo doméstico é contributivo nos termos legais.
+O tomador precisa distinguir contratação autônoma de vínculo doméstico.¦A frequência e os demais requisitos são relevantes para o enquadramento.
-O endereço residencial, sozinho, prova definitivamente a condição de empregador doméstico.¦É necessário examinar a finalidade e a realidade da prestação.
+A condição de empregador não se confunde com a categoria de segurado do trabalhador.¦Tomador e empregado ocupam posições diferentes no custeio.
-A família pode afastar todos os encargos por acordo particular com o empregado.¦Obrigações legais de contribuição não são livremente renunciáveis.
''')

add('B05-S01','c','arts. 10, 11 e 16; CF, art. 195',
'A seguridade é financiada por toda a sociedade, direta e indiretamente. O orçamento federal combina receitas da União, contribuições sociais e outras fontes. O financiamento envolve também estados, Distrito Federal e municípios. A União cobre insuficiências financeiras decorrentes do pagamento de benefícios continuados previdenciários na forma orçamentária.',
'Uma despesa da seguridade não é necessariamente coberta apenas pelo desconto do segurado que a recebe. A lógica de financiamento reúne fontes plurais e recursos orçamentários.',
'Orçamento da seguridade e poupança individual são modelos diferentes. Financiamento social não elimina vinculações e regras de destinação.',
'Recursos, competências e vinculações devem ser conferidos na norma atual; não usar expressões como qualquer receita pode pagar qualquer despesa.', '''
+A sociedade participa direta e indiretamente do financiamento da seguridade.¦O modelo constitucional não se limita a contribuições dos beneficiários.
-Somente os trabalhadores empregados financiam a seguridade social.¦Há recursos públicos, contribuições de outros sujeitos e outras receitas.
+Receitas da União integram o orçamento federal da seguridade.¦O art. 11 da Lei 8.212 enumera essa fonte.
-A participação de estados e municípios é constitucionalmente proibida.¦O art. 195 prevê recursos dos quatro níveis federativos indicados.
+As contribuições sociais são uma das categorias de receita do orçamento federal da seguridade.¦Não constituem, contudo, sua única fonte.
-A obrigação de contribuir existe apenas para quem já recebe benefício.¦A contribuição pode decorrer de atividade e fatos geradores independentemente de benefício atual.
+O caráter solidário não exige correspondência individual exata entre o que cada pessoa paga e recebe.¦O financiamento reúne recursos para proteção social nos termos legais.
-A seguridade é financiada exclusivamente pelo orçamento fiscal da União, sem contribuições sociais.¦A Constituição e a lei estabelecem pluralidade de fontes.
+A União tem responsabilidade legal quanto a insuficiências financeiras ligadas a benefícios continuados previdenciários.¦Essa cobertura deve observar a forma da Lei Orçamentária Anual.
-Uma família pode criar contribuição social obrigatória por acordo privado para toda a população.¦Tributação depende de competência constitucional e norma apropriada.
+Outras fontes são categoria expressamente prevista ao lado de receitas da União e de contribuições.¦O art. 11 adota três grupos de receitas federais.
-Toda receita de seguridade é uma contribuição descontada diretamente de salário.¦Existem receitas de outras bases e de outras fontes.
+As receitas e despesas das áreas devem ser identificadas conforme a organização constitucional.¦Financiamento integrado não significa ausência de controle contábil.
-O déficit de um mês autoriza o atendente do INSS a criar alíquota extra por decisão individual.¦Dever de financiamento não elimina legalidade tributária e competência.
+O financiamento da seguridade deve ser examinado em conjunto com as regras orçamentárias.¦Contribuições e recursos públicos integram uma estrutura normativa de receitas e despesas.
-A perda da qualidade de segurado de uma pessoa extingue todas as fontes de receita do sistema.¦Situação individual não elimina o financiamento social coletivo.
''')
add('B05-S02','c','arts. 20 e 21; EC 103/2019, art. 28',
'A contribuição do segurado depende de categoria, base e regime aplicável. Empregado, doméstico e avulso possuem faixas progressivas conforme a disciplina vigente; contribuinte individual e facultativo têm regras próprias e hipóteses simplificadas condicionadas. Desconto do trabalhador não se confunde com contribuição do tomador.',
'Aplicar a maior alíquota da tabela sobre todo o salário, sem respeitar faixas quando exigidas, produz cálculo diferente da progressividade. Uma guia simplificada também não pode ser escolhida ignorando os requisitos do plano.',
'Alíquota nominal de faixa e alíquota efetiva são diferentes. Desconto do segurado e encargo patronal são obrigações diferentes.',
'Valores das faixas e teto são atualizados: esta aula não fixa tabela anual como regra eterna.', '''
+A categoria do segurado influencia a disciplina da contribuição pessoal.¦Não existe uma única forma contributiva indistinta para todas as categorias.
-A contribuição patronal substitui automaticamente qualquer desconto devido pelo empregado.¦São obrigações distintas previstas na legislação.
+Progressividade por faixas difere de aplicar a maior alíquota sobre toda a remuneração.¦Cada parcela da base é tratada segundo a faixa correspondente.
-A alíquota efetiva de um cálculo progressivo é necessariamente igual à maior alíquota nominal utilizada.¦A carga total resulta da composição das faixas.
+O facultativo possui contribuição própria, sem empregador que a torne dispensável.¦Sua adesão e custeio seguem disciplina específica.
-Qualquer contribuinte pode usar o plano mais barato sem observar requisitos legais.¦Formas simplificadas têm condições e efeitos próprios.
+A contribuição pode ser devida mesmo quando o segurado não pede benefício no mês.¦O fato gerador contributivo não é o requerimento mensal de benefício.
-O aposentado que volta a atividade abrangida jamais contribui por já ter financiado sua aposentadoria.¦A nova atividade se submete à obrigatoriedade de custeio.
+Limites da base devem ser considerados no cálculo da contribuição do segurado.¦O teto e os critérios de mínimo integram o regime aplicável.
-Uma contribuição de segurado e uma contribuição empresarial são sempre valores idênticos.¦Sujeitos, bases e alíquotas podem ser diferentes.
+O código da guia deve corresponder à categoria e à forma de contribuição utilizada.¦Cadastro e recolhimento precisam representar a situação jurídica correta.
-A palavra facultativo indica liberdade para pagar qualquer valor e exigir qualquer efeito.¦Existem bases, limites e requisitos de validade.
+Atividades concomitantes podem exigir informação entre fontes pagadoras para observar o teto.¦A soma das bases do segurado precisa ser coordenada nos termos legais.
-O salário líquido após todos os descontos é sempre a base previdenciária do empregado.¦A base é definida pela legislação contributiva, não pelo resultado líquido do pagamento.
+O pagamento em atraso pode exigir tratamento distinto do recolhimento regular.¦Mora e efeitos previdenciários dependem das regras aplicáveis.
-Uma contribuição isolada prova automaticamente carência suficiente para qualquer prestação.¦Cada benefício tem requisitos e contagem próprios.
''')
add('B05-S03','c','art. 22 e §§',
'A empresa possui contribuição sobre remunerações de segurados a seu serviço conforme a hipótese, além de outras contribuições legalmente previstas. A cota empresarial não é o desconto pessoal do trabalhador. Há regras de substituição e regimes específicos; a base patronal sobre remuneração não se submete automaticamente ao teto individual do segurado.',
'Salário acima do teto pode ter desconto pessoal limitado, sem que isso limite automaticamente a base empresarial comum incidente sobre a remuneração.',
'Limite contributivo do segurado não é limite universal de todo encargo empresarial. Encargo patronal não autoriza descontá-lo do trabalhador como se fosse sua contribuição.',
'Não generalizar alíquota comum a entidades, setores e fatos submetidos a regimes especiais.', '''
+A contribuição da empresa é distinta da contribuição descontada do segurado.¦Os sujeitos e fundamentos das obrigações não se confundem.
-Toda cota patronal é automaticamente limitada ao teto individual de contribuição do empregado.¦O teto do segurado não é limite universal da base empresarial.
+Remunerações pagas ou creditadas a segurados podem compor bases empresariais conforme a lei.¦A base depende do fato gerador e da hipótese legal.
-A falta de lucro elimina qualquer contribuição empresarial sobre remunerações.¦Lucro não é requisito geral dessa incidência sobre trabalho.
+A legislação admite regimes de substituição contributiva em hipóteses específicas.¦A regra comum deve ser confrontada com a norma setorial aplicável.
-A empresa pode transferir livremente sua cota patronal ao empregado como contribuição pessoal dele.¦Obrigações próprias e descontos legais devem ser distinguidos.
+A atividade e o enquadramento do tomador podem alterar o regime de contribuição.¦Há condições e particularidades legais a verificar.
-Toda associação sem fins lucrativos é imune sem qualquer requisito.¦Ausência de lucro não satisfaz automaticamente as condições de imunidade.
+O custeio dos riscos ambientais do trabalho possui disciplina empresarial própria.¦Não deve ser confundido com o desconto pessoal do empregado.
-Uma empresa só deve contribuir quando algum empregado se aposenta.¦A contribuição não depende desse evento individual.
+A folha contém fatos que precisam ser classificados antes de calcular contribuições.¦Nem todo pagamento tem automaticamente a mesma natureza e incidência.
-A soma de descontos dos empregados quita, por definição, todas as contribuições da empresa.¦A cota própria e outros encargos podem continuar devidos.
+O pagamento a contribuinte individual pode gerar deveres contributivos do tomador empresarial.¦As normas distinguem categoria do prestador e obrigações da empresa.
-Toda regra de substituição é facultativa para qualquer empresa por simples conveniência mensal.¦A aplicação depende da legislação específica, requisitos e opções quando admitidas.
+O custeio empresarial exige observar competência e redação temporal da norma.¦Regras e regimes podem mudar ao longo do tempo.
-A base empresarial deve ser sempre o salário líquido recebido pelo empregado.¦A base jurídica não se confunde com o valor líquido após descontos.
''')
add('B05-S04','lc','arts. 31 a 35',
'O empregador doméstico recolhe encargos próprios e a contribuição descontada do trabalhador por meio do regime unificado previsto na LC 150. O DAE pode reunir parcelas com naturezas diferentes, inclusive tributos e FGTS. O valor total da guia não corresponde integralmente a contribuição pessoal do empregado.',
'Uma guia DAE contém valores devidos pelo empregador e valores retidos do empregado. Descontar todo o DAE da remuneração confunde obrigações distintas.',
'Documento único não significa tributo único. Prazo atual do DAE não deve ser confundido com regras antigas de dia sete.',
'Vencimento e incidências podem mudar; para a situação corrente, conferir manual eSocial e competência.', '''
+O DAE pode reunir valores de naturezas jurídicas diferentes.¦Arrecadação unificada não transforma todos os componentes em uma única contribuição.
-Todo valor do DAE deve ser descontado do salário do doméstico.¦A guia inclui encargos próprios do empregador, além de valores retidos.
+O empregador doméstico tem contribuição própria nos termos legais.¦Ela não se confunde com a contribuição do trabalhador.
-O FGTS incluído no DAE é contribuição pessoal do empregado ao RGPS.¦FGTS e contribuição previdenciária possuem natureza e destinação diferentes.
+A remuneração e as informações do vínculo precisam ser corretamente registradas.¦O cálculo depende de informações adequadas no sistema.
-Por ser pessoa física, o empregador doméstico não tem dever de recolher encargos.¦A lei estabelece obrigações específicas para essa categoria.
+A guia única não elimina a necessidade de identificar a competência.¦O recolhimento deve estar vinculado ao período correto.
-Pagar a remuneração líquida prova, sozinho, o recolhimento de todos os encargos do DAE.¦Pagamento salarial e arrecadação de encargos são operações distintas.
+Alterações de remuneração podem afetar os valores calculados na folha doméstica.¦A base precisa refletir fatos e rubricas pertinentes.
-Todo auxílio ou reembolso lançado na folha tem necessariamente a mesma incidência de salário.¦A natureza da verba e seus requisitos precisam ser analisados.
+Desconto do segurado e contribuição patronal podem constar do mesmo documento de arrecadação.¦A unificação operacional não apaga a diferença entre obrigações.
-A família pode substituir o DAE por um acordo particular de quitação de direitos previdenciários.¦Obrigações legais não são afastadas por declaração privada.
+Débitos domésticos em atraso devem seguir a atualização e o procedimento pertinentes.¦O decurso do prazo pode gerar acréscimos legais.
-Uma guia emitida nunca precisa ser paga, pois a emissão já equivale à arrecadação.¦Emissão e pagamento são atos distintos.
+A situação de mais de um empregado exige informações individualizadas corretas.¦O documento unificado não dispensa identificar vínculos e remunerações.
-O regime doméstico transforma automaticamente o empregador em segurado facultativo.¦Posição de empregador e condição previdenciária pessoal são análises separadas.
''')
add('B05-S05','c','arts. 12, VII, 25 e 30',
'Produtor rural pessoa física e segurado especial têm disciplina de custeio ligada à comercialização da produção, observadas as hipóteses legais. Essa contribuição não é conceitualmente idêntica à contribuição sobre folha de empregados. A lei prevê responsabilidades de adquirentes e situações de recolhimento próprio, além de opções e particularidades a examinar.',
'Na venda de produção, identifique quem vende, quem adquire e qual é a operação. Não basta afirmar que todo agricultor paga como empregado ou que toda comercialização possui o mesmo responsável.',
'Categoria do produtor, contribuição sobre produção e encargo sobre empregados devem ser separados.',
'Percentuais e opções dependem da norma vigente; não estenda um regime de pessoa física a toda pessoa jurídica rural.', '''
+A comercialização da produção é relevante para a contribuição rural prevista em lei.¦Ela pode compor fato gerador e base do custeio específico.
-Produtor rural pessoa física e empregado rural são sempre a mesma categoria.¦O vínculo e a forma de atividade distinguem os enquadramentos.
+O segurado especial possui regime de custeio próprio.¦Não deve ser tratado automaticamente como empregado com desconto em folha.
-A contribuição sobre a produção equivale juridicamente a salário recebido pelo produtor de uma empresa.¦Comercialização e remuneração de emprego são fatos distintos.
+A identificação do adquirente é importante para verificar responsabilidade de arrecadação.¦A lei prevê hipóteses de sub-rogação e de recolhimento próprio.
-Toda venda de produção rural é arrecadada obrigatoriamente pelo próprio produtor, sem exceção.¦O responsável varia conforme sujeitos e operação previstos em lei.
+A contratação de trabalhadores pelo produtor pode gerar obrigações distintas da contribuição sobre produção.¦As relações de trabalho exigem exame específico.
-A contribuição sobre produção dispensa qualquer identificação da competência ou documentação da operação.¦Registro e informação adequados continuam necessários.
+O enquadramento como especial depende de requisitos além da existência de receita de produção.¦Atividade, forma de exploração e demais condições são relevantes.
-Pessoa jurídica rural recebe automaticamente todas as regras atribuídas ao segurado especial pessoa física.¦Regimes e sujeitos diferentes não são intercambiáveis.
+Uma hipótese legal de opção contributiva precisa ter suas condições observadas.¦A possibilidade de escolha não é presumida para qualquer sujeito ou período.
-O uso do termo agricultor em um recibo basta para afastar todas as contribuições previstas em lei.¦Descrição informal não constitui exoneração tributária.
+A operação de venda deve ser distinguida do pagamento de salário a empregado rural.¦Os fatos podem gerar deveres de custeio distintos.
-A inexistência de carteira assinada de um produtor o torna necessariamente facultativo.¦A atividade rural pode enquadrá-lo em categoria obrigatória.
+O tratamento legal da comercialização precisa considerar a qualidade das partes da operação.¦Produtor, adquirente e eventual intermediário possuem posições específicas.
-O beneficiário de proteção rural jamais pode contribuir adicionalmente nas hipóteses previstas em lei.¦A legislação admite contribuição facultativa adicional do especial nas condições aplicáveis.
''')
add('B05-S06','c','art. 22, §§ 6º a 11',
'A associação desportiva que mantém equipe de futebol profissional possui contribuição empresarial substitutiva em hipóteses legais, incidente sobre receita bruta de espetáculos e receitas de patrocínio, licenciamento, publicidade, propaganda e transmissão indicadas na norma. O regime não se aplica indistintamente a qualquer clube ou atividade esportiva.',
'Uma receita de patrocínio da associação abrangida precisa ser distinguida do salário do atleta e do valor pessoal de sua contribuição.',
'Receita da associação, contribuição empresarial e desconto do segurado são objetos diferentes.',
'Enquadramento da entidade e operações devem ser conferidos; não presumir regime especial para qualquer academia ou equipe amadora.', '''
+A manutenção de equipe de futebol profissional é elemento da hipótese legal especial.¦A regra não é atribuída indistintamente a qualquer entidade esportiva.
-Toda academia de ginástica está automaticamente no regime da associação com futebol profissional.¦A hipótese legal exige enquadramento específico da entidade.
+A receita bruta dos espetáculos indicados pode integrar a base da contribuição substitutiva.¦O art. 22 prevê receitas específicas ligadas à atividade da associação.
-A contribuição substitutiva é calculada exclusivamente sobre a pensão dos ex-atletas.¦A base legal envolve receitas da associação, não pensões pessoais.
+Patrocínio e licenciamento de marcas podem compor as receitas previstas na disciplina especial.¦São espécies de receita expressamente tratadas pela norma.
-O regime especial extingue a contribuição pessoal de todo atleta empregado.¦Substituição empresarial não elimina automaticamente obrigações do segurado.
+Receita de transmissão deve ser examinada conforme a hipótese de incidência legal.¦A origem da receita importa para o regime de custeio.
-Um clube só amador é equiparado automaticamente a associação com equipe de futebol profissional para esse regime.¦Não basta desenvolver qualquer atividade esportiva.
+A substituição legal se refere a contribuições empresariais indicadas na própria norma.¦Seu alcance não é uma dispensa universal de tributos.
-A palavra substituição autoriza a associação a escolher não financiar a seguridade.¦A norma troca a forma de incidência nas hipóteses previstas, não elimina o dever.
+Valores de publicidade e propaganda precisam ser distinguidos da folha de pagamento.¦As bases possuem fatos e sujeitos próprios.
-Todas as receitas de um atleta individual são receitas da associação para a contribuição especial.¦Receita pessoal e receita da entidade não se confundem.
+A legislação distribui responsabilidades de retenção e recolhimento conforme a operação.¦Quem promove espetáculo e quem paga certas receitas têm deveres a examinar.
-A receita de espetáculo no exterior é automaticamente igual a espetáculo em território nacional para toda regra do art. 22.¦O texto define o alcance territorial pertinente e não autoriza universalização sem análise.
+A natureza profissional da equipe não transforma todos os prestadores em contribuintes individuais.¦Categoria de cada trabalhador depende de sua relação jurídica.
-A contribuição especial permite desconsiderar documentação de receitas de patrocínio.¦A apuração e as obrigações de informação permanecem relevantes.
''')
add('B05-S07','c','art. 26, §§ 4º a 6º; CF, art. 195, III',
'Concursos de prognósticos constituem fonte constitucional de contribuição à seguridade. A Lei 8.212 vincula a base à receita auferida nos concursos, sorteios e loterias e remete o percentual destinado à seguridade à lei de cada modalidade. Não existe um único percentual universal para todo jogo apenas pela expressão prognóstico.',
'Em um problema, receita da modalidade e prêmio individual são grandezas diferentes. A contribuição destinada à seguridade não deve ser confundida com tributação pessoal de um ganhador.',
'Receita arrecadada, custo de operação, prêmio e resultado financeiro são conceitos distintos.',
'A disciplina das modalidades pode mudar; é necessário identificar a modalidade e a lei pertinente antes de usar percentuais.', '''
+A Constituição inclui a receita de concursos de prognósticos entre as fontes de contribuição.¦A previsão está no art. 195, III.
-A seguridade é proibida de receber recursos oriundos de loterias previstas em lei.¦A legislação prevê contribuição sobre receitas dessas modalidades.
+Receita da modalidade e valor de prêmio individual não são conceitos idênticos.¦A base deve ser identificada conforme o texto normativo.
-Existe um percentual invariável aplicável a toda modalidade de loteria sem consultar sua lei.¦A Lei 8.212 remete o percentual à legislação da modalidade.
+A arrecadação da contribuição é destinada ao financiamento da seguridade.¦Essa destinação está prevista no art. 26.
-Contribuição sobre prognósticos é o mesmo fato que contribuição descontada do salário de um empregado.¦São bases e relações tributárias diferentes.
+A análise precisa identificar qual concurso ou modalidade é objeto da receita.¦A disciplina legal da modalidade pode alterar a distribuição.
-O simples nome sorteio em promoção privada cria automaticamente contribuição sem verificar o regime legal.¦Incidência depende de enquadramento e norma pertinente.
+A receita auferida nos concursos, sorteios e loterias é referência da base legal.¦Não se deve substituí-la automaticamente por outra grandeza contábil.
-A quantia destinada ao prêmio sempre equivale à contribuição da seguridade.¦Destinações distintas possuem critérios próprios.
+Mudança na lei da modalidade pode exigir atualização de um exercício com percentuais.¦Gabarito histórico e regra corrente devem ser distinguidos.
-O ganhador de prêmio torna-se empregado da entidade lotérica apenas por receber o valor.¦Prêmio não constitui, por si só, relação de emprego.
+A diversidade da base de financiamento ajuda a compreender essa fonte de receita.¦O financiamento não está restrito à remuneração do trabalho.
-A administração do INSS pode substituir por decisão individual o percentual legal da modalidade.¦Cálculo deve respeitar a norma competente.
+A origem lotérica dos recursos não dispensa sua identificação e controle.¦Destinação social é compatível com obrigações de prestação de contas.
-Uma questão pode usar indistintamente faturamento total, lucro e prêmio como se fossem sempre a mesma base.¦Grandezas econômicas distintas não são intercambiáveis sem previsão legal.
''')
add('B05-S08','c','art. 27, I a VIII',
'Outras receitas incluem multas, atualização monetária e juros moratórios; remuneração por serviços de arrecadação e cobrança a terceiros; receitas de serviços e de fornecimento ou arrendamento de bens; receitas patrimoniais, industriais e financeiras; doações, legados, subvenções e outras fontes legalmente previstas. A enumeração mostra que financiamento não se resume a contribuições sobre trabalho.',
'Receita de arrendamento de bem e contribuição descontada do segurado são ingressos distintos. A destinação previdenciária não transforma uma doação em desconto salarial.',
'Espécie de receita e destinação orçamentária são perguntas diferentes. Não confundir principal contributivo com acréscimos da mora.',
'Dispositivos de percentual e regimes especiais requerem revisão de vigência; esta aula não fixa percentuais de repasses transitórios.', '''
+Multas e juros moratórios figuram entre as outras receitas indicadas na Lei 8.212.¦O art. 27 distingue essas receitas do principal contributivo.
-Toda receita da seguridade deve obrigatoriamente ser desconto de empregado.¦A lei prevê receitas de outras fontes e naturezas.
+Receitas patrimoniais podem integrar o grupo de outras receitas.¦A enumeração legal inclui ingressos patrimoniais, industriais e financeiros.
-Uma doação é juridicamente idêntica a contribuição compulsória de segurado.¦A origem e a natureza da receita são diferentes.
+O arrendamento de bens pode gerar receita prevista na legislação de custeio.¦Fornecimento e arrendamento aparecem no art. 27.
-As receitas financeiras são universalmente proibidas no financiamento da seguridade.¦A lei as contempla entre outras receitas.
+Serviços de arrecadação e cobrança prestados a terceiros podem gerar remuneração legalmente prevista.¦Essa remuneração é uma espécie de receita distinta das contribuições arrecadadas.
-Juros de mora são sempre a contribuição patronal principal sobre salários.¦Acréscimo por atraso e obrigação contributiva principal não se confundem.
+Doações e legados constam da enumeração legal de outras receitas.¦A legislação admite essas espécies de ingresso.
-O recebimento de legado transforma automaticamente o beneficiário final de uma prestação em herdeiro do doador.¦Natureza da receita do sistema não altera a relação jurídica do benefício.
+A lei admite outras receitas previstas em legislação específica.¦A enumeração comporta o fundamento normativo correspondente.
-A previsão de outras receitas autoriza qualquer cobrança inventada pelo agente administrativo.¦Abertura para legislação específica não elimina competência e legalidade.
+Subvenções podem integrar receitas da seguridade conforme a lei.¦A espécie é mencionada na enumeração do art. 27.
-Receita de prestação de serviço nunca pode financiar a seguridade por não ser contribuição social.¦O orçamento admite outras fontes além das contribuições.
+A classificação da receita auxilia a distinguir contribuição, remuneração de serviço e acréscimo legal.¦Ingresso no mesmo orçamento não torna idênticas todas as espécies.
-O sistema de receitas patrimoniais dispensa documentação e controle dos ingressos.¦A natureza da receita não afasta a regularidade administrativa e contábil.
''')
add('B05-S09','cf','art. 195, § 7º; LC 187/2021, arts. 1º a 3º',
'A Constituição protege entidades beneficentes que atendam às exigências legais na hipótese do art. 195, § 7º. O benefício constitucional é tratado como imunidade, embora o texto use isentas. A LC 187 disciplina requisitos e certificação. Não basta ausência de lucro ou um nome filantrópico. Imunidade da cota da entidade não afasta automaticamente descontos dos segurados.',
'Uma entidade pode ser sem fins lucrativos e ainda precisar comprovar requisitos da imunidade. O desconto do trabalhador não se confunde com a contribuição própria da entidade.',
'Imunidade decorre da Constituição; isenção é desoneração legal dentro da competência tributária. Certificação e requisitos devem ser examinados no regime aplicável.',
'Não generalizar o alcance a todo tributo ou obrigação acessória; a hipótese e a lei precisam ser identificadas.', '''
+A ausência de finalidade lucrativa não comprova, isoladamente, todos os requisitos da imunidade contributiva.¦A entidade precisa atender às exigências constitucionais e legais aplicáveis.
-Toda entidade com palavra beneficente no nome fica automaticamente livre de qualquer tributo.¦Denominação não satisfaz requisitos nem confere imunidade universal.
+O benefício do art. 195, § 7º, tem fundamento constitucional.¦Isso o distingue conceitualmente de mera dispensa por lei ordinária.
-Imunidade da entidade significa que seus empregados deixam necessariamente de ser segurados obrigatórios.¦A posição da entidade e a filiação dos trabalhadores são relações distintas.
+A LC 187 disciplina a certificação e requisitos das entidades beneficentes.¦O enquadramento demanda observância do regime legal pertinente.
-Imunidade tributária e isenção são sempre criadas pela mesma espécie de ato administrativo.¦Imunidade tem fundamento constitucional; isenção depende de lei competente.
+O alcance da desoneração deve ser examinado segundo a contribuição e a hipótese abrangidas.¦Não há dispensa indistinta de toda obrigação pelo simples reconhecimento do benefício.
-O reconhecimento de imunidade elimina automaticamente todos os deveres de informação da entidade.¦Obrigações acessórias devem ser analisadas em sua disciplina própria.
+Requisitos legais não podem ser substituídos apenas por declaração de boa intenção social.¦A prova do enquadramento exige cumprimento das condições pertinentes.
-Um servidor pode conceder imunidade fora da Constituição por considerar a entidade simpática.¦A administração deve observar fundamento constitucional e requisitos legais.
+Contribuição patronal e contribuição descontada do segurado precisam ser distinguidas ao examinar a imunidade.¦O sujeito beneficiado e a obrigação abrangida devem estar identificados.
-Uma escola comercial com distribuição de lucro satisfaz automaticamente os requisitos beneficentes por oferecer aula.¦Atividade educacional isolada não comprova enquadramento na imunidade.
+A manutenção do benefício requer observar o regime de requisitos e controles aplicáveis.¦O enquadramento não se presume eternamente sem condições.
-Certificado relativo a uma área autoriza concluir, sem análise, imunidade para qualquer atividade e tributo.¦Âmbito, requisitos e efeitos precisam ser confrontados com a lei.
+A origem constitucional da proteção limita o poder de cobrança na hipótese correspondente.¦Imunidade é limitação constitucional, não mera liberalidade individual do fisco.
-O atendimento de uma única condição dispensa todas as demais exigências legais.¦Os requisitos pertinentes devem ser examinados em conjunto.
''')

add('B06-S01','c','art. 28, I a IV e §§',
'Salário de contribuição é a base legal da contribuição pessoal. Para empregado e avulso, relaciona-se à remuneração destinada a retribuir o trabalho, inclusive valores devidos e utilidades nos termos legais. Para doméstico, remuneração registrada e comprovada; para contribuinte individual, remuneração da atividade; para facultativo, valor declarado, respeitados limites.',
'Um facultativo declara base dentro dos limites permitidos; um empregado não pode simplesmente substituir sua remuneração real por um valor arbitrário declarado.',
'Base de contribuição não é salário líquido nem valor da contribuição. Cada categoria possui definição legal.',
'Parcelas e limites devem ser examinados: a denominação contábil sozinha não decide a incidência.', '''
+O salário de contribuição é uma base sobre a qual se apura a contribuição do segurado.¦Base de cálculo e valor final de contribuição são grandezas diferentes.
-O salário líquido após descontos é necessariamente o salário de contribuição de toda categoria.¦A base decorre da definição legal, não do resultado líquido do pagamento.
+A remuneração devida ao empregado pode integrar a base mesmo antes do efetivo pagamento.¦O art. 28 considera rendimentos pagos, devidos ou creditados destinados a retribuir o trabalho.
-O empregado pode declarar qualquer base sem relação com a remuneração de sua atividade.¦A declaração de valor é disciplina própria do facultativo, não escolha livre do empregado.
+O valor declarado pelo facultativo deve observar os limites legais.¦A liberdade de declaração não afasta mínimo, teto e condições aplicáveis.
-O contribuinte individual possui base formada exclusivamente por salário de emprego.¦A categoria pode obter remuneração por atividade por conta própria ou serviços sem emprego.
+Utilidades habituais podem integrar a remuneração contributiva segundo a lei.¦A forma não monetária não exclui automaticamente a verba.
-Toda quantia recebida por pessoa física é salário de contribuição, sem qualquer exclusão.¦Há definições por categoria e parcelas legalmente não integrantes.
+A base do doméstico deve refletir a remuneração registrada e comprovada segundo a disciplina legal.¦O registro não autoriza substituir os fatos por valor fictício.
-O salário de contribuição é o próprio valor da aposentadoria concedida.¦Base contributiva e renda de benefício são institutos distintos.
+A remuneração de uma ou mais empresas pode ser relevante para a base do empregado.¦Atividades concomitantes exigem exame do conjunto e do limite aplicável.
-O recebimento por hora impede qualquer identificação de base previdenciária.¦A forma horária de remuneração possui tratamento compatível com o custeio.
+Adiantamento decorrente de reajuste salarial pode integrar a remuneração contributiva.¦O art. 28 inclui esse tipo de pagamento destinado ao trabalho.
-O facultativo deve comprovar empregador para existir base de contribuição declarada.¦A categoria não depende de emprego e possui disciplina própria de declaração.
+A natureza retributiva do pagamento importa para classificar a parcela.¦O nome utilizado em recibo não é critério isolado suficiente.
-O teto autoriza ocultar toda remuneração efetiva dos registros de folha.¦Limitar a base contributiva não autoriza falsificar informações remuneratórias.
''')
add('B06-S02','c','art. 28, I, §§ 2º e 7º',
'Integram a base, nas condições legais, remunerações retributivas do trabalho: salários, comissões, gorjetas, horas extras, adicionais remuneratórios e utilidades habituais, sem prejuízo das exclusões específicas. O salário-maternidade é considerado salário de contribuição da segurada pela regra legal própria; o décimo terceiro tem tratamento específico e incidência separada conforme sua disciplina.',
'Uma comissão de venda paga como parte da remuneração não perde natureza retributiva por ser variável. Já uma restituição comprovada de despesa exige análise distinta.',
'Periodicidade ou nome de verba, isoladamente, não substituem exame de natureza e regras legais.',
'A contribuição da segurada sobre salário-maternidade não deve ser confundida com a decisão sobre contribuição patronal dessa verba.', '''
+Comissões destinadas a remunerar vendas podem integrar o salário de contribuição.¦A remuneração variável pelo trabalho não é excluída apenas por não ser salário fixo.
-Gorjetas estão sempre fora da base apenas porque são pagas por clientes.¦O art. 28 inclui gorjetas na remuneração contributiva pertinente.
+Horas extras remuneratórias devem ser consideradas conforme sua natureza e disciplina contributiva.¦A contraprestação pelo trabalho extraordinário não é automaticamente indenização.
-O décimo terceiro é sempre irrelevante para contribuição previdenciária.¦A legislação prevê incidência e tratamento específico da gratificação natalina.
+O salário-maternidade recebe previsão legal como salário de contribuição da segurada.¦A lei estabelece essa regra própria, distinta do debate de contribuição patronal.
-A incidência relativa à segurada prova que a contribuição patronal possui necessariamente o mesmo tratamento no salário-maternidade.¦São obrigações distintas, com disciplina e jurisprudência próprias.
+A utilidade habitual que remunera trabalho exige exame de incidência e das exclusões legais.¦A ausência de dinheiro não basta para afastar a base.
-Chamar salário de ajuda em um recibo afasta automaticamente contribuição.¦A natureza real do pagamento deve ser examinada.
+Valores devidos pelo trabalho podem ser relevantes ainda que não quitados no prazo.¦A definição legal não considera exclusivamente valores efetivamente pagos.
-Toda verba variável é indenizatória e não integra a base.¦Variabilidade não determina, sozinha, natureza indenizatória.
+Adicionais remuneratórios pagos pelo trabalho podem compor a base legal.¦É preciso identificar natureza e regra aplicável à parcela.
-A gratificação natalina necessariamente aumenta a média de salário de benefício porque sofre contribuição.¦Incidência contributiva e inclusão no cálculo do benefício não são efeitos equivalentes.
+Reajuste salarial retroativo deve ser identificado por suas competências e natureza remuneratória.¦Pagamento posterior não torna a verba automaticamente estranha ao custeio.
-A remuneração em múltiplos vínculos permite ignorar salários de uma das fontes sem qualquer ajuste.¦A soma e o limite contributivo precisam ser observados.
+O valor pago como salário básico é um ponto de partida da análise da remuneração contributiva.¦Outras parcelas retributivas e exclusões devem ser examinadas além dele.
-Uma verba remuneratória pode ser excluída livremente pelo empregador para reduzir encargos.¦A incidência é definida pelas normas aplicáveis, não por conveniência.
''')
add('B06-S03','c','art. 28, § 9º',
'O art. 28, § 9º, enumera parcelas não integrantes e condições. Benefícios do RGPS, salvo a regra própria do salário-maternidade; férias indenizadas e adicional correspondente; indenização do FGTS; diárias para viagem; e outras verbas legalmente previstas exigem enquadramento exato. Nem todo pagamento chamado prêmio, ajuda ou reembolso atende automaticamente às condições.',
'Reembolso comprovado de despesa do trabalho deve ser distinguido de salário disfarçado. A exclusão legal deve corresponder aos fatos e à rubrica correta.',
'Férias indenizadas e férias gozadas não são intercambiáveis. Exclusão do segurado e discussão sobre contribuição patronal devem ser separadas.',
'Não resumir a lista a nomes: requisitos, limites e redação vigente importam para a exclusão.', '''
+A lista legal de exclusões deve ser confrontada com a natureza efetiva do pagamento.¦O rótulo utilizado pelo pagador não substitui o enquadramento.
-Todo benefício do RGPS é tratado da mesma forma que remuneração normal de emprego.¦A lei prevê exclusão de benefícios, com ressalva própria do salário-maternidade.
+Férias indenizadas possuem exclusão expressa no art. 28, § 9º.¦Não devem ser confundidas com férias usufruídas e suas regras.
-A exclusão das férias indenizadas demonstra que toda verba chamada férias tem regime idêntico.¦A hipótese indenizada deve ser distinguida das demais.
+Indenização compensatória do FGTS tem natureza distinta de salário retributivo.¦A lei contempla sua exclusão na disciplina pertinente.
-Qualquer valor pago ao trabalhador pode ser excluído se for denominado indenização.¦É necessário verificar a natureza real e a hipótese normativa.
+Diárias para viagens estão tratadas na enumeração de não integrantes na redação legal vigente.¦A classificação exige observar o regime legal da verba.
-Um reembolso fictício de despesa inexistente é necessariamente excluído apenas pelo nome reembolso.¦A rubrica precisa corresponder aos fatos e condições legais.
+O abono de férias previsto na legislação trabalhista tem hipótese própria na lista legal.¦É necessário observar a forma e condições da exclusão.
-A exclusão de uma parcela dispensa manter qualquer documento que demonstre sua natureza.¦Comprovação e informação adequadas continuam relevantes.
+Verbas previdenciárias e salariais devem ser identificadas separadamente na folha.¦A natureza jurídica influencia a incidência e os registros.
-Uma aposentadoria recebida do RGPS é salário de contribuição por ser paga mensalmente.¦Periodicidade mensal não a transforma em remuneração do trabalho contributiva.
+Pagamentos indenizatórios específicos podem estar fora da base mediante previsão e requisitos legais.¦A exclusão decorre do regime jurídico, não de decisão arbitrária.
-Se uma parcela é excluída, toda remuneração restante do segurado também deve ser excluída.¦O tratamento é realizado por verba e hipótese aplicável.
+A leitura da exclusão deve considerar a redação atual e a competência discutida.¦Alterações legislativas podem modificar o tratamento temporal.
-A lista legal autoriza ignorar a diferença entre remuneração efetiva e ressarcimento de despesa.¦Essa distinção é central para aplicar corretamente a base contributiva.
''')
add('B06-S04','c','art. 28, § 3º; CF, art. 195, § 14; EC 103/2019, art. 29',
'O limite mínimo do salário de contribuição deve ser estudado por categoria e regra de remuneração, inclusive piso salarial e duração efetiva do trabalho. É diferente da exigência de contribuição mínima mensal para reconhecimento de competência a partir da EC 103. Uma remuneração proporcional não pode ser simplesmente inventada como se tivesse sido paga integralmente.',
'Em mês de admissão com remuneração proporcional inferior ao mínimo mensal, a informação do trabalho deve refletir os fatos; a utilização previdenciária da competência pode demandar ajuste segundo as regras aplicáveis.',
'Piso de remuneração, base proporcional e condição para reconhecimento previdenciário da competência são perguntas diferentes.',
'Evitar a generalização de que qualquer pagamento abaixo do mínimo em qualquer época produz sempre o mesmo efeito.', '''
+A categoria do segurado é relevante para examinar o limite mínimo da base.¦A Lei 8.212 traz critérios que não podem ser substituídos por uma fórmula indistinta.
-O limite mínimo autoriza informar salário fictício integral em mês de admissão proporcional.¦Informações devem refletir os fatos e ajustes devem seguir a disciplina própria.
+O piso da categoria pode ser relevante para a definição legal do mínimo do empregado.¦A lei considera piso legal ou normativo na hipótese pertinente.
-Remuneração e contribuição são conceitos idênticos, de modo que um real de salário corresponde sempre a um real de contribuição.¦Contribuição resulta da aplicação da regra de cálculo à base.
+A exigência mensal introduzida pela EC 103 deve ser analisada com as formas admitidas de ajuste.¦Contribuição abaixo do mínimo pode demandar complementação, utilização ou agrupamento legal.
-Ter trabalhado um único dia prova automaticamente cumprimento integral de qualquer requisito contributivo mensal posterior à reforma.¦O reconhecimento da competência depende das condições constitucionais e regulamentares.
+Uma competência de data anterior à reforma exige identificar o regime temporal pertinente.¦Não se aplica retroativamente toda regra nova sem análise.
-O salário mínimo de um ano futuro deve ser aplicado automaticamente para reescrever todas as remunerações históricas.¦O período de referência e a norma de atualização precisam ser observados.
+O mínimo da base não se confunde com o valor de todo benefício previdenciário.¦Bases de custeio e rendas de benefício possuem funções diferentes.
-O cumprimento do mínimo dispensa comprovar a existência da atividade obrigatória alegada.¦Valor recolhido não substitui, por si só, a prova do fato de enquadramento.
+A remuneração total em atividades concomitantes pode ser relevante para alcançar o mínimo mensal.¦A disciplina da soma deve ser considerada antes de concluir pela insuficiência.
-Toda remuneração abaixo do mínimo significa necessariamente fraude do trabalhador.¦Podem existir trabalho proporcional e situações regulares que exigem tratamento adequado.
''')
add('B06-S05','c','art. 28, § 5º; art. 22',
'O teto limita a base de contribuição pessoal do segurado conforme a regra aplicável. Não é proibição de receber salários maiores nem teto automático da contribuição patronal sobre remuneração. Atividades concomitantes precisam ser coordenadas para observar a base total. Valores anuais mudam; exercícios podem declarar teto hipotético para testar apenas a lógica.',
'Se o enunciado fixa teto hipotético de R$ 10.000 e remuneração de R$ 12.000 em base ordinária sujeita ao teto, o excedente de R$ 2.000 não integra a base pessoal limitada nessa hipótese.',
'Teto de base não é valor de contribuição, de remuneração ou garantia automática de benefício no teto.',
'O limite e sua incidência devem ser considerados conforme o período e a rubrica; gratificação natalina tem disciplina própria.', '''
+Receber salário acima do teto não é proibido apenas pela existência do limite previdenciário.¦O limite se refere à base contributiva pertinente, não à remuneração total.
-O teto do segurado reduz necessariamente toda base patronal ao mesmo valor.¦A contribuição empresarial possui disciplina própria e não recebe esse limite universal.
+A soma das bases pessoais em atividades concomitantes exige observância do limite aplicável.¦Não se multiplica automaticamente o teto por vínculo.
-Contribuir no teto garante que toda aposentadoria será concedida no teto.¦O cálculo do benefício depende do histórico e das regras aplicáveis.
+Teto hipotético de R$ 10.000 e remuneração de R$ 12.000 permitem base pessoal limitada de R$ 10.000 no exercício declarado.¦A base limitada corresponde ao menor entre a remuneração contributiva e o teto da hipótese.
-O valor do teto é a quantia mensal que todo segurado deve pagar de contribuição.¦É limite da base; a contribuição decorre do cálculo aplicável.
+O teto deve ser identificado segundo a competência estudada.¦Valores podem ser atualizados ao longo do tempo.
-O limite vigente hoje substitui automaticamente todos os limites utilizados em competências passadas.¦Cada período possui referência legal e temporal própria.
+Bases abaixo do teto continuam sujeitas às regras de incidência pertinentes.¦O teto limita o máximo, mas não elimina a contribuição das faixas inferiores.
-Um segurado com dois empregos possui obrigatoriamente dois tetos integrais para sua contribuição pessoal na mesma competência.¦A soma e os procedimentos de limitação devem ser observados.
+Informar remuneração real e limitar base de cálculo são operações distintas.¦A limitação não autoriza falsificar o valor efetivamente remunerado.
-O excedente ao teto do segurado torna toda a remuneração isenta de qualquer encargo previdenciário.¦O limite pessoal não cria essa exclusão universal.
''')
add('B06-S06','c','art. 28, § 5º; normas anuais de reajustamento',
'Limites contributivos e faixas são atualizados por atos e critérios legais. A Lei 8.212 relaciona o reajuste do limite máximo aos critérios dos benefícios continuados. É indispensável identificar competência, publicação e efeitos da tabela. Atualização do teto não significa aumento individual automático de salário nem concessão de benefício maior sem cálculo.',
'Um cálculo referente a janeiro deve usar a tabela com efeitos naquela competência, ainda que o exercício seja resolvido meses depois.',
'Reajuste de limite, reajuste de benefício e aumento salarial individual não são a mesma operação.',
'Não memorizar valor anual como norma permanente. Este material prioriza método e não fixa valores de tabela sujeitos a atualização.', '''
+A competência é necessária para escolher a tabela contributiva adequada.¦O cálculo deve seguir os efeitos temporais da norma pertinente.
-O teto previdenciário é valor fixo imutável desde a publicação da Lei 8.212.¦A legislação prevê reajustamento e atualização dos limites.
+A publicação de tabela nova exige verificar sua data de efeitos.¦Data de publicação e competência de aplicação precisam ser conferidas.
-O aumento do teto significa aumento obrigatório do salário de todo empregado no mesmo percentual.¦Limite contributivo e reajuste salarial individual têm objetos distintos.
+Uma contribuição histórica deve ser examinada com referência ao período correspondente.¦Aplicar valor atual sem base temporal pode produzir erro.
-Atualizar teto é o mesmo que conceder automaticamente aposentadoria a quem ainda não preenche requisitos.¦Alteração de limite não substitui condições de benefício.
+O limite máximo acompanha o regime de reajustamento legalmente previsto.¦A Lei 8.212 não autoriza o empregador a fixá-lo livremente.
-Cada empresa escolhe seu próprio teto previdenciário anual sem norma pública.¦Limites do regime são definidos normativamente.
+Mudança de faixas pode alterar o cálculo mesmo sem mudança de categoria do segurado.¦Valores da tabela e categoria são variáveis distintas.
-Uma tabela sem indicação de ano é sempre suficiente para qualquer questão sobre contribuição.¦A validade temporal é informação essencial.
+A revisão de conteúdo deve registrar a competência dos valores usados em exemplos.¦Isso permite distinguir regra estrutural de número anual.
-A atualização dos limites dispensa reexaminar uma guia com competência informada incorretamente.¦Erro de competência afeta a identificação da regra e do registro corretos.
''')
add('B06-S07','ec','art. 29; INSS, Ajustes para alcance do salário mínimo',
'Na disciplina posterior à EC 103, a soma mensal inferior ao mínimo pode exigir ajuste para reconhecimento da competência. As formas admitidas incluem complementação, uso de excedente de outra competência e agrupamento, nos termos legais. Os ajustes devem respeitar o mesmo ano civil e a orientação do INSS; a iniciativa pode ocorrer a qualquer tempo, com efeitos próprios após processamento.',
'Duas competências insuficientes do mesmo ano podem ser analisadas para agrupamento nos termos permitidos. Não se pode assumir que isso mantém automaticamente duas competências completas.',
'Complementar com pagamento é diferente de usar excedente ou agrupar valores já existentes.',
'Não confundir esse ajuste de alcance do mínimo com complementação de alíquota de plano simplificado para outros efeitos.', '''
+Complementação e agrupamento são formas distintas de ajuste.¦Uma envolve suprir insuficiência; a outra reorganiza competências nos limites admitidos.
-A contribuição abaixo do mínimo após a reforma é sempre irreparável.¦A EC 103 prevê formas de ajuste segundo os requisitos legais.
+As competências usadas nos ajustes devem respeitar o mesmo ano civil na disciplina apresentada pelo INSS.¦O período de janeiro a dezembro é limite relevante da operação.
-A mera solicitação de agrupamento garante manter todas as competências originais como meses completos.¦O aproveitamento depende do resultado e das condições do ajuste.
+O aproveitamento de excedente não equivale necessariamente a novo pagamento.¦Pode utilizar valor já existente segundo as regras aplicáveis.
-O segurado pode tratar décimo terceiro como qualquer competência mensal para os ajustes indicados pelo INSS.¦A orientação exclui o décimo terceiro dessas operações de ajuste.
+A insuficiência deve ser examinada considerando a soma das remunerações pertinentes do mês.¦Não se conclui pelo resultado de um único vínculo quando existem outros.
-Ajustar o mínimo mensal e complementar alíquota de plano simplificado são sempre a mesma operação.¦São problemas contributivos distintos com fundamentos próprios.
+O INSS informa que os ajustes podem ser promovidos por iniciativa do segurado a qualquer tempo, observadas as condições.¦A realização posterior não elimina a exigência de competências do mesmo ano civil.
-A complementação dispensa registrar corretamente a competência beneficiada.¦A identificação do período é essencial ao processamento e aos efeitos.
+Após processados, os ajustes possuem caráter irreversível e irrenunciável segundo a orientação do INSS.¦A escolha deve considerar os efeitos de reorganização das competências.
-Uma contribuição de ano anterior pode ser livremente agrupada com qualquer outra de ano diferente.¦A orientação exige o mesmo ano civil para as competências utilizadas.
''')
add('B06-S08','c','art. 28, I, III e § 5º; Decreto 3.048/1999, art. 214',
'Em atividades concomitantes, devem ser considerados os rendimentos de cada vínculo e os procedimentos de observância do teto da contribuição pessoal. Isso pode demandar informação entre fontes e prova de descontos. O teto não é multiplicado automaticamente por emprego. Base pessoal limitada não afasta obrigações próprias dos tomadores.',
'Com teto hipotético de R$ 10.000 e bases remuneratórias de R$ 6.000 e R$ 6.000 no mesmo mês, a soma é R$ 12.000, mas a base pessoal limitada da hipótese é R$ 10.000.',
'Duas atividades são duas relações de filiação, mas não necessariamente dois tetos pessoais ou dois meses de tempo em um único mês.',
'Os cálculos dependem de categoria e regras de retenção; o exemplo numérico não fixa o teto real de 2026.', '''
+Com teto hipotético de R$ 10.000 e duas bases de R$ 6.000 no mês, a soma remuneratória excede o teto em R$ 2.000.¦A soma é R$ 12.000; o excedente precisa ser distinguido da base pessoal limitada.
-O segurado com dois empregos pode ignorar um vínculo no cadastro por já contribuir no outro.¦As atividades e remunerações devem ser corretamente informadas.
+A comprovação de desconto em outra fonte pode ser relevante para observar o limite contributivo pessoal.¦Os responsáveis precisam aplicar os procedimentos próprios de coordenação.
-Cada empregador cria novo teto pessoal integral sem qualquer consideração dos demais vínculos.¦O teto do segurado deve ser observado no conjunto das bases pertinentes.
+Remuneração acima do teto pode continuar relevante para a base empresarial comum.¦Limite da contribuição pessoal não é teto universal do encargo patronal.
-Concomitância transforma o facultativo em categoria apropriada para toda atividade adicional remunerada.¦Atividade abrangida deve ser classificada em sua categoria obrigatória.
+Com bases de R$ 3.000 e R$ 2.000 e teto hipotético de R$ 10.000, a soma de R$ 5.000 fica abaixo desse teto.¦O limite máximo não é alcançado nessa hipótese numérica.
-A existência de duas fontes permite inventar remuneração zero em uma delas para simplificar recolhimentos.¦Informações devem corresponder aos fatos; ajustes não autorizam falsificação.
+A análise conjunta das atividades não significa que as duas contribuições têm necessariamente o mesmo responsável.¦Responsabilidades variam conforme categoria e tomador.
-Dois empregos no mesmo mês geram automaticamente dois meses de contribuição no mesmo regime.¦Tempo simultâneo não se duplica dessa forma.
+Base total, limite máximo e descontos já realizados devem ser distinguidos no cálculo.¦Misturar as grandezas pode gerar cobrança pessoal acima do limite.
-Contribuir no teto em um mês autoriza deixar de declarar qualquer trabalho no mês seguinte.¦As obrigações são examinadas por competência e atividade.
''')
add('B06-S09','c','art. 28; Lei 8.213/1991, arts. 28 e 29; EC 103/2019, art. 26',
'Salário de contribuição é base de custeio. Salário de benefício é referência de cálculo de determinadas prestações, formada conforme a regra aplicável. Renda mensal é o valor do benefício após aplicar coeficientes, limites e critérios próprios. Nem todo benefício usa cálculo idêntico; a incidência de contribuição sobre uma verba não determina todos os efeitos no cálculo da prestação.',
'Se um exercício declara salário de benefício de R$ 3.000 e coeficiente hipotético de 80%, a renda obtida antes de outros ajustes previstos será R$ 2.400. Isso não significa que R$ 3.000 era o valor da contribuição mensal.',
'Base de contribuição, média de cálculo e renda devida são etapas distintas.',
'O coeficiente do exemplo é explicitamente hipotético; para benefício real, identificar espécie, período e regra vigente.', '''
+Salário de contribuição e salário de benefício exercem funções jurídicas diferentes.¦Um se refere ao custeio; o outro, ao cálculo de determinadas prestações.
-A renda mensal é sempre igual ao último salário de contribuição de qualquer segurado.¦O valor depende da espécie e das regras de cálculo pertinentes.
+Um coeficiente pode ser aplicado à referência de cálculo para obter a renda mensal.¦Essa etapa não deve ser confundida com a base do custeio.
-O valor pago de contribuição mensal é necessariamente o salário de benefício.¦Contribuição é resultado da regra tributária aplicada à base.
+No exemplo hipotético de salário de benefício de R$ 3.000 e coeficiente de 80%, o produto é R$ 2.400.¦O cálculo declarado é 3.000 multiplicado por 0,80, antes de outros ajustes da hipótese.
-Todo benefício do RGPS tem exatamente a mesma fórmula e o mesmo coeficiente.¦Espécies e regimes temporais possuem regras próprias.
+O histórico contributivo pode ser relevante para a formação da referência de cálculo.¦A regra aplicável define quais períodos e valores entram na apuração.
-Se uma verba sofre contribuição, ela integra obrigatoriamente qualquer fórmula de benefício de modo idêntico.¦Incidência e efeitos no cálculo não se confundem automaticamente.
+A espécie do benefício deve ser identificada antes de aplicar uma fórmula.¦Sem isso, é possível usar regra de prestação diferente.
-Salário de contribuição é expressão reservada exclusivamente aos benefícios assistenciais.¦É instituto de custeio previdenciário, não base geral do BPC.
+Limites e reajustes podem afetar a renda conforme a disciplina da prestação.¦O cálculo não termina necessariamente na simples média de valores.
-Uma média hipotética ensinada em aula comprova o valor de aposentadoria real de todo usuário.¦Exemplo pedagógico não substitui cálculo individual conforme dados e norma.
''')

add('B07-S01','rfb','arts. 2º, 3º e 16; INSS, competências institucionais',
'A Lei 11.457 atribuiu à Receita Federal do Brasil administração tributária das contribuições especificadas: tributação, fiscalização, arrecadação, cobrança e recolhimento. O INSS continua com reconhecimento, manutenção e pagamento das prestações e serviços de sua competência. Cobrança tributária não deve ser confundida com concessão de aposentadoria; dívida ativa da União tem atuação própria da PGFN.',
'Um erro em requerimento de aposentadoria não se transforma em procedimento de lançamento tributário apenas porque o interessado recolhe contribuição. Cada órgão atua no processo de sua competência.',
'Receita administra tributos; INSS administra prestações de sua competência. Essa divisão não significa ausência de compartilhamento de informações ou cooperação.',
'Não usar texto histórico que atribua genericamente toda arrecadação ao INSS como se a divisão de 2007 não existisse.', '''
+A RFB possui competência legal de fiscalização das contribuições indicadas na Lei 11.457.¦A lei transferiu atribuições de administração tributária pertinentes à Receita Federal do Brasil.
-O INSS e a Receita Federal são apenas dois nomes da mesma autarquia.¦São estruturas distintas, com competências legalmente diferenciadas.
+O reconhecimento de direito a benefício do RGPS permanece entre as funções institucionais do INSS.¦Administração de prestação não se confunde com administração tributária.
-A Receita Federal concede automaticamente toda aposentadoria por receber informações de contribuições.¦Arrecadação tributária não equivale à competência de concessão de benefício.
+Arrecadação e cobrança de contribuições são atividades de administração tributária previstas para a RFB.¦O art. 2º enumera essas funções na hipótese legal.
-A transferência de atribuições tributárias extinguiu todos os serviços previdenciários do INSS.¦A divisão de competências não suprimiu a administração de benefícios e serviços.
+Obrigações tributárias referentes às contribuições abrangidas devem ser cumpridas perante a RFB.¦A lei explicita o destinatário das obrigações pertinentes.
-Todo recurso de benefício deve ser tratado como impugnação de lançamento tributário na Receita.¦Processos de benefício e processos fiscais possuem objetos e vias próprias.
+A finalidade da contribuição não torna idênticas as competências de tributar e conceder benefício.¦Destinação previdenciária não elimina a divisão legal de atribuições.
-Uma agência do INSS pode dispensar tributo administrado pela RFB por mera conveniência no atendimento.¦Competência, legalidade e procedimento devem ser observados.
+A Lei 11.457 extinguiu a Secretaria da Receita Previdenciária na disciplina de reorganização.¦A reorganização integrou atribuições na Receita Federal do Brasil.
-A fiscalização tributária de contribuições passou a ser opção facultativa das empresas.¦A reorganização administrativa não extinguiu obrigações tributárias.
+O tratamento de dívida ativa da União envolve competência legal da PGFN.¦Essa atuação deve ser diferenciada da análise administrativa de benefício.
-O reconhecimento de atividade pelo INSS significa, por si só, quitação de todo crédito tributário correspondente.¦Reconhecimento de vínculo e pagamento de tributo são questões diferentes.
+A administração tributária pode necessitar de informações cadastrais e remuneratórias.¦A divisão institucional pressupõe o cumprimento de deveres informacionais pertinentes.
-O segurado deve pedir aposentadoria ao empregador como se ele substituísse o INSS.¦O empregador tem deveres de custeio e informação, não competência geral de concessão do RGPS.
+Pagamento de benefício e recolhimento de contribuição são fluxos distintos a identificar em uma questão.¦Misturar esses fluxos pode levar a atribuir competência ao órgão errado.
-A competência fiscal permite à RFB criar por ato próprio qualquer benefício previdenciário.¦Competência tributária administrativa não é poder legislativo ilimitado sobre prestações.
+A divisão de atribuições exige ler a legislação institucional posterior às fontes históricas.¦Textos antigos podem descrever distribuição superada de funções.
-Uma questão sobre benefícios e outra sobre lançamento de contribuição devem necessariamente ter o mesmo órgão e procedimento.¦A matéria e a competência legal determinam os procedimentos adequados.
''')
add('B07-S02','c','art. 30; Lei 10.666/2003, art. 4º; LC 150/2015, arts. 34 e 35',
'Arrecadar contribuição e recolher o valor ao sistema são deveres atribuídos a sujeitos específicos. Empresas descontam contribuições de empregados e avulsos e recolhem nos termos legais. A contratação de contribuinte individual por empresa possui disciplina própria. Facultativo e contribuinte individual responsável pelo próprio pagamento devem observar seu regime. Tomadores rurais e domésticos exigem regras particulares.',
'Descontar do salário e não repassar não equivale a recolher. Emitir guia também não comprova que a obrigação de pagamento foi satisfeita.',
'Ser segurado não significa ser sempre responsável operacional por recolher toda parcela. A cota da empresa é distinta do desconto do trabalhador.',
'Não universalizar uma regra para todos os prestadores; categoria, tomador, atividade e período são necessários.', '''
+A empresa deve observar os deveres legais de desconto e recolhimento relativos a empregados.¦O custeio não é deixado apenas à iniciativa individual de cada empregado.
-Descontar contribuição do salário equivale automaticamente a repassá-la ao fisco.¦Retenção e efetivo recolhimento são etapas diferentes.
+O facultativo deve providenciar o pagamento segundo a disciplina de sua contribuição.¦Sua filiação não pressupõe empregador encarregado da folha.
-A emissão de guia comprova, por si só, que o débito foi integralmente pago.¦É necessário distinguir documento emitido de arrecadação realizada.
+A prestação do contribuinte individual a empresa possui regra específica de arrecadação.¦A responsabilidade não deve ser presumida como idêntica a toda prestação a pessoa física.
-Todo trabalhador, inclusive empregado, deve sempre recolher por conta própria o desconto que a empresa reteve.¦A lei atribui obrigações de arrecadação ao tomador nas hipóteses pertinentes.
+A contribuição própria da empresa deve ser distinguida dos valores descontados dos segurados.¦São obrigações diferentes mesmo quando informadas em sistemas relacionados.
-O acordo de trabalho pode eliminar livremente a responsabilidade de recolhimento imposta pela lei.¦Dever tributário não é afastado por simples pacto entre particulares.
+O empregador doméstico tem responsabilidade de recolhimento no regime próprio da LC 150.¦A natureza familiar não o dispensa da arrecadação legal.
-A existência de terceirização autoriza ignorar qualquer regra de retenção e responsabilidade.¦A operação deve ser examinada conforme seu regime específico.
+O tipo de adquirente de produção rural pode alterar o responsável pela arrecadação.¦As hipóteses legais de sub-rogação e recolhimento próprio precisam ser identificadas.
-Um código bancário escolhido incorretamente prova que o sujeito era legalmente facultativo.¦Código de pagamento não substitui o enquadramento da atividade.
+Dados corretos do trabalhador e da competência são necessários ao recolhimento adequado.¦Pagamento sem identificação correta pode exigir regularização.
-A filiação obrigatória do empregado só existe depois de o banco confirmar o repasse patronal.¦A atividade enquadrada é o fato constitutivo da filiação obrigatória.
+O dever de informar pode continuar relevante mesmo quando não há valor a pagar naquela hipótese.¦Obrigação de informação não se confunde automaticamente com obrigação principal.
-A responsabilidade atribuída à empresa a autoriza a descontar do empregado qualquer encargo patronal.¦O alcance dos descontos depende da lei e não inclui livre transferência de obrigações próprias.
+O recebimento de remuneração pode gerar obrigações contributivas apesar de o trabalhador ter outro vínculo.¦Atividades concomitantes exigem coordenação, não omissão do vínculo.
-A falta de recibo de pagamento é prova absoluta de inexistência da atividade remunerada.¦Fatos e recolhimentos devem ser apurados pelos meios admitidos, sem presunção absoluta desse tipo.
+Recolhimento em duplicidade ou superior ao devido exige procedimento próprio de regularização.¦Não se deve corrigir o erro inventando vínculo ou competência.
-Identificar quem deve pagar é desnecessário quando o enunciado já informa a alíquota.¦Sujeito responsável, base, período e vencimento são elementos distintos do cálculo.
''')
add('B07-S03','c','art. 32 e §§; Lei 11.457/2007, art. 2º, § 3º',
'Obrigações empresariais incluem preparar folha, lançar fatos geradores e contribuições em contabilidade discriminada, prestar informações corretas e cumprir declarações nos meios e prazos normativos. Obrigações acessórias são distintas do pagamento. Sistemas digitais não dispensam veracidade, identificação do trabalhador, competência e natureza das rubricas.',
'Informar folha com salário incorreto pode produzir erro de base mesmo que uma guia seja paga. Retificação declaratória e pagamento de diferenças são operações relacionadas, mas distintas.',
'Declarar não é pagar; pagar não autoriza declarar dados fictícios. Obrigação principal e obrigação acessória não se confundem.',
'O nome do sistema e prazos de transmissão podem mudar. Verifique o regime da competência, evitando ensinar ferramenta histórica como única atual.', '''
+A preparação da folha de pagamento integra as obrigações legais da empresa.¦A lei exige registro adequado de remunerações e segurados pertinentes.
-Pagar uma guia dispensa automaticamente prestar toda informação previdenciária exigida.¦Obrigações principais e acessórias possuem disciplina própria.
+A contabilidade deve discriminar fatos geradores e valores de contribuições conforme a lei.¦O registro contábil não se limita ao valor líquido do salário.
-Uma declaração pode informar qualquer remuneração fictícia desde que a empresa pague algum valor.¦A informação deve refletir os fatos e a base correta.
+A identificação da competência é relevante para associar remunerações e contribuições.¦Erros de período podem exigir regularização e afetar os registros.
-Transmitir declaração equivale necessariamente à quitação bancária de todo débito nela informado.¦Informação e pagamento são atos distintos.
+Retificações devem corrigir fatos incorretos pelos procedimentos adequados.¦A correção não pode ser substituída por apagar arbitrariamente registros históricos.
-A ausência de empregados dispensa invariavelmente toda obrigação cadastral ou declaratória de qualquer empresa.¦A existência e a dispensa de obrigações dependem do regime normativo aplicável.
+A natureza das rubricas precisa ser coerente com os pagamentos efetivos.¦Classificação incorreta pode alterar indevidamente incidência e informação.
-Registrar tudo como indenização torna a folha automaticamente regular.¦O nome da rubrica não substitui a natureza jurídica do pagamento.
+Sistemas digitais exigem dados verídicos e correspondentes ao período.¦A automatização não elimina responsabilidade sobre informações prestadas.
-A empresa pode reclassificar livremente empregados como facultativos na declaração para reduzir encargos.¦O enquadramento decorre da realidade e da lei.
+A obrigação de informar à RFB deve ser observada nas contribuições abrangidas pela Lei 11.457.¦A reorganização tributária define destinatário das obrigações pertinentes.
-A mudança do sistema eletrônico extingue todos os deveres legais de documentação.¦A ferramenta operacional não substitui nem elimina a obrigação legal por si só.
+Diferença entre declarado e devido pode exigir retificação e eventual recolhimento complementar.¦Regularizar informação e regularizar pagamento são medidas distintas conforme o erro.
-Identificação do segurado é dispensável se o total da folha estiver numericamente correto.¦Valores globais não substituem informações individualizadas exigidas.
''')
add('B07-S04','c','art. 30; eSocial, mudança do vencimento do DAE a partir de março/2024',
'Vencimento depende de sujeito, espécie e competência. Contribuinte individual responsável pelo próprio recolhimento e facultativo seguem, na regra mensal, dia 15 do mês seguinte, com postergação ao próximo dia útil sem expediente bancário. Empresas possuem regra geral dia 20 e antecipação se não útil, observadas hipóteses específicas. No DAE doméstico, o vencimento passou ao dia 20 desde março/2024, antecipado se não útil. Não confundir prazo declaratório, salarial e de pagamento de encargo.',
'Uma questão antiga pode usar o dia sete do DAE conforme a época. Para competência posterior à mudança de março/2024, aplicar automaticamente o prazo antigo é erro temporal.',
'Dia 15 com postergação e dia 20 com antecipação são regras distintas. Vencimento do salário não é o mesmo que vencimento de contribuição.',
'Calendário oficial, feriados, prorrogações excepcionais e espécie de obrigação podem alterar a data concreta.', '''
+O facultativo que recolhe mensalmente deve observar a regra geral do dia 15 do mês seguinte.¦O prazo próprio não é confundido com o DAE do empregador doméstico.
-Todo sujeito da seguridade paga obrigatoriamente na mesma data mensal.¦Prazos variam conforme responsabilidade e espécie de recolhimento.
+Na regra de recolhimento próprio do contribuinte individual, a falta de expediente bancário no vencimento leva à postergação prevista.¦A disciplina dessa hipótese difere das regras de antecipação.
-O prazo geral mensal do facultativo é o último dia do próprio mês trabalhado.¦A regra pertinente é o dia 15 do mês subsequente, observadas exceções.
+O DAE doméstico passou a vencer no dia 20 do mês seguinte desde a competência março/2024.¦A alteração oficial exige distinguir questões históricas e atuais.
-O dia sete permanece invariavelmente como vencimento do DAE de toda competência de 2026.¦O eSocial registra a mudança do vencimento a partir de março/2024.
+Quando o dia 20 do DAE não é útil, a orientação atual determina antecipação.¦O critério não é o mesmo da postergação do recolhimento próprio do facultativo.
-Prazo para pagar salário e prazo para recolher contribuição são sempre idênticos por definição.¦São obrigações diferentes, cada qual com sua disciplina.
+Na regra geral empresarial de dia 20, deve ser observada a antecipação quando prevista para dia sem expediente bancário.¦A escolha da data exige identificar a obrigação correta.
-Uma questão de 2016 deve receber automaticamente a data operacional do DAE de 2026 sem análise histórica.¦Gabarito histórico e regra vigente em outro período precisam ser separados.
+A competência da contribuição normalmente antecede seu vencimento mensal subsequente nas hipóteses estudadas.¦Período de referência e data de pagamento não são o mesmo dado.
-Uma prorrogação específica de prazo pode ser presumida sem ato ou calendário oficial.¦Exceções temporais exigem fonte competente e aplicabilidade ao caso.
+Há opção de recolhimento trimestral em hipóteses legais específicas, com regras próprias.¦Ela não é automaticamente admitida para qualquer sujeito e base.
-O prazo de transmissão de uma declaração sempre modifica, por si só, o vencimento do tributo.¦Declaração e pagamento possuem regras distintas e precisam de previsão própria.
+A identificação do tipo de guia ajuda a escolher a regra de vencimento.¦GPS, DAE e documentos empresariais não devem ser tratados como uma única situação.
-Consultar a data atual no celular basta para determinar qualquer vencimento histórico sem conhecer a competência.¦O cálculo depende do período, obrigação, calendário e norma pertinentes.
''')
add('B07-S05','l9430','art. 61; Lei 8.212/1991, art. 35',
'O atraso no pagamento pode gerar acréscimos legais. Para as contribuições abrangidas, a legislação remete ao regime de multa e juros da Lei 9.430. Multa de mora, juros e principal são parcelas diferentes. A multa diária de 0,33% é limitada a 20% no regime do art. 61; juros seguem critérios legais com Selic e regra do mês do pagamento. Não usar juros simples inventados nem confundir multa de mora com penalidade de ofício.',
'Em exemplo limitado à multa de mora do art. 61, principal de R$ 1.000 e atraso de dez dias produzem multa de R$ 33, antes de juros e demais condições. O exemplo não é cálculo de débito real nem substitui sistema oficial.',
'Correção de informação, pagamento do principal e quitação de acréscimos são operações distintas.',
'A apuração concreta depende de vencimento, data de pagamento, regime, eventuais exceções e taxa aplicável. Não inferir crime automaticamente de qualquer atraso.', '''
+O principal da contribuição deve ser distinguido dos acréscimos de mora.¦Atraso pode acrescentar parcelas sem alterar a identificação do tributo principal.
-Todo atraso gera automaticamente apenas juros, sendo impossível incidência de multa.¦O regime legal prevê multa de mora e juros conforme a hipótese.
+A multa de mora do art. 61 possui limite legal de 20%.¦A contagem diária não cresce indefinidamente além desse teto.
-A multa diária de 0,33% significa cobrar 33% do principal por dia.¦0,33% corresponde a 0,0033 da base diária, respeitado o limite.
+No exemplo de R$ 1.000 por dez dias, a multa de 0,33% ao dia resulta em R$ 33, sem outros acréscimos.¦O produto é 1.000 × 0,0033 × 10, abaixo do limite de 20%.
-Multa de mora e multa de ofício são expressões que sempre designam exatamente a mesma penalidade e percentual.¦Elas possuem fundamentos e regimes próprios.
+A Lei 8.212 remete ao regime de acréscimos pertinente da Lei 9.430 para as contribuições abrangidas.¦A apuração não é livre escolha do contribuinte ou do atendente.
-O pagamento do principal apaga necessariamente todo acréscimo legal já devido.¦A quitação deve considerar o débito e as condições legais aplicáveis.
+A data efetiva de pagamento é relevante para calcular a mora.¦Acréscimos dependem do período decorrido e do regime jurídico.
-Emitir guia de débito atrasado equivale a interromper automaticamente toda contagem de acréscimos sem pagar.¦Emissão não é quitação da obrigação.
+Juros calculados pela regra legal não devem ser substituídos por taxa arbitrária mensal.¦A taxa e o período devem seguir a legislação pertinente.
-Qualquer atraso, independentemente dos fatos e do tipo penal, prova automaticamente crime previdenciário.¦Responsabilidade penal exige análise dos requisitos próprios, não mera equivalência com mora.
+Uma retificação declaratória pode exigir reapuração de diferenças e acréscimos.¦Alterar a informação não elimina automaticamente débitos devidos.
-O limite de 20% da multa de mora corresponde a perdão automático do principal que exceder esse percentual.¦O teto limita a multa, não o valor principal da contribuição.
+A utilização de sistema oficial de cálculo reduz risco de aplicar taxa ou calendário incorreto.¦O cálculo concreto depende de informações e critérios atualizados.
-O contribuinte pode eliminar juros legalmente devidos simplesmente chamando o pagamento de contribuição normal.¦A denominação no pagamento não altera o regime jurídico do atraso.
''')

SUPPLEMENT={
'B02-S01':[{'title':S['p'][0],'url':S['p'][1],'locator':'ementa: Plano de Benefícios'}, {'title':S['cf'][0],'url':S['cf'][1],'locator':'arts. 194 a 204'}],
'B02-S02':[{'title':S['cf'][0],'url':S['cf'][1],'locator':'art. 195, § 6º: noventena das contribuições sociais'}],
'B02-S03':[{'title':S['ctn'][0],'url':S['ctn'][1],'locator':'art. 108, §§ 1º e 2º: limites da analogia e equidade'}, {'title':S['cf'][0],'url':S['cf'][1],'locator':'art. 195, § 5º: fonte de custeio total'}],
'B02-S04':[{'title':S['c'][0],'url':S['c'][1],'locator':'art. 85-A: acordos internacionais previdenciários'}, {'title':S['lin'][0],'url':S['lin'][1],'locator':'art. 6º: efeito imediato e proteções intertemporais'}],
'B03-S07':[{'title':S['cf'][0],'url':S['cf'][1],'locator':'art. 201, § 5º'}],
'B05-S02':[{'title':S['ec'][0],'url':S['ec'][1],'locator':'art. 28: progressividade da contribuição de empregado, doméstico e avulso'}],
'B05-S09':[{'title':S['lc187'][0],'url':S['lc187'][1],'locator':'arts. 1º a 3º'}],
'B06-S04':[{'title':S['cf'][0],'url':S['cf'][1],'locator':'art. 195, § 14: contribuição mínima mensal'}, {'title':S['ec'][0],'url':S['ec'][1],'locator':'art. 29: ajustes de contribuições inferiores ao mínimo'}],
'B06-S07':[{'title':'INSS — Ajustes para alcance do salário mínimo','url':'https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/ajustes-para-alcance-do-salario-minimo-emenda-constitucional-no-103-de-2019','locator':'Formas de ajuste; mesmo ano civil; iniciativa; efeitos após processamento'}],
'B06-S09':[{'title':S['p'][0],'url':S['p'][1],'locator':'arts. 28 e 29: salário de benefício'}, {'title':S['ec'][0],'url':S['ec'][1],'locator':'art. 26: cálculo de benefícios na disciplina da reforma'}],
'B07-S01':[{'title':S['h'][0],'url':S['h'][1],'locator':'O INSS — competências institucionais'}],
'B07-S04':[{'title':'eSocial — Mudança na data de vencimento do DAE','url':'https://www.gov.br/esocial/pt-br/noticias/mudanca-na-data-de-vencimento-do-dae','locator':'Competências a partir de março/2024; dia 20; antecipação se não útil'}, {'title':'Manual eSocial Empregador Doméstico 09/01/2026','url':'https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/manual-do-esocial-empregador-domestico-versao-09-01-2026.pdf','locator':'item 4.3.1, pp. 78–79: vencimento normal do DAE'}]
}

def build():
 lessons=[]
 assert len(rows)==50
 for row in rows:
  plan=row['id_planejamento'];key=plan.removeprefix('PREV-')
  assert key in D,('assunto ausente',key)
  source,locator,core,example,contrast,limit,qs=D[key]
  assert len(qs)==row['meta_questoes_autorais'],(key,len(qs),row['meta_questoes_autorais'])
  ref={'title':S[source][0],'url':S[source][1],'locator':locator}
  sources=[ref]+SUPPLEMENT.get(key,[])
  lid='v17-'+plan.lower()
  theory=[]
  for statement,answer,explanation in qs:
   # A explicação contém a regra corrigida também quando o enunciado é falso.
   if explanation not in theory:theory.append(explanation)
  lesson={'id':lid,'d':'prev','title':row['assunto'],'core':core,'rule':core+'\n\nPontos para compreender e aplicar:\n'+'\n'.join('• '+x for x in theory),'example':example,'contrast':contrast,'limit':limit,'source':source,'sources':sources,'minutes':40,'block':row['bloco'],'planId':plan,'subtopics':theory,'questions':[]}
  for i,(statement,answer,why) in enumerate(qs,1):
   assert len(why)>20,(key,i,why)
   qref=ref
   if key=='B02-S02' and i in [8,12]:qref=sources[1]
   if key=='B02-S03' and i in [2,8,9]:qref=sources[1]
   if key=='B02-S03' and i==12:qref=sources[2]
   if key=='B02-S04' and i in [6,7,8,12]:qref=sources[1]
   if key=='B02-S04' and i==9:qref=sources[2]
   if key=='B05-S02' and i in [3,4]:qref=sources[1]
   if key=='B05-S09' and i in [5,9,13,14,16]:qref=sources[1]
   if key=='B06-S04' and i in [5,6,7]:qref=sources[-1]
   if key=='B06-S07':qref=sources[-1]
   if key=='B06-S09' and i in [2,3,5,6,7,8,9,11,12]:qref=sources[1]
   if key=='B07-S01' and i in [3,5,6,8,16,17]:qref=sources[1]
   if key=='B07-S04' and ('DAE' in statement or 'doméstico' in statement):qref=sources[1]
   lesson['questions'].append({'id':f'{lid}-q{i:03d}','text':statement,'answer':answer,'explanation':why+' Fundamento de estudo: '+qref['locator']+'.','kind':'autoral','version':1,'difficulty':['basico','intermediario','avancado'][min(2,(i-1)//6)],'family':f'{plan}-angulo-{i:02d}','microtopic':plan,'sourceRef':qref,'mode':'fixacao' if i<=4 else 'reserva' if i>len(qs)*.75 else 'treino','editorialStatus':'conferencia-editorial-assistida','reviewedAt':'2026-10-27'})
  lessons.append(lesson)
 out={'lessons':lessons,'sources':[{'id':key,'title':v[0],'url':v[1]} for key,v in S.items()],'editorial':{'version':'1.7','authorship':'JARVIS_AUTORAL','createdAt':'2026-10-27','questionCount':sum(len(l['questions']) for l in lessons),'lessonCount':len(lessons),'scope':'PREV-B01 a PREV-B07','method':'Enunciados e justificativas explicitamente redigidos; Python apenas organiza e valida; sem expansão por troca de nomes ou números.','verification':'Conferência estrutural automática e redação editorial assistida. Não há revisão jurídica independente. Planalto bloqueou leitura direta nesta sessão; textos atualizados oficiais da Câmara e páginas INSS/eSocial foram utilizados como alternativa.','checkedOfficialSources':['https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.pdf','https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.pdf','https://www2.camara.leg.br/legin/fed/lei/2007/lei-11457-16-marco-2007-552186-normaatualizada-pl.html','https://www.gov.br/inss/pt-br/acesso-a-informacao/institucional/institucional','https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/ajustes-para-alcance-do-salario-minimo-emenda-constitucional-no-103-de-2019','https://www.gov.br/esocial/pt-br/noticias/mudanca-na-data-de-vencimento-do-dae','https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/manual-do-esocial-empregador-domestico-versao-09-01-2026.pdf'],'limitations':['Valores anuais de teto e faixas não foram fixados como regra permanente. Exemplos numéricos de teto são explicitamente hipotéticos.','Alguns pontos tributários e institucionais exigem conferir fonte vigente para uso profissional; o acervo é material educacional.','Fonte indicada não significa licença de reprodução de prova; nenhum item oficial foi reproduzido.']}}
 qs=[q for l in lessons for q in l['questions']]
 assert len(qs)==716
 assert len({q['id'] for q in qs})==716
 normalized=[re.sub(r'\W+',' ',q['text']).casefold().strip() for q in qs]
 assert len(set(normalized))==716,[x for x,n in collections.Counter(normalized).items() if n>1]
 assert all(type(q['answer']) is bool for q in qs)
 assert all(q['sourceRef']['url'] and q['sourceRef']['locator'] for q in qs)
 assert all(all(len(str(l[k]))>10 for k in ['core','rule','example','contrast','limit']) for l in lessons)
 path=ROOT/'data/prev-base.json';path.parent.mkdir(exist_ok=True);path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'path':str(path),'lessons':len(lessons),'questions':len(qs),'true':sum(q['answer'] for q in qs),'false':sum(not q['answer'] for q in qs),'quotas':'50/50 exatas','duplicates':0,'validation':'OK'},ensure_ascii=False))

if __name__=='__main__':build()
