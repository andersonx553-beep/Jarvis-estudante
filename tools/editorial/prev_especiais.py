"""Assets editoriais autorais. Python organiza e valida; não multiplica modelos de enunciado."""
from pathlib import Path
import json, collections, re
ROOT=Path(__file__).resolve().parents[2]
PLAN=ROOT/'data/curriculum-plan.json'
DATE='2026-10-27'
SOURCES={
'def':{'title':'Lei 10.779/2003 consolidada','url':'https://www.planalto.gov.br/ccivil_03/leis/2003/l10.779compilado.htm','locator':'arts. 1º a 4º, com alterações posteriores'},
'def26':{'title':'Lei 15.399/2026','url':'https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15399.htm','locator':'arts. 1º e 10; alteração da Lei 10.779/2003'},
'mte':{'title':'MTE — Seguro-Desemprego do Pescador Artesanal','url':'https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/seguro-desemprego-do-pescador-artesanal','locator':'Requisitos; Histórico da gestão; Canais de atendimento'},
'loas':{'title':'Lei 8.742/1993 — LOAS','url':'https://www.planalto.gov.br/ccivil_03/leis/l8742.htm','locator':'arts. 1º a 6º; 6º-A a 6º-E; 16 a 18; 20 a 21-A; 26-A a 26-H'},
'bpc':{'title':'MDS — Benefício de Prestação Continuada','url':'https://www.gov.br/mds/pt-br/acoes-e-programas/SUAS/beneficios-assistenciais/beneficio-assistencial-ao-idoso-e-a-pessoa-com-deficiencia-bpc','locator':'Requisitos e renda familiar'},
'ctc':{'title':'MPS — Guia de Certidão de Tempo de Contribuição','url':'https://www.gov.br/previdencia/pt-br/assuntos/rpps/legislacao-dos-rpps/copy2_of_GUIACTC_v5.pdf','locator':'Contagem recíproca, destinação da CTC e vedações'},
'comp':{'title':'Lei 9.796/1999','url':'https://www.planalto.gov.br/ccivil_03/leis/l9796.htm','locator':'arts. 1º a 7º'},
'dcomp':{'title':'Decreto 10.188/2019','url':'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10188.htm','locator':'arts. 1º a 3º; regulamentação da compensação'},
'ec':{'title':'Emenda Constitucional 103/2019','url':'https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm','locator':'arts. 3º, 15 a 21, 24 a 26, 29 e 30'},
'lc':{'title':'Lei Complementar 142/2013','url':'https://presidencia.gov.br/ccivil_03/leis/lcp/lcp142.htm','locator':'arts. 2º a 10'},
'c':{'title':'Lei 8.212/1991','url':'https://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm','locator':'arts. 1º a 3º; 12 a 15; 20 a 22; 28 e 30'},
'p':{'title':'Lei 8.213/1991','url':'https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm','locator':'arts. 10 a 16; 18; 24 a 27-A; 29-A; 94 a 96; 103'},
'r':{'title':'Decreto 3.048/1999 consolidado','url':'https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm','locator':'Regulamento da Previdência Social; arts. 9º, 11, 13, 18, 19 e 19-B'},
'in':{'title':'INSS — IN 128/2022 e atos alteradores','url':'https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/instrucao-normativa/2022','locator':'IN 128/2022; índice de alterações até IN 212/2026'},
'cnis':{'title':'INSS — CNIS e atualização de dados','url':'https://www.gov.br/inss/pt-br/centrais-de-conteudo/publicacoes/outras/declaracao-de-confirmacao-do-envio-de-dados-trabalhistas-e-previdenciarios-pelo-esocial-e-informacoes-dos-numeros-dos-recibos-eletronicos.pdf','locator':'Anexo II da IN 128/2022; confirmação de dados eSocial'},
'cf':{'title':'Constituição Federal','url':'https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm','locator':'arts. 37, 40, 194, 195, 201 e 203'},
'atend':{'title':'Lei 13.460/2017 — direitos do usuário','url':'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13460.htm','locator':'arts. 4º a 6º'},
'saude':{'title':'Decreto 6.833/2009 — SIASS','url':'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6833.htm','locator':'arts. 1º a 3º; não usar comitê revogado do art. 4º'},
}
DATA={}
def add(key,src,core,example,contrast,limit,lines):
 records=[]
 for line in lines.strip().splitlines():
  flag,text,explanation=line.split('|',2)
  assert flag in ['C','E'],(key,line)
  records.append({'text':text.strip(),'answer':flag=='C','explanation':explanation.strip()})
 DATA[key]={'src':src.split(','),'core':core,'example':example,'contrast':contrast,'limit':limit,'records':records}

