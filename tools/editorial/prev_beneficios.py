"""Assets autorais B08–B14. Sem cópia de enunciados oficiais ou aumento por nomes.
Executar da raiz do repositório: python3 tools/editorial/prev_beneficios.py.
As linhas são itens escritos individualmente; Python monta metadados e valida quotas.
"""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[2]
DATA={}
SOURCES={
'p':{'title':'Lei 8.213/1991 — Câmara dos Deputados, texto atualizado','url':'https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html'},
'cp':{'title':'Código Penal — Câmara, texto atualizado inclusive LC225/2026','url':'https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html'},
'crps':{'title':'INSS — recurso administrativo e dúvidas frequentes','url':'https://www.gov.br/inss/pt-br/direitos-e-deveres/recurso/duvidas-frequentes'},
'r':{'title':'Regulamento da Previdência Social — Câmara, texto atualizado','url':'https://www2.camara.leg.br/legin/fed/decret/1999/decreto-3048-6-maio-1999-368532-normaatualizada-pe.html'},
'ec':{'title':'Emenda Constitucional103/2019 — Câmara dos Deputados','url':'https://www2.camara.leg.br/legin/fed/emecon/2019/emendaconstitucional-103-12-novembro-2019-789412-publicacaooriginal-159409-pl.html'},
'ctn':{'title':'Código Tributário Nacional — Câmara, texto atualizado','url':'https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html'},
'l10666':{'title':'Lei10.666/2003 — Câmara, texto atualizado','url':'https://www2.camara.leg.br/legin/fed/lei/2003/lei-10666-8-maio-2003-496649-normaatualizada-pl.html'},
'stf':{'title':'STF — ADI6096: decadência não alcança indeferimento, cancelamento ou cessação','url':'https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=453347'},
'mat':{'title':'INSS — Salário-Maternidade, aplicação das ADIs 2110/2111 e IN188/2025','url':'https://www.gov.br/inss/pt-br/direitos-e-deveres/salario-maternidade/salario-maternidade'},
'tal':{'title':'Lei7.070/1982 — Câmara, texto atualizado — Síndrome da Talidomida','url':'https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7070-20-dezembro-1982-356744-normaatualizada-pl.html'},
'ser':{'title':'Lei 7.986/1989 — seringueiros','url':'https://www.planalto.gov.br/ccivil_03/leis/l7986.htm'},
'exc':{'title':'Lei 8.059/1990 — ex-combatentes','url':'https://www.planalto.gov.br/ccivil_03/leis/l8059.htm'},
'car':{'title':'Lei 9.422/1996 — hemodiálise de Caruaru','url':'https://www.planalto.gov.br/ccivil_03/leis/l9422.htm'},
'ces':{'title':'Lei 9.425/1996 — Césio-137','url':'https://www.planalto.gov.br/ccivil_03/leis/l9425.htm'},
'ani':{'title':'Lei 10.559/2002 — anistiado político','url':'https://www.planalto.gov.br/ccivil_03/leis/2002/l10559.htm'},
'han':{'title':'Lei 11.520/2007 atualizada pela Lei14.736/2023','url':'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11520.htm'},
'hanfaq':{'title':'MDHC — perguntas frequentes de hanseníase, Decreto12.312/2024','url':'https://www.gov.br/mdh/pt-br/navegue-por-temas/pessoa-com-deficiencia/acoes-e-programas/hanseniase/perguntas-frequentes'},
'zik':{'title':'Lei 15.156/2025 — proteção à pessoa com deficiência associada ao Zika','url':'https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15156.htm'},
'zikh':{'title':'Lei 13.985/2020 — referência histórica do edital2022','url':'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l13985.htm'},
'lc225':{'title':'LC225/2026,art.49 — devedor contumaz e efeitos penais','url':'https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-225-8-janeiro-2026-798639-publicacaooriginal-177736-pl.html'},
}
def add(code,source,locator,core,example,lines,extra=None):
    qs=[]
    for line in lines.strip().splitlines():
        if not line.strip():continue
        sign,text,explanation=line.split('|',2)
        assert sign in '+-'
        def typography(value):
            value=re.sub(r'\b(Lei|Decreto|IN|EC|ADI|ADIs|LC|art\.|arts\.|R\$)(?=\d)',r'\1 ',value)
            value=re.sub(r'\b(em|de)(?=\d)',r'\1 ',value)
            return value.strip()
        qs.append({'text':typography(text),'answer':sign=='+','explanation':typography(explanation)})
    DATA['PREV-'+code]=(source,locator,core,example,qs,extra or [])

