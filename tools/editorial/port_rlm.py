"""Itens autorais individuais; Python organiza e confere quotas e exemplos lógicos.
Não clona enunciados nem expande textos para atingir quantidade.
"""
import json,random,re,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PLAN=ROOT/'data/curriculum-plan.json'
plan=json.loads(PLAN.read_text())
sources={
 'pt':{'title':'Manual de Redação da Presidência da República — portal oficial','url':'https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica','locator':'Orientações de gramática, redação e comunicações oficiais; exemplos autorais'},
 'volp':{'title':'Vocabulário Ortográfico da Língua Portuguesa — ABL','url':'https://www.academia.org.br/nossa-lingua/busca-no-vocabulario','locator':'Ortografia e vocabulário; regras do Acordo Ortográfico'},
 'd9758':{'title':'Decreto 9.758/2019 — Câmara dos Deputados','url':'https://www2.camara.leg.br/legin/fed/decret/2019/decreto-9758-11-abril-2019-787965-publicacaooriginal-157737-pe.html','locator':'Arts. 1º a 4º — âmbito, tratamento e endereçamento'},
 'logic':{'title':'Demonstração autoral — lógica e matemática elementar','url':'https://cdn.cebraspe.org.br/concursos/inss_22/arquivos/ED_1_INSS_22_ABERTURA.PDF','locator':'Programa de RLM; gabaritos demonstrados na explicação, não retirados do edital'}
}
DATA={};THEORY={}
def topic(k,core,theory,items,source='pt'):
 parsed=[]
 for line in items.strip().splitlines():
  a,t,e=line.split('|');assert a in ['C','E'];parsed.append((t,a=='C',e))
 DATA[k]=(parsed,source);THEORY[k]=(core,theory)