add('15-01','def,mte,def26','O Seguro-Defeso protege o pescador profissional artesanal na paralisação da pesca para preservação das espécies.','Um pescador que depende da pesca artesanal deve demonstrar a atividade e os demais requisitos; estar apenas cadastrado não comprova tudo.','Pescador profissional artesanal não se confunde com pescador amador, industrial ou familiar sem atividade própria comprovada.','A análise depende da espécie, do período e da legislação aplicável. Não aplicar automaticamente regras de 2022 a pedidos de 2026.', '''
C|A paralisação da pesca para preservar a espécie integra a razão de ser do Seguro-Defeso.|O benefício substitui temporariamente a renda da pesca artesanal no defeso, não remunera qualquer interrupção voluntária.
E|Quem pesca apenas por lazer passa a ter direito ao Seguro-Defeso ao registrar um barco.|O programa atende pescador profissional artesanal que satisfaça requisitos; lazer e registro de embarcação não bastam.
C|A atividade artesanal pode ser exercida individualmente ou em economia familiar.|Essas duas formas de exercício são contempladas no art. 1º da Lei 10.779.
E|Todo familiar de um pescador beneficiário recebe automaticamente uma parcela própria.|O familiar precisa preencher os requisitos; não há extensão automática por parentesco.
E|A inscrição no RGP dispensa a comprovação do exercício da pesca.|Cadastro e prova de atividade são requisitos diferentes e cumulativos quando exigidos.
C|A fonte de renda do requerente importa para aferir a elegibilidade ao Seguro-Defeso.|A lei exige enquadramento do pescador e ausência de outra fonte de renda incompatível.
C|O benefício é pessoal e não pode ser cedido livremente pelo pescador a terceiro.|A Lei 10.779 define o Seguro-Defeso como pessoal e intransferível.
E|Uma indústria pesqueira pode requerer o Seguro-Defeso em seu próprio CNPJ.|O titular protegido é o pescador artesanal, não a empresa industrial.
C|Uma pessoa que só presta apoio à pesca não obtém o Seguro-Defeso por essa atividade de apoio.|A lei exclui a extensão automática às atividades de apoio.
E|O defeso corresponde sempre a férias anuais escolhidas pelo pescador.|É uma restrição de atividade definida para preservação da espécie, não férias escolhidas individualmente.
C|O valor legal do Seguro-Defeso corresponde a um salário mínimo mensal.|Não se calcula o valor individual pela média salarial do pescador.
E|Para receber, basta afirmar que qualquer espécie está em reprodução, sem observar o defeso oficialmente fixado.|A concessão exige período de defeso e enquadramento relacionados à atividade, além dos demais requisitos.
''')
add('15-02','def,mte','O requerente deve observar restrições de renda, de atividade e de acumulação previstas para o Seguro-Defeso.','Receber pensão por morte exige examinar a exceção legal; não autoriza ignorar a comprovação de pesca.','Exceção a uma vedação de acumulação não dispensa os demais requisitos do benefício.','As regras de programas de transferência de renda e da legislação posterior devem ser conferidas para o período do pedido.', '''
C|A existência de outra fonte de renda incompatível pode impedir a concessão do Seguro-Defeso.|A proteção se destina a quem vive da atividade pesqueira e atende às condições legais.
E|O pescador pode manter qualquer emprego remunerado durante o defeso, sem consequência para a habilitação.|Outra atividade remunerada pode descaracterizar as condições exigidas pelo programa.
C|A pensão por morte figura entre as exceções legais à vedação de percepção de benefício contínuo.|A exceção precisa ser lida com os demais requisitos do Seguro-Defeso.
E|A exceção referente à pensão por morte elimina a exigência de comprovar atividade pesqueira.|A exceção trata de acumulação; a atividade continua precisando ser comprovada.
C|O auxílio-acidente é tratado de modo excepcional nas restrições de acumulação do Seguro-Defeso.|O rol de exceções não equivale a liberação de todos os benefícios previdenciários.
E|A autorização relativa ao auxílio-acidente permite também acumular qualquer aposentadoria.|Não se amplia uma exceção específica para toda espécie de benefício.
C|Não se pode presumir direito a vários Seguros-Defeso no mesmo ano por pescar espécies diferentes.|A Lei 10.779 limita o recebimento em defesos de espécies distintas no mesmo ano.
E|O pescador pode transferir uma parcela não utilizada ao cônjuge como se fosse crédito familiar.|A prestação é pessoal e intransferível.
C|Continuar pescando a espécie proibida durante o defeso contraria a finalidade da proteção.|O benefício pressupõe observância da paralisação protegida e das condições do programa.
E|A condição de pescador artesanal torna irrelevante a apuração de fraude na concessão.|O enquadramento profissional não afasta controle, revisão nem consequências legais da fraude.
C|Uma exceção legal de acumulação deve ser analisada pelo seu alcance, sem generalização para prestações distintas.|O detalhe decisivo é qual benefício foi expressamente ressalvado pela lei.
E|Apenas o parentesco com pescador regular basta para afastar impedimentos de renda e de atividade.|O direito não é automaticamente derivado do vínculo familiar.
''')
add('15-03','mte,def26,def','A competência precisa ser situada no tempo: o MTE assumiu os defesos iniciados a partir de novembro de 2025.','Um pedido sobre defeso iniciado em 2022 não deve ser confundido com um defeso iniciado em 2026; as competências de processamento têm marcos históricos.','Competência para habilitar não é necessariamente igual à entidade que pagava historicamente os recursos do FAT.','Prazos de requerimento podem ter mudanças por ato específico; o app não deve congelar um prazo sem data e fonte.', '''
C|Para defesos iniciados a partir de 1º de novembro de 2025, a gestão do programa foi transferida ao MTE.|A página oficial do MTE distingue esse marco da fase em que o INSS habilitava beneficiários.
E|Em outubro de 2026, a regra geral ainda é requerer todo novo defeso exclusivamente no Meu INSS.|Os canais atuais do MTE incluem Carteira de Trabalho Digital e Portal Emprega Brasil.
C|Requerimentos de períodos que pertenciam à competência do INSS precisam respeitar a disciplina histórica correspondente.|A transição não torna todo pedido antigo um pedido novo do MTE.
E|A mudança de órgão converteu o Seguro-Defeso em aposentadoria paga pelo RGPS.|A natureza de seguro-desemprego do pescador não se transforma em aposentadoria.
C|Carteira de Trabalho Digital e Portal Emprega Brasil são canais oficiais indicados pelo MTE.|O canal do requerimento deve ser conferido segundo a competência temporal.
E|Não existe possibilidade de pedido de revisão da negativa do Seguro-Defeso.|O MTE disponibiliza revisão administrativa pelos canais oficiais, com justificativa e documentos.
C|Uma questão sobre competência do programa deve indicar ou permitir identificar a data do defeso.|Sem o marco temporal, pode confundir a regra histórica com a atual.
E|O benefício é financiado necessariamente pelas mesmas contribuições que calculam o salário de benefício de uma aposentadoria.|O Seguro-Defeso é custeado com recursos do FAT; não usa a lógica de renda mensal de aposentadoria.
C|No período de competência do INSS entre abril de 2015 e outubro de 2025, o pagamento continuava vinculado ao MTE e ao FAT.|Habilitação e fonte de pagamento precisam ser distinguidas.
E|Protocolar o requerimento assegura pagamento antes da verificação dos requisitos.|O pedido precisa ser processado e analisado; protocolo não é concessão automática.
C|O pagamento deve observar o período de defeso correspondente e as regras do programa.|A Lei 15.399/2026 vincula o pagamento ao período protegido.
E|Um prazo descrito em apostila de 2022 pode ser usado em qualquer pedido de 2026 sem verificar atos posteriores.|Regras e atos supervenientes devem ser checados para não cobrar uma disciplina temporal superada.
''')
add('15-04','def,def26,mte','Lei, regulamento e atos posteriores devem ser lidos em conjunto, observando hierarquia e data.','Um resumo que cite apenas o Decreto 8.424/2015 pode deixar de fora mudanças das Leis 15.265/2025 e 15.399/2026.','O regulamento detalha a lei; não possui liberdade para contrariar a disciplina legal posterior.','Não confundir menção ao edital histórico com afirmação de que todo o texto original do decreto permanece intacto.', '''
C|O Decreto 8.424/2015 é uma referência regulamentar histórica do Seguro-Defeso.|Seu estudo deve considerar as alterações legais posteriores aplicáveis ao caso.
E|O decreto regulamentar pode conservar regra contrária a lei posterior apenas por ter sido citado no edital de 2022.|A hierarquia e a legislação posterior não são afastadas pela referência no edital antigo.
C|A Lei 15.399/2026 alterou a Lei 10.779/2003 e decorreu da conversão da MP 1.323/2025.|O quadro de atualização é parte necessária da leitura do programa em 2026.
E|A inclusão no CadÚnico para o Seguro-Defeso cria, por si, o mesmo limite de renda do BPC.|A redação legal do Seguro-Defeso prevê inscrição sem efeito de criar limite de renda de acesso por esse cadastro.
C|A legislação de 2026 prevê identificação biométrica do requerente, nos termos da disciplina legal aplicável.|Não é correto tratar o requerimento como imune à identificação cadastral.
E|Falha biométrica torna dispensável qualquer canal de revisão ao interessado.|A Lei 15.399 prevê canais de revisão céleres e gratuitos em falhas cadastrais ou biométricas.
C|O controle do programa pode cruzar informações constantes de bases cadastrais oficiais.|O cruzamento serve à verificação das condições de concessão e manutenção.
E|A lei autoriza divulgar o endereço completo dos beneficiários como requisito de transparência.|A regra de publicidade veda a divulgação do endereço completo ou dados que identifiquem especificamente o domicílio.
C|A lista pública mensal prevista na lei contém nome, município e inscrição no RGP, com proteção de dados do domicílio.|Publicidade e proteção de dados precisam coexistir na forma legal.
E|O relatório de atividade pesqueira pode ser substituído automaticamente por prova de parentesco.|A comprovação da atividade entre defesos obedece aos critérios legais e regulamentares, não ao mero parentesco.
C|Exceções justificadas à impossibilidade de exercício da pesca não autorizam dispensar toda análise documental.|A exceção expressa tem alcance delimitado e deve ser examinada no procedimento.
E|Uma regra histórica da banca deve ser apagada quando surgir lei nova, sem registrar qual era a redação cobrada.|O gabarito histórico deve ser preservado e distinguido do entendimento vigente.
''')
add('16-01','loas,cf','Assistência social é direito do cidadão e dever do Estado, de natureza não contributiva.','Uma pessoa que nunca contribuiu pode buscar proteção assistencial, mas precisa satisfazer os requisitos da prestação solicitada.','Assistência é componente da seguridade; não equivale a previdência nem se limita a caridade.','Não contributividade não significa concessão irrestrita de qualquer benefício.', '''
C|A assistência social integra a seguridade e independe de contribuição prévia do usuário.|O art. 203 da Constituição e o art. 1º da LOAS estabelecem sua natureza não contributiva.
E|A LOAS protege apenas quem manteve qualidade de segurado do RGPS.|A qualidade de segurado não é requisito geral da assistência social.
C|Proteção social, vigilância socioassistencial e defesa de direitos são objetivos da assistência.|A LOAS não reduz sua atuação ao pagamento de dinheiro.
E|A responsabilidade pública pela assistência é excluída quando existem entidades beneficentes.|A atuação da sociedade não elimina o dever estatal.
C|A proteção à família, à maternidade, à infância, à adolescência e à velhice integra o campo da assistência.|Essas dimensões aparecem entre os objetivos constitucionais e legais.
E|Para obter atendimento assistencial, o usuário deve comprovar contribuição mínima de doze meses.|Assistência é não contributiva; a prestação específica pode ter outros requisitos, não essa carência geral.
C|A LOAS prevê respeito à dignidade e à autonomia do cidadão.|O acesso não deve submeter a pessoa a exigências vexatórias de comprovação da necessidade.
E|Um serviço assistencial pode exigir humilhação pública do usuário para demonstrar pobreza.|A dignidade e a vedação de comprovação vexatória orientam a política.
C|A igualdade de acesso deve alcançar populações urbanas e rurais.|Não há autorização para excluir o meio rural da proteção assistencial.
E|O valor de mercado do atendimento prevalece necessariamente sobre as necessidades sociais.|A LOAS determina a supremacia do atendimento às necessidades sociais sobre exigências de rentabilidade econômica.
C|Descentralização e participação da população são diretrizes organizativas da assistência.|A organização não se resume a um comando central sem controle social.
E|Toda prestação da assistência deve ser executada diretamente pela União.|A organização é descentralizada, com atribuições nos diferentes entes.
C|A divulgação de benefícios, serviços e critérios de acesso é compatível com os princípios da LOAS.|Informação acessível integra a possibilidade real de exercício do direito.
E|A assistência social só pode agir depois de esgotada toda ação de saúde e previdência.|São áreas articuladas, mas a LOAS não institui essa condição geral de última instância.
C|A defesa de direitos visa garantir o pleno acesso às provisões socioassistenciais.|A política não se reduz à entrega isolada de benefícios financeiros.
E|Participação popular na assistência significa substituir a legislação por decisões privadas sem controle público.|A participação se exerce na estrutura legal e no controle social, preservando responsabilidade pública.
''')
add('16-02','loas','O SUAS articula proteção social básica e especial, com responsabilidades e níveis de atenção distintos.','Uma família em vulnerabilidade pode demandar prevenção de riscos; uma situação de violência exige resposta especializada e articulação de rede.','Vulnerabilidade e violação de direitos não são situações necessariamente idênticas.','Serviços, programas, projetos e benefícios precisam ser articulados, sem presumir que um equipamento realiza tudo.', '''
C|A proteção básica busca prevenir situações de risco social e fortalecer vínculos.|A LOAS distingue prevenção de riscos das respostas especializadas a violações.
E|A proteção básica pressupõe necessariamente que já houve rompimento total dos vínculos familiares.|O rompimento não é requisito para a atuação preventiva.
C|A proteção especial atende famílias e indivíduos em risco pessoal ou social decorrente de violações de direitos.|Sua atuação exige especialização conforme a situação atendida.
E|A proteção especial exclui o trabalho de reconstrução de vínculos familiares e comunitários.|Reconstrução de vínculos e proteção diante de violações integram sua finalidade.
C|O SUAS compreende gestão compartilhada e articulação entre entes federativos.|A estrutura combina responsabilidades públicas em vez de isolar cada esfera.
E|SUAS é apenas o nome de um benefício mensal pago pelo INSS.|É sistema de organização da política de assistência, não um único benefício.
C|A rede socioassistencial pode incluir entidades sem fins lucrativos vinculadas ao sistema, conforme requisitos legais.|A oferta não é composta exclusivamente por repartições públicas.
E|Qualquer entidade lucrativa passa a integrar a rede socioassistencial ao vender um serviço ao usuário.|A vinculação ao SUAS e a natureza das entidades obedecem a requisitos específicos.
C|A integração da rede ajuda a organizar referência e acompanhamento das necessidades do usuário.|A articulação não dispensa identificar a atribuição de cada serviço.
E|Descentralização significa que os entes ficam livres de padrões nacionais e de controle social.|A descentralização opera dentro da estrutura legal do sistema.
C|O enfrentamento de vulnerabilidades pode exigir atuação intersetorial com saúde, educação e outras políticas.|Intersetorialidade não converte todos os serviços em serviço de saúde ou de previdência.
E|Encaminhar uma família a outra política elimina necessariamente toda responsabilidade de acompanhamento assistencial.|Encaminhamento não autoriza abandono do caso quando houver atribuição de acompanhamento.
C|O fortalecimento da função protetiva da família pode ser uma ação de proteção básica.|A finalidade preventiva não depende de benefício monetário concedido.
E|Acolhimento institucional é a única resposta possível para qualquer vulnerabilidade econômica.|As respostas devem respeitar necessidade, proporcionalidade e tipificação dos serviços.
C|A vigilância socioassistencial pode apoiar o conhecimento territorial de vulnerabilidades e riscos.|Ela subsidia planejamento e oferta, não se confunde com investigação policial.
E|A proteção social especial substitui automaticamente a atuação do sistema de justiça em todos os casos.|O SUAS articula a proteção, sem absorver competências de outros órgãos.
''')
add('16-03','loas','CRAS e CREAS são unidades públicas com papéis diferentes na rede de proteção.','Uma orientação preventiva territorial se relaciona ao CRAS; atendimento especializado diante de violação de direitos pode exigir CREAS.','O critério de escolha não é simplesmente a idade do usuário ou o valor de sua renda.','Unidade de referência não é órgão que concede, por conta própria, todos os benefícios operados por outras instituições.', '''
C|O CRAS é referência pública territorial para a proteção social básica.|Sua atuação se vincula à prevenção e ao fortalecimento de vínculos.
E|O CREAS é apenas outro nome para uma agência da Previdência Social.|CREAS integra a assistência e a proteção especial, não a rede de agências do RGPS.
C|O CREAS pode ter abrangência municipal, estadual ou regional, conforme organização do sistema.|Sua referência é a oferta especializada a famílias e indivíduos em violação de direitos.
E|O CRAS é destinado exclusivamente a investigar crimes praticados por seus usuários.|Sua finalidade é socioassistencial, não de polícia investigativa.
C|O atendimento especializado no CREAS não pressupõe que toda família deva ser institucionalizada.|A intervenção depende das necessidades e dos serviços apropriados.
E|O cadastro realizado no CRAS garante automaticamente a concessão do BPC.|Cadastro e orientação não substituem a verificação dos requisitos pelo procedimento competente.
C|Os equipamentos devem favorecer articulação com a rede de serviços e outras políticas.|Referência territorial não é justificativa para atendimento isolado.
E|Qualquer atividade desenvolvida em um CRAS se transforma em benefício previdenciário.|A natureza assistencial dos serviços não muda por existir relação com proteção social.
C|O trabalho com famílias pode incluir orientação e fortalecimento de vínculos.|A atuação não se resume a distribuir bens materiais.
E|A diferença entre CRAS e CREAS consiste apenas no tamanho físico do prédio.|A distinção principal é função e nível de proteção, não metragem.
C|Uma situação de violência pode exigir encaminhamento especializado e articulação com órgãos competentes.|A resposta adequada considera a violação e as atribuições da rede.
E|Todo usuário idoso é atendido exclusivamente pelo CREAS, mesmo sem situação que exija proteção especial.|A idade, isoladamente, não define o nível de proteção necessário.
C|A acessibilidade e o acolhimento são relevantes para o acesso aos equipamentos socioassistenciais.|Direito formal sem condições reais de acesso não esgota a proteção.
E|Receber orientação no CRAS torna dispensável preservar a privacidade das informações familiares.|Atendimento e compartilhamento de dados exigem finalidade e resguardo adequado.
C|Uma unidade de referência pode orientar sobre serviços sem conceder diretamente cada benefício disponível na rede.|Orientar, encaminhar e conceder são atividades distintas.
E|O funcionamento territorial do CRAS permite excluir arbitrariamente pessoas em vulnerabilidade de toda a rede.|A organização territorial deve orientar o acesso e o encaminhamento adequado, não negar proteção arbitrariamente.
''')
add('16-04','loas','Conselhos de assistência exercem deliberação e controle social com composição prevista em lei.','Um conselho fiscaliza a política e delibera dentro de sua competência; não se torna agência que concede cada benefício individual.','CNAS, conselhos locais e órgão gestor possuem funções diferentes.','Composição e mandatos exigem a norma específica; não transpor automaticamente regras de um colegiado a outro.', '''
C|O CNAS é órgão superior de deliberação colegiada na estrutura prevista pela LOAS.|Sua função não é apenas consultoria informal ao gestor.
E|O CNAS é formado exclusivamente por representantes governamentais.|A LOAS prevê participação governamental e da sociedade civil em sua composição.
C|A composição do CNAS é paritária entre governo e sociedade civil.|A paridade é elemento do modelo de controle social.
E|Conselhos municipais de assistência são subordinados hierarquicamente ao CNAS como departamentos internos.|Cada conselho atua no âmbito e nas competências legais de sua esfera.
C|A fiscalização da política de assistência integra o papel dos conselhos.|O controle social acompanha a gestão e as provisões socioassistenciais.
E|O CNAS substitui o INSS na análise individual de todo requerimento de BPC.|Deliberação e controle não equivalem à operacionalização individual do benefício.
C|A LOAS inclui conselhos nas esferas nacional, estadual, distrital e municipal.|O controle social integra a organização descentralizada.
E|A participação da sociedade civil autoriza conselheiros a ignorar regras legais de funcionamento.|A representação não afasta legalidade, competência e procedimentos do colegiado.
C|Aprovar diretrizes e acompanhar a aplicação de recursos pode integrar competências do CNAS.|A atuação deve ser situada nos incisos do art. 18 da LOAS.
E|Toda decisão judicial sobre assistência depende de autorização prévia do CNAS.|O conselho não condiciona o exercício geral da jurisdição.
C|O CNAS possui dezoito membros titulares e respectivos suplentes, com representação paritária.|O art. 17, § 1º, da LOAS fixa a composição; suplência não elimina a paridade entre governo e sociedade civil.
E|O mandato dos membros do CNAS é de quatro anos e admite reconduções ilimitadas.|A LOAS prevê mandato de dois anos, permitida uma única recondução por igual período.
''')
add('16-05','loas,bpc','O BPC garante um salário mínimo ao idoso ou à pessoa com deficiência que preencha os requisitos assistenciais.','Ter 65 anos cumpre o critério etário, mas não demonstra sozinho renda, cadastro e demais requisitos.','BPC não é aposentadoria e deficiência não se identifica automaticamente com incapacidade total para toda atividade.','Avaliação e procedimentos podem ser alterados por normas posteriores; não confundir diagnóstico clínico isolado com a avaliação legal.', '''
C|O critério etário do BPC ao idoso é de 65 anos ou mais.|A idade precisa ser acompanhada da verificação dos demais requisitos.
E|A idade de 60 anos basta, por si só, para preencher o critério etário do BPC.|A LOAS fixa 65 anos para essa modalidade, não a idade geral de pessoa idosa.
C|O BPC pode ser devido a pessoa com deficiência de qualquer idade, se cumpridos os requisitos.|A modalidade de deficiência não possui a idade mínima de 65 anos.
E|A concessão do BPC exige sempre contribuição anterior ao RGPS.|É benefício assistencial não contributivo.
C|A análise da deficiência considera impedimento de longo prazo em interação com barreiras.|O conceito legal é mais amplo que um diagnóstico tomado isoladamente.
E|Uma doença de curta duração gera automaticamente direito ao BPC da pessoa com deficiência.|É necessário enquadramento na definição legal e cumprimento de todos os requisitos.
C|Para a LOAS, impedimento de longo prazo é o que produz efeitos por no mínimo dois anos.|Não se exige necessariamente caráter permanente para todos os casos.
E|O BPC é pago em valor calculado pela média das contribuições do requerente.|Seu valor é um salário mínimo, sem salário de benefício contributivo.
C|O requerimento pode demandar avaliação social além da avaliação pertinente à condição de deficiência.|A análise não se esgota na leitura de um laudo particular.
E|Completar 65 anos dispensa qualquer exame dos requisitos econômicos.|Idade e situação socioeconômica são condições distintas.
C|A alfabetização ou a escolaridade, sozinhas, não substituem a avaliação legal da deficiência.|Barreiras e impedimentos precisam ser examinados conforme a disciplina do benefício.
E|Para o BPC, deficiência e invalidez previdenciária são conceitos obrigatoriamente idênticos.|São institutos de prestações distintas e não podem ser equiparados sem análise.
''')
add('16-06','loas,bpc','A apuração de renda do BPC exige definir o grupo familiar legal e observar rendas incluídas e excluídas.','Um benefício recebido por outro morador pode exigir análise de exclusão legal; não basta somar todo valor da casa sem qualificar sua natureza.','Família para o BPC não é automaticamente toda pessoa que frequenta a residência nem qualquer cadastro de outro programa.','O limite legal não esgota todas as hipóteses de comprovação da vulnerabilidade; observar as regras e decisões aplicáveis.', '''
C|A renda mensal por pessoa depende da renda computável e do número de integrantes da família legal.|O cálculo exige primeiro definir corretamente numerador e denominador.
E|Toda pessoa que visita a casa do requerente deve integrar o grupo familiar do BPC.|A LOAS delimita familiares e exige condições como a residência sob o mesmo teto.
C|O requerente integra o grupo familiar considerado na apuração da renda.|Não se calcula a renda per capita excluindo automaticamente o próprio interessado.
E|As exclusões legais de renda podem ser ignoradas porque o cadastro informa um valor bruto.|A qualificação das rendas é necessária para aplicar a norma.
C|O parâmetro de um quarto do salário mínimo per capita está previsto na LOAS, com disciplina complementar de avaliação.|É preciso distinguir o critério objetivo das demais regras legais de aferição da vulnerabilidade.
E|Qualquer renda um centavo superior a um quarto do mínimo encerra, em toda hipótese, a análise sem outros elementos.|A legislação admite outros elementos probatórios e disciplina hipóteses adicionais de aferição.
C|Morar no mesmo imóvel não permite tratar como irrelevantes as relações familiares exigidas pela LOAS.|Composição familiar não é simples contagem de pessoas presentes no imóvel.
E|Renda per capita significa dividir o salário mínimo pelo número de requerimentos feitos no mês.|O quociente usa renda computável familiar e integrantes da família legal.
C|Um benefício de até um salário mínimo recebido por outro idoso ou pessoa com deficiência pode demandar a exclusão legal própria.|A hipótese do art. 20 deve ser conferida antes de computar o valor.
E|Gastos de saúde autorizam qualquer dedução inventada pelo atendente, sem fundamento.|Elementos de vulnerabilidade e despesas devem ser tratados conforme regras legais e regulamentares.
C|A atualização cadastral auxilia a análise, mas não altera por si o conceito legal de família.|Cadastro deve refletir os fatos e ser aplicado com a legislação da prestação.
E|O recebimento de uma renda excluída por lei é suficiente, isoladamente, para negar o BPC.|O cálculo deve respeitar a exclusão e os demais requisitos do caso.
''')
add('16-07','loas,bpc','O BPC é pessoal, sujeito à manutenção dos requisitos e a regras próprias de suspensão, cessação e acumulação.','A morte do titular não transforma o BPC em pensão para seus familiares.','Revisão de benefício, suspensão por trabalho e cessação são situações distintas.','Não aplicar revisão médica de modo automático a hipóteses dispensadas pela legislação vigente.', '''
C|O BPC não gera pensão por morte aos dependentes de seu titular.|Não é benefício previdenciário transmissível em forma de pensão.
E|O titular do BPC recebe abono anual previdenciário obrigatoriamente.|O BPC não paga décimo terceiro como aposentadoria ou pensão do RGPS.
C|A dispensa de reavaliação médico-pericial por impedimento permanente não impede apuração fundamentada de fraude ou erro.|O art. 21, § 5º, da LOAS, alterado em 2025, ressalva a suspeita fundamentada de fraude ou erro.
E|Toda pessoa com deficiência deve ser submetida a reavaliação médico-pericial periódica, mesmo com impedimento permanente, irreversível ou irrecuperável.|A LOAS prevê dispensa da avaliação periódica nessa hipótese, ressalvada suspeita fundamentada de fraude ou erro.
C|O exercício de atividade remunerada pela pessoa com deficiência pode levar à suspensão do BPC conforme a disciplina legal.|A lei estabelece uma relação específica entre trabalho, suspensão e possibilidade de retorno.
E|Encerrar o trabalho nunca permite voltar a receber BPC antes suspenso, mesmo preenchidos os requisitos.|Há disciplina de continuidade/restabelecimento, sem presumir vedação absoluta.
C|A LOAS contém regras de vedação de acumulação e exceções que precisam ser examinadas pelo tipo de prestação.|Não basta afirmar que qualquer pagamento é sempre incompatível.
E|Por ser assistencial, o BPC pode ser acumulado livremente com qualquer aposentadoria.|A não contributividade não elimina as vedações de acumulação.
C|Uma medida de suspensão deve ser diferenciada da conclusão definitiva de que o direito cessou.|Causa, procedimento e possibilidade de retomada não são os mesmos em toda hipótese.
E|A morte do titular autoriza transferir definitivamente o benefício a um familiar que não o requereu.|O benefício é pessoal; outro familiar precisa de direito próprio e procedimento adequado.
C|A análise de manutenção pode envolver atualização de informações familiares e cadastrais.|O requisito econômico não se limita à fotografia da data da concessão.
E|A revisão do benefício permite dispensar motivação e defesa do interessado em qualquer cancelamento.|O controle administrativo não afasta garantias do processo.
''')
add('16-08','loas','O auxílio-inclusão apoia o ingresso no trabalho da pessoa com deficiência moderada ou grave nas condições da LOAS.','Quem passa do BPC para trabalho enquadrado precisa verificar remuneração, cadastro e demais requisitos; o auxílio não é a soma livre do BPC com salário.','Auxílio-inclusão não é auxílio-acidente, salário-família nem aposentadoria da pessoa com deficiência.','O ingresso laboral e a remuneração devem ser avaliados junto com todos os demais requisitos legais.', '''
C|A LOAS prevê auxílio-inclusão para pessoa com deficiência moderada ou grave que satisfaça requisitos cumulativos.|A existência de deficiência, sozinha, não basta para a concessão.
E|O auxílio-inclusão equivale sempre ao valor integral do BPC.|Seu valor legal corresponde a metade do BPC em vigor.
C|A remuneração da atividade tem limite de dois salários mínimos na regra de acesso.|O limite remuneratório é um requisito específico, não renda média de contribuições.
E|Receber remuneração dentro do limite dispensa inscrição e atualização no CadÚnico.|As condições cadastrais também precisam ser cumpridas.
C|O exercício de atividade deve enquadrar o interessado como segurado obrigatório do RGPS ou filiado a RPPS, conforme a lei.|Não é qualquer receita eventual que satisfaz a condição laboral.
E|A pessoa pode receber simultaneamente o auxílio-inclusão e o BPC integral sem restrição.|A LOAS prevê incompatibilidade de percepção simultânea dessas prestações.
C|A lei admite situações de quem recebeu BPC nos cinco anos anteriores, observados os requisitos próprios.|A disciplina não se limita ao titular cujo BPC está ativo no exato dia do pedido.
E|O auxílio-inclusão é concedido apenas por completar 65 anos.|O benefício se vincula à deficiência e ao ingresso laboral nas condições legais.
C|A inscrição regular no CPF integra os requisitos legais do auxílio-inclusão.|O controle cadastral é parte da elegibilidade.
E|O auxílio-inclusão gera abono anual e pensão por morte nos mesmos moldes de aposentadoria.|A LOAS não lhe atribui esses efeitos previdenciários.
C|A manutenção exige observar a permanência das condições que justificam o auxílio.|A concessão não afasta verificação de requisitos posteriores.
E|Aposentadoria, pensão, benefício por incapacidade ou seguro-desemprego podem ser acumulados sem limites com o auxílio-inclusão.|A LOAS prevê incompatibilidades expressas com essas prestações.
''')
add('16-09','loas,bpc','A LOAS é a lei central; a Lei 14.176/2021 e o Decreto 6.214/2007 integram a disciplina assistencial em leitura atualizada.','Uma questão elaborada em 2021 deve ser confrontada com o texto vigente antes de ser aplicada como regra atual.','Norma regulamentar detalha a execução; não cria autorização para contrariar a lei.','As alterações posteriores a 2021 e 2022 precisam ser verificadas, em especial renda, cadastro e avaliação.', '''
C|A Lei 14.176/2021 inseriu disciplina do auxílio-inclusão na LOAS.|O auxílio não foi criado pelo regulamento do RGPS como aposentadoria.
E|A Lei 8.742/1993 é a lei de custeio do RGPS.|Ela organiza a assistência social; o custeio da seguridade tem como referência central a Lei 8.212.
C|O Decreto 6.214/2007 regulamenta o BPC previsto na LOAS.|Sua leitura deve ser compatível com leis e alterações posteriores.
E|O decreto pode aumentar por conta própria a idade legal do BPC para setenta anos.|A regulamentação não pode contrariar o critério fixado na lei.
C|É necessário distinguir o BPC do auxílio-inclusão ao estudar a LOAS.|Valor, hipótese e incompatibilidades não são idênticos.
E|Uma lei alteradora dispensa consultar o texto consolidado porque contém obrigatoriamente toda a LOAS.|Lei alteradora pode tratar apenas dos dispositivos modificados.
C|A data da questão pode explicar diferença entre gabarito histórico e regra atual.|A auditoria precisa preservar a história e ensinar a norma aplicável hoje.
E|A menção ao Decreto 6.214 no edital impede estudar qualquer lei posterior pertinente.|A preparação deve atualizar a base sem inventar alcance de edital novo.
C|Um regulamento deve ser interpretado em conjunto com a Constituição e a lei de fundamento.|A hierarquia normativa limita sua aplicação.
E|BPC e benefício previdenciário são intercambiáveis porque ambos podem ser operacionalizados pelo INSS.|O órgão operador não determina a natureza contributiva da prestação.
C|Requisitos, renda, avaliação e manutenção precisam ser examinados de forma articulada.|A mera leitura do valor do benefício não cobre sua disciplina.
E|Uma explicação sem indicar qual versão legal foi usada é sempre suficiente para resolver divergência temporal.|A controvérsia temporal exige fonte, redação e marco de aplicação.
''')
add('17-01','cf,p,comp','RGPS e RPPS são regimes distintos; o vínculo funcional precisa ser enquadrado conforme Constituição e lei.','Um ocupante apenas de cargo em comissão não integra RPPS somente por trabalhar em órgão público.','Servidor público é expressão ampla; titular de cargo efetivo e empregado público não são a mesma categoria previdenciária.','Vínculos simultâneos e situações especiais exigem análise própria; não presumir que um regime absorve todos os vínculos.', '''
C|O RGPS tem caráter contributivo e filiação obrigatória nas hipóteses constitucionais e legais.|Não é regime assistencial de adesão livre para toda atividade.
E|Todo trabalhador de órgão público está necessariamente vinculado a RPPS.|Há agentes sujeitos ao RGPS, como ocupantes exclusivamente de cargo em comissão e empregados públicos.
C|O RPPS previsto no art. 40 se dirige aos titulares de cargos efetivos, no seu âmbito legal.|O vínculo precisa ser compatível com o campo constitucional do regime.
E|BPC é uma aposentadoria concedida indistintamente por RGPS e RPPS.|É prestação assistencial de natureza distinta.
C|A contagem recíproca permite considerar tempo de um regime em outro sob condições legais.|Essa articulação não elimina a identidade de cada regime.
E|Migrar de vínculo torna automaticamente sem valor todo tempo contribuído no regime anterior.|O tempo pode ser aproveitado por contagem recíproca, observadas prova e vedações.
C|A compensação financeira cuida da relação entre regimes na contagem recíproca.|Não é uma segunda aposentadoria paga diretamente ao segurado.
E|Uma CTC converte o RGPS em um RPPS municipal.|A certidão comprova tempo; não transforma o regime emissor.
C|Emprego público e cargo efetivo exigem distinção para o enquadramento previdenciário.|O nome genérico de servidor não resolve o vínculo.
E|Dois vínculos simultâneos podem sempre ser somados em dobro dentro de uma única aposentadoria.|A contagem recíproca possui vedação de duplicidade e de concomitância para o mesmo cômputo.
C|A identificação do regime competente deve preceder a aplicação de regras de aposentadoria.|Aplicar regra do RGPS a qualquer servidor pode produzir erro de enquadramento.
E|A existência de RPPS dispensa contribuição de seus segurados em toda hipótese.|O regime do art. 40 é contributivo e solidário, conforme sua disciplina.
''')
add('17-02','ctc,p','A CTC comprova tempo destinado ao aproveitamento em outro regime, com os requisitos e limites pertinentes.','Um período no RGPS pode ser certificado para uso em RPPS; uma declaração informal não se torna CTC apenas por ter assinatura.','Certificar tempo não equivale a conceder aposentadoria nem a autorizar contagem duplicada.','Revisão, cancelamento e fracionamento dependem das regras e da existência de aproveitamento do tempo.', '''
C|A CTC tem função de comprovar tempo para contagem recíproca entre regimes.|Não se confunde com demonstrativo meramente informativo de cadastro.
E|O regime destinatário pode presumir qualquer tempo do RGPS sem a documentação de certificação exigível.|A prova da contagem recíproca segue disciplina legal própria.
C|A emissão da certidão não concede, por si, aposentadoria no regime de destino.|O instituidor ainda verifica os requisitos do benefício.
E|Qualquer período já usado em aposentadoria pode constar como tempo livre para novo aproveitamento.|A utilização anterior impede reaproveitamento incompatível.
C|A destinação do tempo deve ser observada para impedir uso duplicado.|O documento não autoriza a mesma parcela em múltiplas aposentadorias.
E|CTC e extrato CNIS têm obrigatoriamente a mesma finalidade e produzem efeitos idênticos.|CNIS é base cadastral; a CTC é instrumento formal específico de certificação.
C|A certificação pressupõe verificar períodos e dados que compõem o tempo declarado.|Não se deve transformar erro cadastral conhecido em tempo certificado sem correção.
E|A emissão da CTC obriga o destinatário a aceitar tempo fictício proibido pela Constituição.|A certidão não afasta vedações constitucionais e legais de contagem.
C|Uma retificação relevante pode exigir atuação do regime emissor.|O destinatário não altera livremente o conteúdo de uma certidão de outro regime.
E|A CTC é emitida pelo segurado em formulário próprio, sem intervenção do regime competente.|A emissão é ato do órgão/regime competente.
C|A simples mudança entre órgãos de um mesmo RPPS não é automaticamente contagem recíproca entre regimes.|É necessário distinguir regime previdenciário de órgão de lotação.
E|Solicitar CTC autoriza deixar de informar se o tempo já foi utilizado.|O histórico de aproveitamento é decisivo para evitar duplicidade.
''')
add('17-03','p,ctc,dcomp','A contagem recíproca une tempos válidos de regimes diferentes sem multiplicar o mesmo período.','Dez anos de atividade em um regime podem ser certificados ao outro; não se transformam em vinte por existir emprego simultâneo.','Soma de períodos sucessivos difere de duplicação de períodos concomitantes.','O aproveitamento observa as vedações do art. 96 da Lei 8.213 e a disciplina constitucional.', '''
C|É possível somar períodos não concomitantes de regimes distintos, cumpridos os requisitos legais.|Contagem recíproca é instrumento de aproveitamento, não garantia automática de benefício.
E|A contagem recíproca permite dobrar todo tempo trabalhado no serviço público.|Não há autorização geral para contagem em dobro.
C|Período já utilizado para conceder aposentadoria não pode ser reaproveitado de modo incompatível em outro regime.|A vedação impede que o mesmo tempo sustente duplicidade indevida.
E|Duas atividades exercidas no mesmo mês autorizam computar dois meses naquela mesma contagem recíproca.|Concomitância não multiplica o calendário para uma única aposentadoria.
C|A compensação financeira relaciona-se ao tempo efetivamente aproveitado pelo regime instituidor.|A existência de contribuições, isoladamente, não basta para todo fluxo de compensação.
E|A vedação de contagem duplicada proíbe sempre possuir vínculos em regimes diferentes.|Ter vínculos distintos não é a mesma coisa que duplicar tempo na mesma contagem.
C|O enquadramento temporal do período ajuda a avaliar sua certificação e uso.|A análise precisa considerar as normas pertinentes à situação.
E|O documento de certificação elimina a necessidade de analisar se os períodos se sobrepõem.|A prova formal não dispensa verificar concomitância e vedações.
C|O segurado não recebe diretamente a compensação como saldo de uma conta pessoal.|O mecanismo é uma relação financeira entre regimes.
E|A contagem recíproca equivale à devolução integral das contribuições ao trabalhador.|A finalidade é custear proporcionalmente a obrigação entre regimes, não ressarcir livremente o segurado.
C|O tempo averbado precisa ser compatível com as exigências do regime instituidor.|A averbação não é licença para afastar a legislação do benefício.
E|A mera vontade do interessado permite usar tempo fictício proibido para completar a carência.|A contagem precisa respeitar validade do período e requisitos distintos do benefício.
''')
add('17-04','p,ctc,dcomp','Evitar dupla utilização exige diferenciar concomitância, tempo fictício e tempo já consumido em benefício.','Um período certificado e usado em aposentadoria não pode ser novamente tratado como inteiramente disponível para outra.','Proibição de duplicar um período não significa apagar a existência dos vínculos laborais.','Casos de desaverbação e retificação dependem do uso efetivo e da norma aplicável, não de simples declaração do segurado.', '''
C|Períodos simultâneos demandam análise de sobreposição antes da soma para contagem recíproca.|Somar datas sem comparar calendários pode duplicar tempo.
E|Dois empregos de janeiro a dezembro do mesmo ano sempre equivalem a vinte e quatro meses para uma única contagem.|A concomitância não transforma um ano civil em dois.
C|Tempo fictício não pode ser criado por conveniência para completar o requisito de aposentadoria.|A contagem depende de previsão e limites constitucionais e legais.
E|A ausência de tempo suficiente autoriza o regime destinatário a arredondar cinco anos para dez.|Não existe arredondamento discricionário de tempo contributivo.
C|Saber se o período foi utilizado em benefício anterior é relevante na emissão e uso da CTC.|A informação evita reaproveitamento indevido.
E|O falecimento de um aposentado libera automaticamente todo seu tempo para aposentadoria de outro familiar.|Tempo de contribuição é vinculado à situação previdenciária do titular.
C|Períodos sucessivos podem ser somados sem que isso constitua concomitância.|É preciso distinguir sequência temporal de sobreposição.
E|Averbar um período transforma qualquer tempo privado em tempo público contado em dobro.|A natureza do registro não cria multiplicador geral.
C|A análise de um vínculo concomitante deve considerar se o tempo foi realmente aproveitado pelo instituidor.|O dado decisivo não é apenas a existência de contribuição em outro regime.
E|Uma certidão com erro material conhecido pode ser usada sem correção porque já foi impressa.|Erro no documento exige providência competente; a forma física não convalida o erro.
C|Reaproveitamento de tempo e restituição de contribuição são questões diferentes.|Uma vedação de contagem não cria automaticamente direito a saque de contribuições.
E|A compensação entre regimes autoriza ignorar a proibição de dupla contagem.|O mecanismo financeiro pressupõe contagem válida, não a substitui.
''')
add('17-05','comp,dcomp','Origem é o regime do tempo aproveitado; instituidor é o que concede e paga o benefício com esse tempo.','Se o RGPS concede aposentadoria usando tempo certificado de RPPS, o RGPS é instituidor nesse benefício.','A posição depende do benefício analisado, não de uma superioridade permanente de um regime.', 'Identificar corretamente o papel evita inverter crédito e obrigação na compensação.', '''
C|O regime que concede e paga aposentadoria com tempo de outro é o instituidor naquele benefício.|O conceito é funcional e vinculado ao caso concreto.
E|O INSS é sempre regime de origem, mesmo quando concede a aposentadoria.|O RGPS pode figurar como instituidor ou origem, conforme o aproveitamento do tempo.
C|O regime onde se formou o tempo aproveitado pode ocupar a posição de origem.|A origem é identificada pela vinculação contributiva utilizada, nos termos da lei.
E|O último órgão de lotação é necessariamente o regime instituidor.|Órgão de trabalho e regime previdenciário não são conceitos idênticos.
C|Uma pensão decorrente da aposentadoria pode integrar a disciplina de compensação pertinente.|A análise não deve confundir a pensão com uma nova CTC do dependente.
E|Regime de origem significa sempre o regime do local de nascimento do segurado.|Origem é conceito previdenciário ligado ao tempo e à vinculação, não à naturalidade.
C|O mesmo regime pode ocupar posições distintas em benefícios de pessoas diferentes.|Não há posição fixa de credor ou devedor para todos os casos.
E|A classificação como instituidor permite cobrar diretamente do segurado o repasse da compensação.|A compensação é relação entre regimes, conforme os critérios legais.
''')
add('17-06','comp,dcomp','A compensação previdenciária reparte encargos entre regimes quando há contagem recíproca válida.','Um RPPS que concede benefício usando tempo certificado do RGPS pode requerer compensação conforme as regras e dados exigidos.','Compensar regimes não é devolver contribuições em dinheiro ao aposentado.','A legislação define benefícios abrangidos, critérios, exclusões e procedimentos.', '''
C|A Lei 9.796/1999 é referência legal da compensação financeira na contagem recíproca.|A compensação não depende apenas de acordo verbal entre dirigentes.
E|O Decreto 10.188/2019 regulamenta exclusivamente pagamento do BPC.|Ele disciplina a compensação previdenciária na contagem recíproca.
C|O Decreto 10.188 contempla relações entre RGPS e RPPS e entre regimes próprios.|Não se deve restringir seu alcance apenas à União.
E|Qualquer contribuição em outro regime gera imediatamente transferência ao trabalhador.|É necessário benefício e aproveitamento do tempo nas condições da disciplina de compensação.
C|O tempo não concomitante efetivamente usado na aposentadoria é central para a compensação prevista no decreto.|A compensação não legitima tempo sobreposto ou não utilizado.
E|A compensação aumenta automaticamente o valor mensal do benefício já calculado, como bônus ao segurado.|O repasse entre regimes não é adicional remuneratório ao aposentado.
C|A conferência de dados do benefício e dos períodos contribui para a apuração do repasse devido.|A Lei 9.796 prevê informações e cálculo na relação entre regimes.
E|A falta de personalidade jurídica do RPPS elimina toda obrigação do ente federado na compensação.|A lei atribui ao ente direitos e obrigações quando o regime não possui personalidade própria.
''')
add('18-01','ec,cf','A EC 103 exige separar direito adquirido, regras de transição e regras destinadas a novos filiados.','Uma segurada filiada antes da reforma deve comparar as transições cabíveis; não basta aplicar a idade da regra de novo ingresso.','Preencher só idade, só pontos ou só tempo não significa cumprir todos os requisitos da regra escolhida.','Regras anuais devem identificar o ano. Os exemplos gerais não incluem automaticamente regras de professores, rurais ou servidores.', '''
C|O preenchimento de todos os requisitos antes da reforma pode preservar direito adquirido segundo a disciplina então aplicável.|O art. 3º da EC 103 protege o direito adquirido; isso difere de mera expectativa.
E|Quem já havia cumprido todos os requisitos perdeu automaticamente o direito com a publicação da EC 103.|A reforma não elimina o direito adquirido assegurado pelo seu art. 3º.
C|As regras de transição atendem situações de filiados anteriores à reforma, conforme cada hipótese.|O marco de filiação e os demais requisitos precisam ser conferidos.
E|Um segurado que ingressou no RGPS em 2026 pode escolher livremente qualquer transição criada para filiados anteriores a 2019.|Não se pode ignorar o campo pessoal e temporal da regra.
C|Na regra de pontos do art. 15, somam-se idade e tempo de contribuição, além de exigir tempo mínimo.|Pontuação e tempo mínimo são requisitos cumulativos.
E|Uma mulher com a pontuação exigida na regra geral do art. 15 dispensa os trinta anos de contribuição.|Atingir pontos não afasta o tempo mínimo de contribuição da regra.
C|A regra de pontos geral alcança progressivamente os limites de cem para mulheres e cento e cinco para homens.|A EC 103 prevê acréscimo anual até esses limites.
E|A pontuação permanece congelada em 86 e 96 para todos os anos posteriores à reforma.|Esses números são a referência inicial, sujeita à progressão legal.
C|Em 2026, a progressão geral do art. 15 corresponde a 93 pontos para mulheres e 103 para homens.|Parte-se de 86/96 em 2019 e acrescenta-se um ponto por ano a partir de 2020, respeitados os tetos.
E|Na transição geral da idade progressiva, o requisito etário é idêntico em todos os anos.|O art. 16 prevê aumento de seis meses por ano até os limites legais.
C|Em 2026, a idade progressiva geral do art. 16 é 59 anos e seis meses para mulheres e 64 anos e seis meses para homens.|A idade se soma à exigência de trinta ou trinta e cinco anos de contribuição.
E|Ter a idade progressiva requerida dispensa os demais requisitos contributivos do art. 16.|A idade é apenas uma das condições cumulativas.
C|O pedágio de cinquenta por cento considera o tempo que faltava no marco da reforma para completar o mínimo da regra.|Não corresponde a cinquenta por cento de toda a vida contributiva.
E|O pedágio de cinquenta por cento exige, como regra geral, as mesmas idades de 57 e 60 anos do pedágio de cem por cento.|As duas transições possuem requisitos diferentes; o art. 17 não traz essas idades mínimas gerais.
C|O pedágio de cem por cento do art. 20 exige idade mínima e tempo adicional, além do tempo contributivo da regra.|Não se resume a completar o pedágio.
E|O segurado pode ignorar o requisito de tempo na data da reforma exigido para ingressar no pedágio de cinquenta por cento.|O art. 17 delimita seu público com referência ao tempo superior a 28/33 anos no marco legal.
C|Para novos filiados sujeitos ao art. 19, a referência geral urbana é 62 anos e quinze de contribuição para mulheres, 65 e vinte para homens.|Essa regra não deve ser confundida com a transição do art. 18.
E|Todo homem já filiado antes da reforma passou a precisar de vinte anos na transição por idade do art. 18.|A transição do art. 18 preserva o requisito de quinze anos, observadas suas condições.
C|Na fórmula geral do art. 26, o coeficiente parte de sessenta por cento e admite acréscimos previstos na emenda.|Existem bases, marcos e exceções que precisam ser identificados antes do cálculo.
E|A EC 103 determinou coeficiente único de cem por cento para qualquer aposentadoria do RGPS.|A disciplina de cálculo varia conforme a espécie e a regra.
C|No cálculo geral, o acréscimo de dois pontos percentuais tem referência excedente de quinze anos para mulheres do RGPS e vinte para homens.|O tempo e a regra aplicável precisam ser indicados no caso concreto.
E|A regra geral da média pós-reforma exclui sempre os vinte por cento menores salários como no sistema anterior.|O art. 26 usa a média de cem por cento do período definido na emenda, sem essa exclusão automática geral.
C|O art. 24 disciplina hipóteses de acumulação e recebimento integral do benefício mais vantajoso com frações de outros.|É necessário identificar a hipótese e as faixas, não aplicar soma irrestrita.
E|A reforma proibiu sem exceção toda acumulação de pensão com aposentadoria.|Há hipóteses admitidas, com regras de cálculo e reduções.
C|A EC 103 preservou a disciplina da LC 142 para a aposentadoria da pessoa com deficiência do RGPS, enquanto não vier nova lei pertinente.|O art. 22 não autoriza tratá-la automaticamente como a aposentadoria programada comum.
E|Todo tempo especial exercido depois da reforma pode ser convertido em comum nas mesmas condições do tempo anterior.|O art. 25 diferencia períodos anteriores e posteriores ao marco da emenda.
C|O enquadramento de professor exige verificar exercício das funções de magistério e a regra específica.|A redução não alcança automaticamente qualquer empregado de escola.
E|A regra de um RPPS pode ser aplicada a segurado do RGPS apenas porque ambas tratam de aposentadoria.|Regime, vínculo, data e regra precisam ser compatíveis.
''')
add('18-02','lc,ec,r','A aposentadoria da LC 142 depende de deficiência reconhecida e distingue modalidade por tempo e por idade.','Um homem com deficiência grave precisa verificar o tempo qualificado e a carência; não basta comparar sua idade com a regra comum.','Deficiência, incapacidade laboral e exposição a agente nocivo são conceitos diferentes.','Exemplos presumem tempo na condição e carência; mudança do grau e períodos sem deficiência exigem ajustes regulamentares.', '''
C|A definição legal de deficiência envolve impedimentos de longo prazo em interação com barreiras.|A LC 142 não se restringe à incapacidade total de trabalhar.
E|A pessoa que continua trabalhando está automaticamente impedida de requerer aposentadoria pela LC 142.|Essa aposentadoria se destina a segurados com deficiência, não exige incapacidade laboral total.
C|Na modalidade por tempo, a deficiência grave tem referência de 25 anos para homem e vinte para mulher.|Além do tempo qualificado, é necessário observar carência e demais condições.
E|A deficiência grave exige trinta e três anos para homem e vinte e oito para mulher.|Esses tempos são da deficiência leve, não da grave.
C|Para deficiência moderada, os tempos legais são 29 anos para homem e 24 para mulher.|O grau altera a exigência contributiva na modalidade por tempo.
E|A deficiência moderada recebe exatamente os mesmos tempos da grave, sem distinção legal.|A LC 142 diferencia grave, moderada e leve.
C|Para deficiência leve, os tempos de referência são 33 anos para homem e 28 para mulher.|É preciso enquadramento do grau e do período correspondente.
E|O segurado escolhe livremente o grau que produz a aposentadoria mais rápida.|O grau depende da avaliação nos termos legais e regulamentares.
C|A modalidade por idade prevê sessenta anos para homem e cinquenta e cinco para mulher.|Exige também tempo mínimo e comprovação da deficiência pelo período legal.
E|Na aposentadoria por idade da LC 142, basta a idade e um único mês de deficiência comprovada.|A lei exige quinze anos de contribuição e comprovação da deficiência durante igual período.
C|O grau de deficiência não altera as idades de sessenta e cinquenta e cinco na modalidade por idade.|Isso não elimina os demais requisitos.
E|A aposentadoria por idade da pessoa com deficiência exige sempre grau grave.|A modalidade por idade independe do grau, observado o tempo na condição.
C|A avaliação da deficiência é médica e funcional conforme o regulamento.|Não basta autodeclaração de gravidade pelo requerente.
E|Um atestado particular obriga o INSS a aceitar qualquer grau indicado, sem avaliação própria.|A lei prevê aferição por instrumentos e avaliação próprios.
C|A data provável de início e a variação do grau podem importar para qualificar os períodos.|O mesmo grau não deve ser presumido para toda a vida contributiva.
E|Se a deficiência surgiu depois da filiação, nenhum período pode ser considerado para aposentadoria pela LC 142.|A lei e o regulamento disciplinam ajustes de períodos; não há essa exclusão absoluta.
C|A prova de deficiência anterior à vigência da lei não pode se basear exclusivamente em testemunhas.|A LC 142 estabelece limite probatório específico para esse período.
E|A prova exclusivamente testemunhal é suficiente em qualquer situação de deficiência anterior à lei.|A lei exige comprovação e veda exclusividade testemunhal nessa hipótese.
C|A LC 142 disciplina aposentadoria de segurado do RGPS.|Não é lei de concessão do BPC assistencial.
E|O titular da aposentadoria da LC 142 recebe necessariamente BPC cumulativo por ter deficiência.|A natureza previdenciária e a deficiência não afastam os requisitos e vedações do BPC.
C|Reduções da aposentadoria da pessoa com deficiência e de atividade especial não são livremente somadas sobre o mesmo período.|A lei limita a acumulação das reduções.
E|Um mês com deficiência e exposição nociva deve ser sempre contado em dobro por dois fundamentos.|Os regimes de redução exigem análise própria e não autorizam multiplicação automática.
C|O fator previdenciário só incide na disciplina da LC 142 quando produzir renda mensal mais elevada.|O art. 9º estabelece essa condição de aplicação.
E|O fator previdenciário precisa reduzir o benefício da LC 142 mesmo quando o resultado é desfavorável.|A lei não prevê aplicação prejudicial automática nesse regime.
C|A carência continua sendo requisito a observar, apesar da redução do tempo de contribuição.|Tempo qualificado e carência não são sinônimos.
E|Vinte anos de tempo qualificado dispensam automaticamente qualquer conferência de carência.|A contagem da carência tem regras próprias e precisa ser verificada.
C|A EC 103 remete à LC 142 para a pessoa com deficiência do RGPS até que nova lei discipline a matéria.|A referência constitucional preserva uma via própria de análise.
E|A deficiência leve autoriza reduzir as idades da modalidade por idade em dez anos adicionais.|A LC 142 não estabelece essa redução adicional pela classificação leve.
''')
add('18-03','c,cf','A Lei 8.212 organiza o custeio: sujeitos, bases, contribuições e responsabilidades precisam ser diferenciados.','Antes de calcular, identifique quem contribui, sobre qual base e qual alíquota pertence à categoria.','Salário de contribuição não é salário de benefício; contribuição de empresa não se confunde com contribuição descontada do segurado.','Alíquotas, limites monetários e regimes específicos exigem fonte e competência temporal. Não usar tabela sem ano.', '''
C|A Lei 8.212 é uma referência central da organização e do custeio da seguridade.|Ela não substitui a lei de benefícios na disciplina de cada prestação.
E|O custeio da seguridade provém exclusivamente da contribuição do trabalhador.|A Constituição e a lei preveem financiamento por toda a sociedade e diversas fontes.
C|O enquadramento na categoria de segurado influencia as regras de contribuição.|Não existe uma alíquota individual idêntica para toda pessoa e atividade.
E|Contribuinte individual e empregado são sempre tratados do mesmo modo na responsabilidade de recolher.|Categoria, contratação e hipóteses legais alteram responsabilidades.
C|A contribuição descontada do segurado não se torna contribuição patronal só por ser recolhida pela empresa.|Responsabilidade de repasse não altera a origem da parcela.
E|A existência de contribuição patronal dispensa necessariamente toda contribuição do empregado.|As obrigações são distintas e podem coexistir.
C|O salário de contribuição é base para a contribuição nos limites e condições legais.|Não se confunde com a renda mensal do benefício.
E|Toda quantia recebida pelo trabalhador integra a base, sem qualquer exclusão legal.|O art. 28 contempla parcelas integrantes e exclusões com requisitos.
C|A exclusão de parcela deve respeitar as condições legais da hipótese.|Dar nome de indenização a uma verba não resolve sozinho sua natureza.
E|A empresa pode criar por contrato privado nova isenção de contribuição, válida contra o fisco.|Benefícios e exclusões tributárias dependem de fundamento normativo competente.
C|O teto do salário de contribuição do segurado não deve ser automaticamente transportado a qualquer contribuição empresarial.|As bases empresariais possuem disciplina própria.
E|A soma de dois vínculos permite ao segurado ignorar a existência do limite máximo aplicável a sua base.|Atividades concomitantes exigem análise do teto e dos recolhimentos.
C|A contribuição abaixo do mínimo pode demandar ajuste para cômputo conforme a disciplina pós-reforma.|Não basta presumir que qualquer recolhimento produz todos os efeitos.
E|Completar uma contribuição equivale automaticamente a receber de volta todo o valor pago anteriormente.|Complementação é ajuste contributivo, não restituição geral.
C|Empresa e equiparados a empresa podem ter obrigações previstas na Lei 8.212.|O conceito previdenciário não se limita à sociedade comercial com fins lucrativos.
E|Órgãos públicos ficam necessariamente fora do conceito previdenciário de empresa para todo efeito de custeio.|A lei possui conceito e equiparações que não autorizam essa exclusão geral.
C|O prazo de recolhimento deve ser identificado pelo sujeito e pela obrigação.|Uma data única para todas as categorias seria generalização indevida.
E|Entregar informação cadastral sempre substitui o pagamento de toda contribuição devida.|Obrigação de informar e obrigação de pagar são distintas.
C|O financiamento inclui contribuições de empresas e receitas previstas constitucionalmente.|Diversidade de bases é uma característica do sistema.
E|A contribuição devida pode ser afastada apenas porque o segurado não utilizou serviço do INSS no mês.|O financiamento não é preço individual por atendimento mensal.
C|A situação do produtor rural exige observar a disciplina específica de contribuição e responsabilidade.|Não se deve importar sem análise a regra de uma empresa urbana comum.
E|A imunidade de contribuição pode ser presumida por mera declaração de finalidade social da entidade.|As condições constitucionais e legais precisam ser verificadas.
C|A competência temporal da tabela é relevante para calcular corretamente o recolhimento.|Limites e valores podem ser atualizados e não devem ser usados fora do período.
E|Uma tabela de 2022 necessariamente mantém todos os valores monetários corretos em 2026.|A atualização deve ser conferida na fonte oficial do período.
''')
add('18-04','p,cf','A Lei 8.213 reúne regras de beneficiários, prestações, requisitos, cálculo, prova e manutenção.','Um dependente que pede pensão precisa verificar sua classe e os requisitos da prestação; não basta o segurado ter contribuído uma vez.','Qualidade, carência, tempo de contribuição e dependência são requisitos distintos.','Leitura atual deve incorporar Constituição, EC 103 e alterações posteriores; a redação original de 1991 não é o texto vigente integral.', '''
C|Segurados e dependentes compõem as categorias de beneficiários previstas na Lei 8.213.|As posições jurídicas e prestações acessíveis não são idênticas.
E|Todo dependente é, por essa condição, segurado obrigatório do RGPS.|Dependência e filiação são vínculos diferentes.
C|Benefícios e serviços integram o plano de prestações previdenciárias.|Serviço social e reabilitação não se confundem com renda mensal de aposentadoria.
E|Qualquer serviço previdenciário exige que se calcule previamente salário de benefício.|Serviços não são todos benefícios financeiros calculados por média.
C|A carência mede contribuições mensais exigidas conforme a disciplina da prestação.|Ela não corresponde simplesmente à idade do segurado.
E|Qualidade de segurado, carência e tempo de contribuição são expressões sempre equivalentes.|Cada instituto tem função e regras próprias.
C|A perda da qualidade exige análise específica de seus efeitos sobre o benefício pretendido.|Não se presume que toda prestação usa a mesma regra.
E|Perder a qualidade apaga necessariamente todos os registros contributivos do CNIS.|Perda da condição não destrói a história contributiva.
C|O enquadramento de dependentes precisa observar a classe e a prova exigida pela lei.|Parentesco, por si, não resolve toda hipótese.
E|Toda pessoa economicamente ajudada pelo segurado integra automaticamente o rol de dependentes.|A lei estabelece categorias e condições específicas.
C|O salário de benefício e a renda mensal são etapas conceituais distintas do cálculo.|Uma é base de cálculo; a outra resulta da regra aplicável à prestação.
E|A renda mensal de toda prestação é sempre igual ao total do último salário de contribuição.|Regras de base, coeficiente e limites variam por benefício.
C|O CNIS fornece informações relevantes, mas admite atualização e retificação conforme a lei.|O cadastro não é imune à prova e à correção.
E|A ausência de vínculo no CNIS autoriza negar todo pedido sem possibilidade de outra prova.|A legislação admite prova e acerto de informações nas condições próprias.
C|A manutenção de benefício depende da natureza da prestação e das condições legais pertinentes.|Não há uma regra única de cessação para todas as espécies.
E|Pensão por morte e auxílio por incapacidade temporária têm obrigatoriamente os mesmos requisitos pessoais.|As contingências, titulares e pressupostos são distintos.
C|As regras de contagem recíproca da lei precisam respeitar vedações de dupla utilização.|A soma não pode criar tempo inexistente.
E|O regime de recursos dispensa motivação da decisão inicial de indeferimento.|O controle recursal não elimina a exigência de decisão fundamentada.
C|Direito adquirido pode exigir a análise do marco em que todos os requisitos foram completados.|A data do pedido, sozinha, não encerra toda questão temporal.
E|A lei original de 1991 pode ser aplicada sem considerar nenhuma emenda ou alteração posterior.|O estudo exige texto consolidado e vigência das mudanças.
C|Acidente do trabalho, carência e espécies de incapacidade devem ser diferenciados na análise do caso.|A ocorrência de acidente não uniformiza automaticamente todas as prestações.
E|A existência de contribuição garante qualquer benefício, mesmo sem ocorrência do fato protegido.|Contribuição é parte do sistema; o direito depende dos requisitos da espécie.
C|Decadência da revisão e prescrição de parcelas são institutos que exigem distinção.|Objeto, marcos e hipóteses não podem ser confundidos.
E|Um gabarito antigo dispensa conferir mudanças normativas na aplicação atual da Lei 8.213.|A auditoria deve verificar se o fundamento histórico continua aplicável.
''')
add('18-05','r,p,c','O Decreto 3.048 aprova o Regulamento da Previdência Social e detalha a execução das normas legais.','Ao ler um artigo, confira redação vigente e vínculo com a lei; o número do decreto é de 1999, mas o texto sofreu mudanças.','Regulamentar não equivale a legislar contra a Constituição nem a substituir o controle de legalidade.','Texto compilado contém referências históricas e alterações; trecho revogado não deve ser ensinado como atual.', '''
C|O Decreto 3.048 aprova o Regulamento da Previdência Social.|Seu conteúdo deve ser lido conforme leis e Constituição.
E|Por ser posterior às Leis 8.212 e 8.213, o decreto pode revogá-las livremente.|A hierarquia impede que regulamento contrarie lei por mera posterioridade.
C|O regulamento trata de enquadramento de segurados e procedimentos previdenciários.|Ele não é apenas uma tabela de valores anuais.
E|O número 3.048 significa que todos os seus artigos permanecem com a redação original de 1999.|O decreto sofreu alterações; o texto consolidado identifica redações pertinentes.
C|Filiação do obrigatório e inscrição cadastral possuem conceitos distintos no regulamento.|Vínculo jurídico e ato de cadastro não devem ser confundidos.
E|No regulamento, o exercício de atividade remunerada obrigatória depende sempre de escolha livre de filiação.|A obrigatoriedade decorre do enquadramento legal da atividade.
C|O segurado facultativo requer tratamento próprio quanto à filiação e ao primeiro recolhimento válido.|Não se transporta automaticamente a regra do empregado.
E|Facultativo pode retroagir livremente sua filiação a qualquer idade apenas pagando uma guia.|Há condições e limites para filiação e recolhimento.
C|O período de graça permite manutenção da qualidade nas hipóteses do regulamento e da lei.|Manter qualidade não cria automaticamente contribuição mensal nova.
E|Todo segurado tem exatamente o mesmo período de graça, sem hipótese de diferença.|A duração varia conforme a situação e os requisitos de prorrogação.
C|As informações cadastrais do CNIS servem à prova e ao cálculo, conforme a disciplina previdenciária.|O uso do cadastro não elimina possibilidade legal de acerto.
E|Um registro extemporâneo é sempre suficiente, sem qualquer verificação adicional.|O regulamento permite exigir comprovação em hipóteses de inconsistência ou extemporaneidade.
C|O regulamento contém regras para apresentação e análise de documentos.|O processo não se reduz à leitura de uma tela cadastral.
E|Documento material válido pode ser ignorado em qualquer hipótese porque o sistema não o incorporou automaticamente.|A análise deve observar os meios de prova admitidos e eventual necessidade de acerto.
C|Atividades concomitantes exigem análise de regras de enquadramento e de contribuição.|Uma atividade não apaga necessariamente a outra.
E|Regras de contribuição do facultativo podem ser aplicadas indistintamente a empregador doméstico.|São sujeitos e obrigações diferentes.
C|O estudo de benefícios precisa articular o decreto com a disciplina constitucional pós-reforma.|O regulamento não se interpreta isolado de norma superior.
E|Uma instrução normativa pode autorizar o servidor a desconsiderar o decreto e a lei quando for mais conveniente.|A atuação administrativa deve respeitar hierarquia e legalidade.
C|Um artigo com redação revogada pode ser relevante para entender uma questão histórica.|É preciso explicitar que não se trata automaticamente da regra atual.
E|A consulta a uma compilação dispensa conferir a vigência temporal da redação que aparece na página.|Compilações podem exibir marcas históricas e redações distintas.
C|A categoria previdenciária deve ser identificada pelos fatos e requisitos normativos.|O título de um contrato não resolve sozinho o enquadramento.
E|O regulamento transforma todo trabalho rural em atividade de segurado especial.|A categoria depende de requisitos próprios.
C|Salário de contribuição, carência e período de graça pertencem a funções diferentes na análise.|Separá-los evita concluir por um benefício usando requisito de outro instituto.
E|A aprovação do regulamento eliminou a aplicação da Constituição aos benefícios do RGPS.|A Constituição permanece como norma superior e fundamento do sistema.
''')
add('18-06','in,r,p','A IN 128 organiza regras, procedimentos e rotinas do INSS; deve ser usada em versão atualizada e subordinada às normas superiores.','O índice oficial registra alterações até a IN 212/2026; conferir apenas uma impressão de março de 2022 pode ocultar mudanças.','A norma operacional orienta o processamento, mas não altera por si a Constituição ou a lei.','Esta aula não afirma que cada dispositivo da IN foi auditado integralmente: artigos específicos requerem consulta ao consolidado e ao ato alterador.', '''
C|A IN PRES/INSS 128/2022 disciplina rotinas administrativas de aplicação das normas previdenciárias.|Seu papel operacional não a coloca acima das leis.
E|A IN 128 pode contrariar a Constituição por ser uma norma específica do INSS.|Especialidade administrativa não afasta a hierarquia constitucional.
C|A identificação da versão é relevante porque a IN 128 recebeu alterações após 2022.|O índice oficial registra atos de 2023, 2024, 2025 e 2026.
E|A publicação de uma alteração em 2026 prova que todos os artigos da IN original foram revogados.|O alcance de cada ato depende dos dispositivos que ele efetivamente modifica.
C|A IN 212, de agosto de 2026, consta no índice oficial como ato alterador da IN 128.|Isso exige atenção à compilação usada no estudo.
E|Um manual que reproduz apenas a redação original de 2022 está necessariamente atualizado para outubro de 2026.|As alterações posteriores precisam ser incorporadas ou ressalvadas.
C|A análise administrativa deve combinar fatos, documentos e enquadramento normativo.|Uma lista de documentos não substitui identificar o direito pretendido.
E|O servidor pode criar carência nova por orientação interna sem fundamento legal.|Requisito material do benefício precisa de base normativa competente.
C|Uma referência a anexo da IN deve ser conferida para verificar se o formulário ou a regra foi alterado.|Anexos também podem sofrer alterações e revogações.
E|Todo formulário anexado em 2022 permanece obrigatório exatamente como foi publicado.|É necessário verificar a versão e eventual substituição ou revogação.
C|O direito de apresentar documentação deve ser exercido pelos meios e na forma admitidos no procedimento.|A análise não se limita a dados já visíveis em consulta automática.
E|Uma inconsistência cadastral pode ser resolvida alterando dados sem deixar rastreabilidade no processo.|Acertos devem obedecer a prova, competência e registro adequados.
C|A exigência administrativa deve indicar o que precisa ser esclarecido ou comprovado.|Clareza da exigência favorece defesa e instrução adequadas.
E|Uma exigência genérica permite indeferir sem explicar qual documento ou requisito faltou.|A atuação deve ser motivada e adequada à instrução do caso.
C|A aplicação da IN deve respeitar o marco temporal relevante do benefício.|Não se usa qualquer redação recente para todos os fatos antigos.
E|Atualizar um procedimento autoriza alterar silenciosamente o gabarito histórico de uma prova.|O fundamento histórico e a disciplina atual devem ser registrados separadamente.
C|Uma lei nova pode exigir revisão da interpretação de norma operacional anterior.|A norma subordinada deve permanecer compatível com a superior.
E|A ausência de atualização de uma apostila faz prevalecer a apostila sobre o texto oficial.|O material didático não é fonte superior à legislação.
C|A competência do agente e a etapa do procedimento importam para saber quem pode praticar cada ato.|Não basta conhecer o conteúdo material do benefício.
E|Qualquer usuário do sistema pode alterar decisão ou registro sem atribuição funcional.|A atuação depende de competência e controles administrativos.
C|Uma fonte marcada como não verificada não deve ser apresentada como pesquisa atual concluída.|Transparência de origem e data é parte da qualidade do conteúdo.
E|Citar o número da IN é suficiente para provar qualquer requisito inventado sobre benefício.|A fundamentação precisa localizar a disposição efetivamente pertinente.
C|Mudanças de rotina devem preservar os registros das decisões já tomadas e sua base temporal.|Rastreabilidade evita reescrita silenciosa do histórico.
E|Toda divergência entre lei e instrução deve ser resolvida ignorando a lei.|Norma infralegal não afasta a norma superior.
''')
add('18-07','p,r,in,cnis','O CNIS reúne informações previdenciárias e admite acertos fundamentados; dado cadastral não se confunde com prova imutável.','Um vínculo ausente pode exigir documentos e análise; a ausência não significa automaticamente que nunca houve trabalho.','Cadastro, prova do vínculo, remuneração, contribuição e CTC são informações e instrumentos relacionados, mas diferentes.','Indicadores, extemporaneidade e categorias exigem regras próprias. Não prometer reconhecimento automático de documento.', '''
C|O CNIS contém dados de vínculos, remunerações e contribuições relevantes ao direito previdenciário.|Os dados auxiliam o reconhecimento e o cálculo conforme as regras aplicáveis.
E|O CNIS é um benefício assistencial pago a quem não tem renda.|É cadastro de informações sociais, não uma prestação monetária.
C|A Lei 8.213 admite inclusão, exclusão e retificação de informações do CNIS mediante comprovação pertinente.|O cadastro não é juridicamente imutável.
E|O segurado está proibido de solicitar acerto antes de requerer aposentadoria.|A lei admite solicitação de acertos a qualquer momento, observada a prova.
C|Vínculo não exibido exige analisar a possibilidade de comprovação e atualização.|Ausência de registro não equivale necessariamente à inexistência do fato.
E|Se um contrato não aparece no extrato, nenhum documento pode ser apresentado para analisá-lo.|Há meios de prova e procedimentos de acerto legalmente admitidos.
C|Informação extemporânea pode exigir comprovação adicional.|O tratamento de dados lançados fora de prazo não é igual à aceitação acrítica de qualquer declaração.
E|Um lançamento extemporâneo torna sempre impossível reconhecer tempo, mesmo com prova válida.|A necessidade de prova não é uma proibição absoluta de reconhecimento.
C|A remuneração registrada pode influenciar a base de cálculo do benefício.|Dados financeiros incorretos podem exigir retificação fundamentada.
E|Registrar corretamente o vínculo dispensa toda conferência de remunerações em qualquer cálculo.|Tempo e valores são dimensões diferentes da informação previdenciária.
C|Documentos precisam ser coerentes com o período e a situação que se pretende demonstrar.|O simples número de páginas não garante suficiência probatória.
E|Uma declaração produzida sem base documental obriga o INSS a aceitar qualquer salário informado.|A informação precisa atender à disciplina de comprovação.
C|O eSocial pode alimentar informações trabalhistas e previdenciárias, sujeitas à conferência de consistência.|Integração eletrônica não elimina a necessidade de acerto quando há erro.
E|O recibo de transmissão de um arquivo garante que todos os fatos declarados são verdadeiros.|Comprovante de envio não equivale à validação material de todo conteúdo.
C|A existência de indicador cadastral deve levar à análise de seu significado e dos documentos pertinentes.|Não se deve interpretar todo indicador como prova definitiva de inexistência de direito.
E|Qualquer indicador no CNIS autoriza cancelar o pedido sem análise ou motivação.|A decisão precisa observar o procedimento e o fundamento aplicável.
C|O extrato pode ser usado pelo segurado para identificar lacunas e divergências antes do requerimento.|Conferência prévia ajuda a organizar a prova.
E|O extrato CNIS substitui obrigatoriamente a CTC em toda contagem recíproca.|A CTC tem finalidade formal própria entre regimes.
C|O cadastro pode registrar contribuições que exigem análise de validade para efeitos específicos.|Lançamento não resolve sozinho carência, categoria e mínimo contributivo.
E|Toda contribuição que aparece no extrato satisfaz automaticamente qualquer requisito de qualquer benefício.|Os efeitos dependem das normas de cada instituto e da regularidade do recolhimento.
C|A correção administrativa deve preservar a documentação e a rastreabilidade do acerto.|Não é autorização para apagar a origem dos dados.
E|O atendente pode completar salários por estimativa pessoal quando falta informação.|Valores devem ser tratados conforme prova e regras legais, não por palpite.
C|A prova contemporânea pode ser relevante para confirmar informações referentes ao período alegado.|A análise probatória deve considerar os critérios previstos para o fato e a categoria.
E|CNIS, qualidade de segurado e salário de benefício são o mesmo conceito.|Um é cadastro; os demais são condição de proteção e base de cálculo, com funções diferentes.
''')
add('19-01','atend,cf','O servidor promove acesso a direitos por atendimento legal, claro, respeitoso e acessível.','Uma orientação deve explicar requisito, canal e documento necessário, sem prometer concessão que dependa de análise.','Orientar não é favorecer conhecido nem conceder benefício sem requisitos.','A atuação social do servidor não amplia sua competência nem permite expor dados pessoais sem fundamento.', '''
C|Informação clara sobre requisitos e canais pode reduzir barreiras de acesso a direitos.|A qualidade do atendimento inclui orientação compreensível ao usuário.
E|Atender bem autoriza dispensar requisitos legais para qualquer pessoa em dificuldade.|Acolhimento deve coexistir com legalidade e competência.
C|O tratamento deve respeitar dignidade e igualdade, sem discriminação arbitrária.|Impessoalidade não é indiferença à acessibilidade ou às necessidades do usuário.
E|O servidor pode priorizar amigo por vínculo pessoal, sem base legal, como ação de desenvolvimento social.|O favorecimento pessoal viola a impessoalidade.
C|Encaminhar corretamente uma demanda fora da competência do órgão pode integrar um atendimento adequado.|O servidor deve evitar promessas indevidas e orientar para o serviço competente.
E|O usuário precisa dominar linguagem jurídica para merecer explicação sobre seu pedido.|O dever de informação demanda linguagem clara e adequada.
C|Preservar informações pessoais é compatível com a orientação e a transparência do serviço.|Transparência não implica divulgação irrestrita de dados do cidadão.
E|O agente pode inventar notícia de concessão para motivar quem procura atendimento.|Informação deve ser verdadeira e verificável, sem promessa fictícia.
''')
add('19-02','saude','A atenção à saúde do servidor envolve assistência, perícia oficial, promoção, prevenção e acompanhamento.','Detectar fatores de adoecimento no ambiente exige ações individuais e coletivas, não apenas aguardar afastamentos.','Perícia oficial avalia capacidade para funções; assistência e promoção possuem finalidades distintas.','O Decreto 6.833 mantém os conceitos de seus arts. 1º a 3º; seu comitê do art. 4º foi revogado e não deve ser ensinado como vigente.', '''
C|O SIASS busca coordenar e integrar ações de saúde dos servidores federais em seu âmbito.|Sua finalidade envolve mais que homologar afastamentos.
E|Promoção da saúde se limita obrigatoriamente a tratar doença depois do afastamento.|A atuação inclui prevenção e intervenção sobre o processo de adoecimento.
C|A perícia oficial pode ter natureza médica ou odontológica para avaliar o estado de saúde relacionado ao trabalho.|Não se confunde com toda forma de atendimento assistencial.
E|Assistência à saúde e perícia oficial são expressões de conteúdo idêntico no Decreto 6.833.|O decreto as define separadamente.
C|A promoção e prevenção podem atuar tanto na dimensão individual quanto nas relações coletivas do ambiente de trabalho.|A atenção à saúde não se limita ao indivíduo isolado.
E|A reabilitação da saúde fica necessariamente fora do conceito de assistência do SIASS.|O art. 3º inclui a reabilitação no campo assistencial.
C|Prevenção, detecção precoce e tratamento integram a definição de assistência à saúde do servidor.|O conceito considera diferentes fases do cuidado.
E|O comitê originalmente previsto no art. 4º deve ser tratado como vigente sem considerar a revogação de 2019.|O Decreto 10.087/2019 revogou esse dispositivo; a auditoria precisa distinguir partes vigentes e históricas.
''')