add('B08-S01','p','art.103; STF ADI6096','Decadência de revisão do ato concessório não se confunde com prazo para pedir benefício inicialmente.','Compare uma aposentadoria concedida há anos com um requerimento inicial nunca formulado.',r'''
+|A revisão do ato de concessão pode submeter-se à decadência decenal.|O art.103 estabelece dez anos para revisão do ato concessório, observados os marcos legais.
-|A simples passagem de dez anos sem requerer aposentadoria extingue necessariamente o direito ao benefício inicial.|O prazo de revisão não se confunde com o direito à concessão inicial quando preenchidos os requisitos.
+|No estudo da decadência, é necessário identificar se houve ato de concessão a revisar.|O objeto do pedido distingue revisão de benefício e concessão inicial.
-|A decadência de revisão tem prazo geral de cinco anos.|O prazo de revisão do ato concessório é decenal; cinco anos é referência distinta de prescrição de prestações.
+|O primeiro dia do mês seguinte ao recebimento da primeira prestação é marco legal relevante para a revisão concessória.|Esse é um dos marcos previstos no art.103.
-|Cada reajuste anual reinicia automaticamente o prazo decadencial de toda revisão da concessão.|O marco do ato concessório não se renova simplesmente por cada reajuste.
+|A data da primeira prestação deve ser distinguida da data de uma nova petição revisional.|Pedidos sucessivos não autorizam presumir reinício ilimitado do prazo original.
-|Decadência de revisão e prescrição das parcelas são o mesmo instituto com nomes diferentes.|A primeira limita a revisão do ato; a segunda alcança prestações exigíveis no tempo.
+|Uma revisão pode exigir análise simultânea de decadência e parcelas prescritas.|São filtros temporais de objetos diferentes, que devem ser examinados separadamente.
-|A anotação de dez anos no art.103 dispensa examinar a decisão do STF sobre indeferimento e cessação.|O alcance do dispositivo deve respeitar a ADI6096 e a distinção de concessão inicial.
+|Um resumo antigo que estende decadência a qualquer indeferimento deve ser conferido com o controle de constitucionalidade.|A literalidade histórica foi afetada pela ADI6096.
-|O prazo decadencial é contado sempre da primeira contribuição ao RGPS.|O marco não é a filiação ou a primeira contribuição, mas o evento previsto na norma aplicável.
''',['stf'])
add('B08-S02','p','art.103, parágrafo único','Prescrição diz respeito a prestações vencidas; a competência de cada parcela importa.','Benefício pago mensalmente gera parcelas com datas de exigibilidade próprias.',r'''
+|A prescrição quinquenal pode atingir prestações vencidas sem extinguir por si só o direito às parcelas futuras.|A prescrição das prestações deve ser separada do próprio direito ao benefício.
-|Todas as parcelas de um benefício prescrevem em uma única data, independentemente do vencimento.|Cada prestação tem exigibilidade própria e exige análise do marco temporal.
+|Para analisar atrasados é importante saber quando cada pagamento se tornou exigível.|O vencimento das prestações orienta a contagem do prazo prescricional.
-|A prescrição previdenciária torna irrelevante a situação de incapacidade protegida pela lei.|A norma ressalva direitos de menores, incapazes e ausentes, na forma do Código Civil.
+|Não se deve aplicar prescrição sem verificar causas impeditivas, suspensivas ou interruptivas pertinentes.|A contagem pode ser afetada por fatos legalmente relevantes.
-|O prazo quinquenal das prestações é o mesmo prazo para toda revisão de concessão.|Revisão concessória e cobrança de parcelas têm objetos e prazos distintos.
+|Data do requerimento e datas de vencimento das parcelas são informações diferentes.|Não se presume que todos os marcos temporais coincidam.
-|Uma prestação vencida há quatro anos está prescrita apenas por ter mais de um ano.|O prazo geral das prestações é de cinco anos, ressalvadas situações legais específicas.
+|A análise de uma parcela vencida há mais de cinco anos ainda exige verificar as ressalvas legais.|O simples número de anos não substitui o exame de proteção e causas que afetem o prazo.
-|O pagamento mensal transforma o direito a futuros benefícios em prescrição anual.|Periodicidade de pagamento não cria prazo prescricional de um ano.
+|A correção de um cálculo pode produzir parcelas com alcances temporais diferentes.|Cada diferença devida integra uma competência e pode sofrer efeitos prescricionais próprios.
-|Decadência é sempre aplicada no lugar da prescrição quando há cobrança de atrasados.|A escolha do instituto depende do objeto: revisão do ato ou prestações vencidas.
''')
add('B08-S03','p','art.103-A','A Administração tem prazo para anular atos favoráveis, salvo comprovada má-fé.','Um benefício favorável será revisto administrativamente: identifique pagamento e eventual má-fé.',r'''
+|O art.103-A prevê prazo de dez anos para o INSS anular atos favoráveis, salvo comprovada má-fé.|A norma tutela segurança jurídica, com exceção expressa para má-fé.
-|A simples alegação de má-fé, sem prova, afasta automaticamente a decadência administrativa.|A exceção exige má-fé comprovada, não mera suspeita.
+|Nos efeitos patrimoniais contínuos, o primeiro pagamento é marco relevante para a decadência administrativa.|O art.103-A disciplina especificamente os atos com efeitos continuados.
-|O prazo para o INSS anular ato favorável é sempre de trinta dias.|O art.103-A estabelece prazo decenal, observada a má-fé.
+|A impugnação administrativa da validade do ato é relevante para identificar o exercício do direito de anular.|Medida de autoridade administrativa que impugne a validade conta como exercício desse direito.
-|Todo erro material do INSS demonstra que o beneficiário agiu de má-fé.|Erro da Administração e má-fé do particular não são fatos equivalentes.
+|A anulação de ato favorável exige examinar tempo, legalidade e garantias do interessado.|A existência de poder de revisão não elimina contraditório e motivação.
-|A estabilidade decorrente do prazo autoriza concluir que o ato era necessariamente legal desde a origem.|Decadência é limitação temporal, não demonstração de legalidade material originária.
''')
add('B08-S04','ctn','CTN arts.173–174;Lei8.213,arts.103 e103-A','Prazos tributários e de benefícios protegem relações jurídicas diferentes.','Não aplique à revisão de aposentadoria um prazo de constituição de contribuição tributária.',r'''
+|A contribuição previdenciária tributária e a prestação de benefício exigem identificar regimes de prazo próprios.|Custeio e benefício não autorizam intercâmbio automático de regras de decadência.
-|Todo prazo ligado à Previdência é de dez anos porque existe o art.103 da Lei8.213.|Há regimes tributários e prazos de prestações distintos do prazo revisional.
+|Constituir crédito tributário e cobrar crédito já constituído são etapas diferentes.|Decadência tributária e prescrição tributária têm objetos diferentes.
-|O prazo quinquenal de prestações transforma a contribuição de segurado em benefício assistencial.|Prazo temporal não altera natureza de tributo ou de benefício.
+|Antes de contar um prazo deve-se identificar sujeito, objeto e marco inicial.|O mesmo número de anos pode aparecer em institutos com hipóteses diversas.
-|É correto importar prazo de revisão de aposentadoria para qualquer lançamento fiscal.|Lançamento de contribuição segue regime tributário aplicável, não o art.103 por analogia automática.
+|A classificação de um prazo depende da pretensão examinada, não apenas da palavra previdenciário.|Custeio, revisão concessória e prestações vencidas são relações diferentes.
-|Prescrição e decadência tributárias podem ser redefinidas livremente por instrução normativa do INSS.|Norma infralegal não substitui a reserva normativa constitucional e as regras legais dos prazos.
''',['p'])
add('B09-S01','cp','art.168-A','A apropriação indébita previdenciária envolve omissão de repasse ou recolhimento nas hipóteses tipificadas.','Uma empresa desconta contribuições dos trabalhadores e não as repassa no prazo legal.',r'''
+|Deixar de repassar contribuições recolhidas dos contribuintes, no prazo legal ou convencional, é conduta descrita no art.168-A.|O núcleo do tipo é a omissão de repasse de valores recolhidos.
-|O delito do art.168-A exige necessariamente subtração física de dinheiro de um cofre do INSS.|O tipo não depende de subtração física; a omissão de repasse é a conduta central.
+|Desconto na folha e repasse à Previdência são atos juridicamente diferentes.|A retenção não comprova que o recolhimento ocorreu no prazo.
-|Basta qualquer divergência cadastral sem relação com contribuições para configurar apropriação indébita previdenciária.|É necessário enquadramento na conduta e demais elementos do tipo penal.
+|O art.168-A também contém hipóteses equiparadas nos seus parágrafos.|A análise não pode limitar o estudo apenas à redação do caput.
-|Uma discussão penal pode ignorar quem efetivamente tinha responsabilidade pela obrigação.|A imputação exige individualização da conduta e da responsabilidade.
+|A ausência de repasse deve ser relacionada ao prazo aplicável.|O tipo se refere a prazo e forma previstos legal ou convencionalmente.
-|Sonegação de contribuição e apropriação indébita previdenciária são tipos penais idênticos.|O art.168-A e o art.337-A descrevem condutas diferentes.
+|A prova de que houve pagamento ou regularização precisa ser situada no tempo para avaliar seus efeitos.|Há regras específicas para efeitos do pagamento e da regularização.
-|O simples atraso torna dispensável analisar elemento subjetivo e causas legais de exclusão ou extinção.|Responsabilidade penal não decorre de automatismo administrativo.
+|Uma empresa que retém e não repassa não pode alegar que o desconto em folha equivale ao adimplemento.|Retenção e entrega ao destinatário da contribuição não se confundem.
-|Qualquer contribuinte individual que se esqueça de recolher contribuição própria pratica automaticamente o caput do art.168-A.|É preciso examinar se a conduta se enquadra na omissão de repasse de valores recolhidos e demais hipóteses legais.
''')
add('B09-S02','cp','art.337-A','Sonegação previdenciária envolve supressão ou redução de contribuição por condutas previstas em lei.','Uma folha omite trabalhadores para reduzir o valor declarado de contribuições.',r'''
+|Omitir segurados na folha para suprimir ou reduzir contribuição pode enquadrar-se no art.337-A.|A omissão de trabalhadores em documento exigido é uma das formas tipificadas.
-|O art.337-A pune somente a falta de repasse de valores já retidos, sem outras condutas.|Esse é foco do art.168-A; o art.337-A trata de supressão ou redução por condutas descritas.
+|Deixar de lançar contabilmente quantias descontadas dos segurados pode ser relevante para o art.337-A.|A lei prevê a omissão de lançamentos pertinentes ao custeio.
-|Qualquer erro de digitação constitui sonegação, ainda que não reduza contribuição nem haja elemento subjetivo.|O enquadramento exige elementos objetivos e subjetivos do tipo.
+|Omitir receitas ou outros fatos geradores pode ser meio de reduzir contribuição devida.|O art.337-A abrange omissões com repercussão na contribuição social previdenciária.
-|Folha com todos os trabalhadores registrados comprova, sozinha, a inexistência de qualquer sonegação.|Outras condutas previstas podem envolver contabilidade, remunerações e fatos geradores.
+|Para examinar sonegação é preciso relacionar omissão e resultado de supressão ou redução.|O tipo não é um rótulo genérico para toda irregularidade administrativa.
-|A mesma definição penal pode ser criada por portaria interna sem lei.|Tipo penal exige lei, respeitada a legalidade penal.
+|Distinguir omissão de informação e omissão de repasse ajuda a separar os arts.337-A e168-A.|As figuras podem ter contextos próximos, mas seus núcleos são distintos.
-|A responsabilidade penal de um administrador nasce apenas do título do cargo, sem conduta própria.|A imputação não dispensa individualização da participação e do dolo.
+|A apresentação espontânea de informações antes da ação fiscal tem disciplina própria no art.337-A.|A lei prevê hipótese de extinção em condições específicas.
-|A quitação administrativa e a tipicidade penal devem ser presumidas sem examinar datas e circunstâncias.|Efeitos penais dependem do regime legal aplicável e dos fatos.
''')
add('B09-S03','cp','arts.168-A e337-A','Identificar autor, conduta, resultado e dolo evita transformar irregularidade administrativa em condenação automática.','Um sócio sem gestão financeira não deve ser responsabilizado apenas por constar no contrato social.',r'''
+|A imputação penal deve individualizar a atuação do agente.|Ser sócio ou gestor não dispensa prova de participação relevante.
-|Todo integrante do quadro societário responde objetivamente por qualquer débito previdenciário.|Não há responsabilidade penal objetiva por mera condição societária.
+|O elemento subjetivo deve ser analisado juntamente com a conduta descrita no tipo.|O direito penal exige mais do que demonstrar a existência de uma dívida.
-|O auditor pode dispensar a descrição dos fatos porque a denominação sonegação já prova o crime.|Rótulo jurídico não substitui prova dos elementos do tipo.
+|A pessoa que omite trabalhadores para reduzir contribuição pratica conduta diferente da mera falta de cadastro sem consequência contributiva.|Resultado e finalidade da omissão importam no enquadramento.
-|Uma infração administrativa e um crime têm necessariamente os mesmos requisitos.|Esferas e tipos podem exigir elementos e garantias distintos.
+|A análise de documentos pode demonstrar quem controlava folha, declaração e repasse.|A prova da função efetiva auxilia a individualização da responsabilidade.
-|Basta uma presunção genérica de intenção para condenar qualquer administrador.|O dolo e a autoria devem ser demonstrados a partir dos fatos e das provas.
''')
add('B09-S04','cp','arts.168-A,§§2º–6º;337-A,§§1º–6º;LC225/2026,art.49','Regularização, parcelamento e pagamento possuem efeitos penais que dependem da norma, do momento e das exceções atuais de devedor contumaz.','Não confunda pagar a dívida com apenas negociar um parcelamento ou informar valores.',r'''
+|Fora da exceção legal do devedor contumaz, a hipótese do art.168-A,§2º, exige declarar, confessar, pagar e informar antes da ação fiscal.|As condições do §2º devem ser lidas com a exceção dos §§5º–6º acrescentados pela LC225/2026.
-|Somente prometer pagamento futuro satisfaz integralmente a hipótese do art.168-A,§2º.|Promessa não equivale à regularização exigida no dispositivo.
+|No art.337-A, a declaração e confissão espontâneas antes da ação fiscal têm disciplina própria, ressalvada a exceção atual de devedor contumaz.|O §1º deve ser lido com os §§5º–6º acrescidos pela LC225/2026; não é a mesma redação do art.168-A.
-|Todo parcelamento equivale imediatamente à extinção definitiva de punibilidade.|Suspensão durante parcelamento e extinção por pagamento integral são efeitos diferentes, conforme a lei aplicável.
+|A LC225/2026 ressalva a extinção indicada para agente declarado devedor contumaz por decisão definitiva e inscrito no Cadin.|Os §§5º dos arts.168-A e337-A estabelecem essa exceção, com os requisitos legais.
-|Deixar de ser considerado devedor contumaz afasta a exceção penal quanto aos atos do período em que tinha essa condição.|Os §§6º preservam a aplicação da exceção aos atos do período em que o agente era considerado contumaz.
+|A aplicação de perdão judicial ou multa isolada exige examinar requisitos e legislação pertinente.|Não é uma opção ilimitada fundada apenas na existência de débito pequeno.
-|Qualquer atraso isolado em tributo demonstra automaticamente decisão definitiva de devedor contumaz e inscrição no Cadin.|A exceção possui pressupostos específicos; mera inadimplência não prova todos eles.
''',['lc225'])
add('B10-S01','crps','CRPS; recurso ordinário e especial','O CRPS é órgão colegiado administrativo de julgamento de recursos, distinto do Poder Judiciário.','O segurado contesta uma decisão do INSS na via administrativa.',r'''
+|O CRPS julga recursos administrativos em matéria de sua competência.|Conselho de Recursos não é uma vara judicial nem a agência que concedeu inicialmente o benefício.
-|Recorrer ao CRPS exige, em qualquer caso, contratar advogado.|A via administrativa admite atuação do interessado ou representante, sem obrigatoriedade geral de advogado.
+|O processo recursal deve permitir que o interessado conheça os fundamentos da decisão contestada.|Contraditório e motivação orientam a discussão administrativa.
-|Um recurso administrativo transforma automaticamente o CRPS em órgão do Poder Judiciário.|A natureza do julgamento permanece administrativa.
+|Uma decisão do INSS pode ser contestada pelo recurso cabível, observados prazo e requisitos.|A existência de revisão administrativa é diferente da concessão automática do pedido.
-|O envio de recurso dispensa identificar qual decisão está sendo impugnada.|É preciso vincular a contestação ao ato e à matéria correspondentes.
+|O julgamento deve considerar a legislação e os elementos probatórios do processo.|O recurso não é uma consulta abstrata desvinculada do caso.
-|Toda notícia informal sobre benefício obriga o CRPS a reformar a decisão.|Fontes normativas e provas devem sustentar o pedido, não rumores.
+|Questão recursal e reclamação por demora não são a mesma providência.|Contestar mérito e comunicar atraso têm finalidades distintas.
-|A ausência de pagamento imediato prova que o recurso foi necessariamente desprovido.|Julgamento e cumprimento são etapas diferentes; é preciso verificar o andamento.
+|O acompanhamento pelo interessado permite distinguir diligência, julgamento e cumprimento.|Cada etapa tem significado processual próprio.
-|O órgão recursal pode julgar qualquer assunto público apenas por se chamar conselho.|A atuação depende de competência legal e regimental.
''')
add('B10-S02','crps','Juntas de Recursos e Câmaras de Julgamento','Juntas e Câmaras exercem competências recursais distintas no sistema administrativo.','Não enderece um recurso contra decisão inicial como se já houvesse acórdão da Junta.',r'''
+|As Juntas de Recursos atuam na primeira instância recursal administrativa pertinente.|A decisão inicial do INSS é distinta do julgamento recursal da Junta.
-|As Câmaras de Julgamento equivalem às agências da Previdência no atendimento inicial.|Câmaras são unidades de julgamento recursal, não agências de concessão inicial.
+|O recurso especial pode levar à Câmara matéria decidida pela Junta, quando cabível.|A segunda instância não elimina os requisitos de admissibilidade.
-|Toda decisão de Junta admite necessariamente recurso especial, sem exceções.|É preciso verificar alçada, cabimento e regras regimentais aplicáveis.
+|A identificação da decisão recorrida ajuda a determinar o órgão competente.|Recurso contra decisão inicial e contra acórdão têm percursos diferentes.
-|Uma Câmara é órgão do Tribunal Regional Federal.|A Câmara do CRPS é órgão administrativo, não judicial.
+|O colegiado pode determinar diligências necessárias à instrução, nos termos das regras processuais.|A apreciação do recurso exige um processo suficientemente instruído.
-|A primeira decisão da agência e o acórdão da Junta são o mesmo ato, com nomes diferentes.|Há atos de instâncias distintas, com funções próprias.
+|A competência não se define pela preferência pessoal do recorrente.|Normas legais e regimentais delimitam qual unidade julga o caso.
-|É possível ignorar o conteúdo da decisão porque qualquer unidade do CRPS decide indistintamente todos os recursos.|A competência e o tipo de recurso devem ser examinados.
+|Uma decisão colegiada deve ser distinguida de informação de andamento do Meu INSS.|Andamento não substitui o teor e a fundamentação do acórdão.
-|O recurso à Câmara torna desnecessário indicar razões de discordância.|O pedido de reforma deve ser fundamentado e compatível com o cabimento.
''')
add('B10-S03','crps','recurso ordinário e recurso especial','O recurso correto depende da etapa e da decisão que se pretende contestar.','Decisão inicial indeferiu aposentadoria; o interessado ainda não possui acórdão de Junta.',r'''
+|O recurso ordinário é o instrumento usual para contestar decisão inicial do INSS no CRPS.|O encaminhamento recursal inicial é diferente do recurso especial contra julgamento.
-|Recurso especial significa necessariamente recurso ao Superior Tribunal de Justiça.|No CRPS, a expressão identifica um recurso administrativo previsto no sistema.
+|O interessado deve distinguir indeferimento inicial de acórdão recursal antes de escolher o serviço.|A etapa define o procedimento cabível.
-|Todo documento entregue após a decisão é automaticamente um recurso tempestivo.|É necessário examinar pedido, prazo, identificação da decisão e procedimento.
+|A apresentação de fundamentos e documentos pertinentes pode auxiliar a revisão da decisão.|O recurso deve indicar o erro apontado e sua sustentação.
-|Interpor recurso dispensa verificar se o mesmo pedido está sendo discutido judicialmente.|A identidade de objeto com ação judicial tem efeitos na via administrativa.
+|O prazo de recurso ordinário ou especial informado pelo INSS é de trinta dias da ciência.|A contagem toma como referência o conhecimento da decisão, observadas as normas aplicáveis.
-|Todo incidente processual possui obrigatoriamente o mesmo prazo de qualquer recurso.|Incidentes devem seguir os prazos próprios do regimento.
''')
add('B10-S04','crps','prazo; reconsideração; apresentação eletrônica','Tempestividade e identificação da ciência são tão importantes quanto o mérito.','Uma comunicação informa o resultado; registre quando houve ciência para analisar o prazo.',r'''
+|A data da ciência da decisão é relevante para calcular o prazo recursal.|Não se deve confundir a data da ciência com a data de início da atividade profissional.
-|O prazo geral informado para recurso no INSS é contado sempre do nascimento do segurado.|O marco é a ciência da decisão recorrida, conforme o procedimento.
+|A revisão do próprio ato pela autoridade competente pode ocorrer no fluxo administrativo, conforme a regra aplicável.|Reconsideração e julgamento pelo órgão recursal não são conceitos idênticos.
-|Protocolar uma petição torna dispensável comprovar seu recebimento.|Comprovantes e números de protocolo permitem demonstrar apresentação e acompanhamento.
+|O pedido deve permitir identificar decisão, interessado e razões da contestação.|Esses elementos dão sentido ao exercício do direito de recorrer.
-|Uma exigência de documento significa sempre decisão final desfavorável.|Exigência e indeferimento são eventos diferentes, a serem distinguidos no processo.
+|Os prazos de incidentes processuais precisam ser conferidos no regimento vigente.|Não se importa automaticamente o prazo de recurso para todo incidente.
-|A autoridade pode mudar a data da ciência apenas para considerar qualquer recurso tempestivo.|Marcos processuais devem corresponder aos fatos e às regras aplicáveis.
''')
add('B10-S05','crps','ação judicial de objeto idêntico','A identidade de objeto, e não a simples existência de qualquer processo, orienta os efeitos da judicialização.','Uma ação discute exatamente o benefício que está no recurso; outra trata de assunto alheio.',r'''
+|Ação judicial de objeto idêntico pode implicar renúncia ao recurso administrativo e desistência do já interposto.|A orientação oficial do INSS relaciona o efeito à identidade do objeto.
-|Qualquer ação trabalhista impede todo recurso previdenciário, mesmo sobre matéria diferente.|Não basta qualquer processo: é preciso examinar identidade de objeto.
+|Comparar pedidos e causa discutida ajuda a verificar a identidade entre as vias.|O nome do processo, sozinho, não esclarece o alcance do objeto.
-|A ação judicial sempre suspende o recurso administrativo para julgamento conjunto pelos dois órgãos.|A disciplina da identidade de objeto prevê renúncia e desistência, não essa regra geral de julgamento conjunto.
+|Informações sobre ação judicial devem ser consideradas no exame do processo recursal.|A coexistência pode produzir efeitos procedimentais relevantes.
-|É correto ocultar uma ação de mesmo objeto porque ela nunca tem consequência administrativa.|A identidade de objeto tem efeito expressamente informado pelo INSS.
+|Um processo sobre tema inteiramente distinto não demonstra, por si só, desistência do recurso previdenciário.|A conclusão depende de correspondência material entre os objetos.
-|Renúncia ao recurso de mesmo objeto elimina automaticamente qualquer direito material em discussão judicial.|O efeito na via administrativa não equivale a julgamento do mérito judicial.
''')
add('B11-S01','p','arts.10–16','Beneficiários do RGPS abrangem segurados e dependentes, com posições jurídicas distintas.','Quem trabalha vinculado ao regime é segurado; o familiar pode depender de vínculo e requisitos legais.',r'''
+|Segurados e dependentes integram o conjunto de beneficiários do RGPS.|O art.10 divide os beneficiários nessas duas categorias.
-|Somente quem recolhe contribuição diretamente em seu nome pode ser beneficiário do RGPS.|Dependentes podem receber prestações derivadas sem contribuição própria para essa condição.
+|A qualidade de dependente não se confunde com filiação como segurado.|São vínculos distintos, embora a mesma pessoa possa reunir posições diferentes.
-|Toda pessoa que recebe ajuda financeira de segurado é automaticamente dependente previdenciário.|É necessário enquadramento nas categorias e condições legais.
+|Um filho pode ser dependente e também segurado por atividade própria, conforme o caso.|As duas posições não são logicamente incompatíveis.
-|O BPC transforma seu titular em segurado do RGPS por esse único fato.|BPC é assistencial; seu recebimento não cria filiação previdenciária.
+|Segurado especial é categoria de segurado, não classe de dependente.|Classificação de atividade e ordem de dependência pertencem a eixos diferentes.
-|A condição de dependente elimina todos os requisitos específicos da pensão por morte.|Óbito, qualidade e demais condições precisam ser analisados.
+|Prestação devida ao segurado pode ter requisitos diferentes daquela devida ao dependente.|O evento e o destinatário integram a hipótese de cada benefício.
-|Qualquer beneficiário pode escolher qualquer espécie do plano de benefícios.|As prestações são distribuídas conforme destinatário e risco protegido.
+|A pensão por morte é exemplo de prestação dirigida a dependentes.|Seu fato gerador e destinatários diferem de aposentadoria própria do segurado.
-|A aposentadoria recebida pelo trabalhador é benefício próprio dos seus dependentes.|A aposentadoria é do segurado; dependentes têm proteção derivada nas hipóteses legais.
+|A identificação do beneficiário deve anteceder a análise de carência da prestação.|É preciso saber qual prestação e qual vínculo estão sendo examinados.
-|Segurado facultativo significa familiar dependente que ainda não trabalha.|Facultativo é categoria de segurado que opta por filiação observados requisitos.
+|Filiação obrigatória decorre de atividade enquadrada, enquanto dependência obedece ao rol legal.|Os pressupostos dos dois vínculos não se confundem.
-|Prova de parentesco sempre basta, qualquer que seja a classe de dependência.|Algumas categorias exigem prova econômica e condições adicionais.
''')
add('B11-S02','p','art.16; conferir redação vigente para equiparados','As classes de dependentes têm ordem de preferência e regras próprias de prova econômica.','Cônjuge, pais e irmãos não disputam em condições idênticas quando há classe preferencial.',r'''
+|A existência de dependente de classe anterior exclui o direito das classes seguintes.|O art.16 organiza classes de preferência.
-|Pais e cônjuge sempre dividem a pensão em igualdade, independentemente das classes.|A presença da classe anterior exclui classes subsequentes.
+|A dependência econômica da primeira classe é presumida nos termos legais.|A presunção é diferente da prova exigida para classes posteriores.
-|A dependência econômica dos pais é presumida apenas por serem ascendentes.|Pais precisam comprovar dependência econômica e não podem afastar classe preferencial.
+|Para irmãos, parentesco sozinho não encerra a análise de dependência.|São exigidas condições de idade ou deficiência/invalidez e dependência econômica.
-|Filho universitário tem, por essa única condição, pensão do RGPS garantida até vinte e quatro anos.|A lei não estende genericamente a condição de filho dependente até24 apenas por universidade.
+|Filho não emancipado menor de vinte e um anos integra hipótese legal de dependência.|Idade e demais condições previstas precisam ser examinadas.
-|Qualquer sobrinho entra automaticamente na classe de irmãos porque também é parente colateral.|O rol legal não equipara genericamente sobrinho a irmão.
+|Cônjuge e companheiro estão na primeira classe prevista no art.16.|A proteção da união estável deve ser analisada conforme seus requisitos de prova.
-|Ser herdeiro civil e ser dependente previdenciário são sempre posições idênticas.|Sucessão civil e dependência previdenciária têm regimes próprios.
+|A condição de invalidez ou deficiência relevante deve ser examinada segundo a hipótese legal e temporal.|Não basta usar o termo deficiência sem verificar os requisitos da categoria.
-|A presunção de dependência dispensa demonstrar a própria condição familiar alegada.|Presumir dependência econômica não equivale a presumir casamento, união ou filiação.
+|Documentos que provem união estável e documentos de contribuição têm finalidades distintas.|Um comprova vínculo familiar; o outro se relaciona à filiação e obrigações contributivas.
-|O segurado pode criar uma classe nova de dependentes apenas por declaração particular.|A declaração não substitui a previsão legal de categoria.
+|Alterações legais sobre equiparados exigem consultar o texto vigente, sem congelar a lista de um resumo antigo.|Tutela, enteado e guarda exigem atenção à redação atual e regras pertinentes.
-|A ordem de classes significa que o dependente mais velho sempre exclui os demais da mesma classe.|Preferência entre classes não cria critério genérico de idade dentro da classe.
''')
add('B11-S03','p','art.18;arts.88–93','Benefícios são prestações pecuniárias; serviços têm finalidade e execução próprias.','Reabilitação profissional não é uma aposentadoria paga sob outro nome.',r'''
+|O Plano de Benefícios contém benefícios e serviços.|O art.18 distingue modalidades de proteção.
-|Todo serviço previdenciário é necessariamente pagamento mensal em dinheiro.|Serviço social e reabilitação têm atividades próprias, não se reduzem a renda mensal.
+|A aposentadoria é benefício pecuniário dirigido ao segurado.|A prestação pressupõe requisitos da espécie de aposentadoria.
-|A reabilitação profissional e a pensão por morte têm o mesmo destinatário e o mesmo fato gerador.|São prestações de naturezas e pressupostos distintos.
+|Serviço social busca esclarecer direitos e meios de exercê-los.|O art.88 atribui dimensão de orientação e acesso à proteção.
-|A existência de serviços elimina a obrigação de verificar os requisitos de benefícios monetários.|Cada prestação conserva sua hipótese legal.
+|A habilitação e a reabilitação procuram favorecer ingresso ou reingresso no trabalho e na vida social.|Sua finalidade não se resume a conceder uma renda.
-|Todo dependente tem direito à mesma aposentadoria que o segurado, por derivação.|Benefícios próprios e derivados não são intercambiáveis.
+|Pensão por morte e auxílio-reclusão protegem dependentes nas hipóteses legais.|Não são benefícios pagos ao segurado em razão de incapacidade própria.
-|O segurado pode substituir unilateralmente qualquer benefício por qualquer serviço.|A lei delimita destinatários e condições das prestações.
+|Distinguir natureza da prestação ajuda a analisar carência e qualidade exigidas.|Não se deve aplicar indiscriminadamente regra de benefício a serviço.
-|Abono anual é denominação de um serviço social sem conteúdo monetário.|O abono anual é pagamento relacionado a benefícios previstos na lei.
+|O serviço social pode atuar na identificação de barreiras de acesso a direitos.|A orientação integra sua finalidade legal e institucional.
-|A prestação de orientação prova que o interessado já preenche todos os requisitos de aposentadoria.|Receber informação não substitui a análise do direito ao benefício.
+|Uma mesma pessoa pode necessitar de proteção monetária e de reabilitação conforme os requisitos de cada prestação.|As categorias não são excludentes apenas por terem naturezas diferentes.
-|Benefícios e serviços só se distinguem pelo nome escolhido na plataforma eletrônica.|A diferença decorre da disciplina legal e da natureza da prestação.
''')
add('B11-S04','p','arts.24–27','Carência é número mínimo de contribuições mensais; não se confunde automaticamente com duração do vínculo.','Doze meses desde a inscrição não significam doze contribuições válidas para qualquer categoria.',r'''
+|Carência corresponde ao número mínimo de contribuições mensais exigidas para a prestação.|O conceito legal está no art.24.
-|A inscrição há doze meses demonstra necessariamente doze contribuições de carência.|O tempo cadastral não comprova recolhimentos ou hipóteses de contagem.
+|Para empregado, a contagem de carência considera a filiação segundo a disciplina legal.|Não se deve transferir ao empregado, indistintamente, a regra do primeiro pagamento sem atraso do individual.
-|Contribuinte individual sempre pode inaugurar a carência com qualquer pagamento atrasado.|A lei prevê a referência ao primeiro recolhimento sem atraso para as categorias pertinentes.
+|A categoria do segurado influencia a análise do início da carência.|O art.27 diferencia grupos de segurados.
-|Duas contribuições referentes ao mesmo mês sempre produzem dois meses de carência.|Carência mensal não é multiplicada por pagamentos concomitantes da mesma competência.
+|Cumprir carência não prova por si só idade mínima ou incapacidade.|São requisitos jurídicos diferentes da prestação.
-|Quem tem qualidade de segurado necessariamente cumpriu carência de todos os benefícios.|A qualidade pode existir sem a quantidade exigida para determinada prestação.
+|O pagamento e sua competência devem ser identificados ao examinar carência.|Datas e competências podem afetar a validade da contagem.
-|Carência é o valor monetário mínimo de uma aposentadoria.|Carência é requisito contributivo temporal, não valor de renda.
+|A aposentadoria e o benefício por incapacidade podem ter exigências distintas de carência.|O art.25 e as regras de cada benefício precisam ser examinados.
-|Toda prestação do RGPS exige carência de cento e oitenta contribuições.|Há carências específicas e hipóteses de dispensa.
+|O enquadramento como segurado especial possui disciplina própria de comprovação para benefícios legais.|Não se aplica mecanicamente a todos a mesma forma de recolhimento mensal.
-|O número de anos trabalhados pode ser multiplicado por doze sem examinar documentos e regras de contagem.|A prova e a validade dos períodos precisam ser verificadas.
+|A existência de vínculo não impede que haja discussão sobre competências não aproveitáveis para certa finalidade.|Carência e tempo de contribuição exigem exame próprio do caso.
-|A regra de carência é escolhida apenas pela vontade do requerente.|A espécie de prestação e a norma aplicável definem a exigência.
''')
add('B11-S05','p','art.26; ADIs2110/2111 e IN188/2025','Dispensa de carência não dispensa os demais requisitos da prestação.','Acidente pode dispensar carência de incapacidade, mas é preciso avaliar a incapacidade e o vínculo.',r'''
+|Pensão por morte é prestação que independe de carência.|Dispensa de carência não afasta dependência e demais requisitos.
-|Dispensar carência significa dispensar todo requisito de um benefício.|A dispensa alcança o número mínimo de contribuições, não a hipótese integral.
+|Auxílio-acidente independe de carência.|É necessário verificar a categoria coberta e a sequela com redução laboral.
-|Todo diagnóstico de doença elimina automaticamente a carência do benefício por incapacidade.|Há hipóteses legais específicas; doença comum não é dispensa universal.
+|Acidente de qualquer natureza pode ensejar dispensa de carência em benefício por incapacidade.|A incapacidade e os demais pressupostos precisam existir.
-|Uma doença preexistente sempre gera benefício sem carência e sem avaliar progressão.|Preexistência, progressão e agravamento possuem disciplina própria; não há concessão automática.
+|Serviço social e reabilitação profissional integram hipóteses de proteção sem carência legal.|A natureza e a elegibilidade do serviço ainda precisam ser examinadas.
-|A dispensa de carência para pensão prova que a duração ao cônjuge será sempre vitalícia.|Duração tem regras próprias; carência e tempo de duração são questões diferentes.
+|A aplicação atual do salário-maternidade pelo INSS reconhece a isenção de carência após as ADIs e a IN188/2025.|Resumos que exigem automaticamente dez contribuições estão desatualizados para essa aplicação.
-|Mesmo após a atualização de2025, toda facultativa deve cumprir dez contribuições para salário-maternidade.|O INSS aplica a isenção de carência, preservados os demais requisitos.
+|Auxílio-reclusão não deve ser incluído automaticamente entre prestações atualmente sem carência.|Há exigência contributiva específica aplicável à hipótese atual.
-|A notícia de isenção de carência para maternidade elimina a necessidade de qualidade de segurado.|Qualidade e evento gerador permanecem questões a verificar.
+|Na correção de questão antiga, pode ser necessário preservar gabarito histórico e explicar regra atual diferente.|A data da prova e as mudanças normativas ou judiciais devem ficar claras.
-|A lista de doenças graves dispensa demonstrar que há incapacidade quando se pede benefício por incapacidade.|O diagnóstico e a incapacidade exigida são elementos distintos.
+|Salário-família é outra prestação que independe de carência.|A ausência de carência não elimina limites de renda e condições dos dependentes.
-|A palavra acidente permite conceder qualquer benefício a pessoa sem qualquer vínculo protegido.|É necessário examinar a cobertura e a hipótese de cada prestação.
''',['mat'])
add('B11-S06','p','art.27-A; IN188/2025 para maternidade','Após perda da qualidade, a recuperação de contribuições anteriores depende de regras específicas da prestação.','Compare ter seis novas contribuições para incapacidade e doze para auxílio-reclusão, nas hipóteses legais.',r'''
+|A recuperação de contribuições anteriores após perda da qualidade exige examinar o art.27-A.|Não se deve aplicar um número único a todas as prestações.
-|Após perder a qualidade, todo histórico contributivo é apagado definitivamente para qualquer finalidade.|A lei prevê hipóteses de reaproveitamento condicionadas.
+|Para benefícios por incapacidade sujeitos à carência de doze, a regra legal de reaproveitamento exige metade, nas condições do art.27-A.|Seis novas contribuições não substituem os demais requisitos ou eventuais dispensas.
-|Uma contribuição após a nova filiação sempre recupera integralmente a carência para incapacidade comum.|A regra específica pode exigir seis, salvo hipótese legal de dispensa.
+|Para auxílio-reclusão sujeito à carência de vinte e quatro, a metade corresponde a doze contribuições.|A aplicação depende do fato gerador e do regime temporal pertinente.
-|O requisito de metade significa contar sempre dois recolhimentos no mesmo mês como dois meses.|A referência é a contribuições mensais válidas, sem duplicar competência.
+|A análise deve distinguir perda de qualidade de simples interrupção ainda coberta pelo período de graça.|Nem toda pausa contributiva configura perda da qualidade.
-|Se a qualidade foi mantida, deve-se tratar o segurado obrigatoriamente como alguém que a perdeu.|O fato jurídico da perda precisa existir para aplicar a regra de recuperação.
+|Reaproveitar carência não transforma contribuição inválida em contribuição válida.|A regularidade e a finalidade dos períodos devem ser verificadas.
-|Salário-maternidade atual pode ser resolvido apenas copiando antiga regra de cinco novas contribuições.|A isenção aplicada pelo INSS após ADIs/IN188 exige atualização da análise.
+|Uma lacuna contributiva exige identificar início, duração e hipótese de manutenção da qualidade.|O intervalo isolado não resolve a perda ou a recuperação.
-|O mesmo número mínimo vale para incapacidade e auxílio-reclusão porque ambos são benefícios.|As carências integrais e, consequentemente, as metades podem ser diferentes.
+|O número de novas contribuições precisa ser relacionado a um novo vínculo juridicamente válido.|Pagamento sem enquadramento regular não basta por simples soma aritmética.
-|A recuperação da carência garante benefício mesmo sem ocorrência do risco protegido.|Carência é apenas um dos requisitos da prestação.
+|Contribuições anteriores e posteriores devem ser separadas na análise do reaproveitamento.|A regra relaciona períodos anteriores à perda e novas contribuições.
-|Ter doze anos de contribuição antiga dispensa toda regra de recuperação após perda da qualidade.|A quantidade antiga não afasta automaticamente o art.27-A quando aplicável.
''',['mat'])
add('B11-S07','p','art.29; EC103/2019,art.26','Salário de benefício é base de cálculo e não equivale automaticamente à renda mensal paga.','Uma média contributiva de três mil reais pode receber coeficiente inferior a cem por cento.',r'''
+|Salário de benefício e renda mensal inicial são grandezas que devem ser distinguidas.|A base de cálculo pode receber coeficiente específico da prestação.
-|Todo benefício do RGPS tem valor exatamente igual ao último salário do segurado.|As fórmulas legais consideram bases, médias, coeficientes e limites distintos.
+|O período básico de cálculo exige observar a regra temporal aplicável.|Direito adquirido, transições e regras posteriores não são intercambiáveis.
-|É correto aplicar automaticamente a média dos oitenta por cento maiores salários a todos os benefícios novos.|A EC103 alterou regras de cálculo; a aplicação depende da hipótese.
+|O art.26 da EC103 utiliza, para as hipóteses nele disciplinadas, média de cem por cento do período contributivo definido.|Não se deve substituir essa referência por uma regra histórica sem verificar o caso.
-|Salário de contribuição é o nome técnico do benefício mensal recebido pelo aposentado.|É base contributiva; salário de benefício e renda mensal são conceitos próprios.
+|Correção monetária dos salários considerados na média tem papel diferente do coeficiente da renda.|Atualizar valores e aplicar percentual são operações distintas.
-|Uma média contributiva permite ignorar teto e piso previstos para a prestação.|Limites precisam ser examinados conforme a espécie de benefício.
+|Informações do CNIS podem influenciar o cálculo e exigir acerto de dados.|A base documental integra a análise do período contributivo.
-|Ausência de um vínculo no cadastro prova que o período nunca existiu, sem admitir exame de prova.|Dados cadastrais podem demandar comprovação e correção nos termos legais.
+|A data de entrada no regime não é necessariamente o primeiro mês usado na média de uma regra específica.|O período básico de cálculo é definido pela norma aplicável.
-|Média de contribuição e soma de contribuições produzem necessariamente o mesmo valor.|Somar valores e dividir pelo número de competências são operações diferentes.
+|Antes de calcular, deve-se identificar a espécie do benefício e sua regra.|A média não pode ser escolhida sem a hipótese jurídica.
-|Se o segurado teve dois vínculos, deve-se ignorar sempre um deles no cálculo.|Concomitância exige aplicar regras próprias e limites, sem exclusão genérica.
+|Uma questão histórica pode adotar cálculo que não corresponde à regra de benefício atual.|Preservar contexto temporal evita tratar toda fórmula antiga como atual.
-|O salário de benefício é um imposto recolhido pela empresa.|É grandeza de cálculo previdenciário, não espécie tributária.
''',['ec'])
add('B11-S08','ec','art.26; Lei8.213,arts.29,33,44,61,86','Coeficientes são aplicados à base correspondente e variam entre prestações.','Sessenta por cento de média deR$3.000 corresponde aR$1.800 antes de outros ajustes cabíveis.',r'''
+|Conhecer a média não dispensa identificar o coeficiente aplicável.|A renda depende da combinação da base com a regra da prestação.
-|Toda aposentadoria posterior à reforma equivale invariavelmente a cem por cento da média.|Há fórmulas diferenciadas conforme hipótese, tempo e natureza da incapacidade.
+|Na regra geral pertinente do art.26 da EC103, sessenta por cento é acrescido de pontos percentuais por tempo excedente previsto.|Limiares de tempo e exceções devem ser examinados conforme a categoria.
-|Acrescer dois pontos percentuais significa multiplicar o coeficiente por dois a cada ano.|Ponto percentual se soma ao percentual; não duplica seu valor.
+|Sessenta por cento de uma base deR$3.000 resulta emR$1.800.|O cálculo é3000×0,60, sem confundir base e valor final.
-|Aplicar oitenta por cento aR$2.500 produz renda deR$2.800.|2500×0,80 resulta emR$2.000, antes de eventual limite legal.
+|Benefício por incapacidade permanente decorrente de acidente do trabalho possui regra específica de coeficiente na EC103.|A natureza ocupacional pode alterar o cálculo nas hipóteses constitucionais.
-|Acidente comum e acidente do trabalho são sempre iguais para todo coeficiente da reforma.|A EC103 diferencia hipóteses; não se deve generalizar.
+|Auxílio-acidente tem natureza indenizatória e percentual próprio.|Não deve ser calculado como se fosse aposentadoria programada.
-|Coeficiente de noventa e um por cento e coeficiente de cinquenta por cento representam a mesma parcela da base.|São percentuais distintos de benefícios com regras próprias.
+|A aplicação do salário mínimo depende da natureza substitutiva e das regras da prestação.|Há prestações indenizatórias com disciplina diferente do benefício substitutivo.
-|Uma renda inicialmente calculada nunca precisa ser comparada aos limites legais.|Piso, teto e regras específicas devem ser examinados.
+|Para uma mesma base, coeficientes distintos podem produzir rendas distintas.|A base não determina sozinha a renda.
-|Uma questão de cálculo pode omitir a espécie e ainda exigir aplicar qualquer percentual escolhido pelo candidato.|O coeficiente depende do enquadramento jurídico fornecido.
+|Regra de cálculo deve ser registrada junto à data e à hipótese jurídica.|Isso permite preservar correções históricas e conferir atualizações.
-|A expressão renda mensal inicial significa o total de todas as contribuições pagas ao longo da vida.|RMI é valor mensal inicial da prestação, não soma de contribuições.
''',['p'])
add('B11-S09','p','arts.33 e41-A; CF art.201,§§2ºe4º','Reajuste preserva o valor real segundo critérios legais; não equivale a repetir o salário mínimo para todos.','Benefício acima do mínimo pode ter índice diferente do aumento do piso nacional.',r'''
+|Benefícios devem ser reajustados para preservar o valor real conforme critérios legais.|A proteção constitucional não dispensa os critérios previstos na legislação.
-|Todo benefício acima do mínimo aumenta sempre no mesmo percentual do salário mínimo.|Reajuste dos benefícios e política de valorização do mínimo não são regras idênticas.
+|O art.41-A utiliza o INPC na disciplina de reajustamento ali estabelecida.|É necessário observar data de início e critérios do reajuste.
-|Preservar valor real significa manter o mesmo número nominal para sempre.|Inflação altera poder de compra, razão pela qual há reajustamento.
+|Piso de benefício substitutivo e teto previdenciário são limites de funções distintas.|Um é proteção mínima e o outro limita valores nas hipóteses pertinentes.
-|Toda prestação, inclusive indenizatória, deve necessariamente ser igual ou superior ao mínimo.|A natureza da prestação e sua disciplina específica precisam ser verificadas.
+|O reajuste pode considerar proporcionalidade no ano de início do benefício conforme a regra aplicável.|Não se presume índice integral para qualquer data inicial.
-|Se a aposentadoria vale dois mínimos na concessão, deve manter eternamente a razão exata de dois mínimos.|Não existe vinculação genérica permanente de benefício acima do piso ao número de mínimos.
+|Reajuste anual e revisão do ato de concessão são procedimentos conceitualmente diferentes.|Reajuste atualiza valor; revisão examina o cálculo ou a concessão.
-|A simples mudança do teto corrige automaticamente qualquer erro da concessão original.|A elevação de limite não substitui análise de eventual revisão.
+|Uma questão numérica deve informar índice e hipótese para exigir cálculo de reajuste.|Sem esses dados não se pode inventar percentual atual.
-|O índice de reajuste pode ser escolhido livremente pelo estudante entre inflação e poupança.|O critério decorre da norma aplicável.
+|O valor do teto precisa ser vinculado ao ano da questão.|Limites monetários são temporalmente variáveis.
-|É correto usar valor de2022 como se fosse teto vigente em2026 sem aviso.|Valores históricos devem ser identificados, não apresentados como atuais.
+|A manutenção do poder aquisitivo não transforma benefício previdenciário em aplicação financeira livre.|A proteção segue regime legal, não taxa escolhida pelo beneficiário.
-|O reajustamento anual torna desnecessária a correção dos salários na formação da média inicial.|Cálculo inicial e atualização posterior são etapas diferentes.
''')
add('B11-S10','p','art.124; EC103/2019,art.24','Acumular benefícios exige analisar espécie, titular e marco temporal.','Pensão e aposentadoria podem ter acumulação admitida com aplicação das faixas constitucionais.',r'''
+|A lei veda receber simultaneamente aposentadoria e auxílio por incapacidade temporária do mesmo regime na hipótese comum.|O art.124 estabelece vedações específicas de acumulação.
-|Uma pessoa pode receber duas aposentadorias no RGPS apenas porque teve dois empregos.|Concomitância de vínculos não cria duas aposentadorias no mesmo regime.
+|Auxílio-acidente não pode ser acumulado com aposentadoria na regra atual pertinente.|A natureza indenizatória não elimina a vedação legal.
-|Toda pensão por morte é incompatível com qualquer aposentadoria em qualquer regime.|A acumulação pode ser admitida nas hipóteses legais, com disciplina constitucional de valor.
+|A EC103 prevê hipóteses de acumulação com recebimento integral do benefício mais vantajoso e frações dos demais.|É preciso examinar os benefícios, faixas e regras temporais.
-|Aplicar frações a um segundo benefício significa extinguir sua existência jurídica.|A regra limita o valor acumulado, não se confunde com declarar inexistência da prestação.
+|A origem de cada benefício e o fato gerador ajudam a verificar a acumulação permitida.|Não se decide apenas pelo nome pensão.
-|O art.124 permite acumular qualquer número de auxílios-acidente sem limite.|Há vedação legal à percepção de mais de um auxílio-acidente.
+|Direitos adquiridos antes de mudança normativa devem ser examinados no regime temporal correspondente.|Não se aplica automaticamente regra nova a toda situação antiga.
-|Salário-maternidade pode ser pago junto com qualquer benefício por incapacidade sem considerar suspensão ou ajuste.|Há disciplina própria para coincidência e substituição de prestações.
+|Renunciar a benefício para escolher prestação mais vantajosa exige observar o procedimento e os efeitos legais.|Não basta alterar um campo de aplicativo para eliminar vínculo jurídico.
-|Uma tabela genérica de pode/não pode dispensa conferir exceções e datas.|Acumulação exige análise contextual da hipótese concreta.
''',['ec'])
add('B11-S11','ec','arts.15–20 e26; CF art.201','Aposentadoria programada e transições dependem da data de filiação e dos requisitos próprios.','Não aplique a segurado já filiado antes da reforma a mesma análise incompleta de novo filiado.',r'''
+|A data de filiação anterior ou posterior à reforma pode influenciar a regra de aposentadoria aplicável.|A EC103 distingue regras permanentes, transitórias e de transição.
-|A EC103 extinguiu todos os direitos adquiridos de quem já havia cumprido requisitos.|Direito adquirido deve ser preservado nos termos constitucionais.
+|Uma regra de pontos pode exigir idade e tempo de contribuição somados e mínimos específicos.|Pontos não substituem todos os outros requisitos da hipótese.
-|Em toda transição, basta atingir a soma de pontos, sem tempo mínimo.|As regras podem exigir cumulativamente outros requisitos.
+|Pedágio é requisito adicional de tempo na transição correspondente.|Não é contribuição monetária extra paga em uma única guia para comprar aposentadoria.
-|Qualquer pessoa pode escolher qualquer regra de transição, mesmo sem preencher seu enquadramento.|Cada transição possui público e condições específicos.
+|Os requisitos devem ser verificados na data em que o direito se forma.|Idades ou pontos progressivos exigem referência temporal.
-|A idade de um exemplo de2022 pode ser usada invariavelmente para toda transição em2026.|Regras progressivas podem alterar requisitos ao longo dos anos.
+|A aposentadoria exige também examinar carência quando aplicável.|Idade e tempo de contribuição não encerram todos os filtros.
-|Perda da qualidade impede sempre aposentadoria por idade, mesmo com os demais requisitos legais preenchidos.|Há regras legais próprias que afastam a exigência de qualidade para essa hipótese.
+|A comparação entre regras deve incluir cálculo do benefício, não apenas a data de elegibilidade.|Regras distintas podem produzir valores diferentes.
-|O nome aposentadoria programada dispensa verificar requisitos de sexo, idade e tempo previstos na norma.|A denominação não substitui o enquadramento jurídico.
''',['p','l10666'])
add('B11-S12','p','arts.39,48 e55; CF art.201,§7º','A aposentadoria rural exige atividade e prova pertinentes; rural não significa automaticamente segurado especial.','Trabalhador empregado rural e produtor em economia familiar podem ter enquadramentos distintos.',r'''
+|Empregado rural e segurado especial são categorias distintas.|Atividade no campo não torna todos segurados especiais.
-|Morar em zona rural basta, sozinho, para comprovar todo requisito de aposentadoria rural.|Residência não substitui o exercício de atividade e sua prova.
+|O segurado especial deve comprovar atividade rural no período legalmente exigido.|A proteção possui disciplina própria de comprovação.
-|A prova exclusivamente testemunhal é sempre suficiente, sem qualquer ressalva legal, para qualquer período rural.|A lei exige início de prova material, ressalvadas hipóteses específicas como caso fortuito ou força maior.
+|Na regra constitucional pertinente, a idade rural diferenciada deve ser relacionada ao enquadramento legal.|O redutor não é atributo genérico de quem mora fora da cidade.
-|O fato de exercer trabalho urbano em qualquer dia da vida impede necessariamente toda aposentadoria rural ou híbrida.|É preciso analisar períodos, regras e modalidade, sem vedação genérica absoluta.
+|A aposentadoria híbrida exige examinar combinação de períodos conforme sua disciplina.|Não deve ser confundida automaticamente com aposentadoria exclusiva de segurado especial.
-|A ausência de registro no CNIS prova de modo absoluto que nenhuma atividade rural ocorreu.|A prova e as regras de reconhecimento precisam ser consideradas.
+|Economia familiar envolve condições legais sobre trabalho do grupo e atividade.|Não é sinônimo de qualquer empreendimento rural de grande porte.
-|Toda contratação de pessoa no campo gera automaticamente o mesmo enquadramento para contratante e contratado.|As posições e categorias previdenciárias podem ser diferentes.
+|O início de prova material deve ser avaliado em conjunto com os demais elementos admitidos.|Um documento não é analisado isoladamente sem contexto temporal e familiar.
-|Comprovar atividade rural dispensa a análise da idade exigida.|Atividade e idade são requisitos diferentes.
''')
add('B11-S13','p','arts.57–58; EC103/2019,arts.19 e21','A aposentadoria especial protege hipóteses legais de efetiva exposição, com prova e regras temporais próprias.','Nome do cargo não substitui descrição de exposição a agentes nocivos.',r'''
+|O reconhecimento de tempo especial exige examinar exposição efetiva e prova prevista na norma.|Enquadramento não decorre hoje apenas do título profissional.
-|Todo trabalho cansativo é automaticamente atividade especial para aposentadoria.|É preciso exposição e enquadramento nos critérios normativos.
+|PPP e laudo técnico têm funções relevantes na comprovação de condições de trabalho.|A documentação deve guardar relação com agentes, períodos e atividade.
-|A simples entrega de EPI garante sempre, para qualquer agente e circunstância, afastamento da especialidade.|A eficácia e a disciplina jurídica da exposição precisam ser analisadas; não há conclusão universal pelo fornecimento.
+|As regras de concessão devem considerar a data e o regime anterior ou posterior à reforma.|A EC103 introduziu critérios próprios, inclusive para transição.
-|A reforma manteve para todos os casos novos aposentadoria especial sem qualquer requisito etário ou de pontos.|As hipóteses posteriores e de transição exigem examinar os novos requisitos.
+|Carência e tempo de efetiva exposição são conceitos diferentes.|Cumprir um não implica automaticamente cumprir o outro.
-|Tempo em ambiente nocivo pode ser inventado apenas para completar a quantidade necessária.|O período precisa de prova e enquadramento legal.
+|Ruído exige atenção aos limites, metodologia e período da exposição.|A avaliação não pode ser resolvida por um valor abstrato sem referência temporal.
-|Qualquer adicional trabalhista de insalubridade prova automaticamente todos os requisitos previdenciários.|Os critérios trabalhistas e previdenciários não se identificam integralmente.
+|Na análise de conversão de tempo especial, o marco da EC103 é relevante.|A conversão possui disciplina temporal própria.
-|Aposentadoria especial é benefício assistencial que independe de filiação.|É prestação previdenciária do regime, com requisitos legais.
''',['ec'])
add('B11-S14','p','arts.42–47; EC103,art.26','Incapacidade permanente exige impossibilidade de reabilitação para atividade que assegure subsistência.','Incapacidade para uma profissão pode permitir reabilitação e não prova automaticamente incapacidade permanente.',r'''
+|A incapacidade permanente deve ser distinguida da impossibilidade temporária para a atividade habitual.|A hipótese permanente envolve também a inviabilidade de reabilitação nos termos legais.
-|Qualquer doença diagnosticada gera automaticamente aposentadoria por incapacidade permanente.|Doença e incapacidade previdenciária não são equivalentes.
+|A prova deve relacionar limitações e possibilidade de reabilitação.|A conclusão não se reduz ao nome da doença.
-|Ser incapaz para o trabalho habitual implica sempre ser incapaz para qualquer atividade que assegure subsistência.|Pode haver potencial de reabilitação para outra atividade.
+|Doença anterior à filiação exige analisar progressão ou agravamento quando se discute benefício.|Preexistência não autoriza conclusão automática sem a exceção legal.
-|O retorno voluntário à atividade é sempre indiferente à aposentadoria por incapacidade.|A lei atribui consequências ao retorno voluntário do aposentado.
+|Carência de incapacidade comum e hipóteses de dispensa devem ser diferenciadas.|Acidente e situações legais podem mudar o requisito contributivo.
-|A aposentadoria por incapacidade sempre tem coeficiente idêntico independentemente da causa.|A EC103 diferencia hipóteses, inclusive acidente do trabalho e doença ocupacional.
+|A assistência permanente de outra pessoa pode ser relevante para adicional na hipótese legal própria.|O art.45 não se confunde com adicional genérico de qualquer aposentadoria.
-|Todo aposentado por idade tem automaticamente direito ao adicional do art.45.|O adicional legal se relaciona à aposentadoria por incapacidade e requisitos próprios.
+|A convocação a exame deve observar as isenções e alterações legais vigentes.|Não se deve usar regras antigas de revisão como se fossem universais.
-|O pagamento do benefício torna juridicamente impossível qualquer recuperação da capacidade.|A lei prevê tratamento de recuperação, retorno e revisão nas hipóteses cabíveis.
''',['ec'])
add('B11-S15','p','arts.59–63','Incapacidade temporária protege afastamento laboral nas condições da espécie e da categoria.','Um laudo de diagnóstico deve explicar repercussão funcional no trabalho habitual.',r'''
+|O benefício por incapacidade temporária exige incapacidade para o trabalho ou atividade habitual na hipótese legal.|Diagnóstico clínico, sozinho, não prova todo requisito previdenciário.
-|Auxílio por incapacidade temporária é devido a qualquer pessoa saudável que deseje interromper o trabalho.|O risco protegido exige incapacidade e os demais requisitos.
+|Para empregado, há disciplina específica dos primeiros quinze dias de afastamento.|Não se aplica indistintamente a todas as categorias a mesma obrigação da empresa.
-|O INSS paga necessariamente ao empregado qualquer primeiro dia de afastamento por doença, sem examinar a duração.|A lei distingue período inicial a cargo da empresa e início do benefício.
+|A data de início da incapacidade e a data de requerimento têm funções distintas.|Podem influenciar a análise da qualidade, da carência e dos efeitos financeiros.
-|Retornar ao trabalho e continuar recebendo incapacidade temporária são sempre situações livres de consequência.|O benefício exige afastamento, observadas regras de atividade e efeitos do retorno.
+|Reabilitação pode ser relevante quando a recuperação para a atividade habitual é inviável.|O sistema não impõe aposentadoria permanente automática a toda limitação habitual.
-|Acidente comum nunca pode dispensar carência de incapacidade temporária.|A lei contempla acidente de qualquer natureza na dispensa pertinente.
+|A renda do benefício possui cálculo e limite legal específicos.|Não equivale necessariamente ao último salário integral.
-|A ausência de carência por acidente elimina a necessidade de demonstrar incapacidade.|A dispensa contributiva não dispensa o evento protegido.
+|Havendo várias atividades, é preciso identificar em quais existe incapacidade segundo a regra aplicável.|O exame deve guardar relação com as atividades concretas.
-|Incapacidade temporária e auxílio-acidente são nomes diferentes do mesmo benefício.|O primeiro substitui renda em afastamento; o segundo indeniza redução após consolidação de lesões.
''')
add('B11-S16','p','art.86','Auxílio-acidente é indenização por sequela consolidada que reduz capacidade para o trabalho habitual.','Após a consolidação, a pessoa trabalha com redução funcional: não é necessário estar totalmente incapaz.',r'''
+|O auxílio-acidente tem natureza indenizatória.|É diferente de benefício substitutivo pago pelo afastamento temporário.
-|O auxílio-acidente exige incapacidade total e permanente para qualquer trabalho.|A hipótese é redução da capacidade habitual após consolidação de lesões.
+|Acidente de qualquer natureza pode originar a hipótese legal de auxílio-acidente.|Não se limita, por definição, ao acidente do trabalho.
-|Toda categoria de segurado tem necessariamente direito ao auxílio-acidente.|A cobertura legal da espécie possui delimitação por categoria.
+|Empregado doméstico deve ser considerado na cobertura atual da espécie.|Não se deve repetir lista antiga que o excluía genericamente.
-|O contribuinte individual recebe auxílio-acidente automaticamente nas mesmas condições de empregado.|A cobertura legal não é universal para todas as categorias.
+|O retorno ao trabalho não é incompatível, por si só, com a natureza indenizatória do auxílio-acidente.|O benefício não pressupõe afastamento integral contínuo.
-|A pessoa pode acumular livremente auxílio-acidente e aposentadoria na regra atual.|Há vedação legal de acumulação com aposentadoria.
+|O benefício independe de carência.|Outros requisitos, inclusive sequela e redução laboral, permanecem necessários.
-|Uma lesão ainda não consolidada e sem redução posterior já prova todo requisito do auxílio-acidente.|Consolidação e repercussão funcional integram a hipótese.
+|O percentual próprio da espécie não deve ser confundido com o da incapacidade temporária.|Os benefícios têm cálculos diferentes.
-|O auxílio-acidente se transmite aos herdeiros como benefício vitalício próprio deles.|É benefício do segurado, não pensão hereditária.
''')
add('B11-S17','p','arts.19–23','Acidente do trabalho e doenças ocupacionais exigem nexo e enquadramento, incluindo equiparações legais.','Evento no trabalho e doença relacionada à atividade devem ser examinados por critérios próprios.',r'''
+|Doença profissional e doença do trabalho podem integrar proteção acidentária nos termos legais.|O art.20 disciplina doenças relacionadas ao exercício e às condições do trabalho.
-|Somente uma queda súbita pode ser considerada acidente do trabalho.|Há doenças ocupacionais e hipóteses equiparadas previstas em lei.
+|Nexo entre atividade e agravo é elemento relevante no enquadramento.|Coincidência temporal isolada não substitui a análise causal exigida.
-|Toda doença degenerativa é automaticamente profissional pelo simples fato de surgir durante emprego.|A lei delimita exclusões e admite exame de hipóteses legais específicas, sem automatismo.
+|A CAT comunica o evento, mas não substitui todo o exame do nexo e dos requisitos.|Comunicação e reconhecimento previdenciário não são atos idênticos.
-|Sem CAT emitida pela empresa, nenhum outro legitimado pode comunicar acidente.|A lei admite comunicação por outros sujeitos quando a empresa não o faz.
+|A legislação contempla hipóteses de equiparação além do evento típico.|O art.21 deve ser estudado para não reduzir a proteção ao acidente estrito.
-|Doença profissional e doença do trabalho são sempre sinônimos perfeitos sem distinção conceitual.|Há distinção entre doença peculiar à atividade e condições especiais em que o trabalho é realizado.
+|A data do acidente em doença ocupacional tem disciplina legal própria.|O art.23 define referências pertinentes e não permite escolher data arbitrária.
-|O reconhecimento do acidente prova automaticamente todos os requisitos de qualquer espécie de benefício.|O benefício depende também de incapacidade, sequela ou outro evento da hipótese.
+|Concausa pode ter relevância nas hipóteses previstas na legislação.|O trabalho não precisa ser tratado sempre como causa única e exclusiva para todo enquadramento.
-|Um evento fora do estabelecimento nunca pode receber equiparação legal a acidente do trabalho.|A lei contempla situações fora do local estrito, a serem verificadas.
''')
add('B11-S18','mat','ADIs2110/2111; IN188/2025; Lei8.213,arts.71–73','Salário-maternidade protege afastamento por eventos legais e atualmente é aplicado sem carência pelo INSS.','A adoção pode gerar salário-maternidade; não se resume ao parto da empregada.',r'''
+|Parto, adoção e guarda para adoção são eventos que podem ensejar salário-maternidade.|Cada hipótese depende das condições legais correspondentes.
-|Somente mulher empregada com carteira assinada pode receber salário-maternidade.|O benefício abrange outras categorias e hipóteses legalmente previstas.
+|O INSS aplica isenção de carência conforme ADIs2110/2111 e IN188/2025.|A regra antiga de dez contribuições não pode ser apresentada indistintamente como atual.
-|A isenção de carência transforma o salário-maternidade em benefício assistencial sem vínculo previdenciário.|A natureza continua previdenciária e a qualidade de segurado precisa ser examinada.
+|A duração geral de cento e vinte dias deve ser distinguida de hipóteses especiais de extensão.|A legislação contém situações específicas; não se deve afirmar que inexiste qualquer exceção.
-|Nascimento de gêmeos gera automaticamente dois salários-maternidade simultâneos para a mesma pessoa pelo mesmo evento.|Parto de mais de uma criança não multiplica o benefício dessa forma.
+|O afastamento da atividade integra a finalidade de substituição de renda do salário-maternidade.|Continuar trabalhando deve ser analisado à luz da disciplina de afastamento.
-|Uma pessoa segurada que adota nunca pode ter direito porque não ocorreu gestação própria.|Adoção e guarda para adoção são hipóteses protegidas.
+|A morte do titular pode permitir pagamento do período restante a cônjuge ou companheiro que satisfaça as condições legais.|Não se trata de transmissão genérica a qualquer herdeiro.
-|Toda questão histórica que exigia carência mantém necessariamente o mesmo gabarito sob a orientação aplicada em2026.|A correção atual precisa considerar decisões e atos posteriores, preservando o contexto histórico.
+|Forma de pagamento e cálculo podem variar conforme a categoria do segurado.|Não há uma única fórmula fundada no último salário para todos.
-|Salário-maternidade e licença trabalhista são conceitos integralmente idênticos em qualquer situação.|Benefício previdenciário e afastamento trabalhista são institutos relacionados, mas distintos.
''',['p'])
add('B11-S19','p','arts.65–70','Salário-família é pago nas categorias e condições legais por dependentes qualificados e limite de renda.','Ter filho não dispensa verificar idade ou invalidez, renda e condição do segurado.',r'''
+|Salário-família exige examinar limite de remuneração e categoria coberta.|O benefício não é universal para todo segurado com filhos.
-|Contribuinte individual recebe salário-família em qualquer faixa de renda apenas por ter filho.|A categoria e o limite legal não podem ser ignorados.
+|A idade de quatorze anos é referência legal para filho ou equiparado, ressalvada invalidez nos termos da lei.|Não é a idade genérica de vinte e um anos usada em outra relação de dependência.
-|Todo filho universitário de vinte e três anos garante salário-família sem outra condição.|Universidade não substitui a hipótese legal de idade ou invalidez.
+|A apresentação de documentos e condições de acompanhamento previstas em lei é relevante ao pagamento.|Não basta afirmar verbalmente a existência de filho em qualquer situação.
-|Salário-família exige sempre cento e oitenta contribuições de carência.|A prestação independe de carência.
+|Empregado doméstico integra a cobertura atual da espécie.|A legislação atual não deve ser substituída por resumos anteriores à inclusão da categoria.
-|O valor da cota pode ser inventado sem indicar ano, pois nunca muda.|Limites e cotas monetárias são atualizados e exigem referência temporal.
+|Se ambos os pais preenchem os requisitos legais, a análise não se resolve por proibição genérica a um deles.|A legislação admite percepção conforme as condições de cada segurado.
-|Salário-família é aposentadoria especial concedida a cada filho.|É prestação familiar com natureza e disciplina próprias.
+|A cessação de condição do filho pode influenciar a continuidade da cota.|Idade, invalidez e demais fatos devem ser acompanhados.
-|O direito à cota continua automaticamente para todos os sucessores após a morte do filho.|A prestação depende das condições do dependente que a origina.
''')
add('B11-S20','p','arts.74–79; EC103,art.23','Pensão por morte exige óbito, dependência e condições previdenciárias do instituidor.','A ausência de carência não significa duração vitalícia para todo cônjuge.',r'''
+|A pensão por morte é devida a dependentes, conforme as condições legais.|Não é aposentadoria própria do falecido transferida sem regras.
-|Pensão por morte exige carência geral de cento e oitenta contribuições.|A espécie independe de carência, sem eliminar outros requisitos.
+|A qualidade do segurado na morte ou hipótese legal que preserve direito precisa ser analisada.|A perda da qualidade não encerra o exame quando já existia direito à aposentadoria na forma legal.
-|Todo cônjuge recebe necessariamente pensão vitalícia, qualquer que seja idade e situação.|A duração varia conforme requisitos, eventos e hipóteses legais.
+|Duração da pensão e carência são questões diferentes.|Número de contribuições e duração da união podem influenciar duração sem criar carência de concessão.
-|A existência de pai economicamente dependente elimina o direito do cônjuge da classe anterior.|A ordem de classes do art.16 deve ser respeitada.
+|A data do requerimento pode influenciar o início dos efeitos financeiros conforme a categoria e os prazos legais.|Não se deve presumir a mesma data financeira para qualquer pedido tardio.
-|A pensão posterior à reforma vale sempre cem por cento de qualquer aposentadoria do instituidor.|A EC103 prevê cálculo e hipóteses específicas que exigem análise.
+|A perda da condição de dependente pode extinguir sua cota nos termos legais.|A pensão não é herança patrimonial irrestrita.
-|Condenação por homicídio doloso contra o segurado nunca afeta a pensão do autor.|A lei prevê exclusão nas condições pertinentes.
+|Filho universitário não recebe extensão automática do RGPS até vinte e quatro anos só pela matrícula.|Aplica-se a condição legal de dependência, não uma regra acadêmica genérica.
-|Todos os parentes herdeiros civis recebem cotas independentemente das classes previdenciárias.|Herança civil e dependência previdenciária são regimes diferentes.
''',['ec'])
add('B11-S21','p','art.80; regras posteriores à MP871/2019','Auxílio-reclusão protege dependentes de segurado de baixa renda, nas condições legais atuais.','O preso não é o destinatário do pagamento aos dependentes.',r'''
+|O auxílio-reclusão é benefício destinado a dependentes, não uma remuneração paga ao preso.|A prestação protege dependentes do segurado na hipótese legal.
-|Qualquer pessoa presa recebe pessoalmente auxílio-reclusão automaticamente.|Há requisitos relativos ao segurado, dependentes, renda, regime e contribuições.
+|Na regra atual pertinente, exige-se carência de vinte e quatro contribuições.|Não se deve usar genericamente a antiga dispensa como regra atual.
-|A renda dos dependentes substitui sempre, por si só, o critério legal de baixa renda do segurado.|A lei disciplina a aferição da renda do segurado e sua forma de cálculo.
+|O regime fechado é requisito relevante na disciplina atual da espécie.|Não se pode prometer benefício por qualquer modalidade de prisão sem examinar a norma temporal.
-|O limite de baixa renda pode ser fixado livremente pelo requerente.|O valor e o critério decorrem da norma vigente e do ano aplicável.
+|Manutenção da prisão deve ser comprovada conforme o procedimento legal.|A proteção depende da continuidade das condições da hipótese.
-|Qualidade de segurado é irrelevante porque a prestação é assistencial.|O auxílio-reclusão é previdenciário e exige análise do vínculo protegido.
+|A acumulação com remuneração e outros benefícios deve ser verificada segundo a disciplina legal.|A espécie possui condições negativas e vedações próprias.
-|Todo dependente civil do preso recebe, mesmo havendo classe previdenciária preferencial.|O rol e as classes do art.16 precisam ser respeitados.
+|A data da prisão importa para definir o regime jurídico do benefício.|Mudanças normativas não podem ser ignoradas em questões históricas.
-|Após perda da qualidade, a regra de reaproveitamento para auxílio-reclusão é sempre uma única contribuição.|O art.27-A e a carência pertinente exigem análise específica, inclusive a metade legal.
''')
add('B11-S22','p','art.40;art.101; regras de pagamento','Abono anual e pagamento mensal possuem requisitos e períodos próprios.','Receber benefício por parte do ano pode produzir abono proporcional conforme a espécie.',r'''
+|O abono anual é devido nas hipóteses de benefícios previstas no art.40.|Não é serviço de reabilitação nem pagamento genérico a toda pessoa cadastrada.
-|O BPC gera automaticamente décimo terceiro por integrar o RGPS.|BPC é assistencial e não possui abono anual nessa regra.
+|O tempo de percepção do benefício no ano pode influenciar o abono proporcional.|Não se presume valor integral sem examinar duração e espécie.
-|Todo beneficiário recebe abono anual em valor idêntico, qualquer que seja a renda e o período.|Base e proporcionalidade são relevantes.
+|Abono anual não deve ser confundido com reajuste anual.|Um é pagamento adicional previsto; outro atualiza valor mensal.
-|O direito ao abono elimina as condições de manutenção do benefício principal.|Manutenção, cessação e obrigações legais continuam relevantes.
+|Descontos em benefícios exigem fundamento e limites legais.|O pagamento não autoriza qualquer desconto arbitrário.
-|É possível ceder livremente qualquer prestação previdenciária sem restrição legal.|A proteção dos benefícios e as hipóteses de disposição têm limites normativos.
+|A comprovação de fatos que afetam o direito integra a administração do benefício.|Óbito ou cessação de condição não podem ser ignorados.
-|A data de um crédito bancário sempre altera a data jurídica de início do benefício.|Crédito e início jurídico são marcos distintos.
+|Informações sobre pagamento devem distinguir valor bruto, descontos e valor líquido.|São grandezas diferentes e relevantes para conferir o crédito.
-|O calendário de pagamento de qualquer ano pode ser inventado a partir de memória de calendário antigo.|Calendário é informação atual que exige consulta oficial e referência do ano.
''')
add('B12-S01','p','art.15','Qualidade de segurado é o vínculo de proteção, mantido em hipóteses legais mesmo sem novas contribuições.','Uma pessoa pode manter qualidade após parar de contribuir sem ganhar meses novos de carência.',r'''
+|A cessação de contribuição não causa sempre perda imediata da qualidade.|A lei estabelece hipóteses de manutenção sem contribuições.
-|A qualidade só existe no dia exato em que se paga uma guia.|A proteção não se limita ao instante do pagamento.
+|Período de graça deve ser analisado conforme a hipótese do art.15.|Não existe um prazo único para todos os segurados.
-|Manter qualidade acrescenta automaticamente uma contribuição mensal à carência.|Proteção e contagem de contribuições são institutos diferentes.
+|Durante o prazo legal de manutenção, preservam-se direitos nas condições da lei.|O art.15 protege o vínculo sem dispensar requisitos específicos das prestações.
-|Ter qualidade significa cumprir a idade de aposentadoria.|Qualidade e idade são requisitos diferentes.
+|O gozo de benefício, ressalvada a exceção legal do auxílio-acidente, tem disciplina de manutenção sem limite de prazo.|A exceção impede tratar todo benefício como manutenção ilimitada.
-|Receber somente auxílio-acidente garante sempre qualidade por tempo ilimitado.|O art.15 exclui essa espécie da hipótese de manutenção ilimitada pelo benefício.
+|O segurado facultativo tem prazo de manutenção próprio.|Sua regra não deve ser igualada automaticamente à do segurado obrigatório que cessa atividade.
-|Qualidade é uma avaliação de excelência no desempenho profissional.|É condição jurídica de proteção previdenciária, não nota de produtividade.
+|Na análise de pensão, a situação do instituidor no óbito é relevante.|Qualidade ou exceção legal precisa ser relacionada ao fato gerador.
-|Qualidade de dependente e qualidade de segurado são expressões com mesmo conteúdo.|Dependência e filiação são posições distintas.
+|A nova atividade remunerada enquadrada pode gerar filiação obrigatória conforme a lei.|Aquisição deve ser ligada à categoria e aos fatos da atividade.
-|O nome autônomo no contrato sempre afasta filiação obrigatória.|A atividade real e o enquadramento legal devem ser examinados.
+|Doença diagnosticada durante proteção exige verificar quando começou a incapacidade para benefício correspondente.|Diagnóstico e início do risco previdenciário não são marcos sempre coincidentes.
-|A regra de graça afasta qualquer exame de carência em incapacidade comum.|A manutenção da qualidade não apaga a exigência de carência quando aplicável.
+|A prova do fim do vínculo pode ajudar a calcular o período de manutenção.|É necessário situar o início da interrupção e a hipótese legal.
-|Qualidade é mantida para qualquer pessoa que apenas tenha um número de inscrição antigo.|Cadastro antigo não assegura proteção indefinida.
+|O restabelecimento da qualidade e o reaproveitamento de contribuições devem ser avaliados separadamente.|Retomar o vínculo não resolve automaticamente toda carência.
-|O cálculo do período de graça pode ignorar a categoria do segurado.|A categoria é determinante para a hipótese e para prorrogações.
''')
add('B12-S02','p','art.15,I–VI','O art.15 prevê prazos diferentes de manutenção conforme situação e categoria.','Compare cessação de atividade obrigatória, serviço militar e interrupção de facultativo.',r'''
+|A cessação da atividade remunerada abrangida pelo RGPS pode gerar manutenção por até doze meses na hipótese legal.|O incisoII contém a regra-base, sem dispensar exame de prorrogações.
-|O facultativo possui sempre vinte e quatro meses de graça, mesmo sem regra adicional.|A regra do facultativo prevê seis meses, não esse prazo genérico.
+|Para segurado facultativo, a manutenção por até seis meses após cessar contribuições é hipótese expressa.|Não se importam automaticamente extensões destinadas a outra situação.
-|O segurado incorporado às Forças Armadas tem sempre seis meses após licenciamento.|A hipótese específica prevê três meses após o licenciamento.
+|A incorporação para serviço militar possui manutenção por até três meses após licenciamento.|É prazo distinto da cessação comum de atividade.
-|Após livramento, o segurado recluso tem prazo-base de apenas três dias.|A lei prevê até doze meses após o livramento.
+|O segregado compulsoriamente pode manter qualidade por até doze meses após cessar a segregação.|O marco final da segregação deve ser identificado.
-|A manutenção do recluso é contada exclusivamente da data do primeiro emprego, não do livramento.|A hipótese legal relaciona o prazo ao livramento.
+|Gozo de benefício, exceto auxílio-acidente, pode manter qualidade sem limite na hipótese do incisoI.|A exceção legal deve aparecer no estudo da regra.
-|Todos os períodos de graça se iniciam necessariamente no dia de nascimento do segurado.|Os marcos decorrem dos eventos especificados no art.15.
+|Doze, seis e três meses correspondem a hipóteses diferentes e não são opções livres do interessado.|A situação jurídica define o prazo aplicável.
-|A regra de doze meses elimina qualquer necessidade de examinar extensões.|Os parágrafos podem ampliar o prazo nas condições legais.
+|A data do último vínculo não resolve, sozinha, uma hipótese de segregação compulsória.|O marco pertinente deve ser relacionado ao fato jurídico específico.
-|Toda pessoa que recebe orientação do serviço social mantém qualidade ilimitada por esse atendimento.|A hipótese do incisoI trata do gozo de benefício, com sua exceção, e não de qualquer atendimento.
+|Recebimento exclusivo de auxílio-acidente exige cuidado, pois não sustenta a manutenção ilimitada do incisoI.|O tipo de benefício importa para a conclusão.
-|A lei permite somar livremente prazos de hipóteses diferentes sem qualquer análise dos fatos.|A soma não pode ser feita mecanicamente entre situações diversas.
+|O período de graça preserva vínculo sem produzir automaticamente recolhimentos válidos.|A manutenção não equivale a contribuição mensal.
-|O fim do prazo-base basta para ignorar o marco legal de perda do §4º.|A perda tem disciplina de vencimento própria a considerar.
+|O calendário da hipótese deve ser construído com datas comprovadas.|Sem marcos, não se pode inventar a data de perda.
-|Uma interrupção contributiva curta demonstra necessariamente perda da qualidade.|Pode estar integralmente coberta pelo prazo legal de manutenção.
''')
add('B12-S03','p','art.15,§§1º–2º','Prorrogações dependem de requisitos; não são bônus automáticos para toda interrupção.','Mais de cento e vinte contribuições sem perda e desemprego comprovado são condições que devem ser verificadas.',r'''
+|O prazo do incisoII pode chegar a vinte e quatro meses se houver mais de cento e vinte contribuições sem interrupção que cause perda da qualidade.|A prorrogação exige o histórico contributivo previsto no §1º.
-|Exatamente doze contribuições sempre garantem a extensão por longo histórico.|A regra se refere a mais de cento e vinte, observada ausência de perda.
+|A ausência de perda durante o histórico exigido integra a análise da prorrogação contributiva.|Não basta somar competências sem examinar o vínculo jurídico ao longo do tempo.
-|Qualquer intervalo entre pagamentos impede a extensão, ainda que a qualidade tenha sido mantida.|O critério legal é interrupção que acarrete perda da qualidade, não qualquer pausa.
+|A situação de desemprego comprovada pode acrescentar doze meses na hipótese legal.|A extensão exige os requisitos pertinentes, não mera alegação abstrata.
-|Trabalhador que deixou atividade por vontade própria recebe automaticamente toda extensão sem prova.|É necessário examinar o fato e os requisitos da hipótese de desemprego.
+|As duas extensões do art.15 podem produzir até trinta e seis meses na situação que reúna os requisitos.|O resultado depende da combinação efetivamente demonstrada.
-|Trinta e seis meses é prazo mínimo de graça de todo filiado ao RGPS.|É possibilidade condicionada, não piso universal.
+|A falta de um novo registro de trabalho não deve ser confundida, isoladamente, com prova completa de desemprego em qualquer caso.|É necessário avaliar os elementos probatórios admissíveis.
-|O facultativo pode importar automaticamente todas as prorrogações do incisoII.|A regra própria do facultativo não autoriza essa extensão mecânica.
+|Um histórico com cento e cinquenta contribuições pode exigir análise de eventual perda entre os períodos.|A quantidade total não resolve sozinha a condição do §1º.
-|Quem possui apenas cento e vinte contribuições preenche necessariamente a expressão legal mais de cento e vinte.|Mais de cento e vinte exige ultrapassar esse número.
+|A prova de desemprego deve ser relacionada ao período discutido.|Uma condição em data alheia não comprova automaticamente a interrupção examinada.
-|A extensão altera carência de incapacidade de doze para trinta e seis contribuições.|Extensão de qualidade e carência são requisitos diferentes.
+|A manutenção prolongada pode permitir examinar fato gerador ocorrido sem recolhimentos recentes.|Os demais requisitos da prestação continuam relevantes.
-|A prorrogação concede automaticamente benefício por incapacidade a pessoa capaz.|Manter qualidade não demonstra ocorrência do risco.
+|Antes de fixar perda, é preciso verificar se há prorrogação cabível e comprovada.|Ignorar extensões pode levar a marco incorreto.
-|Uma declaração genérica de longo vínculo permite dispensar todos os registros contributivos.|O requisito demanda comprovação nos termos aplicáveis.
+|O mesmo caso pode exigir separar extensão por contribuições e extensão por desemprego.|São fundamentos distintos com requisitos próprios.
-|A concessão de uma extensão transforma o segurado obrigatório em facultativo.|A extensão protege qualidade; não altera por si só a categoria original.
''')
add('B12-S04','p','art.15,§4º;art.27-A','A perda tem marco legal e não se confunde com simples ausência de nova guia.','Após determinar o período de graça, examine o vencimento que a lei usa para a perda.',r'''
+|A perda da qualidade ocorre segundo o marco previsto no §4º do art.15.|Não é necessariamente o último dia do prazo-base isoladamente considerado.
-|A qualidade é perdida automaticamente na primeira hora do mês sem pagamento.|A lei prevê manutenção e marco próprio de perda.
+|O art.15 relaciona a perda ao dia seguinte ao vencimento da contribuição referente ao mês posterior ao fim do período de graça.|O calendário deve respeitar a sequência normativa e a hipótese aplicável.
-|A perda é sempre retroativa ao primeiro dia de filiação.|Perda posterior não apaga o vínculo que existiu nos períodos anteriores.
+|Adquirir novamente qualidade não equivale a recuperar automaticamente toda carência.|É preciso verificar a regra de reaproveitamento quando aplicável.
-|Toda pessoa que volta ao regime recebe imediatamente qualquer benefício independentemente de preexistência.|Risco, carência, qualidade e regras de preexistência precisam ser avaliados.
+|Benefícios cujo direito admite perda da qualidade em condições próprias exigem exame específico.|Não se aplica impedimento universal a toda aposentadoria.
-|A perda cancela o número de inscrição e obriga sempre criar identidade previdenciária nova.|Cadastro e qualidade são conceitos diferentes.
+|Dados de início e fim de atividade auxiliam a verificar aquisição e manutenção do vínculo.|A análise não deve se basear em memória imprecisa de datas.
-|Novo pagamento válido e início de atividade são sempre fatos equivalentes para qualquer categoria.|A forma de filiação depende da categoria.
+|No facultativo, a regularidade do primeiro recolhimento tem relevância na filiação.|Não se atribui retroação automática por qualquer pagamento atrasado.
-|Uma guia paga após o fato gerador sempre assegura cobertura retroativa sem limites.|É preciso observar filiação, atraso, categoria e regra aplicável.
+|Carência antiga pode permanecer registrada mesmo quando seu reaproveitamento depende de novas contribuições.|Perda da qualidade não equivale a apagar os registros.
-|O app deve excluir todo histórico de contribuições quando identifica perda de qualidade.|A análise jurídica exige preservar dados; não apagar informação histórica.
+|A data do fato gerador deve ser comparada ao período de proteção.|O benefício depende da situação relevante quando ocorre o risco, ressalvadas exceções legais.
-|A prova de qualidade atual demonstra necessariamente que ela existia em qualquer data passada.|A condição deve ser aferida no marco temporal pertinente.
+|Uma questão de perda de qualidade deve informar fatos suficientes para calcular o prazo.|Não se pode inventar datas ou assumir prorrogação ausente.
-|A perda significa que toda contribuição recolhida deve ser devolvida automaticamente.|Não há essa consequência genérica pela simples perda.
+|Identificar o marco legal evita confundir mês de cobertura com data de vencimento.|As duas referências podem não coincidir.
-|O restabelecimento dispensa classificar o segurado na nova atividade.|A categoria determina a formação e os efeitos do vínculo.
''')
add('B12-S05','p','arts.15,24–27-A','Qualidade, carência e tempo de contribuição são eixos próprios e devem ser demonstrados separadamente.','Uma pessoa pode manter qualidade sem acumular novas contribuições durante a graça.',r'''
+|Manter qualidade não significa somar automaticamente meses de carência.|A graça preserva vínculo, não cria pagamento fictício.
-|Carência e tempo de contribuição são sempre números idênticos em qualquer situação.|Regras de contagem e finalidades podem produzir resultados distintos.
+|Ter idade de aposentadoria não prova carência cumprida.|Idade é requisito diferente do número mínimo contributivo.
-|Inscrição antiga garante qualidade atual por prazo ilimitado.|Cadastro e proteção ativa não são sinônimos.
+|Recolhimento em atraso exige examinar se vale para a finalidade discutida.|Aproveitamento como tempo não resolve automaticamente sua carência.
-|Um pagamento referente a dois vínculos no mesmo mês duplica sempre a carência mensal.|Concomitância não produz automaticamente dois meses de carência.
+|Uma prestação sem carência ainda pode exigir qualidade e ocorrência do evento protegido.|Dispensa de um requisito não é dispensa de todos.
-|A expressão segurado de baixa renda é outra forma de dizer carência cumprida.|Baixa renda e requisito contributivo são critérios diferentes.
+|O histórico contributivo e os períodos de proteção devem ser organizados separadamente.|A distinção permite verificar cada requisito com seu fundamento.
-|A ausência de trabalho remunerado elimina imediatamente qualquer vínculo protegido.|Há manutenção legal e filiação facultativa nas condições pertinentes.
+|No retorno após perda, a qualidade nova e o reaproveitamento antigo podem depender de análises diferentes.|O art.27-A não pode ser substituído por mera confirmação de inscrição.
-|Uma contribuição mensal sempre equivale a um ano de tempo de contribuição.|Unidades e contagem temporal não podem ser confundidas.
+|Qualidade de segurado deve ser aferida no momento juridicamente relevante para a prestação.|O marco depende do evento e das regras da espécie.
-|A existência de carência suficiente permite conceder incapacidade a pessoa sem incapacidade.|O risco protegido é requisito autônomo.
+|Um mesmo documento pode contribuir para a prova de mais de um requisito sem torná-los idênticos.|A prova compartilhada não elimina diferenças conceituais.
-|O correto é resolver qualidade, carência e tempo com uma única marca de aprovado, sem fundamentação.|Cada requisito deve ter conclusão e fundamento identificáveis.
''')
add('B13-S01','p','art.88','Serviço social esclarece direitos e meios de exercê-los, contribuindo para acesso à proteção.','O atendimento identifica barreira de informação e orienta o cidadão sobre como exercer direito.',r'''
+|Esclarecer direitos sociais e meios de exercê-los integra a finalidade do serviço social.|O art.88 relaciona orientação e acesso à proteção.
-|O serviço social tem por única atribuição calcular alíquotas empresariais.|Sua finalidade legal é social e orientadora, não exclusivamente tributária.
+|A Lei8.213 dá prioridade aos segurados em benefício por incapacidade temporária e atenção especial a aposentados e pensionistas no serviço social.|A prioridade do art.88,§1º, não transforma o serviço em atendimento exclusivo desses públicos.
-|Informar um direito significa concedê-lo automaticamente sem análise dos requisitos.|Orientação e concessão são atos diferentes.
+|O art.88,§5º, incluído em2025, contempla orientação sobre direitos ligados à incapacidade nos equipamentos de saúde em que atua serviço social.|A Lei15.288/2025 ampliou expressamente a referência à orientação nesses locais, nos termos do ato aplicável.
-|A atuação depende sempre de o interessado já possuir aposentadoria concedida.|O serviço não se limita a aposentados que já recebem benefício.
+|Identificar a situação do usuário ajuda a oferecer orientação adequada.|Requisitos e caminhos variam conforme a demanda concreta.
-|A atividade permite inventar benefício não previsto em lei para atender necessidade percebida.|A orientação deve respeitar os direitos e instrumentos existentes.
+|Linguagem acessível contribui para o exercício informado dos direitos.|Compreensão é parte relevante da orientação.
-|Desconhecimento do usuário autoriza negar informação como forma de punição.|O papel do serviço é esclarecer, não sancionar falta de conhecimento.
+|Serviço social e reabilitação profissional possuem funções diferentes, embora possam se articular.|Um esclarece e facilita acesso; a outra atua na habilitação/reabilitação conforme sua disciplina.
-|Atendimento social pode ser apresentado como garantia de deferimento de qualquer pedido.|A decisão depende da análise legal e probatória da prestação.
''')
add('B13-S02','p','arts.89–93','Habilitação e reabilitação visam meios de readaptação profissional e social, conforme elegibilidade.','Pessoa com limitação funcional pode receber orientação para nova atividade compatível.',r'''
+|A reabilitação busca proporcionar meios de readaptação profissional e social.|A finalidade inclui participação no trabalho e no contexto de vida.
-|A reabilitação consiste exclusivamente no pagamento de aposentadoria definitiva.|É serviço com meios de readaptação, não sinônimo de aposentadoria.
+|Próteses, órteses e instrumentos de auxílio podem integrar a prestação nas hipóteses legais.|Os meios devem ter pertinência com a habilitação ou reabilitação.
-|Todo atendimento de reabilitação garante contratação imediata por qualquer empregador escolhido.|A prestação não equivale a promessa individual de emprego.
+|O programa deve considerar capacidade residual e possibilidades de readaptação.|O foco não é exigir desempenho impossível de pessoa com limitação.
-|Se há limitação para a atividade habitual, a única solução legal é aposentadoria imediata.|Pode haver reabilitação para outra atividade que assegure subsistência.
+|Certificado ao final pode indicar atividades que o beneficiário poderá exercer.|O documento não transforma qualquer trabalho em atividade compatível sem exame.
-|Reabilitação profissional e fiscalização tributária têm objeto idêntico.|São atividades de naturezas e finalidades distintas.
+|O estudo do serviço exige distinguir fase de avaliação, programa e conclusão.|As etapas têm funções próprias.
-|A pessoa pode exigir qualquer equipamento sem relação com a necessidade de reabilitação.|A prestação depende de indicação e pertinência legal ao processo.
+|A participação do beneficiário deve ser analisada conforme obrigações e ressalvas legais.|A lei contém disciplina própria, inclusive sobre procedimentos facultativos.
-|A reabilitação autoriza impor cirurgia obrigatória a todo beneficiário.|Cirurgia e transfusão de sangue têm ressalvas de facultatividade na disciplina legal pertinente.
''')
add('B13-S03','p','arts.26,89–93 e101','Beneficiários e meios do serviço devem ser identificados sem importar carência de aposentadoria.','Serviço de reabilitação não pode ser negado apenas porque o candidato não tem180 contribuições.',r'''
+|A reabilitação profissional independe de carência legal.|Isso não elimina critérios de encaminhamento e elegibilidade do serviço.
-|O serviço exige sempre a mesma carência da aposentadoria programada.|A lei prevê a reabilitação entre hipóteses sem carência.
+|O art.90 prevê reabilitação obrigatória aos segurados, inclusive aposentados, e aos dependentes na medida das possibilidades do órgão.|A disciplina distingue a obrigatoriedade para segurados e a condição de atendimento de dependentes.
-|Todo dependente tem garantia incondicional do serviço, independentemente das possibilidades do órgão da Previdência.|O art.90 condiciona a extensão aos dependentes à medida das possibilidades do órgão.
+|O transporte e outros meios pertinentes podem integrar o apoio à reabilitação nas condições legais.|A prestação compreende meios relacionados ao processo, não qualquer despesa desejada.
-|O fornecimento de órtese significa que toda futura despesa pessoal será assumida sem limites.|Os meios são vinculados à necessidade e à previsão do serviço.
+|A natureza do serviço deve ser distinguida da cota de contratação de reabilitados prevista na lei.|Prestação individual e obrigação empresarial são instrumentos relacionados, mas diferentes.
-|O certificado de reabilitação elimina automaticamente todas as limitações de saúde da pessoa.|A conclusão registra capacidade para atividades indicadas; não significa cura universal.
+|A continuidade de benefício por incapacidade durante reabilitação exige analisar a espécie e as regras legais.|Não se presume cessação automática apenas por encaminhamento ao programa.
-|A inscrição no programa transforma qualquer ausência voluntária em causa automática de benefício vitalício.|Há obrigações e consequências a verificar conforme o procedimento.
+|Meios de reabilitação devem guardar relação com o objetivo profissional e social do serviço.|A finalidade orienta a pertinência dos instrumentos fornecidos.
-|Toda atividade terapêutica, particular ou pública, é por definição o mesmo serviço previdenciário de reabilitação.|O serviço do RGPS tem enquadramento e disciplina próprios.
''')
add('B14-S01','tal','Lei7.070/1982,arts.1º–3º; Lei8.686/1993;Lei12.190/2010','Talidomida tem pensão especial própria, vitalícia e intransferível, sem confusão com aposentadoria do RGPS.','Deficiência decorrente da substância exige comprovação específica; não basta qualquer deficiência.',r'''
+|A pensão especial da talidomida depende da deficiência relacionada ao uso da substância.|O nexo específico é parte da hipótese legal.
-|Qualquer deficiência física, sem relação com talidomida, gera automaticamente a pensão da Lei7.070.|A lei se refere à síndrome e à comprovação pertinente.
+|A pensão possui caráter vitalício e intransferível nos termos legais.|Não deve ser tratada como pensão por morte comum do RGPS.
-|Falecido o titular, seus herdeiros passam automaticamente a receber a mesma pensão vitalícia.|A intransferibilidade impede essa sucessão genérica do benefício.
+|O grau de dependência resultante da deformidade participa da disciplina de cálculo.|O valor não é simplesmente a última remuneração do beneficiário.
-|O cálculo deve ignorar totalmente a avaliação da deficiência e dependência.|A avaliação é relevante para a graduação prevista na legislação.
+|A pensão especial e a indenização por dano moral da legislação específica são institutos distintos.|Uma prestação mensal e uma indenização não se confundem apenas pela mesma origem.
-|A concessão exige sempre a carência de180 contribuições da aposentadoria.|A pensão especial não é aposentadoria contributiva comum.
+|Acumulação deve ser examinada nas regras próprias e nas exceções legais.|Não se pode presumir vedação ou autorização universal.
-|O valor nominal de um ponto em qualquer resumo antigo é necessariamente o valor vigente hoje.|Atualizações de valores exigem consulta ao período correspondente.
+|A perícia e a documentação devem sustentar o nexo e os critérios de avaliação.|A mera declaração informal não prova todos os pressupostos.
-|A Lei7.070 regula a pensão dos seringueiros da Segunda Guerra.|Essa hipótese é tratada por legislação diferente, especialmente a Lei7.986.
''')
add('B14-S02','ser','arts.1º–5º;ADCT,art.54','A pensão de seringueiro está ligada ao esforço de guerra amazônico e à situação de carência econômica.','Não confunda carência econômica dessa lei com número de contribuições mensais do RGPS.',r'''
+|O benefício protege seringueiros das hipóteses do esforço de guerra na região Amazônica.|Não abrange automaticamente todo extrativista de qualquer período.
-|Qualquer pessoa que produza borracha em2026 recebe a pensão apenas por essa atividade.|A lei vincula a hipótese ao contexto e requisitos históricos determinados.
+|A Lei7.986 prevê pensão mensal vitalícia equivalente a dois salários mínimos.|O parâmetro legal difere de outras pensões especiais.
-|A carência exigida nessa hipótese significa obrigatoriamente180 contribuições mensais.|A carência tratada na lei é situação econômica de subsistência, não a carência contributiva comum.
+|Dependentes podem receber transferência se comprovarem o estado de carência nos termos legais.|A transferibilidade é condicionada, diferente de pensões personalíssimas.
-|A pensão de seringueiro é necessariamente intransferível em toda hipótese.|O art.2º admite transferência a dependentes com carência comprovada.
+|A prova do serviço deve ter início de prova material na disciplina atual do art.3º.|A lei não admite genericamente prova exclusivamente testemunhal.
-|Uma lista informal de testemunhas dispensa sempre qualquer início de prova material.|A comprovação deve observar a exigência legal pertinente.
+|A Defensoria Pública pode atuar na justificação judicial do necessitado conforme a lei.|Não se deve atribuir automaticamente a função à instituição indicada em redação antiga revogada.
-|O benefício depende apenas de filiação recente como contribuinte individual.|Filiação recente não prova serviço histórico nem carência econômica.
+|A Lei7.986 prevê instrução do pedido e comprovação da condição do beneficiário.|O benefício não nasce de mera autodeclaração sem exame.
-|O requisito de carência econômica e a condição de segurado especial são conceitos idênticos.|São critérios de regimes e finalidades diferentes.
''')
add('B14-S03','exc','arts.1º–6º e13','Pensão especial de ex-combatente tem regime próprio ligado à participação na Segunda Guerra e aos dependentes legais.','Não transforme qualquer serviço militar em participação de ex-combatente para essa lei.',r'''
+|A Lei8.059 disciplina pensão especial de ex-combatentes da Segunda Guerra e dependentes.|A norma tem contexto e público próprios.
-|Todo militar que prestou serviço obrigatório em qualquer ano se torna ex-combatente dessa lei.|A condição depende da hipótese legal específica, não de qualquer serviço militar.
+|O parâmetro legal da pensão é a pensão militar deixada por segundo-tenente das Forças Armadas.|Não é automaticamente um salário mínimo ou teto do RGPS.
-|A pensão é calculada sempre como percentual da média contributiva do RGPS do requerente.|O regime especial possui parâmetro próprio.
+|A condição de dependente deve ser verificada segundo a disciplina da Lei8.059.|Não se importa integralmente o rol do art.16 sem examinar a lei especial.
-|Por ser especial, o benefício dispensa comprovar a condição de ex-combatente.|O enquadramento e sua prova integram a concessão.
+|Reversão e redistribuição de cotas têm disciplina legal própria.|Não se decide transmissão apenas pelas regras da herança civil.
-|A pessoa pode acumular qualquer pagamento dos cofres públicos sem analisar vedações e exceções.|A lei contém limites e ressalvas que devem ser examinados.
+|A comprovação documental deve relacionar o requerente ao público da norma.|Narrativa genérica de serviço nacional não encerra a análise.
-|Essa pensão é o mesmo benefício devido às vítimas de Caruaru.|Fatos geradores e leis instituidoras são diferentes.
+|A legislação especial deve ser lida em conjunto com normas constitucionais e alterações pertinentes.|A data e o regime aplicável influenciam a análise.
-|Pensão especial significa que qualquer parente recebe cota sem habilitação.|A condição legal e a habilitação do dependente são necessárias.
''')
add('B14-S04','car','arts.1º–5º','A pensão de Caruaru tem destinatários e evento delimitados pela Lei9.422.','É necessário ligar o óbito à contaminação do período e instituição previstos.',r'''
+|A Lei9.422 trata de dependentes das vítimas fatais da contaminação em hemodiálise especificada.|Não é pensão geral para toda pessoa submetida a hemodiálise.
-|Todo paciente renal do Brasil recebe automaticamente pensão da Lei9.422.|A lei delimita fato, local, período e beneficiários.
+|O evento legal se refere ao Instituto de Doenças Renais de Caruaru, em fevereiro e março de1996.|A delimitação é parte do enquadramento.
-|O simples diagnóstico de doença renal em2026 comprova a hipótese de Caruaru.|É necessário nexo com o evento histórico legalmente previsto.
+|A lei prevê valor de um salário mínimo e retroatividade à data do óbito na hipótese definida.|O parâmetro difere da pensão de seringueiro.
-|O valor legal é sempre dois salários mínimos porque toda pensão especial tem esse valor.|Cada pensão especial tem disciplina de valor própria.
+|Mais de um pensionista habilitado atrai a remissão legal ao art.77 no que couber.|A pluralidade não multiplica livremente a pensão sem regra.
-|Após a morte do último beneficiário, a pensão é transmitida indefinidamente aos herdeiros.|O art.4º prevê extinção e não transmissão ao sucessor.
+|Atestado de óbito, causa relacionada e prontuário têm relevância na comprovação.|A lei especifica os elementos probatórios pertinentes.
-|A mera condição de vizinho da vítima basta para integrar o rol legal.|É preciso uma das qualificações previstas na lei.
+|A lei contempla consequência se houver condenação dos proprietários a pagar pensão ou indenização aos dependentes.|O art.5º deve ser considerado ao examinar eventual duplicidade reparatória.
-|A comprovação do fato gerador pode ser substituída por notícia de acidente nuclear em Goiânia.|Goiânia e Caruaru são eventos e regimes jurídicos diferentes.
''')
add('B14-S05','ces','arts.1º–4º','A pensão do Césio137 é indenização especial personalíssima vinculada ao acidente de Goiânia.','O dependente não recebe transmissão automática de benefício personalíssimo do titular falecido.',r'''
+|A pensão especial da Lei9.425 liga-se às vítimas do acidente com Césio137 em Goiânia.|Não é benefício universal por qualquer exposição a radiação.
-|Todo trabalhador que utiliza equipamento de radiologia recebe essa pensão automaticamente.|A hipótese é o acidente e os enquadramentos determinados pela lei.
+|A lei caracteriza a pensão como personalíssima e não transmissível ao cônjuge ou herdeiros.|Não é pensão por morte comum do RGPS.
-|Com a morte do titular, o cônjuge passa a receber integralmente a mesma pensão por simples herança.|A regra expressa é de não transmissão.
+|A lei estabelece categorias de valor relacionadas à situação das vítimas.|Não se aplica valor único livremente escolhido.
-|A avaliação da exposição e das sequelas é irrelevante para o enquadramento.|A lei prevê classificação e comprovação por junta médica oficial.
+|A comprovação envolve junta médica oficial ligada à Fundação Leide das Neves, nos termos legais.|A mera narrativa informal não encerra os requisitos.
-|Os valores históricos em UFIR podem ser tratados como moeda atual sem qualquer conversão ou atualização.|A lei disciplina base temporal e atualização; não se inventa equivalência atual.
+|A lei contempla situação de descendentes nascidos com anomalia decorrente da exposição comprovada dos genitores.|Trata-se de hipótese própria, não de transmissão hereditária da pensão do genitor.
-|A previsão para descendentes prova que toda pensão do titular se transmite a qualquer filho.|Direito próprio por enquadramento e sucessão do benefício são institutos diferentes.
+|Havendo condenação da União por responsabilidade civil, a lei prevê dedução do montante da pensão da condenação.|A interação reparatória tem disciplina expressa.
-|A pensão da Lei9.425 exige sempre a carência contributiva de aposentadoria.|A hipótese é indenizatória especial, não aposentadoria contributiva comum.
''')
add('B14-S06','ani','arts.1º,3º–6º,10,13 e19','A reparação do anistiado político tem caráter indenizatório e modalidades próprias.','Prestação única e prestação mensal permanente não são escolhidas sem observar enquadramento e critérios.',r'''
+|A Lei10.559 disciplina reparação econômica de caráter indenizatório ao anistiado político.|Não é aposentadoria comum por idade do RGPS.
-|A condição de anistiado político nasce automaticamente de qualquer divergência com o governo.|É necessário enquadramento legal e reconhecimento segundo o procedimento.
+|A reparação pode ocorrer em prestação única ou mensal permanente e continuada, conforme a hipótese legal.|As modalidades têm requisitos e critérios próprios.
-|Prestação única e prestação mensal devem sempre ser pagas cumulativamente pelo mesmo fundamento.|A lei distingue modalidades, sem autorizar cumulação universal.
+|A relação com atividade laboral é relevante para a modalidade mensal na disciplina legal.|O cálculo não é uma escolha sem vínculo com fatos e parâmetros.
-|O valor mensal corresponde sempre a um salário mínimo, sem exceção.|A lei utiliza critérios de remuneração e limites próprios.
+|O falecimento pode ensejar transferência a dependentes nos termos dos regimes legais indicados.|Não se confunde com herança irrestrita a qualquer sucessor.
-|Todo amigo do anistiado pode receber reparação mensal por declaração particular.|É necessária condição legal de dependente e habilitação.
+|A falsidade dos motivos do reconhecimento pode levar à nulidade, com direito de defesa.|A lei prevê procedimento e consequências para irregularidade.
-|Comprovar falsidade autoriza afastar qualquer defesa e motivação no procedimento.|As garantias de defesa são expressamente relevantes.
+|O art.19 prevê continuidade de pagamentos excepcionais anteriores até substituição pelo regime da lei.|É transição de regimes, não prova de que todos os benefícios são idênticos.
-|O cadastro no INSS, sozinho, equivale a portaria reconhecendo anistia.|Inscrição previdenciária não substitui reconhecimento da condição especial.
''')
add('B14-S07','han','arts.1º–3º;Lei14.736/2023;Decreto12.312/2024','A pensão de hanseníase indeniza isolamento ou internação compulsória nas hipóteses legais, hoje abrangendo filhos separados.','Não confunda ter hanseníase com comprovar o tratamento compulsório ou a separação prevista na lei.',r'''
+|O diagnóstico de hanseníase, sozinho, não prova todos os requisitos da pensão especial.|É necessário enquadramento nas hipóteses de isolamento, internação ou separação legalmente protegidas.
-|Qualquer pessoa que teve hanseníase em qualquer data recebe automaticamente a pensão.|A lei delimita situação histórica e condições específicas.
+|A legislação atual inclui filhos separados dos genitores em razão do isolamento ou internação destes, nas condições legais.|A ampliação da Lei14.736/2023 deve aparecer na teoria atual.
-|O filho só pode receber por transmissão hereditária da pensão do genitor.|A lei institui hipótese própria de indenização ao filho separado; a pensão é intransferível.
+|A prestação é mensal, vitalícia e intransferível nos termos legais.|Não é pensão por morte comum.
-|A intransferibilidade autoriza automaticamente pagamento aos netos após morte do titular.|A característica impede essa sucessão genérica.
+|As condições de compulsoriedade e o marco histórico precisam ser comprovados.|Não se presume a hipótese a partir do nome de uma doença.
-|O antigo valor nominal de um resumo permanece obrigatoriamente inalterado apesar da reforma legal.|A legislação atual alterou o parâmetro e exige observar o mínimo legal.
+|A Lei14.736 alterou tanto o valor quanto o público beneficiário da proteção.|Usar apenas a redação original de2007 deixa lacunas relevantes.
-|A pensão especial pode sempre acumular indenização da União pelos mesmos fatos sem ressalva.|A lei trata de vedação e direito de opção na interação com indenização pelos mesmos fatos.
+|Regulamentação e procedimento atuais devem ser conferidos, incluindo o Decreto12.312/2024.|A aplicação exige regras operacionais além do resumo histórico.
-|Receber essa pensão transforma automaticamente o titular em segurado obrigatório do RGPS.|Prestação indenizatória e filiação por atividade não se confundem.
''',['hanfaq'])
add('B14-S08','zik','Lei13.985/2020 histórica;Lei15.156/2025,arts.1º–3º','O estudo de Zika deve separar a referência histórica do edital2022 da ampliação legislativa de2025.','Uma questão explicitamente sobre a lei de2020 não deve ser corrigida como se descrevesse sem aviso o regime de2025.',r'''
+|A Lei13.985/2020 integra a referência histórica de conteúdos do edital2022.|A base histórica deve ser identificada como tal.
-|O programa histórico de2022 permite ignorar toda alteração posterior sobre proteção ligada ao Zika.|O estudo atual precisa confrontar o regime antigo com a legislação superveniente.
+|A Lei15.156/2025 dispõe sobre indenização e pensão especial à pessoa com deficiência permanente associada à síndrome congênita do Zika.|A norma ampliou a proteção e precisa ser incluída no repertório atualizado.
-|A nova proteção se refere a qualquer resfriado ocorrido em pessoa que mora em área com mosquito.|É necessário nexo com deficiência permanente decorrente da síndrome congênita associada ao vírus.
+|Indenização por dano moral e pensão especial mensal são prestações de natureza e periodicidade diferentes.|Não devem ser somadas conceitualmente como se fossem uma única renda mensal.
-|A pensão nova equivale necessariamente ao valor de três mínimos da antiga referência, sem conferir a Lei15.156.|A lei nova possui parâmetros próprios; não se transporta automaticamente o valor histórico.
+|A data e a lei expressamente adotadas pelo item são necessárias para interpretar seu gabarito.|A correção deve distinguir histórico e atual, preservando ambas as informações.
-|Uma alteração normativa autoriza reescrever sem registro as respostas antigas do estudante.|Versões e contexto histórico devem ser preservados, com atualização explícita.
''',['zikh'])
add('B14-S09','car','comparação:Leis7.986,9.422,9.425,11.520 e15.156','Pensões especiais precisam ser comparadas por titular, fato gerador, cálculo, acumulação e transmissão.','Ser especial não significa possuir os mesmos requisitos de toda outra pensão especial.',r'''
+|A transferibilidade da pensão de seringueiro não pode ser atribuída automaticamente à pensão do Césio137.|A primeira admite dependentes carentes; a segunda é personalíssima e intransmissível.
-|Toda pensão especial possui necessariamente o mesmo valor e os mesmos destinatários.|Cada lei define público, cálculo e condições próprias.
+|Em Caruaru, a lei dirige a prestação aos dependentes definidos das vítimas fatais.|O titular imediato difere de benefício personalíssimo concedido à própria vítima.
-|O direito próprio do filho separado na lei de hanseníase significa herdar a pensão intransferível do genitor.|A hipótese própria de indenização não é transmissão por morte.
+|Uma análise de acumulação deve identificar quais prestações e quais fatos reparatórios estão envolvidos.|As leis podem prever vedações, dedução ou opção em contextos distintos.
-|Usar apenas a palavra pensão dispensa verificar se a prestação é previdenciária, assistencial ou indenizatória.|Natureza e lei instituidora importam para a solução.
+|Valores históricos devem ser apresentados com seu regime e data, sem inventar valores monetários atuais.|Índices e alterações legais podem afetar o pagamento.
-|A cessação e transmissão de todas as pensões são resolvidas apenas pela ordem de herdeiros do Código Civil.|As leis especiais estabelecem condições que não se confundem com sucessão civil.
''',['ser','ces','han','zik'])