topic('PORT-B01-S01','Leitura literal recupera informação expressa e preserva seus limites.','Localize sujeitos, condições, números, datas e restrições. Uma paráfrase pode usar palavras diferentes e manter a informação. Não transforme alguns em todos, possibilidade em certeza ou ausência de informação em negação.', '''
C|Texto: “A unidade atende presencialmente às terças e quintas, mediante agendamento.” O texto exige agendamento para esse atendimento presencial.|A condição “mediante agendamento” restringe o atendimento informado.
E|Texto: “Três dos cinco guichês funcionaram pela manhã.” Todos os guichês funcionaram nesse período.|Três de cinco não equivalem à totalidade dos guichês.
C|Texto: “O portal permite consultar o pedido, mas não substitui a análise documental.” A consulta eletrônica não elimina a análise dos documentos.|A oposição explicita o limite da consulta eletrônica.
E|Texto: “A entrega poderá ocorrer até sexta-feira.” A entrega ocorrerá obrigatoriamente na sexta-feira.|“Poderá” indica possibilidade; “até” estabelece limite, não data obrigatória.
E|Texto: “O curso é gratuito para servidores inscritos.” Qualquer pessoa pode participar gratuitamente.|A gratuidade foi atribuída aos servidores inscritos, não a qualquer pessoa.
C|Texto: “O atendimento foi suspenso porque faltou energia.” A falta de energia é apresentada como causa da suspensão.|A oração introduzida por “porque” fornece a causa expressa.
C|Texto: “O relatório abrange apenas os pedidos de janeiro.” Pedidos de fevereiro ficam fora do recorte declarado.|“Apenas” limita o conjunto aos pedidos de janeiro.
E|Texto: “Nem todos os processos estavam completos.” Nenhum processo estava completo.|Negar a totalidade não equivale a negar todos os casos.
C|Texto: “A nova sala tem vinte lugares, dez a mais que a anterior.” A sala anterior tinha dez lugares.|A comparação expressa permite subtrair dez de vinte.
E|Texto: “O sistema voltou a funcionar às 14h.” A pane começou às 14h.|O horário informado é de restabelecimento, não de início da pane.
E|Texto: “Os visitantes devem apresentar documento.” O texto autoriza documento de qualquer espécie, sem restrição possível.|Não se pode acrescentar uma autorização irrestrita que o trecho não formula.
C|Texto: “O aviso será publicado depois da reunião.” A publicação é posterior à reunião.|“Depois” estabelece essa sequência temporal.
E|Texto: “O serviço funciona em duas cidades.” O serviço funciona somente nessas duas cidades de todo o país.|A palavra “somente” acrescenta exclusividade não expressa.
C|Texto: “A resposta foi enviada a todos os solicitantes.” Nenhum solicitante ficou fora do envio afirmado.|“Todos” abrange o conjunto de solicitantes mencionado.
C|Texto: “O projeto foi aprovado com duas ressalvas.” A aprovação não ocorreu sem ressalvas.|O complemento registra duas restrições à aprovação.
E|Texto: “O uso do aplicativo é opcional.” O trecho proíbe o atendimento presencial.|A opcionalidade do aplicativo não enuncia proibição de outro canal.
''')
topic('PORT-B01-S02','Inferir é concluir com apoio no texto; extrapolar é acrescentar algo sem apoio suficiente.','Diferencie pressupostos, consequências necessárias e hipóteses apenas possíveis. Palavras como voltou, ainda e deixou de trazem informações implícitas. Um caso isolado não sustenta regra universal; sucessão temporal não prova causalidade.', '''
C|Ao afirmar “A agência voltou a abrir aos sábados”, o enunciador pressupõe que ela já abria aos sábados anteriormente.|O verbo “voltar” indica retomada de uma situação anterior.
E|“O atendimento melhorou após a troca do sistema” prova que a troca foi a única causa da melhora.|A sequência temporal não demonstra causa exclusiva.
E|Um texto relata que dois candidatos estudaram juntos e foram aprovados. Disso se conclui que estudar em grupo garante aprovação.|Dois casos não sustentam garantia universal.
C|Em “Mesmo com chuva, a equipe chegou”, apresenta-se a chuva como possível obstáculo superado.|A construção concessiva contrapõe obstáculo e resultado.
C|Se o aviso diz “Ainda há vagas”, pressupõe-se que havia vagas em momento anterior.|“Ainda” marca continuidade da situação.
E|A frase “A direção não confirmou o adiamento” permite concluir que a direção confirmou a manutenção da data.|Não confirmar uma hipótese não confirma automaticamente a oposta.
C|“O setor deixou de receber formulários em papel” pressupõe recebimento desses formulários antes da mudança.|“Deixar de” indica interrupção de prática anterior.
E|O autor cita uma crítica ao aplicativo. Logo, necessariamente concorda com essa crítica.|Citação e adesão são atos distintos; a posição depende do contexto.
C|Se todos os servidores do plantão fizeram o curso e Ana integra esse plantão, o texto permite concluir que Ana fez o curso.|A conclusão decorre da inclusão no conjunto universalmente descrito.
E|“Apenas candidatos inscritos acessaram a sala” significa que todos os inscritos acessaram a sala.|O trecho restringe quem acessou, sem garantir participação de todos os inscritos.
E|De “Alguns usuários preferem o canal remoto” conclui-se que a maioria o prefere.|“Alguns” não determina maioria.
C|Ao recomendar “Confirme o endereço antes de sair”, o texto trata a confirmação prévia como conduta desejável.|A forma imperativa exprime orientação, não relato de fato realizado.
C|“O resultado surpreendeu até os especialistas” sugere que a surpresa destes era menos esperada.|“Até” inclui elemento apresentado como extremo da escala contextual.
E|“O portal não é suficiente para eliminar filas” implica que o portal é inútil.|Insuficiência para resolver integralmente um problema não equivale a inutilidade.
C|Se “O documento só será emitido após a conferência”, a conferência aparece como condição necessária para a emissão.|“Só após” impede emissão anterior à condição indicada.
E|Em texto sem informação sobre o custo de um serviço, seu silêncio permite classificá-lo como gratuito.|Ausência de informação não constitui afirmação de gratuidade.
''')
topic('PORT-B01-S03','Tema é o assunto; tese é a posição defendida sobre ele.','Identifique o problema tratado, a afirmação central e os argumentos que a sustentam. Exemplo ilustra uma ideia sem provar automaticamente uma regra geral. Contra-argumento pode ser citado para refutação; conclusão deve se ligar às premissas.', '''
C|“A digitalização deve ampliar o acesso, pois reduz deslocamentos.” A defesa da ampliação do acesso por digitalização constitui a tese do trecho.|A posição defendida vem acompanhada de justificativa causal.
E|No enunciado “Filas no atendimento público”, há necessariamente uma tese completa.|A expressão apresenta um tema, sem posição argumentativa completa.
C|“Embora a ferramenta seja útil, não dispensa orientação humana.” O autor admite uma qualidade e limita seu alcance.|A concessão reconhece utilidade sem aceitar suficiência irrestrita.
E|Um exemplo de atendimento bem-sucedido prova, sozinho, que todas as unidades funcionam bem.|Exemplo individual não demonstra universalidade.
C|Em “Precisamos revisar o procedimento: três etapas são redundantes”, a redundância é usada como argumento para revisão.|A segunda parte justifica a proposta apresentada.
E|Todo texto argumentativo precisa empregar a palavra “portanto” para ter conclusão.|A relação conclusiva pode existir sem marcador explícito.
E|A apresentação de dados numéricos torna qualquer interpretação desses dados necessariamente correta.|A validade da conclusão depende da relação entre dados e inferência.
C|“Alguns defendem eliminar o atendimento presencial; essa solução excluiria pessoas sem internet.” A primeira posição é apresentada para contestação.|O segundo segmento formula objeção à proposta citada.
C|O assunto “acesso digital” pode sustentar teses opostas em textos distintos.|Tema comum não determina posição única.
E|Se o autor apresenta vantagem e desvantagem, não pode defender conclusão alguma.|Ponderação de argumentos é compatível com tese definida.
C|“Como os pedidos aumentaram, será necessário ampliar a equipe.” O crescimento da demanda fundamenta a proposta.|A oração causal funciona como argumento.
E|Título informativo substitui obrigatoriamente todos os argumentos do desenvolvimento.|O título pode orientar a leitura, mas não dispensa sustentação da tese.
C|Uma comparação entre dois modelos pode constituir estratégia argumentativa.|A comparação pode sustentar avaliação e escolha.
E|Confundir causa de um problema com medida para resolvê-lo preserva sempre a organização argumentativa.|Diagnóstico causal e proposta de solução têm funções diferentes.
C|“A proposta parece simples, mas seu custo a torna inviável.” A restrição introduzida por “mas” orienta a avaliação final.|A oposição destaca o obstáculo determinante da conclusão.
E|Reconhecer uma exceção equivale necessariamente a abandonar toda a tese defendida.|Uma tese pode admitir delimitações e exceções.
''')
topic('PORT-B01-S04','Tipologia descreve organização linguística; gênero corresponde a uma prática social de comunicação.','Narração relata acontecimentos; descrição caracteriza; exposição explica; argumentação defende posição; injunção orienta ação. Um gênero pode combinar tipos, com predominância de um deles. Formato e função não se reduzem ao tamanho do texto.', '''
C|“Abra o portal, escolha o serviço e confirme os dados.” O trecho apresenta organização predominantemente injuntiva.|A sequência orienta ações do destinatário.
E|Uma notícia não pode conter trechos narrativos, pois notícia e narração são classificações incompatíveis.|Gênero e tipo são níveis distintos e podem coexistir.
C|“A sala era ampla, clara e silenciosa.” Predomina a caracterização descritiva.|Os predicados apresentam atributos do ambiente.
E|A simples presença de um verbo no passado torna qualquer texto predominantemente narrativo.|A predominância depende da organização global, não de um verbo isolado.
C|Um artigo de opinião é gênero frequentemente associado à argumentação.|Sua função típica envolve defender uma posição.
C|“Primeiro chegou o pedido; depois a equipe verificou os anexos.” Há sequência temporal de acontecimentos.|A progressão de ações caracteriza segmento narrativo.
E|Textos expositivos exigem que o autor defenda uma opinião polêmica em todos os parágrafos.|A exposição tem como função central apresentar ou explicar conhecimento.
C|Um manual pode combinar explicação de conceitos e instruções de uso.|Gêneros reais admitem combinação de tipos textuais.
E|“O prazo é de dez dias” constitui obrigatoriamente uma narrativa completa.|A informação isolada não organiza sequência de acontecimentos.
E|Todo texto com números é científico e pertence ao mesmo gênero.|Números aparecem em gêneros diversos e não determinam classificação.
C|Uma carta de reclamação pode empregar descrição do problema como apoio a um pedido.|A descrição pode integrar finalidade comunicativa mais ampla.
C|A predominância tipológica é identificada pela função e pela organização do conjunto.|A classificação considera o desenvolvimento textual.
E|Uma receita culinária e uma lei são o mesmo gênero porque ambas podem orientar comportamentos.|Semelhança de tipo não elimina diferenças de situação social e gênero.
C|“A água evapora quando recebe energia suficiente” exemplifica explicação expositiva.|O trecho apresenta relação explicativa sobre um fenômeno.
E|Um anúncio deixa de ser anúncio se contiver uma pequena história.|A presença de narração não altera necessariamente sua função publicitária.
C|Vocabulário, interlocutores, suporte e finalidade ajudam a reconhecer o gênero.|Esses elementos integram a situação comunicativa.
''')
topic('PORT-B01-S05','Coesão cria vínculos entre partes do texto e referenciação permite recuperar seus participantes.','Pronomes e expressões nominais podem retomar antecedentes ou antecipar informação. Verifique gênero, número e compatibilidade semântica; proximidade não resolve toda referência. Anáfora retoma; catáfora antecipa; repetição controlada pode dar precisão.', '''
C|“O formulário chegou ontem. Ele será conferido hoje.” O pronome “ele” retoma “o formulário”.|A forma masculina singular e o sentido estabelecem a retomada.
E|Todo pronome retoma obrigatoriamente a palavra mais próxima no texto.|A referência depende da sintaxe e do sentido, além da proximidade.
C|“Só peço isto: confira o endereço.” “Isto” antecipa a orientação seguinte.|A referência voltada para informação posterior é catafórica.
E|Em “A diretora falou com a servidora sobre seu relatório”, “seu” elimina qualquer dúvida sobre a autora do relatório.|O possessivo pode gerar ambiguidade entre possíveis possuidoras.
C|“Os protocolos foram separados; esses documentos serão digitalizados.” A expressão nominal retoma os protocolos.|A reformulação lexical mantém a continuidade referencial.
C|Em “A equipe entregou o parecer, que foi aprovado”, “que” pode retomar “parecer”.|O relativo introduz comentário sobre o antecedente nominal.
E|Repetir um termo técnico é sempre defeito de coesão, mesmo quando evita ambiguidade.|A repetição pode preservar precisão e clareza.
E|“Maria informou Ana de que ela seria transferida” define de modo inequívoco quem será transferida.|O pronome admite mais de um referente feminino no contexto.
C|“O portal falhou. Esse problema atrasou os pedidos.” “Esse problema” encapsula o fato relatado.|A expressão transforma a ocorrência anterior em referente nominal.
E|A troca de “alguns pedidos” por “todos eles” preserva necessariamente a abrangência da referência.|“Todos” pode ampliar indevidamente o conjunto referido.
C|“João apresentou o comprovante e o arquivou.” O pronome átono pode recuperar “o comprovante”.|A construção fornece antecedente compatível para o objeto.
C|“A unidade, cuja equipe foi ampliada, reduziu a espera.” “Cuja” estabelece relação entre unidade e equipe.|O relativo possessivo relaciona o antecedente ao nome subsequente.
E|Na norma-padrão, é necessário escrever “cuja a equipe”.|Não se intercala artigo entre “cuja” e o substantivo que ela determina.
C|“Recebi o arquivo e a mensagem; aquela estava incompleta.” Pelo gênero, “aquela” não retoma naturalmente “arquivo”.|O demonstrativo feminino concorda com referente feminino.
E|Um texto sem pronomes não pode apresentar coesão referencial.|Repetições, sinônimos e expressões nominais também promovem referência.
C|A expressão “tal medida” exige que o leitor recupere uma medida identificável no contexto.|O demonstrativo depende de referência contextual.
''')
topic('PORT-B01-S06','Conectores articulam relações de sentido, não apenas ligam palavras.','Distinguir causa, consequência, conclusão, oposição, concessão, condição, finalidade, proporção, tempo e adição. A substituição depende do contexto e pode exigir mudança verbal. Não confundir “à medida que” com “na medida em que”.', '''
C|“O sistema falhou; portanto, a emissão foi adiada.” “Portanto” introduz conclusão ou consequência inferida.|O segundo segmento decorre do primeiro no encadeamento apresentado.
E|Em “Embora estivesse cansada, terminou a leitura”, “embora” exprime condição.|O conector apresenta concessão: obstáculo que não impede o resultado.
C|“Se houver vaga, o pedido será atendido.” O atendimento está condicionado à existência de vaga.|A oração introduzida por “se” expressa condição.
E|Trocar “porque” por “para que” sempre preserva a relação de causa.|“Para que” normalmente introduz finalidade, não causa.
C|“Estudou para compreender o procedimento.” O infinitivo introduz finalidade.|A compreensão é o objetivo da ação.
C|“Quanto mais revisava, menos confundia os termos.” Há relação proporcional entre as duas variações.|A correlação expressa progressão conjunta inversamente orientada.
E|“No entanto” estabelece, por definição, adição simples de argumentos.|A locução é adversativa e introduz oposição ou ressalva.
E|“Assim que chegou, consultou o protocolo.” A locução estabelece comparação.|A locução indica tempo e imediata sucessão.
C|“Não apenas leu, mas também resumiu.” A estrutura acrescenta uma segunda ação com realce.|A correlação tem valor aditivo.
E|“À medida que a fila crescia, aumentava a espera” usa “à medida que” com valor causal inequívoco.|A locução marca proporcionalidade entre crescimentos.
C|“A solicitação foi aceita, pois estava completa.” “Pois” introduz justificativa ou causa para a aceitação.|A segunda oração fundamenta a primeira.
E|A substituição de “ainda que” por “desde que” preserva sempre a concessão.|“Desde que” pode estabelecer condição ou tempo e altera a relação.
C|“Ou envie o arquivo, ou entregue a cópia.” A repetição de “ou” organiza alternativas.|A estrutura correlativa apresenta possibilidades alternativas.
C|“Conforme o aviso determina, a entrada será pela lateral.” O conector exprime conformidade.|A conduta é apresentada de acordo com o aviso.
E|“Caso falte documento, avise” afirma que a falta de documento já ocorreu.|A condição não confirma a ocorrência do fato hipotético.
C|Conectores semanticamente próximos podem exigir ajustes sintáticos ao serem substituídos.|Manutenção do sentido não garante encaixe gramatical idêntico.
''')
topic('PORT-B01-S07','Reescrever exige preservar simultaneamente correção, sentido e alcance.','Examine agentes, negações, quantificadores, relações lógicas, tempo verbal e ambiguidades. Voz passiva mantém relações de participação se construída adequadamente. Correção gramatical não assegura equivalência semântica.', '''
C|“A equipe conferiu os anexos” pode ser reescrita, sem mudar o agente, como “Os anexos foram conferidos pela equipe”.|A transformação passiva preserva agente, paciente e tempo.
E|“Nem todos compareceram” equivale a “Ninguém compareceu”.|A primeira nega universalidade; a segunda nega qualquer comparecimento.
E|“O pedido pode ser aceito” e “O pedido será aceito” apresentam o mesmo grau de certeza.|Possibilidade e afirmação futura diferem modalmente.
C|“A comissão analisará o caso amanhã” preserva a informação básica em “Amanhã, o caso será analisado pela comissão”.|Tempo, agente e objeto foram mantidos na passiva.
C|“O portal só aceita arquivos PDF” mantém sua restrição em “O portal aceita apenas arquivos PDF”.|As duas formulações limitam o formato aceito.
E|Trocar “alguns servidores” por “os servidores” mantém sempre a extensão do grupo.|O artigo definido pode generalizar ou identificar conjunto diferente.
C|“Não enviou o arquivo porque estava sem conexão” admite paráfrase causal: “Como estava sem conexão, não enviou o arquivo”.|A reordenação conserva a causa declarada.
E|“Estudou muito, mas errou” mantém a oposição em “Estudou muito, portanto errou”.|O conector conclusivo altera a relação entre estudo e erro.
C|“É necessário conferir os dados” pode ser reescrita como “A conferência dos dados é necessária”.|A nominalização mantém a obrigação geral expressa.
E|“Os usuários que agendaram serão atendidos” equivale necessariamente à versão com “que agendaram” entre vírgulas.|A pontuação pode alterar restrição para explicação.
C|“O atendimento começa às oito horas” preserva a indicação temporal em “Às oito horas, começa o atendimento”.|O deslocamento não altera o horário informado.
E|Uma frase gramaticalmente correta é, por isso, paráfrase fiel de qualquer frase sobre o mesmo assunto.|Correção e equivalência são critérios distintos.
C|“A resposta não foi enviada por Ana” não equivale obrigatoriamente a “Ana não enviou resposta alguma”.|A primeira nega autoria de uma resposta específica; a segunda tem alcance mais amplo.
E|“Até dez pessoas entrarão” significa exatamente “Dez pessoas entrarão”.|O limite máximo não garante ocupação total.
C|Na reescrita, trocar um pronome por seu referente pode aumentar a clareza sem mudar a informação.|A explicitação adequada preserva a referência.
E|Eliminar uma condição de uma autorização sempre preserva o sentido original.|A supressão pode ampliar a autorização.
''')
topic('PORT-B02-S01','Ortografia convencional e hífen precisam ser conferidos por regras e vocabulário.','Empregue por que em pergunta; porque em explicação; por quê ao final; porquê como substantivo. Mal opõe-se a bem; mau a bom. Em prefixação, vogais iguais costumam exigir hífen; vogais diferentes costumam uni-las; r e s podem duplicar. Observe exceções registradas no VOLP.', '''
C|Em “Não explicou por que faltou”, a expressão interrogativa indireta está corretamente escrita.|Pergunta indireta admite “por que” separado.
E|“O por que da decisão foi esclarecido” apresenta grafia adequada para o substantivo que significa motivo.|O substantivo é “porquê”, junto e acentuado.
C|“Você saiu cedo por quê?” emprega corretamente a forma no final da pergunta.|Antes da pausa final, a expressão interrogativa recebe acento.
C|“Não compareceu porque estava doente” emprega conjunção explicativa ou causal com grafia adequada.|A causa é introduzida por “porque”.
E|Em “Ele é um mal gestor”, “mal” foi corretamente usado como adjetivo oposto a bom.|O adjetivo é “mau”; “mal” pode ser advérbio oposto a bem.
C|“A equipe trabalhou mal” usa adequadamente a forma que se opõe a “bem”.|Nesse contexto “mal” modifica o verbo.
E|A grafia “auto-escola” corresponde à convenção atual do Acordo Ortográfico.|Vogais diferentes unem-se: “autoescola”.
C|“Micro-ondas” conserva hífen diante da repetição da vogal o.|Prefixo terminado em vogal diante da mesma vogal exige hífen nessa formação.
E|“Antisocial” é a grafia convencional da formação anti + social.|Diante de s, sem hífen nessa formação, duplica-se a consoante: “antissocial”.
E|O prefixo anti exige hífen em qualquer palavra, independentemente do elemento seguinte.|A regra depende do início do segundo elemento.
C|“Coautor” é grafado sem hífen na convenção atual.|O prefixo co aglutina-se nesse vocábulo.
C|“Ex-servidor” mantém hífen com o prefixo ex no sentido de estado anterior.|O hífen marca essa formação prefixal.
''','volp')
topic('PORT-B02-S02','Acentuação gráfica depende de tonicidade, terminação e encontros vocálicos.','Proparoxítonas são acentuadas. Observe oxítonas em a/e/o e paroxítonas nas terminações previstas. Hiatos com i/u tônicos têm condições próprias; ditongos abertos em paroxítonas perderam certos acentos. Diferencie pôde/pode, pôr/por e têm/tem.', '''
C|“Público” recebe acento por ser proparoxítona.|A sílaba tônica é a antepenúltima.
E|“Saída” é acentuada por ser proparoxítona.|O i tônico forma hiato; a palavra é paroxítona.
C|A grafia “ideia” dispensa o acento que existia no ditongo aberto de palavra paroxítona.|O Acordo suprimiu esse acento em paroxítonas.
E|Na convenção atual, “heroi” deve permanecer sem acento por terminar em i.|A forma correta é “herói”, oxítona com ditongo aberto ói.
C|Em “Ontem ela pôde entrar; hoje pode sair”, o circunflexo distingue o passado do presente.|“Pôde” é pretérito; “pode” é presente.
E|“Eles tem acesso” está corretamente acentuado para o plural.|A terceira pessoa plural é “têm”.
C|“País” e “pais” diferem na tonicidade e no sentido.|O acento marca hiato tônico em “país”.
E|O verbo “pôr” perdeu obrigatoriamente seu acento diferencial.|O acento de “pôr” foi mantido para distingui-lo da preposição “por”.
C|A grafia “voo” está de acordo com o Acordo Ortográfico.|Não se mantém o circunflexo do antigo encontro oo.
E|“Fácil” recebe acento por ser oxítona terminada em l.|É paroxítona terminada em l.
C|“Juiz” não recebe acento, enquanto “juízes” recebe.|No plural, o i tônico em hiato não forma sílaba com o z seguinte.
E|Todas as palavras com hiato recebem obrigatoriamente acento.|A acentuação de hiatos obedece a condições específicas.
''','volp')
topic('PORT-B02-S03','Uma classe de palavra é reconhecida pela função no contexto.','Substantivos nomeiam, adjetivos caracterizam, verbos indicam processos e estados. Advérbios modificam verbos/adjetivos/advérbios e orações; pronomes referem ou determinam; artigos determinam nomes. A mesma forma pode mudar de classe; preposições e conjunções articulam relações.', '''
C|Em “O atendimento rápido ajudou”, “rápido” caracteriza um substantivo e funciona como adjetivo.|O termo qualifica “atendimento”.
E|Em “Ela fala baixo”, “baixo” é obrigatoriamente substantivo.|A palavra modifica “fala”, com valor adverbial de modo.
C|Em “O amanhã preocupa”, “amanhã” foi substantivado pelo artigo.|O termo funciona como núcleo nominal.
E|A palavra “que” pertence sempre à mesma classe, em qualquer construção.|Pode ser pronome, conjunção e assumir outras funções conforme o contexto.
C|Em “Aquela unidade fechou”, “aquela” é pronome demonstrativo que determina o nome.|O demonstrativo acompanha “unidade”.
C|Em “A unidade fechou e a equipe saiu”, “e” coordena duas orações.|A conjunção liga segmentos coordenados.
E|“Com” em “falou com calma” é artigo definido.|“Com” é preposição que introduz a expressão de modo.
C|Em “Os dois chegaram”, o numeral participa da identificação quantitativa dos referentes.|“Dois” expressa quantidade definida.
E|Em “Recebi o relatório”, “o” é pronome pessoal átono que substitui o relatório.|Aqui “o” acompanha o nome e é artigo.
C|Em “Recebi-o ontem”, “o” é pronome pessoal que funciona como complemento verbal.|O clítico substitui um referente masculino singular.
E|Todo adjetivo é invariável em gênero e número.|Adjetivos normalmente apresentam concordância, conforme sua forma.
C|“Estudar é importante” apresenta infinitivo verbal exercendo função de sujeito.|A função sintática não elimina a natureza verbal do infinitivo.
''')
topic('PORT-B02-S04','O alcance de um modificador define o que exatamente se afirma ou restringe.','Somente, quase, até, ainda e já podem alterar foco e pressupostos. Observe posição e contexto. Advérbios não se limitam a modificar verbos: podem graduar adjetivos, outros advérbios ou expressar avaliação da oração.', '''
C|“Somente Ana revisou o texto” restringe o conjunto de pessoas que o revisaram.|O foco recai sobre o sujeito Ana.
E|“Ana revisou somente o texto” significa necessariamente que mais ninguém o revisou.|A restrição recai sobre o objeto revisado, não sobre o agente.
C|Em “O prazo está muito curto”, “muito” intensifica o adjetivo.|O modificador atua sobre “curto”.
C|“Ela chegou bastante cedo” apresenta intensificação de um advérbio.|“Bastante” modifica “cedo”.
E|“Quase todos concluíram” afirma que todos concluíram sem exceção.|“Quase” afasta a totalidade plena.
C|“Até o coordenador errou” inclui o coordenador em escala de surpresa.|O foco pressupõe inclusão de participante menos esperado.
E|Trocar “ainda não chegou” por “já chegou” mantém a negação e o estado temporal.|A troca afirma realização antes negada.
C|“Infelizmente, o arquivo foi perdido” apresenta avaliação do enunciador sobre o fato.|O advérbio incide sobre a oração.
E|Todo advérbio de intensidade altera o número de participantes da ação.|Intensidade pode graduar qualidade ou modo sem quantificar participantes.
C|“Ele apenas consultou o processo” pode limitar a ação praticada, distinguindo consulta de alteração.|O contexto define o foco de “apenas”.
E|“Nunca” indica frequência eventual, equivalente a “às vezes”.|“Nunca” nega ocorrência no intervalo considerado.
C|Mover “só” pode modificar o foco mesmo quando a frase resultante continua gramatical.|Posição e escopo têm efeito semântico.
''')
topic('PORT-B02-S05','Tempos e modos verbais situam ações e expressam atitudes como certeza, hipótese e comando.','Indicativo costuma apresentar fatos; subjuntivo aparece em hipóteses e desejos; imperativo orienta. Pretérito perfeito tende a apresentar ação concluída; imperfeito pode indicar hábito ou duração. Locução reúne auxiliar e principal.', '''
C|“Quando era criança, lia todas as tardes” emprega imperfeito para indicar hábito passado.|A repetição habitual é marcada pelo contexto e pelo tempo verbal.
E|“Se ele estudasse, entenderia” apresenta fato passado seguramente ocorrido.|A construção exprime hipótese, não fato confirmado.
C|Em “Estamos analisando o pedido”, auxiliar e gerúndio formam locução verbal.|A locução apresenta ação em desenvolvimento.
C|“Ontem conferimos os dados” situa a conferência como evento passado concluído no contexto.|O marcador temporal orienta a leitura do perfeito.
E|“Talvez chegue amanhã” emprega indicativo na forma “chegue”.|“Chegue” está no presente do subjuntivo.
C|“Leia o aviso antes de enviar” emprega forma de orientação ao destinatário.|O comando tem valor imperativo.
E|A substituição de “enviará” por “enviaria” preserva sempre o grau de compromisso com o fato.|Futuro do presente e futuro do pretérito admitem valores distintos.
E|Toda sequência de dois verbos constitui locução verbal indivisível.|Pode haver duas orações com verbos semanticamente autônomos.
''')
topic('PORT-B03-S01','Crase é fusão de sons; o acento grave registra determinadas fusões de a.','Teste a regência e a presença de artigo feminino: entregar algo a alguém + a diretora = à diretora. Antes de verbo e de palavra masculina, em regra, não há fusão com artigo feminino. Observe demonstrativos aquele/aquela/aquilo, locuções femininas e indicação de horas; não acentue qualquer a por estar diante de nome feminino.', '''
C|“Entregou o documento à diretora” apresenta crase pela combinação da preposição com o artigo.|O destinatário é introduzido por a e o nome admite artigo feminino.
E|“Começou à estudar” emprega corretamente o acento grave.|Não se usa artigo feminino antes de infinitivo; escreva “a estudar”.
C|“Referiu-se àquela decisão” contém fusão da preposição com o a inicial do demonstrativo.|A regência de referir-se fornece a preposição a.
E|“O servidor foi à pé” apresenta locução corretamente acentuada.|A locução é “a pé”, sem artigo feminino.
C|“Às vezes, o sistema demora” emprega acento em locução adverbial feminina.|A locução consagrada é “às vezes”.
E|Em “Daqui à dois dias”, a indicação de futuro exige crase.|Escreva “daqui a dois dias”; não há artigo feminino.
C|“A reunião começará às oito horas” apresenta indicação de horário com acento grave.|A construção reúne preposição e artigo plural.
C|“Obedeceu às normas” apresenta crase devida à regência de obedecer e ao artigo.|O verbo exige a; “as normas” fornece o artigo plural.
E|“Visitou à agência” está correto porque agência é palavra feminina.|Visitar, nesse sentido, é direto: “visitou a agência”.
C|“A solução é semelhante à proposta anterior” emprega crase conforme a regência nominal.|Semelhante exige a e proposta admite artigo.
E|Todo a colocado antes de pronome pessoal recebe acento grave.|Pronomes pessoais como ela não admitem esse artigo: “a ela”.
C|“Chegou a casa cedo”, sem especificação e no sentido de lar próprio, dispensa o artigo.|Sem artigo, não se forma a crase nessa construção.
C|“Foi à casa de uma amiga” admite artigo por haver especificação do nome.|A determinação favorece a combinação de a com a.
E|“Falou à todos” emprega corretamente crase diante de pronome indefinido masculino.|Escreva “a todos”; falta artigo feminino.
C|“À medida que praticava, melhorava” apresenta locução conjuntiva grafada com acento grave.|A expressão proporcional é “à medida que”.
E|Em “Referiu-se àquilo”, o acento depende de aquilo ser palavra feminina.|Ocorre fusão da preposição a com o a inicial de aquilo, pronome neutro.
''')
topic('PORT-B03-S02','Termos da oração são funções; classes de palavras são outra classificação.','Identifique sujeito, complementos verbais, adjuntos, predicativos, aposto e vocativo pelas relações sintáticas. Objeto direto não exige preposição; indireto exige. Complemento nominal completa nome; adjunto adnominal determina ou caracteriza nome. Agente da passiva executa ação em construção passiva.', '''
C|Em “A equipe conferiu o cadastro”, “o cadastro” exerce função de objeto direto.|É complemento de conferir sem preposição exigida.
E|Em “A equipe precisa de apoio”, “de apoio” é sujeito.|É complemento verbal preposicionado de precisar.
C|Em “O relatório final chegou”, “final” exerce função adnominal.|O adjetivo caracteriza diretamente o substantivo relatório.
C|Em “A revisão é necessária”, “necessária” é predicativo do sujeito.|A característica é atribuída por verbo de ligação.
E|Em “Colegas, confiram os dados”, “colegas” é o sujeito gramatical expresso de confiram.|É vocativo; o sujeito do comando é vocês, subentendido.
C|Em “Joana, coordenadora da unidade, assinou”, a expressão intercalada é aposto explicativo.|Ela explica a identidade de Joana.
E|Todo termo introduzido por preposição é objeto indireto.|Há complementos nominais, adjuntos e outros termos preposicionados.
C|Em “O pedido foi analisado pela equipe”, “pela equipe” é agente da passiva.|A expressão identifica quem executa a análise.
C|Em “A análise de dados exige cuidado”, “cuidado” é objeto direto de exige.|O verbo transitivo recebe complemento sem preposição necessária.
E|Em “Ela chegou ontem”, “ontem” completa obrigatoriamente o sentido de um nome.|O advérbio é adjunto adverbial de tempo.
C|Em “Tenho confiança no procedimento”, “no procedimento” completa o nome confiança.|A relação é de complementação nominal.
E|A função de sujeito só pode ser exercida por uma palavra isolada.|Sintagmas e orações podem funcionar como sujeito.
C|Em “Durante a manhã, analisaram o processo”, a expressão inicial indica circunstância temporal.|É adjunto adverbial de tempo.
E|“Senhor diretor” em “Senhor diretor, seguem os dados” é aposto de dados.|O segmento é vocativo dirigido ao destinatário.
C|O núcleo de “os relatórios da comissão” é o substantivo relatórios.|Os demais termos determinam ou especificam o núcleo nominal.
E|Um predicativo só pode ser atribuído ao sujeito, nunca ao objeto.|Há predicativo do objeto, como em “considerou o prazo insuficiente”.
''')
topic('PORT-B03-S03','Sujeito não é sinônimo de agente, e predicação depende do emprego do verbo.','Sujeito pode ser simples, composto, oculto ou indeterminado; há orações sem sujeito. Identifique o núcleo antes da concordância. Verbo de ligação conecta sujeito e predicativo; transitividade é contextual. Haver existencial e fazer temporal são impessoais.', '''
C|Em “Os dados do formulário foram alterados”, o núcleo do sujeito é dados.|“Do formulário” modifica o núcleo, sem assumir a concordância.
E|Em “Havia dúvidas”, dúvidas é sujeito plural que exige “haviam”.|Haver existencial é impessoal; dúvidas é complemento.
C|Em “Faz dois anos que estudo”, fazer indica tempo decorrido e permanece no singular.|O emprego temporal é impessoal.
E|Todo sujeito é o agente que pratica a ação verbal.|Na passiva, o sujeito pode ser paciente; em estados, não há ação praticada.
C|Em “Ana e Rui revisaram”, o sujeito é composto.|Há dois núcleos coordenados.
C|Em “Chegamos cedo”, o sujeito é identificado pela desinência verbal.|A forma permite recuperar nós, sem expressão do pronome.
E|Em “Precisam de servidores”, sem antecedente que identifique os agentes, há sujeito composto expresso.|A terceira pessoa plural pode indeterminar o sujeito nesse contexto.
C|Em “A resposta parece adequada”, parecer liga sujeito a predicativo.|O verbo tem emprego de ligação na oração.
E|“A equipe está na sala” obriga classificar “na sala” como predicativo adjetival.|O segmento expressa localização, não uma qualidade adjetival.
C|Em “Choveu durante a madrugada”, no sentido meteorológico literal, a oração não apresenta sujeito.|O verbo de fenômeno natural é impessoal nesse uso.
E|“Existem vagas” é oração sem sujeito, assim como “Há vagas”.|Existir é pessoal e concorda com vagas, seu sujeito.
C|Em “O documento precisa de revisão”, precisar exige complemento preposicionado.|Nesse emprego, o verbo é transitivo indireto.
E|O sujeito precisa sempre aparecer antes do verbo.|A ordem pode ser invertida, como em “Chegaram os relatórios”.
C|Em “Consideraram a medida útil”, útil predica uma qualidade do objeto.|A oração contém predicativo do objeto medida.
E|Um verbo classificado como transitivo em uma frase conserva obrigatoriamente a mesma predicação em todas.|A predicação depende do sentido e da construção usados.
C|Em “É necessário estudar”, a oração reduzida estudar exerce função de sujeito.|Pode-se desenvolver a estrutura como oração substantiva subjetiva.
''')
topic('PORT-B03-S04','Orações podem coordenar-se ou exercer função dentro de outra oração.','Coordenadas não desempenham função sintática uma dentro da outra. Subordinadas substantivas exercem funções nominais; adjetivas modificam antecedentes; adverbiais estabelecem circunstâncias. Restritivas delimitam grupo; explicativas acrescentam comentário. Orações reduzidas usam formas nominais do verbo.', '''
C|“Leu o aviso e enviou o pedido” apresenta coordenação aditiva.|As ações se articulam por conjunção aditiva.
E|Em “Espero que ele volte”, a oração iniciada por que caracteriza o substantivo volta.|A oração completa o verbo espero, funcionando como objeto direto.
C|“Se houver alteração, avisaremos” contém oração subordinada adverbial condicional.|A hipótese condiciona a ação principal.
C|“O usuário que agendou chegou” contém oração adjetiva restritiva.|A oração delimita qual usuário é referido.
E|Orações adjetivas explicativas dispensam sempre o isolamento por vírgulas.|A pontuação distingue o comentário explicativo da restrição.
C|Em “É importante que todos entendam”, a subordinada exerce função subjetiva.|O conteúdo importante é expresso pela oração sujeito.
E|Toda oração introduzida por que é subordinada adjetiva.|Que também introduz subordinadas substantivas e outras construções.
C|“Estava cansada, mas permaneceu” contém coordenação adversativa.|O conector marca oposição entre expectativa e resultado.
C|Em “Estuda para compreender”, a oração infinitiva expressa finalidade.|O infinitivo indica o objetivo da ação principal.
E|“Quando chegou, telefonou” apresenta oração causal obrigatoriamente.|Quando estabelece relação temporal no contexto.
C|“Embora discordasse, cumpriu a decisão” apresenta oração concessiva.|A discordância é obstáculo insuficiente para impedir o cumprimento.
E|Uma oração reduzida precisa conter verbo em modo finito.|Orações reduzidas empregam infinitivo, gerúndio ou particípio.
C|“Ao concluir a leitura, fez o resumo” possui oração reduzida de infinitivo.|A construção com ao estabelece circunstância temporal.
E|A oração “que ele enviou” em “o arquivo que ele enviou” é complemento do verbo principal recebeu, ainda que esteja dentro do sintagma nominal.|Ela modifica arquivo como subordinada adjetiva; o grupo nominal pode exercer outra função.
C|Em “Desejo isto: que todos aprendam”, a oração após os dois-pontos explica o demonstrativo.|É oração substantiva apositiva.
E|Uma subordinada precisa aparecer depois da oração principal.|Orações adverbiais, por exemplo, podem ser antepostas.
''')
topic('PORT-B03-S05','Se e que assumem funções distintas conforme a construção.','Que relativo retoma antecedente e exerce função na subordinada; que integrante introduz oração substantiva. Se pode integrar verbo pronominal, indicar condição, indeterminar sujeito ou marcar passiva sintética. Na passiva, o sujeito paciente orienta concordância; no índice de indeterminação, o verbo fica singular.', '''
C|Em “Os documentos que chegaram serão lidos”, que é pronome relativo.|Retoma documentos e funciona como sujeito de chegaram.
E|Em “Espero que o arquivo chegue”, que retoma necessariamente um substantivo anterior.|É conjunção integrante, sem antecedente nominal retomado.
C|“Vendem-se equipamentos” admite leitura passiva equivalente a equipamentos são vendidos.|O se é apassivador e equipamentos é sujeito paciente.
E|Em “Precisa-se de técnicos”, técnicos é sujeito que exige “precisam-se”.|O verbo indireto com se indetermina o sujeito e fica singular.
C|Em “Se chover, avise”, se introduz condição.|A oração apresenta hipótese condicionante.
C|Em “Ela se feriu”, se pode funcionar como pronome reflexivo.|O sujeito é também participante afetado pela ação.
E|O se de “Ela se arrependeu” deve ser classificado como conjunção condicional.|Integra o verbo pronominal arrepender-se.
C|Em “O relatório a que me referi”, a preposição decorre da regência de referir-se.|O relativo conserva a preposição exigida na subordinada.
E|Todo que pode ser substituído por o qual sem ajuste ou mudança de função.|A substituição só é pertinente a determinados usos relativos.
C|“Sabe-se que haverá reunião” apresenta estrutura passiva com sujeito oracional.|O conteúdo sabido é a oração iniciada por que.
E|“Trata-se de demandas urgentes” deve flexionar tratar no plural por causa de demandas.|O segmento preposicionado não é sujeito; mantém-se trata-se.
C|Em “Foi tão rápido que surpreendeu”, que integra construção consecutiva.|A intensidade antecedente se liga à consequência.
C|Em “Não sei se haverá reunião”, se introduz interrogação indireta.|A oração exprime conteúdo interrogativo dependente de saber.
E|“Que bela solução!” usa que como pronome relativo com antecedente expresso.|O emprego é exclamativo, sem antecedente nominal retomado.
C|“As cópias foram feitas” e “Fizeram-se as cópias” podem representar o mesmo processo passivo.|Na sintética, cópias continua sujeito paciente plural.
E|A presença de se torna impessoal qualquer verbo, sem análise de regência.|A classificação depende do emprego verbal e das funções dos termos.
''')
topic('PORT-B03-S06','Colocação pronominal exige reconhecer fatores de atração e formas verbais.','Na escrita formal, evite iniciar oração com pronome átono. Negação, relativos e certas palavras atrativas favorecem ou exigem próclise. Não ligue clítico ao particípio; na locução, examine o auxiliar. Futuro sem fator de próclise pode admitir mesóclise. O, a, os, as exercem objeto direto; lhe(s) tipicamente indireto.', '''
C|Na escrita formal, “Não me enviaram o arquivo” apresenta próclise motivada pela negação.|Não, sem pausa que a desligue, atrai o pronome.
E|“Não enviaram-me o arquivo” é a única colocação admitida no padrão formal.|A negação exige próclise nessa construção.
C|“O documento que me entregaram está completo” apresenta próclise após relativo.|Que é fator de atração para o clítico da subordinada.
E|“Tinha enviado-me a resposta” liga corretamente o clítico ao particípio.|Não se prende pronome átono ao particípio; ajuste a posição na locução.
C|“Entregue-me o formulário” é construção compatível com o imperativo afirmativo formal.|O pronome pode ser colocado após o verbo nessa estrutura.
C|“Disseram-lhe a verdade” emprega lhe como destinatário da informação.|Dizer algo a alguém admite objeto indireto representado por lhe.
E|Em “Vi-lhe ontem”, lhe substitui regularmente o objeto direto de ver na norma-padrão estrita.|Para esse complemento, emprega-se o/a: vi-o ou vi-a.
C|“Enviar-lhe-ei a resposta” exemplifica mesóclise no futuro do presente.|O clítico se insere entre base e terminação de futuro.
E|Em “Nunca lhe direi isso”, o futuro obriga trocar a próclise por mesóclise.|A palavra negativa atrai o pronome.
C|Em “Quero vê-lo”, a forma do clítico se ajusta à queda do r do infinitivo.|Após r suprimido, o objeto o assume a forma lo.
E|“Encontraram-o” é a forma adequada do pronome após terminação nasal verbal.|Emprega-se “encontraram-no”.
C|Escolher a posição do clítico exige examinar a oração, não apenas o verbo isolado.|Fatores sintáticos do contexto influenciam a colocação.
''')
topic('PORT-B03-S07','Pontuação organiza relações sintáticas e pode alterar sentidos.','Não separe sujeito e verbo nem verbo e complemento sem intercalação justificável. Isole vocativos, apostos e comentários; enumerações e deslocamentos obedecem à estrutura. Dois-pontos podem anunciar explicação; aspas indicam citação ou uso especial. Não reduza vírgula a uma pausa respiratória.', '''
C|“Os candidatos aprovados apresentaram os documentos” não exige vírgula entre sujeito e verbo.|O sujeito, ainda que longo, não deve ser separado do predicado por esse motivo.
E|“Os candidatos aprovados, apresentaram os documentos” usa vírgula obrigatória pela extensão do sujeito.|A vírgula separa indevidamente sujeito e verbo.
C|“Senhora diretora, encaminho o relatório” isola corretamente o vocativo.|O destinatário chamado é separado da oração.
C|“A unidade, segundo o aviso, abrirá amanhã” emprega duas vírgulas para a intercalação.|A expressão intercalada fica delimitada dos dois lados.
E|Retirar uma das vírgulas de uma intercalação preserva sempre a correção.|A delimitação pode ficar incompleta e prejudicar a estrutura.
C|“Faltavam três itens: assinatura, data e anexo” usa dois-pontos para anunciar enumeração.|O segundo segmento especifica os itens anunciados.
E|Em qualquer frase, inserir vírgula antes de que preserva a interpretação.|O sinal pode transformar restrição em explicação e alterar o alcance.
C|“Os servidores que estavam de plantão chegaram” restringe o grupo referido.|Sem vírgulas, a oração adjetiva delimita o conjunto.
E|Aspas em uma palavra provam, em qualquer contexto, concordância do autor com seu emprego.|Podem indicar citação, distanciamento ou ironia, conforme o contexto.
C|“A equipe leu, comparou e corrigiu” emprega vírgula entre elementos coordenados.|As ações integram uma sequência enumerada.
E|A pontuação de um texto deve ser decidida apenas pelo ponto em que o leitor respira.|A sintaxe e as relações de sentido orientam os sinais.
C|“João, o coordenador, assinou” isola aposto explicativo.|O segmento nominal explica o referente João.
''')
topic('PORT-B03-S08','Concordância verbal parte do sujeito e inclui casos de impessoalidade.','Localize o núcleo, mesmo em ordem inversa. Haver existencial e fazer temporal ficam singulares; existir é pessoal. Na passiva sintética, verbo concorda com sujeito paciente; no sujeito indeterminado com se, fica singular. Sujeito composto anteposto normalmente leva plural.', '''
C|“Chegaram os relatórios” apresenta concordância adequada com o sujeito posposto.|O sujeito plural exige a flexão plural.
E|“Houveram muitos pedidos” está correto porque pedidos é plural.|Haver existencial é impessoal: houve muitos pedidos.
C|“Faz três meses” está correto quando fazer exprime tempo decorrido.|O verbo temporal permanece singular.
E|“Existe várias opções” concorda corretamente com o sujeito.|Existir é pessoal: existem várias opções.
C|“Devem existir soluções” preserva o plural do sujeito na locução.|O auxiliar concorda com soluções.
E|“Devem haver soluções” é a concordância adequada do haver existencial.|A impessoalidade alcança o auxiliar: deve haver soluções.
C|“Analisaram-se os documentos” concorda com sujeito paciente plural.|A passiva sintética admite “os documentos foram analisados”.
E|“Precisam-se de revisores” é a forma regular de indeterminar o sujeito com precisar de.|Emprega-se “precisa-se de revisores”.
C|“O conjunto de regras foi atualizado” concorda com o núcleo singular conjunto.|O complemento plural não substitui o núcleo do sujeito.
C|“Ana e Rui concluíram o trabalho” apresenta plural devido ao sujeito composto anteposto.|Os dois núcleos orientam a concordância plural.
E|“Os resultados da pesquisa confirmou a hipótese” concorda com pesquisa corretamente.|O núcleo do sujeito é resultados: confirmaram.
E|A posição do sujeito depois do verbo dispensa qualquer concordância.|A inversão não elimina a relação de número e pessoa.
''')
topic('PORT-B03-S09','Concordância nominal relaciona determinantes e qualificadores aos nomes.','Artigos, pronomes, numerais e adjetivos ajustam-se conforme seu emprego. Anexo como adjetivo varia; em anexo é locução invariável. Meio como advérbio e menos são invariáveis; mesmo e obrigado podem flexionar. Não aplique uma única regra a toda palavra com forma semelhante.', '''
C|“Seguem anexas as declarações” apresenta concordância de anexo como adjetivo.|O adjetivo acompanha declarações no feminino plural.
E|“As servidoras estão meias cansadas” emprega corretamente o advérbio meio.|Como intensidade, meio é invariável: meio cansadas.
C|“Havia menos pessoas” emprega corretamente menos, sem flexão de gênero.|A palavra menos é invariável, mesmo diante de nome feminino.
E|“As cópias seguem em anexas” está correto porque cópias é feminino plural.|A locução é invariável: em anexo.
C|Uma servidora pode agradecer dizendo “Muito obrigada”.|A forma de agradecimento concorda com quem agradece.
C|“Elas mesmas conferiram os dados” apresenta flexão de reforço ligada ao pronome.|Mesmo varia quando reforça identidade do referente.
E|“É proibida entrada”, sem artigo e em indicação genérica, exige obrigatoriamente essa flexão.|A construção genérica consagrada é “é proibido entrada”; com artigo, “é proibida a entrada”.
C|“A entrada é proibida” mantém concordância com sujeito feminino determinado.|O predicativo acompanha a entrada.
E|“Documentos e certidões atualizadas” só pode significar que ambos os nomes foram qualificados.|O feminino pode ligar-se apenas a certidões; a relação pode ser ambígua.
C|“As respostas foram bastante claras” usa bastante como intensificador invariável.|O termo modifica o adjetivo claras.
E|“Havia bastante dúvidas” é necessariamente a flexão adequada do determinante quantitativo.|Determinando dúvidas, a forma plural é bastantes.
C|“As próprias candidatas assinaram” apresenta concordância nominal regular.|Próprias determina candidatas no feminino plural.
''')
topic('PORT-B03-S10','Regência verbal descreve a relação do verbo com seus complementos.','O sentido do verbo pode mudar a preposição: assistir a no sentido de ver; aspirar a no sentido de almejar; visar a no sentido de ter objetivo no padrão estrito tradicional. Obedecer e referir-se exigem a. Preferir A a B evita dupla comparação. O relativo conserva a preposição regida.', '''
C|“Os candidatos assistiram à palestra” segue a regência tradicional de assistir no sentido de ver.|O verbo exige a; a palestra admite artigo.
E|“Prefiro revisar do que decorar” é a construção de preferência prescrita na norma-padrão estrita.|A construção é preferir uma coisa a outra.
C|“O servidor obedeceu ao regulamento” apresenta complemento com preposição exigida.|Obedecer rege a, que se combina com o artigo masculino de regulamento.
E|“O assunto que me referi” conserva integralmente a regência de referir-se.|Falta a preposição: o assunto a que me referi.
C|“Aspirava ao cargo” usa a regência de aspirar no sentido de desejar.|O sentido de almejar admite complemento com a.
C|“Aspirou o ar da sala” usa aspirar em sentido de inalar, com complemento direto.|A mudança de sentido muda a construção.
E|Se um verbo tem dois sentidos, sua regência é necessariamente idêntica em ambos.|A regência pode variar conforme a acepção.
C|“Informou o prazo aos candidatos” apresenta informação direta e destinatário preposicionado.|A construção de informar admite esses dois complementos.
E|“Ela chegou no órgão” e “ela chegou ao órgão” são indistintamente a forma prescrita pelo padrão estrito tradicional de chegar a.|O padrão tradicional adota chegar a; usos correntes devem ser distinguidos do registro cobrado.
C|“Lembrou-se do compromisso” apresenta construção pronominal com complemento de.|Na construção pronominal, lembrar-se introduz o complemento com de.
E|“Esqueceu-se o documento”, no sentido de não se lembrar dele, é a única regência correta.|A forma pronominal usa de: esqueceu-se do documento; a direta dispensa se.
C|Em “A norma a que obedecemos”, a preposição antes do relativo vem da regência de obedecer.|O vínculo se mantém mesmo com o complemento anteposto.
''')
topic('PORT-B03-S11','Regência nominal examina complementos exigidos por substantivos, adjetivos e advérbios.','Reconheça o nome regente antes de escolher a preposição. São construções usuais: acesso a, necessidade de, compatível com, favorável a, responsável por, apto a/para e próximo de/a conforme contexto. A preposição exigida pode levar à crase diante de artigo feminino.', '''
C|“Acesso à informação” combina regência de acesso a com artigo feminino.|A fusão produz o acento grave.
E|Em “necessidade de revisão”, a preposição é exigida por um verbo expresso imediatamente anterior.|O substantivo necessidade rege o complemento com de.
C|“Compatível com a norma” emprega preposição adequada ao adjetivo.|Compatível se constrói com com.
C|“Favorável à proposta” admite acento grave pela regência do adjetivo.|Favorável a encontra artigo de a proposta.
E|“Responsável com o arquivo”, no sentido de encarregado dele, é a regência usual equivalente a responsável por.|Para indicar encargo, emprega-se responsável por.
C|“Apto para o trabalho” apresenta construção admitida com apto.|O adjetivo pode reger para nesse sentido.
E|Todo nome exige sempre a preposição a, independentemente do sentido.|A seleção depende do nome e da construção.
C|“Respeito aos usuários” contém complemento nominal introduzido por a.|O substantivo respeito estabelece a relação regencial.
E|“Semelhante com a anterior” é a construção padrão de semelhante nesse contexto comparativo.|Emprega-se semelhante a.
C|“O receio de falhar” apresenta complemento do substantivo receio.|O infinitivo é introduzido pela preposição de.
E|A existência de regência nominal dispensa conferir se há artigo antes da crase.|Regência fornece preposição; a fusão exige também o outro elemento.
C|“Ela ficou satisfeita com o resultado” emprega complemento ligado ao adjetivo satisfeita.|O complemento completa o estado de satisfação.
''')
topic('PORT-B04-S01','O sentido de uma palavra depende do contexto e de suas relações com outras.','Diferencie sentido literal e figurado, polissemia, sinonímia contextual e antonímia. Hipônimo é espécie mais específica; hiperônimo é categoria ampla. Não trate sinônimos de dicionário como substitutos universais; ironia depende do contexto.', '''
C|Em “A notícia acendeu a esperança”, acender tem sentido figurado.|A esperança não é combustão literal; a expressão indica despertar.
E|Duas palavras sinônimas em uma frase podem ser trocadas em todas as frases sem mudança alguma.|A sinonímia depende do contexto e do registro.
C|“Veículo” é termo mais amplo que “ônibus” na classificação usual.|Veículo é hiperônimo; ônibus é um tipo de veículo.
E|“A agência fechou” significa obrigatoriamente que ela deixou de existir para sempre.|Fechar pode designar término do expediente ou encerramento definitivo, conforme o contexto.
C|Em “O atendimento foi frio”, frio pode caracterizar falta de acolhimento.|O adjetivo admite emprego figurado.
C|“Claro” em “texto claro” e “dia claro” apresenta acepções relacionadas, mas não idênticas.|Trata-se de variação de sentido conforme o nome qualificado.
E|A oposição entre “permitido” e “proibido” é relação de sinonímia.|É relação antonímica no contexto normativo.
C|“Poucos pedidos foram aceitos” e “muitos pedidos foram aceitos” alteram a avaliação quantitativa.|Os quantificadores orientam sentidos diferentes.
E|A frase “Que pontualidade!”, dirigida a quem se atrasou, deve ser interpretada literalmente em qualquer situação.|O contexto pode produzir ironia e sentido avaliativo oposto.
C|“Retificar” e “ratificar” não são equivalentes: corrigir difere de confirmar.|A proximidade formal não implica identidade de sentido.
E|“Eventualmente” significa necessariamente “com certeza e sempre”.|O advérbio indica ocorrência eventual ou possível, não universalidade.
C|Para julgar substituição vocabular, é preciso ler a oração e o desenvolvimento textual.|O contexto delimita a acepção efetiva.
''')
topic('PORT-B04-S02','Correspondência oficial deve adequar forma, finalidade e destinatário.','O padrão ofício organiza comunicações oficiais. Escreva assunto objetivo, contexto suficiente, solicitação ou informação clara e identificação do signatário. E-mail institucional não dispensa padrão de linguagem; envio não garante leitura. Diferencie regras históricas do Manual e normas posteriores aplicáveis.', '''
C|Um e-mail institucional deve preservar clareza e adequação de linguagem.|O meio eletrônico não dispensa qualidade da comunicação oficial.
E|A rapidez do e-mail autoriza omitir o assunto mesmo quando isso dificulta identificar a demanda.|A identificação objetiva do assunto favorece organização e compreensão.
C|Uma comunicação pode começar diretamente pela informação ou solicitação necessária.|Objetividade evita fórmulas introdutórias vazias.
E|Anexar um documento dispensa qualquer indicação de sua finalidade na mensagem.|É importante indicar o anexo e a razão do encaminhamento.
C|Na terceira edição do Manual de 2018, o padrão ofício unifica as antigas distinções entre aviso, ofício e memorando.|A classificação histórica não deve ser aplicada como se não tivesse havido alteração.
E|Um ofício dirigido a outro órgão deve incluir opiniões pessoais irrelevantes para provar autenticidade.|A comunicação representa a atuação institucional, não preferências privadas.
C|O signatário deve ser identificável no documento oficial.|A autoria institucional não elimina a identificação de quem assina.
C|“Solicito o envio da planilha até 5 de maio” apresenta ação e prazo de modo direto.|O pedido é específico e operacionalizável.
E|Confirmar o envio de mensagem prova, em todos os sistemas e situações, sua leitura pelo destinatário.|Envio, entrega e leitura são eventos distintos.
C|Um arquivo anexo deve ter nome compreensível e relação clara com a mensagem.|Isso facilita identificação e uso da informação.
E|A comunicação oficial precisa conter linguagem rebuscada para ser formal.|Formalidade não se confunde com obscuridade ou excesso de cerimônia.
C|Uma regra histórica de tratamento deve ser cotejada com norma posterior antes de orientar comunicação atual.|A atualização evita aplicar instrução superada ou fora de âmbito.
''')
topic('PORT-B04-S03','Clareza, concisão e impessoalidade melhoram a utilidade da comunicação.','Prefira termos precisos, ordem compreensível e informação necessária. Concisão elimina redundância sem amputar requisitos. Impessoalidade afasta promoção pessoal e opiniões privadas; não proíbe toda primeira pessoa. Padronização não autoriza texto automático com dados errados.', '''
C|Retirar “venho por meio deste” pode tornar um pedido mais direto sem eliminar seu conteúdo.|A fórmula frequentemente acrescenta palavras sem informação operacional.
E|Concisão significa escrever sempre o menor número possível de palavras, mesmo omitindo condição relevante.|A economia deve preservar informação necessária.
C|“Envie o formulário assinado até amanhã” é mais preciso que “Resolva isso logo”, se esse for o pedido pretendido.|A formulação especifica objeto, condição e prazo.
E|A primeira pessoa em “Informo que o prazo terminou” torna o documento necessariamente pessoal e inadequado.|A forma verbal não implica promoção ou opinião privada.
C|Explicar uma sigla pouco conhecida na primeira ocorrência favorece clareza.|O destinatário passa a identificar seu significado.
C|Impersonalidade é compatível com tratamento respeitoso e acessível ao cidadão.|A atuação institucional não exige frieza ou desatenção.
E|Reutilizar um modelo dispensa conferir nomes, datas e referências.|Padronização não elimina a responsabilidade pela correção dos dados.
E|Substituir todo termo técnico por expressão vaga melhora obrigatoriamente a clareza.|Precisão técnica pode ser necessária; explique o termo quando apropriado.
''')
topic('PORT-B04-S04','Estrutura documental e tratamento devem seguir o âmbito normativo da comunicação.','No padrão ofício, confira identificação, local/data, destinatário, assunto, texto, fecho e signatário conforme o modelo aplicável. No âmbito do Decreto 9.758/2019, usa-se senhor/senhora; observe exceções legais de âmbito. Pronomes de tratamento levam concordância verbal em terceira pessoa. Não use o nome do cargo como autorização para tratamento inventado.', '''
C|No âmbito do Decreto 9.758/2019, a forma de tratamento padrão é senhor, com flexões de gênero e número.|O art. 2º estabelece senhor e suas flexões.
E|O Decreto 9.758/2019 torna obrigatório “Vossa Excelência” para todo ministro do Executivo federal.|O decreto simplifica o tratamento no seu âmbito de aplicação.
C|O decreto contém exceções de âmbito para comunicações com autoridades estrangeiras e certas relações com outros Poderes e entes.|O art. 1º, §3º, impede generalização sem verificar a situação.
E|Um erro na forma de tratamento autoriza negar a realização do ato administrativo no âmbito do decreto.|O art. 3º, §2º, veda essa recusa por tal motivo.
C|No padrão formal de concordância, “Vossa Senhoria poderá” usa terceira pessoa, e não “podereis”.|Tratamentos de segunda pessoa indireta levam concordância de terceira pessoa.
C|O campo assunto deve antecipar de modo conciso o objeto da comunicação.|A identificação facilita o encaminhamento e a compreensão.
E|O endereçamento no âmbito do Decreto 9.758/2019 exige sempre nome pessoal e tratamento cerimonioso.|O art. 4º estabelece regra diversa e admite hipóteses específicas.
E|O fecho e a identificação de quem assina são a mesma parte e têm função idêntica.|Fecho encerra a mensagem; identificação aponta o signatário.
''','d9758')
topic('RLM-B01-S01','Proposição é uma declaração à qual se atribui valor verdadeiro ou falso.','Na lógica bivalente clássica, cada proposição tem um dos dois valores. Perguntas, ordens e exclamações não são proposições declarativas por si. Não confunda ser falso com não ser proposição. O contexto precisa fixar referentes e condições.', '''
C|“Dois mais três é igual a cinco” é uma proposição verdadeira na aritmética usual.|É uma declaração com valor de verdade determinado.
E|Uma afirmação falsa deixa, por isso, de ser proposição.|Proposições podem ser falsas; a falsidade é um de seus valores.
C|“Sete é um número par” é proposição, embora falsa.|A declaração tem valor falso, pois sete não é divisível por dois.
E|A pergunta “Qual é o prazo?” tem, por si, valor verdadeiro ou falso.|Perguntas solicitam informação e não afirmam conteúdo bivalente.
C|“Assine o formulário” é ordem, não proposição declarativa.|O imperativo não atribui verdade a uma declaração.
E|Na lógica bivalente clássica, a mesma proposição deve ser simultaneamente verdadeira e falsa.|A bivalência atribui exatamente um dos dois valores em uma interpretação.
C|Uma frase longa pode expressar uma única proposição simples se não houver conectivo lógico articulando proposições.|Extensão em palavras não mede complexidade lógica.
E|Desconhecer a resposta de um fato torna toda declaração sobre ele uma sentença não proposicional.|Desconhecimento do observador não elimina necessariamente o valor de verdade.
''','logic')
topic('RLM-B01-S02','Sentença aberta contém variável livre e precisa de interpretação para virar proposição.','Fixar uma variável ou quantificá-la pode fechar a sentença. Ordens, perguntas e paradoxos autorreferentes não devem ser tratados como proposições bivalentes comuns. A definição do universo muda o alcance de quantificadores.', '''
C|“x + 2 = 5”, com x livre, é sentença aberta.|O valor depende da atribuição feita a x.
E|Atribuir x = 3 à sentença x + 2 = 5 produz uma proposição falsa.|A substituição resulta em 3 + 2 = 5, que é verdadeira.
C|No universo dos inteiros, “existe x tal que x + 2 = 5” é proposição verdadeira.|O inteiro três satisfaz a igualdade.
E|“Todo inteiro x satisfaz x + 2 = 5” é verdadeira porque existe uma solução.|Um exemplo não satisfaz o quantificador universal.
C|“Abra o documento” continua sendo ordem mesmo quando o destinatário está identificado.|Fixar destinatário não transforma comando em declaração.
E|Uma sentença com variável livre tem obrigatoriamente o mesmo valor em todas as atribuições.|A variável pode produzir avaliações distintas.
C|Em “Para todo inteiro x, x² é não negativo”, a variável está quantificada.|Não há variável x livre nessa declaração universal.
E|O universo considerado é irrelevante para julgar “existe x tal que x² = 2”.|Há solução real, mas não solução inteira; o universo altera o julgamento.
''','logic')
topic('RLM-B01-S03','Proposições compostas resultam de operações lógicas sobre proposições.','Reconheça os átomos pelo conteúdo declarado, não por conjunções gramaticais isoladas. Negação também é operação lógica. Um nome com e não cria necessariamente conjunção de duas proposições. Um mesmo átomo repetido não conta como variável independente nova.', '''
C|Se p significa “o portal abriu”, ¬p é a negação dessa proposição.|A operação inverte o valor de verdade de p.
E|A expressão p ∧ q contém necessariamente três proposições simples independentes.|Há duas letras proposicionais, p e q.
C|“A equipe de saúde e segurança chegou”, sem decomposição adicional do predicado, não forma automaticamente p ∧ q.|A conjunção dentro de um nome não garante duas declarações autônomas.
E|Uma frase negativa é sempre proposição simples, pois não tem dois verbos.|Na análise formal, ¬p envolve o conectivo de negação.
C|Em p ∨ (q ∧ r), aparecem três variáveis proposicionais distintas.|São p, q e r; os conectivos não acrescentam variável.
C|Em p ∧ p, repetir p não cria uma segunda variável independente.|O valor das duas ocorrências deve coincidir.
E|O número de palavras de uma declaração determina o número de linhas de sua tabela-verdade.|As linhas dependem do número de variáveis independentes.
E|Uma proposição composta não pode conter outra proposição composta como parte.|Parênteses podem organizar composições aninhadas.
''','logic')
topic('RLM-B01-S04','Cada conectivo tem condições de verdade definidas.','Conjunção é verdadeira apenas com ambos verdadeiros. Disjunção inclusiva falha apenas com ambos falsos. Condicional só falha em V→F; bicondicional é verdadeira quando os valores coincidem. Não transfira automaticamente o ou exclusivo cotidiano para o símbolo ∨.', '''
C|Com p verdadeira e q falsa, p ∧ q é falsa.|A conjunção exige ambos os componentes verdadeiros.
E|Com p falsa e q verdadeira, p ∧ q é verdadeira por haver um componente verdadeiro.|Um único verdadeiro não satisfaz a conjunção.
C|Se p e q são verdadeiras, p ∨ q também é verdadeira na disjunção inclusiva.|A inclusiva aceita verdade simultânea.
E|A disjunção inclusiva p ∨ q é falsa quando p e q são ambas verdadeiras.|Ela só é falsa no caso F,F.
C|A condicional p → q é falsa quando p é verdadeira e q é falsa.|Esse é o único caso de falsidade da implicação material.
E|Com p falsa e q falsa, p → q é falsa.|A implicação com antecedente falso é verdadeira na tabela clássica.
C|Com p e q falsas, p ↔ q é verdadeira.|A bicondicional exige igualdade dos valores.
E|A bicondicional é verdadeira sempre que pelo menos um de seus componentes é verdadeiro.|Com valores diferentes ela é falsa.
''','logic')
topic('RLM-B01-S05','Tradução lógica exige conservar negações, agrupamento e direção da condição.','Defina cada letra e mantenha seu sentido. Se p então q é p→q; p somente se q também exige p→q. Não confunda nem com conjunção de afirmativas. Parênteses indicam o alcance dos conectivos e da negação.', '''
C|Definindo p como “leu” e q como “resumiu”, “leu e não resumiu” é p ∧ ¬q.|A conjunção liga a leitura à negação do resumo.
E|Com p = “agendou” e q = “entrou”, “se agendou, então entrou” se traduz por q → p.|A direção é p → q, sem inversão.
C|Se p = “foi aprovado” e q = “cumpriu o requisito”, “foi aprovado somente se cumpriu o requisito” é p → q.|O requisito é condição necessária da aprovação.
E|“Nem leu nem resumiu” corresponde a p ∧ q quando p e q são as ações afirmativas.|A tradução é ¬p ∧ ¬q.
C|Se p = “há energia” e q = “há conexão”, “não é verdade que há energia e conexão” é ¬(p ∧ q).|A negação abrange toda a conjunção.
C|“Há senha ou há token, e o sistema funciona” pode exigir parênteses para eliminar ambiguidade de agrupamento.|A língua natural pode deixar incerto o escopo de e e ou.
E|Trocar p → q por q → p sempre preserva o sentido de uma condição.|A recíproca não é equivalente em geral.
E|“Se e somente se” pode ser traduzido apenas por uma disjunção inclusiva.|A expressão corresponde à bicondicional.
''','logic')
topic('RLM-B01-S06','Uma tabela completa possui 2ⁿ linhas para n variáveis bivalentes independentes.','Conte letras distintas, não ocorrências e não conectivos. Duas variáveis geram quatro combinações; três geram oito. A ordenação das linhas pode variar, mas todas as combinações precisam aparecer uma vez.', '''
C|Uma tabela completa para p, q e r independentes possui oito linhas.|Existem 2³ combinações bivalentes.
E|A expressão p ∧ ¬p exige quatro linhas porque p aparece duas vezes.|Há uma só variável independente; são duas linhas.
C|A tabela de (p ∨ q) → (r ∧ s) tem dezesseis linhas.|Quatro variáveis distintas geram 2⁴ combinações.
E|Cinco variáveis independentes produzem dez linhas em tabela completa.|O total é 2⁵ = 32, não 2 × 5.
C|Para p ↔ q, as linhas VV, VF, FV e FF cobrem todas as combinações.|São as quatro possibilidades de duas variáveis.
E|Acrescentar uma variável independente triplica o número de linhas.|Acrescentar uma variável bivalente duplica o número.
C|As duas ocorrências de q em (p ∧ q) ∨ (q ∧ r) devem receber o mesmo valor em cada linha.|Uma letra representa a mesma proposição em toda a expressão.
E|Uma tabela de seis variáveis é completa com apenas 36 combinações.|O total completo é 2⁶ = 64.
''','logic')
topic('RLM-B01-S07','Negar uma proposição exige produzir exatamente o valor oposto em todas as interpretações.','Pelas leis de De Morgan, ¬(p∧q) equivale a ¬p∨¬q e ¬(p∨q) a ¬p∧¬q. A negação de p→q é p∧¬q. A contrapositiva ¬q→¬p é equivalente à condicional.', '''
C|A negação de “leu e resumiu” é “não leu ou não resumiu”, com ou inclusivo.|De Morgan troca conjunção por disjunção e nega os componentes.
E|A negação de “leu ou resumiu” é “não leu ou não resumiu”.|A negação correta exige “não leu e não resumiu”.
C|A negação de p → q é p ∧ ¬q.|A condicional só é falsa com antecedente verdadeiro e consequente falso.
E|p → q é equivalente, em geral, a ¬p → ¬q.|A equivalente contrapositiva é ¬q → ¬p.
''','logic')
topic('RLM-B01-S08','Em p→q, p é suficiente para q e q é necessária para p.','Condição necessária não é garantia de suficiência. O requisito pode ser cumprido sem que o fato condicionado ocorra. Bicondicional reúne as duas direções. Concluir antecedente a partir do consequente é raciocínio inválido sem premissa adicional.', '''
C|Em “Se houve aprovação, houve inscrição”, a inscrição é condição necessária da aprovação.|Aprovação implica inscrição; sem inscrição não pode haver aprovação sob a premissa.
E|Se inscrição é necessária para aprovação, toda pessoa inscrita foi aprovada.|Necessidade não transforma inscrição em condição suficiente.
C|Se concluir o curso basta para obter certificado, concluir é condição suficiente para obtê-lo.|A suficiência fornece a direção conclusão → certificado.
E|Dizer que p é necessária e suficiente para q exige apenas p → q.|São necessárias as duas direções, formando p ↔ q.
''','logic')
topic('RLM-B02-S01','Tautologia é sempre verdadeira; contradição é sempre falsa; contingência varia.','Classifique após examinar todas as interpretações possíveis. Um exemplo verdadeiro não prova tautologia. p∨¬p é tautologia; p∧¬p é contradição. Equivalência compara colunas completas, não apenas uma linha.', '''
C|p ∨ ¬p é tautologia na lógica clássica.|Em qualquer valor de p, um dos disjuntos é verdadeiro.
E|p ∧ ¬p é uma contingência.|Os componentes nunca são simultaneamente verdadeiros; é contradição.
C|p → p é tautologia.|Não há linha com antecedente verdadeiro e consequente falso.
C|p ∧ q é contingente quando as variáveis são independentes.|É verdadeira em VV e falsa nas demais linhas.
E|Uma expressão verdadeira em uma linha já pode ser classificada como tautologia.|Tautologia exige verdade em todas as linhas.
C|A negação de uma tautologia é contradição.|Inverter uma coluna inteiramente verdadeira produz coluna inteiramente falsa.
E|p ↔ ¬p é verdadeira em todas as interpretações.|p e ¬p têm sempre valores diferentes; a expressão é contradição.
E|Duas fórmulas com o mesmo número de letras são necessariamente equivalentes.|Equivalência exige coincidência dos valores em todas as interpretações.
''','logic')
topic('RLM-B02-S02','Argumento válido não admite premissas todas verdadeiras com conclusão falsa.','A validade trata da relação inferencial, não da verdade isolada da conclusão. Modus ponens e modus tollens são válidos. Afirmar o consequente e negar o antecedente são falácias. Um contraexemplo basta para provar invalidade.', '''
C|Das premissas p → q e p, conclui-se validamente q.|É a forma válida modus ponens.
E|Das premissas p → q e q, conclui-se necessariamente p.|A afirmação do consequente falha quando p é falsa e q verdadeira.
C|Das premissas p → q e ¬q, conclui-se validamente ¬p.|É a forma válida modus tollens.
E|Das premissas p → q e ¬p, conclui-se necessariamente ¬q.|Pode ocorrer p falsa e q verdadeira, invalidando a inferência.
C|Para mostrar invalidade, basta uma interpretação com premissas verdadeiras e conclusão falsa.|Esse é o contraexemplo definido pelo critério de validade.
E|Uma conclusão verdadeira no mundo torna válido qualquer argumento que a apresente.|Verdade da conclusão não garante a relação de consequência.
C|De “todos os A são B” e “todo B é C”, segue “todo A é C”.|A inclusão de A em B e de B em C é transitiva.
E|De “algum A é B” e “algum B é C”, segue necessariamente “algum A é C”.|Os elementos de B usados nas premissas podem ser diferentes.
''','logic')
topic('RLM-B03-S01','Pertinência relaciona elemento a conjunto; inclusão relaciona conjuntos.','Use ∈ para pertence e ⊆ para subconjunto. Conjunto vazio não contém elementos e é subconjunto de todo conjunto. Ordem e repetição não alteram um conjunto. Um elemento pode ser um conjunto, mas isso precisa estar explicitado.', '''
C|Se A = {2,4,6}, então 4 ∈ A.|O número quatro está listado entre os elementos.
E|Se A = {2,4,6}, então {4} ∈ A.|O elemento é 4, não o conjunto unitário {4}.
C|Se A = {2,4,6}, então {2,6} ⊆ A.|Todos os elementos do conjunto menor pertencem a A.
E|O conjunto vazio possui exatamente um elemento, o número zero.|O vazio não possui elementos; zero seria um elemento de outro conjunto.
C|O conjunto vazio é subconjunto de qualquer conjunto A.|Não existe elemento do vazio que viole a inclusão em A.
C|Os conjuntos {1,2,2} e {2,1} são iguais.|Repetição e ordem não alteram os elementos do conjunto.
E|A ⊆ B obriga B ⊆ A, quaisquer que sejam os conjuntos.|A inclusão inversa só é garantida quando há igualdade.
E|Se A = {{1},2}, então 1 ∈ A.|Os elementos explicitados são o conjunto {1} e o número 2.
''','logic')
topic('RLM-B03-S02','União reúne; interseção exige pertencimento simultâneo; diferença depende da ordem.','A∪B inclui elementos de pelo menos um conjunto. A∩B inclui elementos de ambos. A−B contém quem está em A e não está em B. União e interseção são comutativas; diferença geralmente não é. Verifique elementos um a um antes de contar.', '''
C|Para A = {1,2,3} e B = {3,4}, a união é {1,2,3,4}.|A união reúne todos os elementos, sem repetir o três.
E|Para A = {1,2,3} e B = {3,4}, a interseção é {1,2,3,4}.|A interseção contém apenas o elemento comum: {3}.
C|Para A = {1,2,3} e B = {3,4}, A − B = {1,2}.|Retiram-se de A os elementos que também pertencem a B.
E|Para A = {1,2,3} e B = {3,4}, B − A = {1,2}.|A diferença inversa é {4}.
C|A ∩ B = B ∩ A para quaisquer conjuntos.|Pertencer simultaneamente aos dois não depende da ordem.
E|A − B é sempre igual a B − A.|A diferença depende do conjunto de partida.
C|A união de um conjunto com o vazio é o próprio conjunto.|O vazio não acrescenta nenhum elemento.
E|Se A e B são disjuntos e não vazios, sua interseção contém todos os elementos de A.|Disjunção entre conjuntos significa interseção vazia.
''','logic')
topic('RLM-B03-S03','Complementar só é definido depois de fixar o universo.','O complementar de A em U é U−A, com A contido em U. Duplo complementar recupera A. Complemento não é conjunto de tudo que existe; é relativo ao universo escolhido.', '''
C|Se U = {1,2,3,4,5} e A = {2,4}, o complementar de A em U é {1,3,5}.|São os elementos do universo que não estão em A.
E|O complementar de A é independente da escolha do universo.|Mudar U pode acrescentar ou retirar elementos do complementar.
C|Se A ⊆ U, o complementar do complementar de A em U é A.|Retirar duas vezes a exclusão recupera o conjunto original.
E|O complementar de U em relação a ele mesmo é U.|O complementar é U − U, portanto vazio.
''','logic')
topic('RLM-B03-S04','Na contagem de dois conjuntos, subtraia a interseção somada duas vezes.','A fórmula é n(A∪B)=n(A)+n(B)−n(A∩B). Somente A exclui a interseção. Nenhum é o total do universo menos a união. Confira se o enunciado fala em uma categoria ou em pelo menos uma.', '''
C|Em 60 pessoas, 32 estudam Português, 28 estudam RLM e 10 estudam ambos. Cinquenta estudam pelo menos uma dessas matérias.|A união é 32 + 28 − 10 = 50.
E|Em 80 pessoas, 50 usam portal, 40 usam telefone e 20 usam ambos. Vinte pessoas não usam nenhum dos dois.|A união é 50 + 40 − 20 = 70; fora dela ficam 80 − 70 = 10, e não vinte.
C|Se 25 pessoas estudam A e 9 delas também estudam B, 16 estudam A sem estudar B.|Somente A é 25 − 9 = 16.
E|Se 18 pessoas estão em A e 14 em B, somar 32 sempre fornece a união mesmo com interseção não vazia.|Os participantes comuns seriam contados duas vezes.
''','logic')
topic('RLM-B04-S01','Porcentagem é uma razão com base cem, e sua base precisa estar clara.','Calcule r% de N como rN/100. Para recuperar a base, divida a parte pela taxa decimal. Aumento é variação dividida pelo valor inicial. Percentual e quantidade absoluta não são a mesma grandeza.', '''
C|Vinte por cento de 250 pedidos correspondem a 50 pedidos.|Multiplicar a base 250 pela taxa decimal 0,20 produz cinquenta pedidos.
E|Se 30 pedidos representam 15% do total, o total é 450.|A base é 30 ÷ 0,15 = 200.
C|Uma taxa que sobe de 40 para 50 teve aumento relativo de 25%.|O acréscimo dez é dividido pela base inicial quarenta.
E|Passar de 80 para 100 significa aumento de 20%, pois a diferença é vinte.|A taxa é 20 ÷ 80 = 25%.
C|Se 18 pessoas são 30% de um grupo, o grupo possui 60 pessoas.|A base é recuperada dividindo dezoito por 0,30, o que produz sessenta.
E|Desconto de 25% em R$ 200 deixa preço de R$ 175.|O desconto é R$ 50; o preço restante é R$ 150.
C|Metade de um conjunto corresponde a 50% dele.|Uma metade equivale à razão 50/100.
E|Uma porcentagem pode ser interpretada sem nenhuma referência a base ou universo.|O significado quantitativo depende da base considerada.
''','logic')
topic('RLM-B04-S02','Percentual de percentual exige multiplicar as taxas aplicadas em sequência.','Se a fração a de um grupo contém uma fração b com certa característica, a participação conjunta é a×b. Determine se a segunda taxa incide no total ou no subgrupo. Somar taxas de bases diferentes pode produzir resultado incorreto.', '''
C|Se 40% dos pedidos são digitais e 25% dos digitais exigem ajuste, os digitais com ajuste representam 10% do total.|A taxa conjunta é o produto 0,40 × 0,25 = 0,10, equivalente a dez por cento.
E|Se metade da turma revisou e metade dos que revisaram acertou tudo, 50% da turma acertou tudo nesse subgrupo.|A metade da metade corresponde a 25% da turma.
C|Em 300 processos, 20% são urgentes; dentre os urgentes, 10% foram devolvidos. São seis devoluções urgentes.|300 × 0,20 × 0,10 = 6.
E|Somar 30% e 20% fornece o percentual de quem pertence a um grupo que é 30% do total e a um subgrupo que é 20% daquele grupo.|O percentual conjunto é 0,30 × 0,20 = 6%.
C|Se 60% usam aplicativo e 50% desses também usam telefone, 30% do total usam os dois nesse recorte.|O subgrupo corresponde a 0,60 × 0,50 = 0,30.
C|Se 15% dos 200 atendimentos receberam retorno e 40% desses retornos foram presenciais, houve 12 retornos presenciais.|200 × 0,15 × 0,40 = 12.
E|Dez por cento de vinte por cento de uma quantidade equivalem a trinta por cento dela.|O produto é 2%, e não a soma de 30%.
E|Reduzir uma parte de 50% do total pela metade faz essa parte passar a representar 40% do total fixo.|Metade de 50% corresponde a 25% do total fixo.
''','logic')
topic('RLM-B04-S03','Aumentos e descontos sucessivos se calculam por fatores multiplicativos.','Aumento r usa 1+r e desconto d usa 1−d, com taxas decimais. As taxas não se anulam por mera oposição: a segunda incide na nova base. Para recuperar preço anterior, divida pelo fator.', '''
C|Um preço de R$ 100 aumentado em 20% e depois reduzido em 20% termina em R$ 96.|100 × 1,20 × 0,80 = 96.
E|Dois descontos sucessivos de 10% equivalem a desconto único de 20%.|O fator é 0,90² = 0,81: desconto de 19%.
C|Aumentos sucessivos de 10% e 20% produzem aumento total de 32%.|O produto dos fatores 1,10 × 1,20 = 1,32 representa aumento de trinta e dois por cento.
E|Se um preço ficou em R$ 80 após desconto de 20%, o preço original era R$ 96.|Dividir 80 por 0,80 produz R$ 100.
''','logic')
topic('RLM-B04-S04','Comparar percentuais exige distinguir taxa, quantidade e pontos percentuais.','De 20% para 30% há dez pontos percentuais e aumento relativo de cinquenta por cento. Taxa maior em base menor pode produzir quantidade menor. Relações inversas usam bases diferentes, por isso os percentuais não são simétricos.', '''
C|Uma taxa que passa de 20% para 30% sobe dez pontos percentuais.|Pontos percentuais medem a diferença direta entre taxas percentuais.
E|A passagem de 20% para 30% é aumento relativo de apenas 10%.|O aumento relativo é (30 − 20) ÷ 20 = 50%.
C|Dez por cento de 1.000 é maior que vinte por cento de 400.|As quantidades são 100 e 80, respectivamente.
E|Se A é 50% maior que B, B é necessariamente 50% menor que A.|Com B=100 e A=150, B é 33,33…% menor que A.
''','logic')