def main():
 manifest=json.loads(PLAN.read_text())
 targets=[r for r in manifest['assuntos'] if r['disciplina']=='Previdenciário e legislação social' and 15<=int(r['id_planejamento'].split('-B')[1][:2])<=19]
 lessons=[]
 for r in targets:
  pid=r['id_planejamento'];key=pid[6:].replace('B','').replace('S','')
  # PREV-B15-S01 -> 15-01
  key=pid.split('-B')[1].replace('-S','-')
  item=DATA[key]; records=item['records']; n=r['meta_questoes_autorais']
  assert len(records)==n,(pid,len(records),n)
  lid='v17-'+pid.lower()
  sources=[{**SOURCES[s],'checkedAt':DATE} for s in item['src']]
  questions=[]
  # Deterministic ordering avoids C/E alternation becoming a response cue.
  order=sorted(range(n),key=lambda i:hashlib_sha(lid+str(i)))
  for qi,idx in enumerate(order,1):
   q=records[idx]
   questions.append({**q,'id':f'{lid}-q{qi:03d}','kind':'autoral','version':1,'difficulty':'basico' if idx<n//3 else 'intermediario' if idx<4*n//5 else 'avancado','family':f'{pid.lower()}-aspecto-{idx+1:02d}','microtopic':pid,'sourceRef':sources[0],'mode':'reserva' if qi%4==0 else 'fixacao' if qi%4==1 else 'treino','editorialStatus':'revisao-editorial-ia','reviewedAt':DATE})
  # Explanations are authored independently. Their affirmative legal points also form the taught theory.
  rule=item['core']+' '+ ' '.join(dict.fromkeys(q['explanation'] for q in records))
  legacy_source='b' if pid.startswith('PREV-B16') else 'cf' if pid in ['PREV-B18-S01','PREV-B19-S01'] else 'c' if pid=='PREV-B18-S03' else 'r' if pid=='PREV-B18-S05' else 'p'
  lessons.append({'id':lid,'d':'prev','title':r['assunto'],'core':item['core'],'rule':rule,'example':item['example'],'contrast':item['contrast'],'limit':item['limit'],'source':legacy_source,'sources':sources,'minutes':40,'block':r['bloco'],'planId':pid,'subtopics':list(dict.fromkeys(q['explanation'] for q in records)),'questions':questions,'version':1,'contentVersion':2,'status':'pendente','editorialStatus':'revisao-editorial-ia','updatedAt':DATE})
 allq=[q for l in lessons for q in l['questions']]
 norm=lambda s:re.sub(r'\s+',' ',s.strip().casefold())
 assert len(lessons)==28 and len(allq)==424
 assert len({q['id'] for q in allq})==424
 assert len({norm(q['text']) for q in allq})==424
 assert all(type(q['answer']) is bool for q in allq)
 assert all(len(q['text'])>35 and len(q['explanation'])>30 for q in allq)
 out={'lessons':lessons,'sources':[{**v,'checkedAt':DATE} for v in SOURCES.values()],'editorial':{'author':'JARVIS — elaboração própria','date':DATE,'method':'v1.7 Cara a Cara com a Banca','questionCount':len(allq),'lessonCount':len(lessons),'status':'revisão editorial por IA com validação estrutural; sem revisão jurídica humana independente','generation':'424 enunciados escritos individualmente; Python organiza e valida, sem multiplicar nomes ou modelos','limitations':['Não representa auditoria integral de toda a legislação até 27/10/2026.','Atos posteriores e jurisprudência podem exigir nova revisão; valores anuais não foram presumidos.','IN 128: índice oficial de alterações conferido; não houve leitura integral de cada ato alterador.','Prazos específicos atuais de Seguro-Defeso não foram congelados; fonte MTE de outubro/2026 informa alteração.','Fontes Planalto tiveram bloqueios intermitentes; foram consultados texto consolidado acessível, índices e fontes oficiais alternativas.']}}
 path=ROOT/'data/prev-especiais.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'file':str(path),'lessons':28,'questions':424,'textos_unicos':len({norm(q['text']) for q in allq}),'modes':dict(collections.Counter(q['mode'] for q in allq))},ensure_ascii=False))

def hashlib_sha(s):
 import hashlib
 return hashlib.sha256(s.encode()).hexdigest()
if __name__=='__main__':main()