def main():
    manifest=json.loads((ROOT/'data/curriculum-plan.json').read_text())
    planned={r['id_planejamento']:r for r in manifest['assuntos']}
    lessons=[];alltexts=set();allids=set()
    for planid,(src,locator,core,example,qs,extra) in DATA.items():
        b,s=planid.split('-')[1:];point=planned[planid];expected=point['meta_questoes_autorais']
        assert len(qs)==expected,(planid,len(qs),expected)
        lessonid='v17-'+planid.lower()
        sources=[{**SOURCES[k],'locator':locator,'checkedAt':'2026-10-27'} for k in [src]+extra]
        # A teoria reúne fundamentos explicativos redigidos em cada ângulo, sem expor gabaritos/itens.
        teachings=list(dict.fromkeys(q['explanation'] for q in qs))
        lesson={'id':lessonid,'d':'prev','title':point['assunto'],'core':core,'rule':' '.join(teachings),'example':example,'contrast':'Separe o fato gerador, os requisitos de acesso, o cálculo e os efeitos. Um requisito demonstrado não prova automaticamente os demais.','limit':'O enquadramento depende da hipótese e do marco temporal indicados. Consulte as fontes e não transporte regras históricas sem verificar alterações.','source':src if src in ['p','r'] else 'p','sources':sources,'minutes':40,'block':point['bloco'],'planId':planid,'subtopics':[core,locator],'questions':[]}
        for i,q in enumerate(qs,1):
            qid=lessonid+f'-q{i:03d}';assert qid not in allids;assert q['text'] not in alltexts,(planid,q['text']);allids.add(qid);alltexts.add(q['text'])
            lesson['questions'].append({'id':qid,**q,'kind':'autoral','version':1,'difficulty':'basico' if i<=4 else 'intermediario' if i<=expected*0.8 else 'avancado','family':planid+f'-angulo-{i:02d}','microtopic':planid,'sourceRef':sources[0],'mode':'fixacao' if i<=expected//4 else 'reserva' if i>expected-expected//4 else 'treino'})
        lessons.append(lesson)
    assert len(lessons)==52
    assert sum(len(l['questions']) for l in lessons)==660
    output={'lessons':lessons,'sources':[{'id':k,**v} for k,v in SOURCES.items()],'editorial':{'version':'1.0.0','method':'JARVIS v1.7','date':'2026-10-27','authorship':'JARVIS AUTORAL; itens redigidos individualmente, sem reprodução de prova','count':660,'topics':52,'validation':'Quotas, IDs e textos únicos, tipos e metadados verificados por Python; conferência editorial de fontes sem revisão jurídica independente.','notes':['Correção temporal incluída para salário-maternidade sem carência conforme IN188/2025 e ADIs2110/2111.','Hanseníase contempla Lei14.736/2023 e regulamentação2024.','Zika separa Lei13.985/2020 histórica e Lei15.156/2025.','Dificuldade é rótulo editorial inicial; não há calibração psicométrica.','Questões autorais não são itens reais CEBRASPE.']}}
    out=ROOT/'data/prev-beneficios.json';out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'path':str(out),'lessons':len(lessons),'questions':660,'uniqueTexts':len(alltexts),'uniqueIds':len(allids)},ensure_ascii=False))
if __name__=='__main__':main()
