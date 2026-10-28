"""Assets autorais por microassunto. Cada linha contém uma regra e um caso de erro.
Não altera o runtime. Python monta e verifica quotas sem inventar gabaritos.
"""
import json, collections, re, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PLAN=ROOT/'data/curriculum-plan.json'
SOURCES={
'cf':('Constituição Federal — Câmara dos Deputados','https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html'),
's':('Lei 8.112/1990','https://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm'),
'a':('Lei 9.784/1999 — texto atualizado Câmara','https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html'),
'im':('Lei 8.429/1992 atualizada — Câmara','https://www2.camara.leg.br/legin/fed/lei/1992/lei-8429-2-junho-1992-357452-normaatualizada-pl.html'),
'dl':('Decreto-Lei 200/1967','https://www.planalto.gov.br/ccivil_03/decreto-lei/del0200.htm'),
'serv':('Lei 8.987/1995','https://www.planalto.gov.br/ccivil_03/leis/l8987compilada.htm'),
'stf':('STF — Tema 532','https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=4005451&numeroTema=532'),
'rju':('STF — ADI 2135','https://portal.stf.jus.br/processos/detalhe.asp?incidente=11299'),
'ec138':('Emenda Constitucional 138/2025','https://planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc138.htm')}
DATA={}
def add(pid,src,loc,raw):
 pairs=[tuple(v.strip() for v in line.split('||')) for line in raw.strip().splitlines() if line.strip()]
 assert all(len(p)==2 for p in pairs),pid
 DATA[pid]=(src,loc,pairs)