proofs=[]
def check(k,n,calculated,method):
 expected=DATA[k][0][n-1][1]
 assert bool(calculated)==expected,(k,n,expected,calculated)
 proofs.append({'topic':k,'item_autoral':n,'method':method,'result':bool(calculated)})
imp=lambda p,q:(not p) or q
valuations=list(itertools.product([False,True],repeat=2))
check('RLM-B01-S04',1,(True and False)==False,'Tabela-verdade: conjunção V,F')
check('RLM-B01-S04',2,(False and True)==True,'Tabela-verdade: conjunção F,V')
check('RLM-B01-S04',3,(True or True)==True,'Tabela-verdade: disjunção V,V')
check('RLM-B01-S04',4,(True or True)==False,'Tabela-verdade: disjunção V,V')
check('RLM-B01-S04',5,imp(True,False)==False,'Tabela-verdade: condicional V,F')
check('RLM-B01-S04',6,imp(False,False)==False,'Tabela-verdade: condicional F,F')
check('RLM-B01-S04',7,(False==False)==True,'Tabela-verdade: bicondicional F,F')
check('RLM-B01-S04',8,all((p==q)==(p or q) for p,q in valuations),'Exaustão das quatro linhas')
for n,cal in [(1,2**3==8),(2,2**1==4),(3,2**4==16),(4,2**5==10),(5,len(valuations)==4),(6,2**3==3*2**2),(7,all(q==q for p,q,r in itertools.product([False,True],repeat=3))),(8,2**6==36)]:check('RLM-B01-S06',n,cal,'Potências de dois e contagem de variáveis distintas')
check('RLM-B01-S07',1,all((not(p and q))==((not p)or(not q)) for p,q in valuations),'Lei de De Morgan em quatro linhas')
check('RLM-B01-S07',2,all((not(p or q))==((not p)or(not q)) for p,q in valuations),'Teste da falsa equivalência em quatro linhas')
check('RLM-B01-S07',3,all((not imp(p,q))==(p and not q) for p,q in valuations),'Negação de condicional em quatro linhas')
check('RLM-B01-S07',4,all(imp(p,q)==imp(not p,not q) for p,q in valuations),'Teste de inversão em quatro linhas')
for n,cal in [(1,all(p or not p for p in [False,True])),(2,len(set(p and not p for p in [False,True]))>1),(3,all(imp(p,p)for p in [False,True])),(4,len(set(p and q for p,q in valuations))==2),(5,all(p or q for p,q in valuations)),(6,all((not(p or not p))==False for p in [False,True])),(7,all(p==(not p)for p in [False,True])),(8,all((p and q)==(p or q) for p,q in valuations))]:check('RLM-B02-S01',n,cal,'Enumeração de valores e classificação lógica')
def valid(premises,conclusion):return all(not all(f(p,q) for f in premises) or conclusion(p,q) for p,q in valuations)
for n,pr,co in [(1,[imp,lambda p,q:p],lambda p,q:q),(2,[imp,lambda p,q:q],lambda p,q:p),(3,[imp,lambda p,q:not q],lambda p,q:not p),(4,[imp,lambda p,q:not p],lambda p,q:not q)]:check('RLM-B02-S02',n,valid(pr,co),'Todas as interpretações das premissas e conclusão')
A={2,4,6}
for n,cal in [(1,4 in A),(2,frozenset({4}) in A),(3,{2,6}<=A),(4,len(set())==1),(5,set()<=A),(6,{1,2,2}=={2,1}),(7,{1,2}<={1}),(8,1 in {frozenset({1}),2})]:check('RLM-B03-S01',n,cal,'Operações nativas de conjuntos Python')
A={1,2,3};B={3,4}
for n,cal in [(1,A|B=={1,2,3,4}),(2,A&B=={1,2,3,4}),(3,A-B=={1,2}),(4,B-A=={1,2}),(5,A&B==B&A),(6,A-B==B-A),(7,A|set()==A),(8,{1}&{2}=={1})]:check('RLM-B03-S02',n,cal,'União, interseção e diferença em Python')
U={1,2,3,4,5};A={2,4}
for n,cal in [(1,U-A=={1,3,5}),(2,U-A==(U|{6})-A),(3,U-(U-A)==A),(4,U-U==U)]:check('RLM-B03-S03',n,cal,'Complemento relativo ao universo explícito')
for n,cal in [(1,32+28-10==50),(2,80-(50+40-20)==20),(3,25-9==16),(4,18+14-1==32)]:check('RLM-B03-S04',n,cal,'Princípio da inclusão-exclusão')
for n,cal in [(1,250*20/100==50),(2,30/0.15==450),(3,(50-40)/40==0.25),(4,(100-80)/80==0.20),(5,18/0.30==60),(6,200*(1-0.25)==175),(7,1/2==50/100)]:check('RLM-B04-S01',n,cal,'Cálculo direto ou inversão de base percentual')
for n,cal in [(1,0.40*0.25==0.10),(2,0.50*0.50==0.50),(3,300*0.20*0.10==6),(4,0.30*0.20==0.50),(5,0.60*0.50==0.30),(6,200*0.15*0.40==12),(7,0.10*0.20==0.30),(8,0.50*0.50==0.40)]:check('RLM-B04-S02',n,cal,'Produto de taxas com bases sucessivas')
for n,cal in [(1,abs(100*1.20*0.80-96)<1e-9),(2,abs((1-0.9**2)-0.20)<1e-9),(3,abs(1.10*1.20-1-0.32)<1e-9),(4,80/0.80==96)]:check('RLM-B04-S03',n,cal,'Fatores multiplicativos de aumento e desconto')
for n,cal in [(1,30-20==10),(2,(30-20)/20==0.10),(3,0.10*1000>0.20*400),(4,(150-100)/150==0.50)]:check('RLM-B04-S04',n,cal,'Comparação de bases, taxas e pontos percentuais')