add('CONST-B01-S01','cf','art. 5º, caput, III, XXII a XXV, XLVII e §1º','''
A Constituição protege conjuntamente vida, liberdade, igualdade, segurança e propriedade. || Uma autoridade pode excluir a propriedade da proteção constitucional porque apenas a vida está no caput do art. 5º.
A igualdade jurídica impede diferenciações arbitrárias e admite distinções constitucionalmente justificadas. || Uma política que trate desigualmente situações distintas é inconstitucional apenas por estabelecer qualquer diferenciação.
A função social limita o exercício do direito de propriedade. || O dono de um imóvel pode afastar toda exigência de função social invocando a proteção constitucional da propriedade.
A Constituição proíbe a tortura e o tratamento desumano ou degradante. || Uma pessoa presa perde a proteção contra tratamento degradante devido à gravidade do crime imputado.
A pena de morte é constitucionalmente vedada, ressalvada a hipótese de guerra declarada nos termos constitucionais. || A Constituição autoriza a pena de morte para todo crime hediondo, mesmo em tempo de paz.
O perigo público iminente permite o uso de propriedade particular pela autoridade competente, com indenização ulterior se houver dano. || Ao requisitar um imóvel em perigo público iminente, a autoridade deve sempre indenizar previamente, ainda que não ocorra dano.
As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata. || O estudante pode concluir que nenhum direito fundamental produz efeitos enquanto não for criada uma lei específica para cada inciso.
A proteção da liberdade convive com restrições que tenham fundamento constitucional e observem as garantias aplicáveis. || O fato de a liberdade constar do caput impede qualquer prisão, inclusive a prisão em flagrante admitida na própria Constituição.
''')
add('CONST-B01-S02','cf','art. 5º, I, II, XXXIV, XXXVI, XLV, LIV, LXXVII e §2º','''
Homens e mulheres são iguais em direitos e obrigações nos termos constitucionais. || Um edital pode excluir todas as mulheres de cargo público sem fundamento jurídico apenas por preferência administrativa.
O direito de petição aos poderes públicos, em defesa de direitos ou contra ilegalidade ou abuso, independe do pagamento de taxas. || Para receber uma petição contra abuso de poder, o órgão pode exigir taxa como condição constitucional obrigatória.
A obtenção de certidões em repartições públicas para defesa de direitos e esclarecimento de situações de interesse pessoal é gratuita. || A certidão destinada exclusivamente a esclarecer situação pessoal do requerente necessariamente exige taxa, segundo o art. 5º.
A lei não prejudicará o direito adquirido, o ato jurídico perfeito e a coisa julgada. || A edição de lei nova autoriza desconsiderar automaticamente a coisa julgada, ainda que não haja fundamento para sua desconstituição.
Nenhuma pena passará da pessoa do condenado, observados os limites constitucionais para reparação do dano e perdimento de bens. || A morte de um condenado autoriza executar a pena de prisão pessoalmente contra seus filhos.
Ninguém será privado da liberdade ou de seus bens sem o devido processo legal. || Para retirar definitivamente um bem de alguém, o Estado pode ignorar todo procedimento por considerar sua própria decisão suficiente.
O registro civil de nascimento e a certidão de óbito são gratuitos para os reconhecidamente pobres, na forma da lei. || O texto constitucional limita essa gratuidade ao registro de nascimento e exclui expressamente a certidão de óbito dos pobres.
O catálogo do art. 5º não exclui direitos decorrentes do regime, dos princípios constitucionais e dos tratados de que o Brasil seja parte. || Um direito deve ser rejeitado apenas porque não está escrito literalmente em um dos incisos do art. 5º.
''')
add('CONST-B01-S03','cf','art. 5º, II, IV, VI, VIII, IX e XIII','''
Ninguém é obrigado a fazer ou deixar de fazer algo senão em virtude de lei. || Uma autoridade pode criar obrigação para o cidadão com base unicamente em sua preferência pessoal, sem fundamento jurídico.
A manifestação do pensamento é livre, vedado o anonimato. || A liberdade de pensamento constitucional garante o direito irrestrito de publicar acusações anonimamente, sem possibilidade de identificação.
É livre a expressão intelectual, artística, científica e de comunicação, independentemente de censura ou licença. || Uma obra científica depende sempre de licença estatal prévia como requisito imposto pelo art. 5º.
A liberdade de consciência e de crença é protegida, com livre exercício dos cultos religiosos e proteção legal de seus locais e liturgias. || A proteção constitucional da crença permite ao Estado proibir indistintamente todos os cultos minoritários.
A crença não afasta obrigação legal a todos imposta quando a pessoa também se recusa a cumprir prestação alternativa fixada em lei. || Invocar crença religiosa sempre elimina obrigação legal comum, mesmo com recusa da prestação alternativa legal.
O exercício profissional é livre, atendidas as qualificações que a lei estabelecer. || A Constituição impede o legislador de estabelecer qualquer qualificação para profissão regulamentada.
''')
add('CONST-B01-S04','cf','art. 5º, V, X, XII, XXXIII e LXXIX','''
A intimidade e a vida privada são invioláveis, assegurada indenização pelo dano decorrente da violação. || Divulgar indevidamente a intimidade de alguém jamais gera reparação porque o art. 5º protege apenas o patrimônio material.
A honra e a imagem recebem proteção constitucional própria. || Uma pessoa pública perde integralmente os direitos à honra e à imagem ao assumir cargo estatal.
O direito de resposta é proporcional ao agravo e não exclui indenização por dano material, moral ou à imagem. || Depois de concedido direito de resposta, a Constituição proíbe qualquer indenização relacionada à mesma ofensa.
A proteção dos dados pessoais, inclusive nos meios digitais, é direito fundamental expresso. || A proteção constitucional dos dados pessoais se limita aos arquivos em papel e não alcança meios digitais.
O direito à informação convive com ressalvas constitucionais de sigilo, inclusive para a segurança da sociedade e do Estado. || O acesso a informações permite exigir a divulgação irrestrita de qualquer dado sigiloso, sem considerar exceções constitucionais.
A tutela da privacidade não impede responsabilização pelo exercício abusivo de outro direito. || A liberdade de comunicação torna juridicamente indiferente a divulgação ilícita da vida privada de terceiros.
''')
add('CONST-B01-S05','cf','art. 5º, XI e XII','''
A casa é asilo inviolável, ressalvadas as hipóteses constitucionais de ingresso sem consentimento. || O agente pode entrar em residência por simples curiosidade funcional, sem consentimento e sem hipótese constitucional.
Em flagrante delito, a Constituição admite ingresso na casa sem consentimento do morador. || Mesmo diante de flagrante efetivamente caracterizado, o agente precisa sempre aguardar o consentimento do morador.
O socorro e o desastre são exceções constitucionais à inviolabilidade domiciliar. || Um bombeiro deve deixar de prestar socorro urgente em casa fechada até obter mandado judicial diurno.
O ingresso domiciliar por determinação judicial, na regra constitucional, ocorre durante o dia. || Um mandado judicial comum autoriza, por si só, ingresso domiciliar em qualquer horário noturno.
O consentimento válido do morador afasta a vedação constitucional ao ingresso na casa. || A entrada consentida por morador é inconstitucional em qualquer horário, mesmo sem coação.
A interceptação de comunicações telefônicas depende de ordem judicial nas hipóteses e forma legais, para investigação criminal ou instrução processual penal. || Um superior administrativo pode determinar interceptação telefônica para pesquisa de satisfação, dispensando juiz e finalidade penal.
''')
add('CONST-B01-S06','cf','art. 5º, XVI a XXI','''
A reunião pacífica e sem armas em local aberto ao público independe de autorização, com prévio aviso à autoridade competente. || Para realizar reunião pacífica sem armas em praça, os organizadores dependem sempre de autorização discricionária do prefeito.
Uma reunião não pode frustrar outra anteriormente convocada para o mesmo local. || O prévio aviso confere aos organizadores poder de impedir reunião que já havia sido convocada antes para o mesmo local.
A liberdade de associação para fins lícitos é plena, vedada a de caráter paramilitar. || A Constituição protege obrigatoriamente a criação de associação paramilitar por se tratar de exercício associativo.
A criação de associações independe de autorização estatal, vedada interferência estatal em seu funcionamento. || Uma associação lícita só pode nascer depois de receber licença política individual do Executivo.
A dissolução compulsória de associação exige decisão judicial transitada em julgado; a suspensão das atividades exige decisão judicial. || Uma autoridade administrativa pode dissolver definitivamente uma associação por despacho, sem decisão judicial.
Ninguém pode ser compelido a associar-se ou a permanecer associado. || Ao ingressar voluntariamente em associação, a pessoa perde para sempre a possibilidade de dela se desligar.
''')
add('CONST-B01-S07','cf','art. 5º, §§2º a 4º','''
Tratados de direitos humanos aprovados em cada Casa do Congresso, em dois turnos, por três quintos dos votos dos membros equivalem a emendas constitucionais. || Um tratado de direitos humanos aprovado em turno único por maioria simples equivale automaticamente a emenda constitucional.
O quórum qualificado deve ser observado tanto na Câmara quanto no Senado. || A aprovação qualificada apenas pelo Senado já basta para conferir equivalência constitucional, dispensada a Câmara.
O procedimento do §3º exige dois turnos de votação em cada Casa. || Duas votações somadas, uma na Câmara e outra no Senado, satisfazem o número de turnos exigido para cada Casa.
A equivalência prevista no §3º refere-se a tratados e convenções internacionais sobre direitos humanos. || Qualquer tratado comercial aprovado por três quintos passa necessariamente a equivaler a emenda com fundamento no art. 5º, §3º.
O catálogo constitucional de direitos admite proteção proveniente de tratados internacionais de que o Brasil seja parte. || O art. 5º impede que tratados de direitos humanos ampliem a proteção além dos direitos expressamente enumerados.
O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão. || A adesão do Brasil à criação de Tribunal Penal Internacional nunca pode produzir submissão à sua jurisdição por vedação constitucional expressa.
''')
add('CONST-B01-S08','cf','art. 5º, XXXV, LIII a LVI, LX e LXXVIII','''
A lei não excluirá da apreciação do Judiciário lesão ou ameaça a direito. || A tutela judicial só pode ser buscada depois que a lesão estiver consumada, pois ameaças nunca autorizam acesso à justiça.
O contraditório e a ampla defesa são assegurados aos litigantes em processo judicial ou administrativo e aos acusados em geral. || Em processo administrativo sancionador, a defesa é dispensável porque essa garantia existe apenas na ação penal.
O devido processo legal protege tanto a liberdade quanto os bens. || A retirada de propriedade não precisa observar devido processo legal por se tratar de bem e não de liberdade.
O juiz natural exige processamento e julgamento pela autoridade competente. || É constitucional escolher um tribunal de exceção exclusivamente depois de conhecido o acusado.
As provas obtidas por meios ilícitos são inadmissíveis no processo, na regra constitucional. || Toda prova produzida por meio ilícito deve ser admitida somente por ser útil ao acusador.
A razoável duração do processo e os meios que garantam sua celeridade são direitos nos âmbitos judicial e administrativo. || A garantia constitucional de duração razoável se aplica apenas aos tribunais e exclui processos no INSS.
''')
add('CONST-B01-S09','cf','art. 5º, LVII e LXI a LXVI','''
Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória. || O simples recebimento da denúncia equivale constitucionalmente à condenação penal definitiva.
Investigação e acusação não são sinônimos de condenação transitada em julgado. || O registro de investigação policial basta, por si só, para transformar o investigado em culpado definitivo.
A presunção de inocência não elimina a possibilidade de prisão cautelar constitucionalmente fundamentada. || A ausência de condenação definitiva impede absolutamente qualquer prisão em flagrante ou cautelar.
Uma sentença condenatória sujeita a recurso não se confunde conceitualmente com trânsito em julgado. || Havendo recurso cabível e pendente, a condenação já se tornou necessariamente definitiva apenas por ter sido proferida.
A Constituição prevê relaxamento imediato da prisão ilegal pela autoridade judiciária. || O princípio da inocência autoriza manter prisão reconhecidamente ilegal até o final da ação penal.
A liberdade provisória deve ser observada quando admitida em lei, com ou sem fiança. || A autoridade pode manter alguém preso quando a lei admite liberdade provisória, apenas para antecipar punição pela acusação.
''')
add('CONST-B01-S10','cf','art. 5º, LVIII; Lei 12.037/2009, arts. 1º a 3º','''
O civilmente identificado não será submetido a identificação criminal, salvo hipóteses previstas em lei. || Apresentar identificação civil impede identificação criminal em qualquer circunstância, mesmo diante de exceção legal.
A ressalva constitucional depende de lei, não de preferência pessoal do agente. || Um policial pode criar nova hipótese de identificação criminal por costume da unidade, ainda que não exista previsão legal.
Documento civil com indícios de falsificação pode justificar identificação criminal na forma legal. || A apresentação de documento aparentemente falsificado torna obrigatória sua aceitação sem qualquer identificação criminal prevista em lei.
Identificação civil e identificação criminal são institutos distintos. || A coleta de dados para documento civil constitui, em todos os casos, condenação criminal de seu titular.
A identificação criminal não constitui, por si só, prova de culpa definitiva. || O fato de terem sido coletadas impressões digitais em procedimento criminal substitui a sentença condenatória transitada em julgado.
A lei pode admitir identificação criminal quando documentos apresentados sejam insuficientes para identificar cabalmente o indiciado. || Documentação insuficiente impede qualquer providência legal de identificação, porque basta apresentar algum papel para afastar todas as exceções.
''')
add('CONST-B01-S11','cf','art. 5º, LXI a LXVIII','''
A prisão pode decorrer de flagrante delito ou de ordem escrita e fundamentada de autoridade judiciária competente, ressalvadas hipóteses militares constitucionais. || Um servidor administrativo pode prender por ordem verbal imotivada para punir atraso em requerimento, sem flagrante ou hipótese constitucional.
A prisão e o local onde a pessoa se encontre serão comunicados imediatamente ao juiz competente e à família ou pessoa indicada. || A comunicação ao juiz pode ser adiada livremente por semanas para preservar a conveniência da investigação.
O preso tem direito ao silêncio e à assistência da família e de advogado. || O preso é obrigado a confessar e perde o direito à assistência de advogado enquanto permanecer custodiado.
O preso tem direito à identificação dos responsáveis por sua prisão ou interrogatório policial. || Os responsáveis pelo interrogatório podem impedir toda identificação perante o preso, por regra constitucional geral.
A prisão ilegal será imediatamente relaxada pela autoridade judiciária. || Reconhecida judicialmente a ilegalidade, a prisão deve continuar apenas para servir de exemplo social.
O habeas corpus protege contra violência ou coação ilegal ou abusiva à liberdade de locomoção, inclusive ameaça. || O habeas corpus só pode ser usado depois de efetivada prisão, mesmo diante de ameaça concreta ilegal à locomoção.
''')
add('CONST-B01-S12','cf','art. 5º, LXVIII a LXXIII e LXXVII','''
Habeas corpus tutela a liberdade de locomoção contra ilegalidade ou abuso de poder. || Para corrigir exclusivamente dados pessoais em cadastro público, sem risco à locomoção, o instrumento constitucional específico é necessariamente o habeas corpus.
Mandado de segurança protege direito líquido e certo não amparado por habeas corpus ou habeas data, observados seus requisitos. || Qualquer direito, mesmo dependente de extensa produção de prova, é automaticamente líquido e certo para mandado de segurança.
Habeas data permite conhecer informações relativas à pessoa do impetrante em registros públicos ou de caráter público e retificá-las nos termos constitucionais. || Habeas data é instrumento para obter indistintamente todos os dados pessoais de terceiros sem vínculo com o impetrante.
Mandado de injunção é cabível diante de falta de norma regulamentadora que inviabilize direitos, liberdades ou prerrogativas constitucionais indicados no art. 5º. || A inexistência de qualquer ato administrativo conveniente, sem inviabilização de direito constitucional, basta sempre para mandado de injunção.
Qualquer cidadão é parte legítima para ação popular nos termos do art. 5º, LXXIII. || A ação popular é reservada exclusivamente ao Ministério Público e nunca pode ser proposta por cidadão.
As ações de habeas corpus e habeas data são gratuitas. || A Constituição impõe taxa judiciária obrigatória como condição de acesso ao habeas corpus e ao habeas data.
''')
add('CONST-B02-S01','cf','arts. 6º a 11','''
Educação, saúde, alimentação, trabalho e moradia integram o rol de direitos sociais. || A moradia não pode ser classificada como direito social por não estar no art. 6º.
Previdência social e assistência aos desamparados estão entre os direitos sociais constitucionais. || O art. 6º exclui a assistência aos desamparados e contempla apenas proteção de quem contribui.
O lazer e a segurança integram o rol expresso do art. 6º. || O lazer é constitucionalmente irrelevante e não aparece entre direitos sociais.
Os direitos dos trabalhadores incluem redução dos riscos inerentes ao trabalho por normas de saúde, higiene e segurança. || A proteção constitucional do trabalho permite eliminar todas as normas de segurança para reduzir custos do empregador.
A sindicalização é livre, vedadas interferência e intervenção do poder público na organização sindical nos termos constitucionais. || O Estado pode escolher diretamente todos os dirigentes sindicais como consequência necessária da liberdade sindical.
O direito de greve atribui aos trabalhadores decidir sobre a oportunidade de exercê-lo e os interesses a defender, observada a lei. || Qualquer greve autoriza desconsiderar integralmente a disciplina legal de serviços essenciais e o atendimento das necessidades inadiáveis.
''')
add('CONST-B02-S02','cf','art. 12, I a III e §§2º a 5º; EC 131/2023','''
São brasileiros natos os nascidos no Brasil, ainda que de pais estrangeiros, desde que estes não estejam a serviço de seu país. || Todo nascimento em território brasileiro gera nacionalidade nata, inclusive quando ambos os pais estrangeiros estão a serviço de seu país.
O nascimento no exterior de pai brasileiro ou mãe brasileira a serviço do Brasil pode gerar nacionalidade nata. || O filho nascido no exterior de mãe brasileira a serviço do Brasil será necessariamente apenas naturalizado.
A Constituição prevê nacionalidade nata para nascidos no exterior registrados em repartição brasileira competente, nas condições do art. 12. || O registro em repartição brasileira competente só permite naturalização e jamais nacionalidade nata.
A lei não estabelecerá distinção entre brasileiros natos e naturalizados, salvo nos casos previstos na Constituição. || Uma lei ordinária pode criar livremente qualquer privilégio de natos sobre naturalizados, sem base constitucional.
Presidente e Vice-Presidente da República são cargos privativos de brasileiro nato. || Um brasileiro naturalizado pode ocupar a Presidência da República em igualdade com o nato, porque nenhuma exceção constitucional existe.
A aquisição de outra nacionalidade não implica automaticamente perda da nacionalidade brasileira segundo a redação da EC 131/2023. || Um brasileiro que adquira outra nacionalidade perde obrigatoriamente a brasileira pelo simples fato da aquisição, sem considerar a alteração de 2023.
''')
add('CONST-B02-S03','cf','arts. 1º, II, 14, 15 e 16','''
A cidadania é fundamento da República e se relaciona à participação na vida política. || A Constituição trata a cidadania apenas como vantagem remuneratória do servidor, sem relação com participação política.
A soberania popular é exercida pelo sufrágio universal e pelo voto direto e secreto, com valor igual para todos, e nos termos da lei por instrumentos participativos. || A Constituição atribui valor superior ao voto de pessoas com maior renda.
Plebiscito, referendo e iniciativa popular são formas constitucionais de participação. || A participação popular constitucional se esgota na eleição periódica e exclui plebiscito e referendo.
A Constituição distingue direitos políticos positivos e restrições ao seu exercício. || O direito de votar implica automaticamente elegibilidade para qualquer cargo, independentemente de condições constitucionais.
Mudança no processo eleitoral sujeita-se à regra constitucional de anterioridade do art. 16. || Uma lei que altera o processo eleitoral se aplica necessariamente a eleição ocorrida poucos dias depois de sua vigência, ignorando o art. 16.
A perda ou suspensão de direitos políticos só ocorre nas hipóteses constitucionais; sua cassação é vedada. || A autoridade administrativa pode cassar direitos políticos apenas por discordância ideológica com o cidadão.
''')
add('CONST-B02-S04','cf','art. 14, §§1º a 4º','''
Alistamento eleitoral e voto são obrigatórios para os maiores de dezoito anos, ressalvadas as hipóteses constitucionais de facultatividade. || A Constituição determina voto obrigatório para toda pessoa maior de dezoito anos, inclusive analfabetos e maiores de setenta.
Alistamento e voto são facultativos para analfabetos, maiores de setenta e maiores de dezesseis e menores de dezoito anos. || Uma pessoa de dezessete anos está constitucionalmente impedida de alistar-se porque o voto é obrigatório apenas a partir de dezoito.
Estrangeiros e conscritos durante o serviço militar obrigatório não podem alistar-se como eleitores. || Um estrangeiro pode alistar-se automaticamente como eleitor brasileiro apenas por residir no país.
A elegibilidade exige condições como nacionalidade brasileira, pleno exercício dos direitos políticos e alistamento eleitoral. || A pessoa sem pleno exercício dos direitos políticos possui elegibilidade garantida para qualquer cargo apenas por ter idade suficiente.
A idade mínima constitucional varia conforme o cargo eletivo. || A Constituição estabelece a mesma idade mínima para vereador e Presidente da República.
Os analfabetos são inelegíveis, embora possam votar facultativamente. || Como o voto dos analfabetos é facultativo, sua candidatura a qualquer cargo eletivo é constitucionalmente assegurada sem restrição.
''')
add('CONST-B02-S05','cf','art. 15, I a V','''
A cassação de direitos políticos é vedada. || Uma lei pode atribuir ao prefeito poder de cassar direitos políticos dos opositores por conveniência política.
A condenação criminal transitada em julgado suspende direitos políticos enquanto durarem seus efeitos. || Uma condenação criminal ainda recorrível produz, pelo simples fato de existir, a mesma suspensão definitiva prevista para o trânsito em julgado.
O cancelamento da naturalização por sentença transitada em julgado é hipótese constitucional de perda dos direitos políticos. || A naturalização pode ser cancelada para efeitos políticos por simples notícia de jornal, sem sentença definitiva.
A improbidade administrativa pode acarretar suspensão de direitos políticos nos termos do art. 37, §4º. || Toda suspeita de improbidade impõe perda automática de direitos políticos, dispensando o regime jurídico e a decisão aplicáveis.
A recusa de cumprir obrigação a todos imposta e prestação alternativa nos termos constitucionais pode afetar direitos políticos. || A mera crença religiosa, sem recusa de obrigação e de prestação alternativa, autoriza cassação política por discricionariedade administrativa.
As hipóteses do art. 15 não autorizam criação de punição política pessoal sem previsão constitucional. || A falta de pagamento de conta particular permite ao credor suspender direitos políticos do devedor por iniciativa própria.
''')
add('CONST-B02-S06','cf','art. 5º, LXIX a LXXIII; art. 8º, III; art. 14','''
O mandado de segurança coletivo tem legitimados próprios previstos na Constituição. || Qualquer associação recém-criada, independentemente dos requisitos constitucionais, possui sempre legitimidade para mandado de segurança coletivo.
Partido político com representação no Congresso Nacional pode impetrar mandado de segurança coletivo. || A Constituição exige representação do partido em todas as assembleias estaduais, em vez de representação no Congresso, para essa legitimidade.
O sindicato tem legitimidade constitucional para defender direitos e interesses coletivos ou individuais da categoria, inclusive em questões judiciais e administrativas. || A representação sindical se limita a interesses econômicos coletivos e exclui qualquer questão administrativa da categoria.
O habeas data é uma garantia de acesso ou retificação de informações pessoais nas condições constitucionais. || Habeas data é substituto universal de ação popular para proteger patrimônio histórico sem relação com informações do impetrante.
A ação popular pode visar anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural. || A ação popular só protege dinheiro público e jamais pode tutelar meio ambiente.
Os instrumentos de democracia direta coexistem com a representação política. || A existência de representantes eleitos proíbe o uso de plebiscito e referendo no sistema constitucional brasileiro.
''')
add('CONST-B03-S01','cf','art. 37, caput e §1º','''
Legalidade, impessoalidade, moralidade, publicidade e eficiência são princípios expressos do art. 37. || O princípio da eficiência permite que a Administração desobedeça a lei sempre que pretenda agir rapidamente.
A legalidade administrativa exige atuação conforme o ordenamento jurídico. || O gestor pode criar qualquer obrigação particular sem autorização jurídica porque o particular também tem liberdade de agir.
A impessoalidade impede favorecimento pessoal incompatível com a finalidade pública. || O atendimento em órgão público pode priorizar amigos do servidor sem critério legal por ser escolha de relacionamento pessoal.
A moralidade administrativa integra o controle da atuação pública. || Um ato formalmente permitido fica imune a exame de moralidade administrativa em qualquer circunstância.
A publicidade não elimina hipóteses juridicamente protegidas de sigilo. || O princípio da publicidade obriga divulgar irrestritamente prontuários e dados pessoais protegidos, sem exame de sigilo.
A publicidade institucional deve ter caráter educativo, informativo ou de orientação social, sem promoção pessoal de autoridades ou servidores. || A campanha oficial pode usar dinheiro público prioritariamente para exaltar o nome e a imagem pessoal do gestor.
''')
add('CONST-B03-S02','cf','art. 37, I a V e IX','''
A investidura em cargo ou emprego público depende, em regra, de aprovação prévia em concurso. || A contratação para emprego público permanente dispensa concurso apenas porque o vínculo é regido pela CLT.
O concurso pode ser de provas ou de provas e títulos, conforme natureza e complexidade do cargo ou emprego, na forma da lei. || A Constituição exige concurso exclusivamente de títulos para todos os cargos públicos.
O prazo de validade do concurso é de até dois anos, prorrogável uma vez por igual período. || Um concurso válido por um ano pode ser prorrogado sucessivamente todos os anos, sem limite de renovações.
Cargos em comissão declarados em lei de livre nomeação e exoneração constituem ressalva à exigência de concurso. || Um cargo efetivo se torna dispensado de concurso apenas porque a autoridade decidiu chamá-lo informalmente de cargo de confiança.
Funções de confiança são exercidas exclusivamente por servidores ocupantes de cargo efetivo. || Uma pessoa sem cargo efetivo pode ocupar qualquer função de confiança por livre escolha, nos mesmos termos de um cargo em comissão.
A lei estabelecerá casos de contratação por tempo determinado para atender necessidade temporária de excepcional interesse público. || A necessidade permanente ordinária autoriza contratação temporária ilimitada sem requisitos legais, apenas para evitar concurso.
''')
add('CONST-B03-S03','cf','art. 37, XIX e XX','''
Autarquia é criada por lei específica. || Um decreto autônomo pode criar autarquia federal sem lei específica.
A instituição de empresa pública depende de autorização por lei específica. || A aprovação administrativa do plano de negócios, sem autorização legal específica, basta para instituir empresa pública.
A instituição de sociedade de economia mista depende de autorização por lei específica. || A Constituição determina que sociedade de economia mista nasça diretamente como pessoa jurídica pela mera publicação de qualquer decreto.
A lei complementar define as áreas de atuação das fundações a que se refere o art. 37, XIX. || A Constituição atribui a definição dessas áreas exclusivamente a regulamento interno de cada fundação, sem lei complementar.
A criação de subsidiárias das entidades mencionadas no art. 37, XX, depende de autorização legislativa nos termos constitucionais. || A criação de subsidiária está sempre livre de qualquer autorização legislativa por decisão exclusiva de sua diretoria.
A Administração direta e a indireta submetem-se aos princípios do art. 37. || Empresas estatais deixam de observar impessoalidade e moralidade apenas por terem personalidade de direito privado.
''')
add('CONST-B03-S04','ec138','CF, art. 37, XVI e XVII; EC 138/2025','''
A acumulação remunerada de cargos públicos é vedada como regra, com exceções constitucionais e compatibilidade de horários. || Dois cargos que não se enquadrem em exceção podem ser acumulados só porque os horários são diferentes.
A Constituição admite acumulação de dois cargos de professor quando houver compatibilidade de horários. || Dois cargos de professor jamais podem ser acumulados porque a proibição constitucional não possui exceções.
Desde a EC 138/2025, a alínea b admite um cargo de professor com outro de qualquer natureza, observadas as condições constitucionais. || Em questão sobre a redação atual, um professor só pode acumular cargo técnico ou científico, pois a EC 138/2025 manteve essa restrição.
A Constituição admite dois cargos ou empregos privativos de profissionais de saúde com profissões regulamentadas, observadas suas condições. || Qualquer par de empregos públicos pode usar a exceção da saúde, ainda que nenhum seja privativo de profissional regulamentado.
A vedação de acumular estende-se a empregos e funções e alcança entidades da Administração indireta nos termos do inciso XVII. || O vínculo com empresa pública nunca conta para a vedação de acumulação porque a entidade tem personalidade privada.
As exceções de acumulação não autorizam ignorar a compatibilidade de horários. || Um professor pode exercer simultaneamente dois cargos com jornadas coincidentes apenas porque a natureza dos cargos é constitucionalmente acumulável.
''')
add('CONST-B03-S05','cf','art. 37, X a XV; art. 39, §4º','''
A remuneração dos servidores e o subsídio somente podem ser fixados ou alterados por lei específica, observadas as iniciativas próprias. || Uma chefia pode aumentar vencimentos de sua equipe por mensagem eletrônica, sem lei específica.
A revisão geral anual observará a mesma data e não poderá distinguir índices nos termos constitucionais. || A Constituição transforma revisão geral anual em autorização irrestrita para cada chefe fixar índice próprio por portaria.
O art. 37 prevê teto remuneratório e subtetos conforme os âmbitos constitucionais. || A invocação de autonomia administrativa permite ao órgão afastar todos os limites constitucionais de remuneração.
É vedada vinculação ou equiparação de espécies remuneratórias para efeito de remuneração de pessoal do serviço público. || Uma carreira pode obter aumento automático vinculado a outra por simples ato administrativo sem considerar a vedação constitucional.
Os acréscimos pecuniários não serão computados nem acumulados para concessão de acréscimos ulteriores, na regra do art. 37, XIV. || Toda vantagem deve servir obrigatoriamente de base para novas vantagens em efeito cascata ilimitado.
Subsídio em parcela única sujeita-se às ressalvas e ao regime constitucional; não é sinônimo de vencimento básico acrescido de toda vantagem possível. || Classificar pagamento como subsídio libera automaticamente gratificações ilimitadas e afasta o art. 39, §4º.
''')
add('CONST-B03-S06','cf','art. 38, I a V','''
Servidor investido em mandato federal, estadual ou distrital ficará afastado de cargo, emprego ou função. || Um servidor pode conservar exercício regular do cargo durante mandato de deputado estadual apenas por haver compatibilidade de horários.
O servidor investido no mandato de prefeito será afastado, facultada a opção pela remuneração. || Ao assumir como prefeito, o servidor deve obrigatoriamente perder toda possibilidade de opção remuneratória prevista no art. 38.
Havendo compatibilidade de horários, o vereador pode perceber as vantagens do cargo, emprego ou função sem prejuízo da remuneração eletiva. || O vereador com horários compatíveis é constitucionalmente obrigado a abandonar o exercício do cargo público em qualquer situação.
Sem compatibilidade de horários, aplica-se ao vereador a norma de afastamento e opção remuneratória do prefeito. || Um vereador com jornadas incompatíveis pode manter ambos os exercícios sem afastamento porque a acumulação é sempre livre.
Nos afastamentos para mandato eletivo, o tempo de serviço será contado para todos os efeitos legais, exceto promoção por merecimento. || O período de afastamento para mandato eletivo obrigatoriamente gera promoção por merecimento em todas as carreiras.
O servidor segurado de regime próprio permanecerá filiado a esse regime no caso de afastamento para mandato eletivo. || O exercício de mandato eletivo impõe automaticamente desligamento do regime próprio do servidor, segundo o art. 38, V.
''')
add('CONST-B03-S07','rju','CF, arts. 39 e 40; STF, ADI 2135, decisão com efeitos ex nunc','''
Na ADI 2135, o STF validou a alteração da EC 19/1998 que retirou a obrigatoriedade constitucional de regime jurídico único. || A decisão da ADI 2135 determina obrigatoriamente o mesmo regime estatutário único para todas as contratações futuras em qualquer ente.
A decisão da ADI 2135 vedou a transmudação do regime dos servidores atuais, conforme a modulação estabelecida. || O julgamento permite converter automaticamente todos os servidores estatutários atuais em celetistas, independentemente de suas condições.
A possibilidade de regimes distintos não afasta a necessidade constitucional de concurso para vínculos permanentes sujeitos à regra. || A flexibilização de regime validada pelo STF autoriza contratar permanentemente qualquer pessoa sem concurso.
A Lei 8.112 continua sendo referência do regime estatutário federal para os vínculos por ela regidos. || O julgamento da ADI 2135 revogou integralmente a Lei 8.112 por si só, sem necessidade de qualquer alteração normativa.
O art. 40 disciplina o regime próprio dos titulares de cargos efetivos nos termos constitucionais. || A ocupação exclusivamente de cargo em comissão torna a pessoa automaticamente titular de cargo efetivo para o art. 40.
Regime de vínculo funcional e regime de previdência são classificações relacionadas, mas distintas. || Dizer que alguém possui vínculo trabalhista resolve automaticamente toda análise previdenciária sem considerar o art. 40 e as demais regras aplicáveis.
''')
add('CONST-B03-S08','cf','art. 41, caput e §§1º a 4º; art. 169, §4º','''
São estáveis após três anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo em virtude de concurso público. || A simples aprovação em concurso, antes da nomeação e do exercício, já confere estabilidade constitucional.
A avaliação especial de desempenho por comissão instituída para essa finalidade é condição para aquisição da estabilidade. || O transcurso de três anos dispensa, em qualquer hipótese, a avaliação especial exigida no art. 41, §4º.
O servidor estável pode perder o cargo por sentença judicial transitada em julgado. || Estabilidade é garantia absoluta de permanência mesmo após sentença judicial definitiva que imponha perda do cargo.
A perda do cargo por processo administrativo exige ampla defesa. || A estabilidade permite demissão administrativa sem procedimento e sem defesa quando a chefia alegar urgência.
A avaliação periódica de desempenho pode fundamentar perda do cargo na forma de lei complementar e assegurada ampla defesa. || Qualquer comentário informal de desempenho substitui a lei complementar e a defesa exigidas para perda do cargo por avaliação periódica.
Extinto o cargo ou declarada sua desnecessidade, o servidor estável ficará em disponibilidade com remuneração proporcional até adequado aproveitamento. || A extinção do cargo de servidor estável determina automaticamente sua exoneração sem considerar a disponibilidade constitucional.
''')
add('ADM-B01-S01','cf','arts. 1º, 2º, 18 e 37; noções de organização estatal','''
O Estado possui organização política e jurídica que não se confunde com o governo temporariamente em exercício. || A troca do chefe do Executivo extingue a pessoa jurídica estatal e cria necessariamente um novo Estado.
O governo exerce direção política, enquanto a Administração desempenha atividades de execução administrativa nos limites jurídicos. || A execução rotineira de protocolo por uma repartição equivale necessariamente à formulação da direção política do Estado.
Povo, território e poder soberano são elementos tradicionalmente estudados na caracterização do Estado. || Uma secretaria municipal isolada reúne soberania própria e por isso constitui um Estado independente.
A separação dos Poderes admite funções típicas e atípicas nos termos constitucionais. || O Judiciário nunca exerce atividade administrativa, nem ao organizar seus próprios serviços de pessoal.
''')
add('ADM-B01-S02','dl','arts. 4º a 6º; Administração em sentido subjetivo e objetivo','''
Em sentido subjetivo, Administração designa órgãos, entidades e agentes incumbidos da função administrativa. || Ao listar ministérios e autarquias, um texto está descrevendo exclusivamente o sentido objetivo da Administração, sem referência a sujeitos.
Em sentido objetivo ou material, Administração refere-se à atividade administrativa desempenhada. || Descrever a prestação de um serviço público é identificar uma pessoa jurídica determinada, e não uma atividade.
As funções administrativas podem ser exercidas por órgãos dos diferentes Poderes. || Um tribunal, ao gerir contratos de manutenção de sua sede, atua necessariamente apenas em função jurisdicional.
O critério orgânico e o critério material respondem a perguntas distintas: quem exerce e qual atividade é exercida. || Saber que um ato foi praticado pelo Legislativo elimina a necessidade de examinar se sua atividade concreta era administrativa.
''')
add('ADM-B01-S03','a','art. 2º, caput e parágrafo único','''
A atuação administrativa deve atender fins de interesse geral, vedada promoção pessoal de agentes ou autoridades. || Conceder um benefício administrativo para recompensar amizade pessoal atende à finalidade pública apenas porque a autoridade é competente.
Razoabilidade e proporcionalidade orientam a adequação entre meios e fins administrativos. || Para infração leve, a autoridade pode escolher medida manifestamente excessiva sem examinar proporcionalidade.
A Administração deve observar padrões éticos de probidade, decoro e boa-fé. || A ausência de proibição literal específica torna irrelevante a boa-fé na condução de processo administrativo.
As competências administrativas são instrumentos para cumprir finalidades públicas, não privilégios pessoais. || O titular de uma competência pode comercializar seu exercício porque o poder lhe pertence como patrimônio particular.
''')
add('ADM-B01-S04','a','arts. 1º e 2º; fontes e princípios do Direito Administrativo','''
O Direito Administrativo disciplina a função administrativa e suas relações jurídicas, sob bases constitucionais e legais. || A função administrativa não sofre influência da Constituição porque pertence exclusivamente ao regulamento interno de cada órgão.
A lei é fonte central da atuação administrativa, ao lado de outras fontes reconhecidas pelo ordenamento. || Um costume administrativo pode afastar norma legal válida apenas por ser praticado há muitos anos.
A jurisprudência auxilia a interpretação e pode produzir efeitos vinculantes nas hipóteses previstas pelo ordenamento. || Toda opinião individual publicada por qualquer pessoa equivale a precedente judicial vinculante para a Administração.
Princípios jurídicos integram o controle de validade administrativa, inclusive quando não resumidos a uma regra operacional. || Um ato administrativo não pode ser questionado por violação a princípios, ainda que afronta finalidade ou moralidade.
''')
add('ADM-B01-S05','dl','art. 4º; CF, art. 37, XIX','''
A Administração direta corresponde à atuação dos entes políticos por seus órgãos. || Uma autarquia federal é simples órgão sem personalidade da Administração direta porque recebe supervisão ministerial.
Entidades da Administração indireta possuem personalidade jurídica própria. || A personalidade da empresa pública e a da União são sempre a mesma pessoa jurídica, sem distinção patrimonial ou organizacional.
''')
add('ADM-B01-S06','a','art. 1º, §2º, I a III','''
Órgão é unidade de atuação integrante da estrutura da Administração direta ou indireta; entidade possui personalidade jurídica. || Um departamento interno de autarquia adquire personalidade jurídica autônoma apenas por receber denominação própria.
Autoridade é servidor ou agente público dotado de poder de decisão na definição da Lei 9.784. || Qualquer sala de repartição constitui autoridade administrativa, independentemente da existência de agente e poder decisório.
''')
add('ADM-B01-S07','dl','art. 5º; CF, art. 37, XIX; Lei 13.303/2016, arts. 3º e 4º','''
Autarquias possuem personalidade jurídica de direito público e exercem atividade administrativa descentralizada. || A autarquia necessita constituir-se como sociedade anônima privada para integrar a Administração indireta.
Empresas públicas e sociedades de economia mista possuem personalidade de direito privado, mas permanecem sujeitas a regras públicas aplicáveis. || A personalidade privada de uma estatal permite ignorar integralmente concurso, impessoalidade e controle público.
''')
add('ADM-B01-S08','dl','arts. 4º e 10; distinções de organização administrativa','''
Desconcentração distribui competências dentro da mesma pessoa jurídica, sem criar nova entidade. || A criação de departamentos internos de um ministério constitui necessariamente descentralização por criação de nova pessoa jurídica.
A descentralização pode transferir execução administrativa a outra pessoa jurídica; a centralização mantém execução no próprio ente. || Transferir serviço à autarquia significa apenas dividir tarefas internamente entre órgãos da União, sem outra pessoa jurídica.
''')
add('ADM-B02-S01','s','arts. 1º a 4º; CF, art. 37','''
Na Lei 8.112, servidor é a pessoa legalmente investida em cargo público. || Qualquer fornecedor contratado para entregar material torna-se automaticamente servidor estatutário da Lei 8.112.
Agente público é expressão mais ampla que servidor estatutário. || Empregado público celetista nunca pode ser considerado agente público, apenas por não ocupar cargo estatutário.
Agentes políticos desempenham funções de direção política previstas na estrutura constitucional. || O simples exercício de atividade administrativa rotineira transforma todo servidor em agente político eleito.
O vínculo funcional deve ser identificado antes de aplicar regras específicas de direitos e deveres. || A existência de remuneração paga pelo Estado torna aplicável a Lei 8.112 a qualquer pessoa, sem considerar seu vínculo jurídico.
''')
add('ADM-B02-S02','s','arts. 116 a 126','''
O servidor deve exercer com zelo e dedicação as atribuições do cargo. || O ocupante de cargo pode recusar todo dever de diligência porque a remuneração não depende da satisfação pessoal do usuário.
O servidor deve cumprir ordens superiores, exceto quando manifestamente ilegais. || A subordinação obriga executar ordem manifestamente ilegal e impede o servidor de questioná-la.
O dever de guardar sigilo abrange assunto da repartição quando juridicamente protegido. || O dever de publicidade permite ao servidor divulgar livremente qualquer dado sigiloso conhecido no trabalho.
O servidor deve tratar as pessoas com urbanidade e representar contra ilegalidade, omissão ou abuso de poder. || A urbanidade vale apenas no relacionamento com a chefia e dispensa respeito aos usuários do serviço público.
''')
add('ADM-B02-S03','s','arts. 2º, 3º e 9º; CF, art. 37, II e V','''
Cargo público reúne atribuições e responsabilidades previstas na estrutura organizacional e é criado por lei. || A chefia pode criar cargo efetivo com vencimento público por acordo verbal com a pessoa escolhida.
Emprego público se distingue do cargo estatutário pelo vínculo trabalhista a que se submete. || O uso da palavra emprego torna desnecessária qualquer observância das regras constitucionais de ingresso no serviço público.
Funções de confiança são exclusivas de servidores ocupantes de cargo efetivo. || A designação para função de confiança equivale a ingresso livre de pessoa sem cargo efetivo em qualquer atividade permanente.
Cargos em comissão destinam-se apenas a atribuições de direção, chefia e assessoramento nos termos constitucionais. || É constitucional criar todos os cargos operacionais permanentes como comissionados somente para dispensar concurso.
''')
add('ADM-B02-S04','s','arts. 7º a 10 e 24 a 29','''
A investidura em cargo público ocorre com a posse. || A inscrição em concurso já constitui investidura no cargo, mesmo sem aprovação, nomeação ou posse.
A nomeação é forma de provimento originário; a Lei 8.112 também prevê formas derivadas. || A promoção cria sempre um vínculo originário com pessoa totalmente estranha à carreira, dispensando seus requisitos.
Readaptação considera limitação da capacidade física ou mental verificada em inspeção médica e as atribuições compatíveis. || A readaptação é punição disciplinar imposta a servidor saudável por atraso ao serviço.
Reintegração é retorno do servidor estável quando invalidada sua demissão, conforme o regime legal. || O retorno depois de demissão invalidada denomina-se obrigatoriamente remoção, pois reintegração é sinônimo de mudança de sede.
''')
add('ADM-B02-S05','s','art. 33','''
Exoneração e demissão são hipóteses distintas de vacância. || Toda exoneração possui necessariamente natureza de penalidade disciplinar, exatamente como a demissão.
A aposentadoria é hipótese legal de vacância do cargo. || A aposentadoria mantém obrigatoriamente o cargo ocupado pelo aposentado e nunca provoca vacância.
Falecimento e posse em outro cargo inacumulável são hipóteses de vacância previstas na Lei 8.112. || A posse em outro cargo inacumulável não afeta o cargo anterior porque a lei só prevê vacância por morte.
Promoção e readaptação figuram no rol legal de vacância e também podem relacionar-se ao provimento. || Um instituto nunca pode aparecer nos estudos de provimento e de vacância, pois essas listas são necessariamente incomunicáveis.
''')
add('ADM-B02-S06','s','arts. 36 e 37','''
Remoção é deslocamento do servidor no âmbito do mesmo quadro, com ou sem mudança de sede. || A movimentação de servidor dentro do mesmo quadro é sempre redistribuição de cargo, ainda que nenhum cargo seja deslocado.
Redistribuição é deslocamento de cargo de provimento efetivo ocupado ou vago nos termos do art. 37. || Só existe redistribuição quando o próprio servidor requer deslocamento pessoal para dentro do mesmo quadro.
A remoção pode ocorrer de ofício, no interesse da Administração, ou a pedido nas modalidades legais. || Toda remoção depende obrigatoriamente de pedido do servidor, sem hipótese de atuação de ofício.
Há hipóteses de remoção a pedido independentemente do interesse da Administração, desde que preenchidos os requisitos legais. || A menção a remoção por motivo de saúde permite dispensar todos os requisitos e a comprovação legal exigida.
''')
add('ADM-B02-S07','s','arts. 38 e 39','''
Os servidores investidos em cargo ou função de direção ou chefia e ocupantes de cargo de natureza especial terão substitutos indicados no regimento ou previamente designados. || Toda substituição depende de nomeação para novo cargo efetivo e de novo concurso específico.
O substituto assume automaticamente e cumulativamente o exercício nos afastamentos e impedimentos legais ou regulamentares do titular e na vacância, na forma legal. || A ausência do titular elimina a competência do substituto previamente designado para atuar nos casos previstos em lei.
A substituição não se confunde com provimento definitivo do cargo efetivo do titular. || Depois de substituir a chefia por alguns dias, o servidor adquire titularidade definitiva e dispensa o retorno do titular.
As consequências remuneratórias da substituição seguem as hipóteses e condições do art. 38. || A substituição permite receber livremente todas as remunerações integrais, sem observar opção ou condições previstas na Lei 8.112.
''')
add('ADM-B02-S08','s','arts. 40 a 49 e 58 a 61','''
Vencimento é a retribuição pecuniária pelo exercício de cargo público com valor fixado em lei. || Uma verba eventual de ressarcimento de viagem constitui necessariamente vencimento básico permanente do cargo.
Remuneração compreende vencimento do cargo efetivo acrescido das vantagens pecuniárias permanentes estabelecidas em lei. || Todo recebimento eventual ou indenizatório se incorpora automaticamente e para sempre à remuneração do cargo.
Indenizações não se incorporam ao vencimento ou provento para qualquer efeito. || Diárias pagas para compensar gastos de viagem devem necessariamente integrar o vencimento básico após a primeira viagem.
As vantagens previstas na lei incluem indenizações, gratificações e adicionais, com regimes próprios. || A Administração pode tratar toda vantagem como indenização apenas para afastar os requisitos legais de gratificação e adicional.
''')
add('ADM-B02-S09','s','arts. 81 e 91 a 96-A','''
A Lei 8.112 prevê diversas licenças com requisitos e efeitos próprios, inclusive quanto à remuneração e contagem de tempo. || Toda licença estatutária possui obrigatoriamente a mesma duração, remuneração e efeito funcional, sem distinção de fundamento.
Licença para tratar de interesses particulares é concedida a critério da Administração ao servidor ocupante de cargo efetivo que não esteja em estágio probatório, nas condições legais. || Todo recém-empossado em estágio probatório tem direito automático e irrestrito à licença para interesses particulares remunerada.
''')
add('ADM-B02-S10','s','arts. 116 e 117','''
O servidor deve levar irregularidades de que tenha ciência em razão do cargo à autoridade superior ou a outra competente nos casos legais. || Descobrir irregularidade no trabalho autoriza ocultá-la definitivamente para preservar amizade com o responsável.
É proibido retirar documento ou objeto da repartição sem prévia anuência da autoridade competente. || A condição de servidor autoriza levar documentos públicos para casa para uso particular sem autorização.
''')
add('ADM-B02-S11','s','arts. 121 a 126-A','''
O servidor pode responder civil, penal e administrativamente pelo exercício irregular de suas atribuições, nas condições legais. || Uma mesma conduta nunca pode ser examinada em mais de uma esfera de responsabilidade.
A absolvição criminal que negue a existência do fato ou sua autoria afasta a responsabilidade administrativa correspondente. || Toda absolvição penal, inclusive por falta de provas, afasta obrigatoriamente qualquer responsabilidade administrativa, sem examinar seu fundamento.
''')
add('ADM-B02-S12','s','arts. 127, 128, 143 e 148','''
Na aplicação de penalidades serão consideradas natureza e gravidade da infração, danos, circunstâncias e antecedentes funcionais nos termos legais. || A autoridade deve aplicar a mesma sanção a qualquer falta, sem considerar gravidade ou circunstâncias previstas na lei.
A autoridade que souber de irregularidade no serviço público deve promover apuração imediata mediante sindicância ou processo disciplinar, assegurada ampla defesa. || A mera notícia de irregularidade autoriza demissão imediata sem apuração e sem defesa.
''')
add('ADM-B03-S01','a','arts. 11 a 15; organização e poder hierárquico','''
O poder hierárquico permite organização, coordenação e controle interno de atividades no âmbito das relações hierárquicas. || A supervisão ministerial torna um ministério superior hierárquico de qualquer pessoa jurídica distinta em todos os seus atos.
Delegar competência não exige necessariamente relação hierárquica na Lei 9.784. || A delegação é inválida pelo simples fato de o delegado não ser subordinado hierárquico, mesmo presentes todos os requisitos legais.
Avocação temporária pressupõe órgão hierarquicamente inferior e motivos relevantes devidamente justificados. || A autoridade pode avocar permanentemente atribuição de órgão sem vínculo hierárquico apenas por preferência de gestão.
O poder hierárquico não autoriza descumprir competência exclusiva nem ordem jurídica. || O superior pode assumir qualquer competência legalmente exclusiva de outra autoridade com base apenas na hierarquia.
''')
add('ADM-B03-S02','s','arts. 116, 127, 128 e 143','''
O poder disciplinar permite apurar infrações e aplicar sanções a sujeitos vinculados por relação jurídica específica, observadas as garantias legais. || A chefia pode punir servidor sem identificar infração ou fundamento apenas para demonstrar autoridade.
Poder disciplinar e poder de polícia têm âmbitos de incidência distintos. || Punir servidor por falta funcional é necessariamente exercício de polícia administrativa sobre toda a coletividade.
A atividade disciplinar deve respeitar contraditório e ampla defesa. || Chamar a punição de ato interno torna desnecessária qualquer oportunidade de defesa ao acusado.
A sanção deve ser aplicada pela autoridade competente e em conformidade com o regime legal. || Qualquer colega de setor pode impor demissão porque também integra a Administração.
''')
add('ADM-B03-S03','cf','art. 84, IV e VI','''
O decreto regulamentar destina-se à fiel execução da lei e não pode contrariá-la. || Ao regulamentar uma lei, o Executivo pode revogá-la por discordar de sua orientação.
O poder regulamentar não autoriza criar obrigações primárias sem fundamento jurídico adequado. || Um regulamento pode inventar livremente tributo sem qualquer suporte legal apenas por ser ato do chefe do Executivo.
A Constituição prevê decretos autônomos nas hipóteses delimitadas do art. 84, VI. || A existência de decreto autônomo permite ao Presidente legislar por decreto sobre qualquer assunto de competência do Congresso.
A extinção de cargos ou funções vagos pode ocorrer por decreto nos termos constitucionais. || O art. 84, VI, autoriza extinguir por decreto qualquer cargo ocupado, sem considerar a ressalva constitucional.
''')
add('ADM-B03-S04','stf','STF, Tema 532; CTN, art. 78; CF, art. 5º, II e LIV','''
Polícia administrativa limita ou condiciona direitos e atividades para proteção de interesses públicos, dentro da ordem jurídica. || Fiscalizar atividade econômica autoriza ignorar a lei porque o interesse público elimina qualquer limite ao poder de polícia.
Coercibilidade não torna toda medida de polícia automaticamente autoexecutória. || A possibilidade de impor obrigações permite sempre executar qualquer cobrança ou sanção materialmente sem base legal ou controle.
Medidas de polícia devem observar competência, proporcionalidade e devido processo quando exigível. || A Administração pode usar medida manifestamente desproporcional apenas porque o particular está sujeito à fiscalização.
O poder de polícia administrativa não se confunde com a investigação penal exercida pela polícia judiciária. || Todo ato de licença ou fiscalização sanitária constitui necessariamente investigação de crime pelo mesmo regime da polícia judiciária.
''')
add('ADM-B03-S05','stf','Tema 532, tese de repercussão geral','''
O STF admite delegação por lei a pessoa jurídica privada da Administração indireta que preencha os requisitos da tese 532. || A tese 532 autoriza delegar por simples contrato, sem lei, a qualquer empresa privada atuante no mercado.
Capital majoritariamente público, serviço público exclusivo de atuação própria do Estado e regime não concorrencial integram as condições da tese. || Basta haver uma pequena participação estatal no capital para dispensar todos os demais requisitos do Tema 532.
''')
add('ADM-B03-S06','stf','Tema 532; DL 200/1967, art. 4º','''
A presença de entidade na Administração indireta é requisito da hipótese de pessoa jurídica privada admitida no Tema 532. || Uma empresa particular sem integrar a Administração indireta está abrangida pela tese apenas por manter contrato com o município.
Órgãos da Administração direta e entidades da indireta não são categorias idênticas de organização. || Uma secretaria e uma sociedade de economia mista são ambas órgãos sem personalidade própria e, por isso, intercambiáveis na análise da delegação.
''')
add('ADM-B03-S07','stf','Tema 532; Informativo STF 996','''
O Tema 532 afasta a afirmação de que toda personalidade privada impede, em qualquer hipótese, delegação de poder de polícia. || Para rejeitar delegação que cumpre a tese do STF, basta afirmar que a entidade possui personalidade de direito privado.
Nem toda entidade da Administração indireta satisfaz automaticamente as condições específicas do Tema 532. || Integrar a indireta dispensa examinar composição do capital, exclusividade do serviço e regime de concorrência.
''')
add('ADM-B03-S08','stf','Tema 532, limites subjetivos da tese','''
A tese 532 não concede autorização genérica a particulares estranhos à Administração indireta. || Uma empresa privada comum pode aplicar sanção estatal por mera contratação de serviço de apoio, com fundamento automático no Tema 532.
A contratação de apoio material não se confunde, por si só, com transferência de competência decisória sancionadora. || Quem instala equipamento de fiscalização recebe necessariamente poder para decidir e aplicar qualquer sanção administrativa.
''')
add('ADM-B03-S09','stf','Tema 532; Informativo STF 996, ordem, consentimento, fiscalização e sanção','''
A análise do ciclo de polícia distingue ordem, consentimento, fiscalização e sanção, observados os limites jurídicos. || A prestação de atividade material de fiscalização autoriza o contratado a criar, por conta própria, novas infrações gerais.
O julgamento do Tema 532 admitiu atividade de policiamento de trânsito, inclusive multas, nos limites da tese; a ordem legislativa de polícia permanece indelegável. || A decisão do STF transferiu à empresa o poder legislativo de criar livremente infrações de trânsito por ato empresarial.
''')
add('ADM-B03-S10','stf','RE 633.782, Tema 532; Informativo STF 996','''
O precedente deve ser aplicado considerando seus requisitos objetivos, não apenas o nome da entidade julgada. || A tese só pode ser lida como autorização ilimitada a qualquer entidade que use a mesma sigla empresarial da recorrente.
A verificação de eventual alteração jurisprudencial exige consulta ao registro oficial antes de afirmar atualização. || Uma publicação sem identificação do processo basta para substituir silenciosamente a tese oficial e alterar gabaritos históricos.
''')
add('ADM-B03-S11','stf','Tema 532, aplicação cumulativa dos requisitos','''
Sociedade de capital majoritariamente público, integrante da indireta, que atua exclusivamente em serviço próprio do Estado e sem concorrência pode enquadrar-se na hipótese da tese mediante lei. || Sociedade com capital majoritariamente privado se enquadra automaticamente na mesma hipótese apenas porque atua em serviço útil à população.
A análise de caso deve conferir cada condição da tese de modo conjunto. || Verificada atuação em regime concorrencial, o examinador pode ignorar esse dado porque a presença de capital público isoladamente resolve o caso.
''')
add('ADM-B03-S12','a','art. 2º, parágrafo único, II e VI; teoria de abuso de poder','''
Excesso de poder envolve atuação além dos limites de competência; desvio de finalidade envolve uso da competência para finalidade imprópria. || Um ato praticado por autoridade competente com finalidade de perseguição é válido apenas porque não houve excesso de competência.
O interesse público não legitima abuso de poder nem desrespeito a limites legais. || A autoridade pode defender qualquer perseguição pessoal invocando abstratamente o interesse público sem examinar fatos e finalidade.
''')
add('ADM-B04-S01','a','arts. 2º, 11, 22 e 50; elementos do ato administrativo','''
Competência, finalidade, forma, motivo e objeto são elementos tradicionalmente examinados na validade do ato administrativo. || Para avaliar validade, basta conferir a assinatura, pois finalidade e motivo nunca têm relevância jurídica.
A competência deve ser exercida por quem a ordem jurídica atribui a função. || A concordância pessoal de todos os interessados permite dispensar competência legal de quem decide.
O objeto do ato deve ser juridicamente admissível. || Um ato com objeto proibido em lei torna-se válido apenas porque a autoridade está de boa-fé.
A finalidade pública e a finalidade específica prevista na norma devem ser observadas. || A competência para remover servidor pode ser usada validamente com único objetivo de persegui-lo, sem conexão com finalidade legal.
''')
add('ADM-B04-S02','a','arts. 2º, 26 e 53; atributos e efeitos dos atos','''
A presunção de legitimidade do ato administrativo é relativa e admite impugnação. || A assinatura de autoridade torna impossível demonstrar ilegalidade do ato por qualquer meio.
A imperatividade se relaciona à imposição unilateral de obrigações, mas não é atributo de todo ato administrativo. || Um atestado administrativo precisa impor obrigação ao destinatário porque todo ato é imperativo por definição.
A autoexecutoriedade não está presente em todos os atos administrativos. || Qualquer crédito público pode ser cobrado mediante retirada forçada de dinheiro pelo agente, dispensando sempre o procedimento legal.
Validade, existência e eficácia são planos de análise distintos. || Um ato existente no mundo jurídico produz necessariamente todos os efeitos, mesmo quando depende de condição ou publicação exigida.
''')
add('ADM-B04-S03','a','art. 2º; CF, art. 5º, XXXV; vinculação e discricionariedade','''
No ato vinculado, a norma delimita a atuação sem margem de escolha administrativa no aspecto vinculado. || A autoridade pode negar licença devida a quem preenche todos os requisitos vinculados apenas por discordância pessoal.
Discricionariedade é margem de escolha juridicamente delimitada, não liberdade para violar a lei. || Um ato discricionário pode usar critério discriminatório ilícito porque o mérito administrativo é espaço sem regras.
O controle de legalidade alcança atos discricionários. || Todo ato rotulado discricionário fica absolutamente imune ao Judiciário, inclusive quando houver desvio de finalidade.
Conveniência e oportunidade são avaliadas dentro dos limites legais e da finalidade pública. || Alegar oportunidade permite afastar todos os requisitos legais de competência e forma de qualquer decisão.
''')
add('ADM-B04-S04','a','art. 50 e §§1º a 3º; motivo, motivação e motivos determinantes','''
Motivo corresponde aos pressupostos de fato e de direito; motivação é a exposição das razões do ato. || Os termos motivo e motivação significam sempre a mesma coisa, sem qualquer distinção na análise do ato.
A Lei 9.784 exige motivação com indicação de fatos e fundamentos jurídicos nas hipóteses do art. 50. || Uma decisão que negue direito pode ser mantida sem qualquer razão, porque a lei federal dispensa motivação de todos os atos.
A motivação deve ser explícita, clara e congruente, nas condições legais. || Uma frase sem conexão com os fatos satisfaz necessariamente a motivação apenas porque ocupa espaço no documento.
A indicação de motivos vincula a validade do ato à correspondência desses motivos com a realidade e o direito, conforme a teoria dos motivos determinantes. || A autoridade pode declarar fato inexistente como fundamento decisivo e preservar a validade apenas afirmando que poderia ter decidido de outro modo.
''')
add('ADM-B04-S05','a','arts. 22 e 50; classificação dos atos por formação e destinatários','''
Classificar um ato exige identificar o critério utilizado, como destinatários, formação ou grau de vinculação. || Um ato deixa de poder ser vinculado apenas porque também foi classificado como individual, já que os critérios são incompatíveis.
Atos gerais e individuais diferenciam-se pelo alcance dos destinatários, não necessariamente pela autoridade que os assina. || Todo ato assinado pelo dirigente máximo é automaticamente geral, mesmo quando decide situação de uma pessoa determinada.
''')
add('ADM-B04-S06','a','art. 22, caput e §§1º a 4º','''
Os atos do processo administrativo não dependem de forma determinada senão quando a lei expressamente a exigir. || A Administração é obrigada a criar formalidade solene para todo ato, mesmo quando nenhuma lei a prevê.
Atos do processo devem ser produzidos por escrito, em vernáculo, com data, local e assinatura da autoridade responsável, conforme a disciplina legal. || O art. 22 permite dispensar sempre a identificação e a assinatura do responsável em qualquer decisão escrita.
''')
add('ADM-B04-S07','a','arts. 53 e 54','''
A Administração deve anular atos ilegais e pode revogar atos por conveniência ou oportunidade, respeitados os direitos adquiridos. || A revogação é o instrumento próprio para declarar a ilegalidade originária de um ato, enquanto a anulação depende apenas de nova conveniência.
O direito de anular atos administrativos de efeitos favoráveis decai em cinco anos, salvo comprovada má-fé, na disciplina do art. 54. || A Administração pode ignorar para sempre a decadência de ato favorável praticado de boa-fé, sem examinar o prazo ou exceção legal.
''')
add('ADM-B04-S08','a','art. 55','''
Atos com defeitos sanáveis podem ser convalidados pela Administração quando não houver lesão ao interesse público nem prejuízo a terceiros. || Qualquer vício, mesmo insanável e prejudicial a terceiros, deve ser automaticamente convalidado para economizar tempo.
Convalidação depende da natureza sanável do defeito e dos requisitos legais; não é perdão irrestrito de ilegalidades. || Um objeto expressamente proibido torna-se lícito por simples declaração de convalidação sem alteração do fundamento jurídico.
''')
add('ADM-B05-S01','serv','arts. 2º e 6º; CF, art. 175','''
Incumbe ao poder público prestar serviços públicos diretamente ou sob delegação, nos termos constitucionais. || Ao delegar serviço, o poder público perde definitivamente toda titularidade e qualquer responsabilidade de controle.
A concessão de serviço público é delegação de prestação nos termos legais, não transferência da soberania estatal. || A concessionária passa a criar livremente leis gerais do serviço porque a concessão lhe transfere poder soberano.
O serviço adequado envolve regularidade, continuidade, eficiência, segurança, atualidade, generalidade, cortesia e modicidade tarifária. || Atender usuários com descortesia é juridicamente indiferente porque serviço adequado só significa funcionamento técnico.
A classificação dos serviços deve considerar o critério adotado e seu regime jurídico. || Todo serviço útil ao público recebe necessariamente o mesmo regime de delegação e cobrança, independentemente de previsão constitucional ou legal.
''')
add('ADM-B05-S02','serv','arts. 29 a 31','''
O poder concedente deve regulamentar e fiscalizar permanentemente a prestação do serviço concedido. || A assinatura da concessão impede o poder concedente de fiscalizar o serviço durante a vigência contratual.
A concessionária deve prestar serviço adequado e permitir acesso à fiscalização nos termos legais. || A personalidade privada da concessionária autoriza impedir toda inspeção pública sobre a execução do serviço delegado.
''')
add('ADM-B05-S03','serv','arts. 6º e 7º','''
Atualidade do serviço compreende modernidade das técnicas, equipamentos e instalações, conservação e melhoria, na forma legal. || O serviço é atual apenas por ter sido inaugurado recentemente, ainda que abandone conservação e melhoria.
O usuário tem direitos como receber serviço adequado e informações para defesa de interesses, nos termos legais. || A condição de usuário elimina o direito de obter informação sobre o serviço e reclamar de falhas.
''')
add('ADM-B05-S04','serv','arts. 2º e 40; CF, art. 175','''
Concessão e permissão de serviço público seguem disciplina legal e exigência constitucional de licitação. || A permissão de serviço público dispensa sempre licitação porque a lei a descreve como precária.
A autorização possui hipóteses constitucionais e setoriais próprias, não substituindo indiscriminadamente qualquer concessão exigida por lei. || Chamar um contrato de autorização permite afastar automaticamente toda exigência legal de concessão, licitação ou regulação.
''')
add('ADM-B05-S05','serv','arts. 35 a 39','''
Encampação é retomada do serviço por interesse público, durante a concessão, mediante lei autorizativa específica e prévia indenização na forma legal. || A encampação é punição aplicada por culpa da concessionária e sempre dispensa autorização legislativa e indenização.
Caducidade relaciona-se à inexecução da concessão e exige apuração em processo administrativo com ampla defesa nos termos legais. || O descumprimento contratual permite declarar caducidade sem qualquer verificação ou oportunidade de defesa da concessionária.
''')
add('ADM-B06-S01','a','arts. 53 a 65; controle e autotutela administrativa','''
A autotutela permite à Administração examinar seus próprios atos quanto a legalidade e, nos casos cabíveis, mérito. || Uma vez assinado o ato, a Administração perde qualquer competência para corrigir ilegalidade sem autorização judicial prévia.
O controle administrativo deve respeitar direitos e garantias procedimentais. || A autotutela autoriza retirar todo direito individual consolidado sem considerar prazo, defesa ou boa-fé.
Recurso administrativo pode discutir legalidade e mérito nos termos da Lei 9.784. || O recurso administrativo é restrito a erros de digitação e não pode questionar fundamentos jurídicos da decisão.
A correção de ilegalidade não se confunde com revogação por mudança de conveniência. || Reconhecer que um ato nasceu ilegal equivale necessariamente a dizer que ele era válido, mas tornou-se inconveniente.
''')
add('ADM-B06-S02','cf','art. 5º, XXXV e LIV; controle judicial da Administração','''
O Judiciário pode apreciar lesão ou ameaça a direito decorrente da atuação administrativa. || Uma portaria pode impedir definitivamente todo acesso ao Judiciário para discutir ato administrativo ilegal.
Atos discricionários submetem-se ao controle de juridicidade, inclusive competência, finalidade e limites. || A menção à discricionariedade impede verificar se um ato foi praticado por autoridade absolutamente incompetente.
O controle de legalidade não autoriza substituir indistintamente toda escolha administrativa lícita pela preferência pessoal do juiz. || Qualquer juiz pode revogar ato válido apenas porque escolheria solução mais conveniente em seu lugar.
A ausência de lesão consumada não afasta, por si só, a tutela jurisdicional de ameaça a direito. || A pessoa ameaçada por ato administrativo ilegal deve sempre aguardar o dano efetivo porque a Constituição não protege ameaças.
''')
add('ADM-B06-S03','cf','arts. 49, X, 70 e 71','''
O Congresso exerce fiscalização e controle dos atos do Executivo, inclusive da Administração indireta, nos termos constitucionais. || Entidades da Administração indireta ficam excluídas de controle parlamentar por possuírem personalidade própria.
O controle externo da União é exercido pelo Congresso com auxílio do Tribunal de Contas da União. || O TCU substitui integralmente o Congresso e passa a exercer sozinho toda função legislativa de controle externo.
A fiscalização abrange aspectos contábeis, financeiros, orçamentários, operacionais e patrimoniais na disciplina constitucional. || O controle externo se limita à existência física de dinheiro e jamais examina legitimidade ou economicidade.
Quem administra dinheiros, bens e valores públicos deve prestar contas nos termos do art. 70, parágrafo único. || Uma pessoa jurídica privada que gerencie recursos públicos fica automaticamente dispensada de prestar contas apenas por sua natureza privada.
''')
add('ADM-B06-S04','cf','art. 37, §6º','''
Pessoas jurídicas de direito público respondem pelos danos que seus agentes, nessa qualidade, causem a terceiros, conforme o art. 37, §6º. || Para toda responsabilidade estatal prevista no §6º, a vítima deve necessariamente provar intenção dolosa pessoal do agente.
A Constituição estende o regime do art. 37, §6º, às pessoas jurídicas privadas prestadoras de serviços públicos. || Uma concessionária de serviço público está excluída do §6º apenas porque possui personalidade privada.
O direito de regresso contra o agente exige dolo ou culpa nos termos constitucionais. || A responsabilização objetiva da pessoa jurídica torna automaticamente objetiva e sem exame de culpa a ação regressiva contra o agente.
O nexo entre conduta atribuída ao serviço e dano é relevante na análise da responsabilidade. || A responsabilidade objetiva transforma o Estado em segurador de qualquer dano do mundo, mesmo sem relação com sua atuação.
''')
add('ADM-B06-S05','im','arts. 1º, §§1º a 3º, 9º a 12; redação da Lei 14.230/2021','''
A Lei 8.429 atualizada caracteriza como improbidade as condutas dolosas tipificadas nos arts. 9º, 10 e 11, ressalvados tipos previstos em leis especiais. || Qualquer mero erro culposo do agente configura automaticamente todos os atos de improbidade dos arts. 9º, 10 e 11 na redação atual.
O enriquecimento ilícito do art. 9º envolve vantagem patrimonial indevida mediante conduta dolosa vinculada ao exercício da função. || Receber vantagem patrimonial indevida em razão do cargo só pode ser improbidade quando não houver dolo.
O art. 10 exige perda patrimonial efetiva e comprovada nos termos de seu texto atual. || O dano meramente presumido satisfaz sempre o art. 10, dispensada a comprovação de perda patrimonial efetiva.
A mera voluntariedade do agente não basta para caracterizar o dolo definido pela Lei de Improbidade. || Para comprovar dolo de improbidade, basta demonstrar que o agente praticou voluntariamente qualquer ato, sem examinar a finalidade ilícita tipificada.
''')
add('ADM-B06-S06','a','arts. 1º a 3º','''
A Lei 9.784 regula normas básicas do processo administrativo federal direto e indireto e alcança Legislativo e Judiciário no desempenho administrativo. || A Lei 9.784 só se aplica a ministérios do Executivo e exclui toda atividade administrativa de tribunal federal.
O administrado tem direito a ciência da tramitação, vista dos autos, cópias e conhecimento das decisões, observadas as condições legais. || A instauração de processo administrativo elimina o direito do interessado de conhecer decisões e acompanhar sua tramitação.
''')
add('ADM-B06-S07','a','arts. 11 a 15','''
Não podem ser delegadas edição de atos normativos, decisão de recursos administrativos e matérias de competência exclusiva. || A autoridade pode delegar decisão de recurso administrativo só por incluir a transferência em portaria interna.
A avocação é excepcional, temporária e exige motivos relevantes devidamente justificados, de competência de órgão hierarquicamente inferior. || A avocação pode ser permanente, imotivada e dirigida a qualquer entidade autônoma sem hierarquia.
''')
add('ADM-B06-S08','a','arts. 18 a 21','''
Interesse direto ou indireto na matéria é hipótese de impedimento de servidor ou autoridade no processo. || A autoridade com interesse pessoal direto pode decidir normalmente porque impedimento só existe quando houver parentesco.
A suspeição pode decorrer de amizade íntima ou inimizade notória com interessados ou pessoas indicadas no art. 20. || Ter amizade íntima com interessado nunca é relevante à imparcialidade porque apenas parentesco pode justificar afastamento.
''')
add('ADM-B06-S09','a','arts. 50, 56, 59, 61 e 64','''
O recurso administrativo pode impugnar razões de legalidade e de mérito; em regra, o prazo é de dez dias, salvo disposição legal específica. || O interessado sempre dispõe de trinta dias para qualquer recurso sob a Lei 9.784, sem possibilidade de prazo legal diverso.
Se a decisão recursal puder agravar a situação do recorrente, ele deverá ser cientificado para formular alegações antes da decisão. || A autoridade recursal pode agravar a situação do recorrente surpreendendo-o, sem a ciência para alegações exigida no art. 64.
''')