lessons=[]
proof_by_topic={}
for p in proofs:proof_by_topic.setdefault(p['topic'],[]).append(p)
for r in plan['assuntos']:
 k=r['id_planejamento']
 if k not in DATA:continue
 parsed,src=DATA[k];assert len(parsed)==r['meta_questoes_autorais'],(k,len(parsed),r['meta_questoes_autorais'])
 core,theory=THEORY[k];lid='v17-'+k.lower();d='port' if k.startswith('PORT') else 'rlm'
 sr={**sources[src],'locator':sources[src]['locator']+' • '+r['assunto']}
 order=list(enumerate(parsed,1));random.Random(k).shuffle(order)
 qs=[]
 for i,(original,(t,a,e))in enumerate(order,1):
  qs.append({'id':f'{lid}-q{i:03d}','text':t,'answer':a,'explanation':e,'kind':'autoral','version':1,'difficulty':'basico' if original<=len(parsed)//3 else 'intermediario' if original<=2*len(parsed)//3 else 'avancado','family':f'{k}-aspecto-{original:02d}','microtopic':k,'sourceRef':sr,'mode':'fixacao' if i<=max(4,len(parsed)//4) else 'reserva' if i>len(parsed)*3//4 else 'treino','editorialStatus':'conferencia_autoral','reviewedAt':'2026-10-27'})
 # O conhecimento cobrado é explicitado antes da rodada; não há cobrança de regra sem teoria.
 notes=list(dict.fromkeys(e for _,_,e in parsed))
 rule=theory+' Pontos de aplicação: '+' '.join(notes)
 lesson={'id':lid,'d':d,'title':r['assunto'],'core':core,'rule':rule,'example':parsed[0][0]+' Análise: '+parsed[0][2],'contrast':'Compare regra geral, hipótese e conclusão: '+parsed[1][2],'limit':'Não generalize por reconhecimento. '+theory.split('. ')[-1],'source':'pt' if d=='port' else 'logic','sources':[sr],'minutes':40,'block':r['bloco'],'planId':k,'subtopics':notes,'questions':qs}
 lessons.append(lesson)
assert len(lessons)==45
allq=[q for l in lessons for q in l['questions']]
assert len(allq)==480,len(allq)
assert len({q['id']for q in allq})==480
assert len({q['text']for q in allq})==480
assert all(isinstance(q['answer'],bool) and len(q['explanation'])>20 for q in allq)
assert all(len(l[f])>10 for l in lessons for f in ['core','rule','example','contrast','limit'])
out={'lessons':lessons,'sources':list(sources.values()),'editorial':{'version':1,'authorship':'JARVIS AUTORAL','date':'2026-10-27','counts':{'port':360,'rlm':120,'lessons':45},'method':'Itens individualmente escritos; ordem reprodutivelmente embaralhada, sem multiplicação por troca de nomes ou números. Cálculos e relações lógicas conferidos com Python. Dificuldades são rótulos editoriais iniciais, sem calibração estatística.','review':'Conferência autoral e estrutural; não revisão independente.','sourceAccess':'Portal Gov.br e VOLP consultados; Planalto retornou bloqueio ao Manual e ao D9.758. Regra normativa de tratamento conferida em publicação oficial da Câmara e em fonte oficial federal; acesso alternativo ao Manual SIGEPE identificado como edição antiga e não usado para regras documentais de 2018.','computationalChecks':proofs}}
target=ROOT/'data/port-rlm.json';target.parent.mkdir(exist_ok=True);target.write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'file':str(target),'lessons':len(lessons),'questions':len(allq),'checks':len(proofs)},ensure_ascii=False))