def build():
 plan=json.loads(PLAN.read_text())
 targets=[r for r in plan['assuntos'] if r['disciplina'] in ('Constitucional','Administrativo')]
 assert len(DATA)==len(targets),(len(DATA),len(targets))
 lessons=[]
 for r in targets:
  pid=r['id_planejamento'];src,loc,pairs=DATA[pid]
  n=r['meta_questoes_autorais'];assert len(pairs)*2==n,(pid,len(pairs)*2,n)
  lid='v17-'+pid.lower();stitle,surl=SOURCES[src]
  ref={'title':stitle,'url':surl,'locator':loc,'checkedAt':'2026-10-27'}
  questions=[]
  for i,(rule,case) in enumerate(pairs):
   # Pares testam uma regra abstrata e aplicação equivocada, não meras trocas de nomes.
   for answer,text in ((True,rule),(False,case)):
    j=len(questions)
    questions.append({'id':lid+'-q'+str(j+1).zfill(3),'text':text,'answer':answer,'explanation':('A afirmação está correta. ' if answer else 'O caso aplica incorretamente a regra. ')+rule+' Fundamento: '+loc+'.','kind':'autoral','version':1,'difficulty':('basico' if j<n*.35 else 'intermediario' if j<n*.8 else 'avancado'),'family':pid+'-fundamento-'+str(i+1),'microtopic':pid,'sourceRef':ref,'mode':('fixacao' if j<n*.25 else 'treino' if j<n*.75 else 'reserva')})
  rules=[p[0] for p in pairs]
  lesson={'id':lid,'d':'const' if r['disciplina']=='Constitucional' else 'adm','title':r['assunto'],'core':rules[0],'rule':'\n\n'.join(rules),'example':'Examine esta situação: '+pairs[0][1]+'\nCorreção: '+rules[0],'contrast':'Compare o fundamento jurídico com a conclusão do caso. '+(rules[1] if len(rules)>1 else rules[0]),'limit':'A aula cobre os fundamentos listados; casos fora dessas premissas exigem nova consulta à fonte. '+loc+'. Revisão editorial com consulta oficial em 27/10/2026; não é parecer jurídico nem revisão jurídica independente.','source':src if src in ('cf','s','a','stf') else 'cf' if r['disciplina']=='Constitucional' else 'a','sources':[ref],'minutes':40,'block':r['bloco'],'planId':pid,'subtopics':rules,'questions':questions}
  lessons.append(lesson)
 questions=[q for l in lessons for q in l['questions']]
 assert len(questions)==640,len(questions)
 assert len({q['id'] for q in questions})==640
 norm=lambda s:re.sub(r'\s+',' ',s.strip().casefold())
 duplicates=[(s,n) for s,n in collections.Counter(norm(q['text']) for q in questions).items() if n>1]
 assert not duplicates,duplicates
 assert all(type(q['answer']) is bool for q in questions)
 result={'lessons':lessons,'sources':[{'id':k,'title':v[0],'url':v[1]} for k,v in SOURCES.items()],'editorial':{'version':'1.7.1','date':'2026-10-27','author':'JARVIS — elaboração própria','count':640,'lessons':len(lessons),'method':'Regras e casos de erro escritos por microassunto; Python apenas compila e valida quotas, IDs, textos e gabaritos booleanos.','review':'Conferência editorial e pesquisa de fundamentos oficiais; sem revisão jurídica independente.','limitations':['Profundidade introdutória e intermediária; não substitui consulta à lei atualizada e jurisprudência.','Dificuldade é classificação editorial, não estimativa psicométrica.','Cada família inclui regra e caso de erro para recuperação; não considerar acerto de um par memorizado como domínio.'],'verifiedUpdates':['EC 138/2025: professor + outro cargo de qualquer natureza, com condições constitucionais.','ADI 2135: flexibilização do RJU, efeitos ex nunc e vedação de transmudação dos vínculos atuais.','Tema 532: requisitos cumulativos para delegação de polícia à entidade privada da indireta.']}}
 out=ROOT/'data/const-adm.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2))
 print(json.dumps({'file':str(out),'lessons':len(lessons),'questions':len(questions),'counts':dict(collections.Counter(l['d'] for l in lessons)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},ensure_ascii=False))
if __name__=='__main__':build()
