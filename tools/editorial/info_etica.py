"""Monta itens escritos individualmente; não expande templates nem duplica enunciados."""
from pathlib import Path
import json, collections, re
ROOT=Path(__file__).resolve().parents[2]
PLAN=json.loads((ROOT/'data/curriculum-plan.json').read_text())
S={
'cert':{'title':'CERT.br — Cartilha de Segurança para Internet','url':'https://cartilha.cert.br/fasciculos/','locator':'Fascículos Redes, Privacidade, Computadores e Códigos Maliciosos'},
'auth':{'title':'CERT.br — Autenticação','url':'https://cartilha.cert.br/fasciculos/autenticacao/fasciculo-autenticacao.pdf','locator':'Senhas, fatores e proteção das contas'},
'backup':{'title':'CERT.br — Backup','url':'https://cartilha.cert.br/fasciculos/backup/fasciculo-backup.pdf','locator':'Cópias de segurança e recuperação'},
'excel':{'title':'Microsoft — Excel','url':'https://support.microsoft.com/pt-br/excel/','locator':'Fórmulas, dados e referências'},
'ref':{'title':'Microsoft — Referências relativas, absolutas e mistas','url':'https://support.microsoft.com/pt-br/excel/switch-between-relative-absolute-and-mixed-references','locator':'Tabela de atualização de referências ao copiar fórmulas'},
'sumif':{'title':'Microsoft — SOMASE','url':'https://support.microsoft.com/pt-br/excel/functions/sumif-function','locator':'Sintaxe, critérios e intervalo_soma'},
'word':{'title':'Microsoft — Auxílio e aprendizado do Word','url':'https://support.microsoft.com/pt-br/word/','locator':'Formatação, layout e colaboração'},
'ppt':{'title':'Microsoft — Auxílio e aprendizado do PowerPoint','url':'https://support.microsoft.com/pt-br/powerpoint/','locator':'Slides, apresentação e design'},
'outlook':{'title':'Microsoft — Auxílio e aprendizado do Outlook','url':'https://support.microsoft.com/pt-br/outlook/','locator':'Email, pastas, regras e calendário'},
'windows':{'title':'Microsoft — Ajuda do Windows','url':'https://support.microsoft.com/pt-br/windows/','locator':'Arquivos, ferramentas e segurança'},
'winend':{'title':'Microsoft — Encerramento do suporte regular ao Windows 10','url':'https://support.microsoft.com/pt-br/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025','locator':'Suporte regular encerrado em 14/10/2025; programas de extensão têm condições próprias'},
'e':{'title':'Decreto 1.171/1994 — texto atualizado na Câmara','url':'https://www2.camara.leg.br/legin/fed/decret/1994/decreto-1171-22-junho-1994-449441-normaatualizada-pe.pdf','locator':'Anexo, incisos I a XVI, XVIII, XXII e XXIV, conforme assunto'},
'et':{'title':'Decreto 6.029/2007 — Câmara dos Deputados','url':'https://www2.camara.leg.br/legin/fed/decret/2007/decreto-6029-1-fevereiro-2007-550363-publicacaooriginal-66313-pe.html','locator':'Artigos 1 a 25, conforme assunto'}
}
S['countif']={'title':'Microsoft — CONT.SE','url':'https://support.microsoft.com/pt-br/excel/get-started/use-the-countif-function-in-microsoft-excel','locator':'Sintaxe CONT.SE e critérios textuais/numéricos'}
S['sumifs']={'title':'Microsoft — SOMASES','url':'https://support.microsoft.com/pt-br/excel/functions/sumifs-function','locator':'Sintaxe e ordem de argumentos em comparação com SOMASE'}
D={}
def put(id,source,locator,core,contrast,example,lines):
    qs=[]
    for line in lines.strip().splitlines():
        a,t,e=line.split('|',2)
        qs.append((a=='C',t,e))
    D[id]=(source,locator,core,contrast,example,qs)
put('INFO-B01-S01','cert','Fascículo Redes: Internet e redes locais','Internet é a interligação global de redes; intranet é uma rede de uso interno controlado. Ambas podem empregar TCP/IP e aplicações web.','Restrição de acesso não é um protocolo próprio nem garantia de segurança. Extranet permite acesso controlado a participantes externos.','Um órgão disponibiliza páginas internas por navegador e exige autenticação de seus servidores.', '''
C|Um portal interno pode usar HTTP e navegador sem se tornar, por isso, um serviço público aberto na Internet.|O mesmo conjunto de tecnologias web pode servir a uma intranet com acesso restrito.
E|Uma intranet é definida pela obrigação de utilizar protocolos incompatíveis com os da Internet.|A intranet pode empregar TCP/IP, HTTP e outras tecnologias usadas na Internet; a distinção central é o uso restrito.
E|Se a rede de um órgão não oferece conexão externa, ela deixa de poder ser classificada como intranet.|Uma rede interna pode funcionar sem acesso à Internet.
C|Conceder a fornecedores acesso autenticado a uma parte da rede institucional é compatível com uma extranet.|A extranet estende serviços restritos a participantes externos autorizados.
C|Restringir uma página a funcionários não dispensa controles de acesso e atualização do servidor.|A restrição de público não elimina ameaças internas, credenciais comprometidas nem vulnerabilidades.
E|Uma VPN torna público todo serviço da intranet que o usuário acessa remotamente.|A VPN pode criar um canal protegido até a rede privada; o serviço não se torna aberto ao público.
E|Internet e Web designam exatamente a mesma estrutura, pois não existem serviços de Internet fora de páginas web.|A Web é um serviço sobre a Internet; email e outros serviços não se reduzem a páginas web.
C|Um sistema interno pode usar nomes de domínio e endereços IP mesmo sem aparecer em buscadores públicos.|DNS e IP não dependem de indexação por mecanismos de busca públicos.
''')
put('INFO-B01-S02','cert','Fascículo Redes: endereçamento e conexão','Endereços IP identificam interfaces no contexto da rede. IPv4 usa 32 bits e IPv6 usa 128; DNS relaciona nomes e dados de endereçamento.','IP, endereço físico MAC, nome de domínio e conta de email são identificadores de camadas e funções distintas.','Um computador recebe um endereço do roteador por DHCP e consulta um nome via DNS.', '''
E|O IPv6 usa endereços de 32 bits, enquanto o IPv4 usa 128 bits.|Os comprimentos foram invertidos: IPv4 tem32 bits; IPv6,128.
C|Um serviço DHCP pode distribuir automaticamente parâmetros de configuração de rede a computadores.|DHCP automatiza atribuição de configurações como endereço IP e outros parâmetros.
E|DNS é o serviço cuja função principal é criptografar todos os arquivos de um computador.|DNS resolve nomes e outros registros; não é uma ferramenta de criptografia de arquivos.
C|Um endereço IPv4 privado pode ser reutilizado em redes privadas diferentes sem funcionar como endereço público global exclusivo.|Endereços privados têm escopo interno e não devem ser confundidos com endereços públicos globalmente roteáveis.
E|Dois equipamentos da mesma rede local podem usar simultaneamente o mesmo endereço IP sem risco de conflito apenas por terem MACs diferentes.|A duplicação do IP no mesmo contexto de rede pode causar conflito; MACs distintos não eliminam esse problema.
C|Um nome de domínio pode continuar igual mesmo que o endereço IP do servidor mude.|O DNS permite atualizar o endereço associado ao nome.
C|O endereço MAC e o endereço IP têm papéis diferentes na comunicação de rede.|O MAC atua no enlace; o IP serve ao endereçamento lógico entre redes.
E|Um endereço de email no formato pessoa@orgao.gov.br é, por definição, um endereço IPv6.|Email identifica caixa/usuário em domínio; IPv6 é outra estrutura de endereçamento.
''')
put('INFO-B01-S03','cert','Navegação segura; programas e serviços web','Navegador é um aplicativo cliente que apresenta conteúdo web; buscador é um serviço que ajuda a localizar conteúdo.','A barra de endereços pode integrar pesquisa sem transformar o navegador no próprio índice de busca.','O servidor abre o Firefox e pesquisa uma norma em um buscador, depois acessa diretamente a URL oficial.', '''
C|Firefox e Edge são navegadores, enquanto um mecanismo de busca consulta um índice de informações.|Aplicativo de navegação e serviço de pesquisa desempenham funções diferentes.
E|Acessar uma URL conhecida exige, necessariamente, pesquisar primeiro seu nome em um buscador.|É possível informar a URL diretamente na barra de endereços.
C|Uma busca feita na barra de endereços pode usar o mecanismo de pesquisa configurado como padrão.|Navegadores costumam integrar o envio de termos a um serviço de busca escolhido.
E|O primeiro resultado patrocinado de uma pesquisa é prova de autenticidade do endereço apresentado.|Anúncios e posição nos resultados não garantem legitimidade; é necessário verificar domínio e contexto.
C|É possível mudar o buscador padrão sem substituir o navegador instalado.|A configuração do serviço de busca e a escolha do aplicativo são decisões distintas.
E|Um favorito armazena obrigatoriamente uma cópia integral da página para leitura offline.|O favorito normalmente guarda a referência ao endereço; não garante arquivamento do conteúdo.
E|Se um navegador exibe a página sem erro, o conteúdo publicado nela é necessariamente verdadeiro.|Renderização correta não é verificação de fatos, autoria ou confiabilidade.
C|Downloads devem ser avaliados também pela origem, pelo tipo de arquivo e pelo contexto, mesmo quando o navegador permite baixá-los.|Permissão técnica para download não certifica segurança do arquivo.
''')
put('INFO-B01-S04','cert','Fascículos Redes e Privacidade: HTTPS e navegação','URL localiza um recurso e pode conter esquema, host, caminho, consulta e fragmento. HTTPS usa TLS para proteger a comunicação.','HTTPS protege o canal; não garante honestidade do comerciante, ausência de fraude ou veracidade de uma página.','Uma página falsa pode ter certificado válido para o domínio falso escolhido pelo golpista.', '''
C|Na URL https://servico.exemplo.gov.br/pedido?id=4, o esquema indica HTTPS.|A parte anterior a :// identifica o esquema de acesso; o host é servico.exemplo.gov.br.
E|Um certificado HTTPS válido comprova que todos os produtos oferecidos pelo site serão entregues.|O certificado autentica o domínio no canal protegido; não certifica a conduta comercial.
C|TLS ajuda a proteger a confidencialidade e a integridade dos dados em trânsito entre cliente e servidor.|A proteção do canal reduz leitura e alteração indevida durante o transporte.
E|Usar HTTPS elimina a necessidade de examinar se o domínio contém imitações do nome oficial.|Um golpista pode obter certificado para seu próprio domínio enganoso.
E|Tudo o que aparece depois de uma barra na URL faz parte obrigatória do nome de domínio.|Após o host podem existir caminho, consulta e fragmento; não são todos componentes do domínio.
C|Um alerta de certificado deve motivar verificação, sobretudo antes de fornecer senha ou informação sensível.|Ignorar o alerta pode expor o usuário a comunicação não confiável ou configuração inadequada.
C|HTTP e HTTPS não significam, por si, que uma página foi indexada por um buscador.|Protocolo de acesso e indexação são aspectos independentes.
E|Criptografar o tráfego torna dispensável proteger os dados armazenados no computador e no servidor.|TLS protege o trânsito; proteção em repouso e controles dos dispositivos continuam necessários.
''')
put('INFO-B01-S05','cert','Fascículo Privacidade: cookies e rastros','Cookies armazenam dados associados à navegação; cache reaproveita recursos para reduzir transferências. Navegação privativa tem alcance local limitado.','Limpar cookies pode encerrar sessões; limpar cache pode exigir novo download. Navegação privativa não significa anonimato global.','Ao limpar cookies de um portal, o usuário precisa autenticar-se novamente.', '''
C|Apagar cookies de autenticação pode fazer um portal exigir novo login.|O estado de sessão pode estar associado a cookies; removê-los pode invalidar a continuidade do acesso local.
E|A janela privativa impede que o provedor, o empregador e os sites observem qualquer atividade de rede.|O modo privativo reduz rastros locais; não oculta automaticamente o tráfego de todos os participantes da comunicação.
E|Cache e cookie têm exatamente a mesma finalidade: ambos guardam apenas senhas do usuário.|Cache reaproveita recursos; cookies podem manter preferências e sessões. Nenhum se define como depósito exclusivo de senhas.
C|Remover recursos do cache pode aumentar o volume baixado na próxima visita à página.|Sem a cópia local reutilizável, o navegador pode precisar transferir os recursos novamente.
''')
put('INFO-B01-S06','outlook','Email: destinatários, anexos, pastas e respostas','Para identifica destinatários principais; Cc envia cópias visíveis e Cco oculta essa lista dos demais destinatários. Anexos exigem avaliação de segurança.','Responder, responder a todos e encaminhar têm efeitos diferentes. Limites de anexos dependem do serviço.','Uma circular externa é enviada a várias pessoas com os endereços em Cco para não expor a lista.', '''
E|Colocar todos os destinatários em Cc oculta seus endereços uns dos outros.|Cc é cópia visível; Cco é o campo utilizado para ocultar a lista dos demais destinatários.
C|Responder a todos pode divulgar a resposta a mais pessoas do que responder somente ao remetente.|O comando inclui destinatários envolvidos conforme os campos e o cliente; a lista deve ser conferida.
E|Um arquivo anexo passa a ser seguro apenas porque chegou no email de um conhecido.|Contas podem ser comprometidas e remetentes falsificados; contexto e arquivo precisam ser avaliados.
C|Encaminhar uma mensagem pode transportar seu conteúdo e anexos a novos destinatários, exigindo cuidado com dados pessoais.|O encaminhamento pode ampliar a exposição de informação; não é uma operação sem efeito de privacidade.
''')
put('INFO-B01-S07','outlook','Organizar email e calendário no Outlook','O Outlook reúne email e recursos de organização, com funcionalidades que variam entre versões clássica, nova e web.','Categoria identifica; pasta organiza; regra automatiza ações. Excluir não é o mesmo que arquivar.','Uma regra move mensagens de um remetente institucional para uma pasta de trabalho.', '''
C|Uma regra de email pode automatizar o encaminhamento de mensagens para uma pasta conforme critérios definidos.|Regras permitem ações automáticas; os critérios e as limitações dependem da versão e da conta.
E|Arquivar uma mensagem equivale sempre a apagá-la definitivamente e torná-la irrecuperável.|Arquivamento e exclusão são operações diferentes; arquivar mantém a mensagem em local de organização.
E|A existência de um evento no calendário garante que o participante aceitou o convite.|Criar ou enviar convite não é o mesmo que receber a aceitação do convidado.
C|Categorias podem servir à classificação de mensagens sem exigir que cada categoria corresponda a uma pasta diferente.|Categorias são marcadores organizacionais e podem coexistir com a estrutura de pastas.
''')
put('INFO-B01-S08','backup','Nuvem, sincronização e proteção de arquivos','Nuvem oferece recursos remotos por rede. Compartilhamento e sincronização precisam de permissões e não dispensam planejamento de backup.','Uma cópia sincronizada pode refletir exclusões; disponibilidade offline depende de configuração e cópia local.','Um arquivo compartilhado somente com leitura pode ser consultado sem autorizar alteração do original.', '''
E|Se uma pasta é sincronizada, qualquer exclusão acidental será impedida automaticamente em todos os dispositivos.|A sincronização pode propagar exclusões; recuperação depende de recursos como lixeira, versões e backup.
C|Compartilhar um arquivo apenas para leitura é diferente de conceder permissão de edição.|Permissões delimitam o que cada destinatário pode fazer; leitura não autoriza alterar o original.
C|Um arquivo marcado para uso offline pode ter cópia local, enquanto um arquivo somente online pode exigir conexão para ser aberto.|A disponibilidade depende da configuração do cliente e da existência de conteúdo local.
E|Armazenar dados na nuvem transfere ao provedor toda a responsabilidade por senhas e concessão de acesso feitas pelo usuário.|O usuário continua responsável por proteger credenciais e configurar acessos adequadamente.
''')
put('INFO-B02-S01','word','Word: formatação, seções, estilos e revisão','Word é editor de documentos. Formatação de caracteres e parágrafos, estilos, quebras de página e seções têm alcances diferentes.','Enter encerra parágrafo; quebra de página inicia outra página; seção permite configurar partes do documento.','Para reunir capítulos em um sumário, aplicar estilos de títulos é mais robusto do que apenas aumentar a fonte.', '''
C|Aplicar um estilo de título pode dar estrutura ao documento e alimentar um sumário automático.|Os estilos de títulos identificam a hierarquia estrutural usada pelo sumário.
E|Aumentar manualmente o tamanho de uma palavra garante que ela será incluída em qualquer sumário automático.|A aparência visual, sozinha, não garante a classificação como título usada pelo sumário.
C|Uma quebra de seção pode permitir orientação de página diferente em uma parte do documento.|Seções delimitam configurações de layout, como orientação e cabeçalhos, conforme a configuração adotada.
E|Pressionar Enter e inserir uma quebra de página são operações estruturalmente idênticas no Word.|Enter cria parágrafo; quebra de página força a passagem para a próxima página.
E|O alinhamento justificado altera necessariamente o tipo e o tamanho da fonte selecionada.|Alinhamento de parágrafo e propriedades de fonte são atributos distintos.
C|O controle de alterações permite registrar revisões para posterior aceitação ou rejeição.|Registrar alterações não significa aceitá-las automaticamente no texto final.
E|Exportar um documento para PDF elimina a necessidade de conferir sua paginação e legibilidade.|A exportação pode mudar a apresentação; o resultado precisa ser verificado.
C|Cabeçalhos e rodapés podem conter campos de numeração de página que se atualizam conforme a organização do documento.|Campos de página não precisam ser números digitados manualmente em cada folha.
''')
put('INFO-B02-S02','ref','Referências relativas, absolutas e mistas: tabela de deslocamentos','Referências relativas mudam com o deslocamento ao copiar fórmulas; o cifrão fixa coluna e/ou linha.','A1 é relativa; $A$1 é absoluta; $A1 e A$1 são mistas. As questões de cópia usam a operação copiar, não mover.','Copiar =A1*$B$1 de C1 para C2 produz =A2*$B$1.', '''
C|Copiar =A1 de B1 para B2 ajusta a fórmula para =A2.|A linha relativa acompanha o deslocamento de uma linha para baixo.
E|Copiar =$A$1 duas colunas para a direita transforma a referência em =$C$1.|O cifrão fixa a coluna A e a linha1; a referência absoluta permanece $A$1.
C|Em =$A1, a coluna está fixa, mas a linha continua relativa.|O cifrão anterior à letra fixa apenas a coluna.
E|Na referência A$1, tanto a coluna quanto a linha estão fixas.|Somente a linha1 está fixa; a coluna A pode se ajustar ao copiar.
C|Copiar =A$1 de B2 para C3 produz =B$1.|O deslocamento de uma coluna altera A para B; a linha1 permanece fixa.
C|Copiar =$A1 de B2 para D5 produz =$A4.|A coluna A permanece fixa e a linha aumenta três posições, de1 para4.
E|O conteúdo numérico de uma célula determina se sua referência é relativa ou absoluta.|O tipo de referência depende da notação com cifrões na fórmula, não do número armazenado.
E|Em uma fórmula copiada, =A1+$B$2 e =$A$1+B2 sempre sofrem os mesmos ajustes.|As duas fórmulas fixam referências diferentes; seus ajustes dependem de quais colunas e linhas são relativas.
''')
put('INFO-B02-S03','excel','Excel: operadores e ordem de cálculo','Fórmulas começam usualmente com =. Parênteses, potência, multiplicação/divisão e soma/subtração delimitam a ordem de cálculo; & concatena texto.','Exibição formatada não deve ser confundida com valor armazenado. Operadores de comparação retornam valores lógicos.','Com A1=3 e B1=4, =A1+B1*2 resulta11, enquanto =(A1+B1)*2 resulta14.', '''
C|Com A1=3 e B1=4, a fórmula =A1+B1*2 resulta em11.|A multiplicação4×2 é feita antes da soma3+8.
E|Com A1=3 e B1=4, =(A1+B1)*2 resulta em11.|Os parênteses determinam primeiro3+4=7;7×2=14.
E|O operador & soma obrigatoriamente dois números como uma operação aritmética.|& concatena representações de texto; a soma aritmética usa +.
C|A fórmula =5>3 produz um resultado lógico verdadeiro.|O operador > compara valores e retorna VERDADEIRO quando a relação procede.
C|Uma formatação com duas casas decimais pode mudar a exibição sem arredondar permanentemente o valor armazenado.|Formatação visual e alteração do conteúdo são operações diferentes; cálculos podem usar a precisão armazenada.
E|Na expressão =2+3*4, o Excel calcula a soma antes da multiplicação só porque o sinal + aparece primeiro.|A precedência da multiplicação leva ao resultado14, não20.
C|Em =10/2*3, operações de mesma precedência são avaliadas da esquerda para a direita, resultando15.|Primeiro10÷2=5; depois5×3=15.
E|Uma fórmula que mostra erro de divisão por zero pode ser considerada correta apenas por estar bem formatada.|Formatação não resolve erro de cálculo; denominador e lógica precisam ser revistos.
''')
put('INFO-B02-S04','sumif','SOMASE e CONT.SE; Excel pt-BR com separador de argumentos ponto e vírgula','SOMASE soma valores que atendem a um critério; CONT.SE conta células que o atendem. Critérios textuais ou com operadores ficam entre aspas.','Contar registros não é somar valores. SOMASES/CONT.SES aceitam múltiplos critérios e não se confundem com as versões de um critério.','Com A1:A3 contendo2,5,8, CONT.SE(A1:A3;">4") conta2 e SOMASE(A1:A3;">4") soma13.', '''
C|Se A1:A3 contém2,5 e8, =CONT.SE(A1:A3;">4") resulta2.|Dois valores,5 e8, atendem ao critério; a função conta as células, não soma13.
E|Se A1:A3 contém2,5 e8, =SOMASE(A1:A3;">4") resulta2.|SOMASE soma os valores elegíveis:5+8=13.
C|Em =SOMASE(A1:A4;"Sul";B1:B4), o critério é aplicado em A e os valores correspondentes são somados em B.|O terceiro argumento indica o intervalo_soma; o primeiro é avaliado pelo critério.
E|O critério ">=10" usado em SOMASE deve ser escrito sem aspas para funcionar como uma comparação textual de critério.|Critérios que incluem operador de comparação são apresentados entre aspas na sintaxe indicada.
C|CONT.SE permite contar ocorrências de um texto específico em um intervalo.|A função aceita critérios textuais além de comparações numéricas.
E|SOMASE e SOMASES têm obrigatoriamente a mesma ordem e a mesma quantidade de argumentos.|São funções distintas; SOMASES começa pelo intervalo de soma e permite pares de intervalos/critérios.
E|Na função SOMASE, omitir intervalo_soma impede sempre qualquer resultado válido.|Quando omitido, a soma é feita no próprio intervalo ao qual o critério foi aplicado.
C|Com valores10,20 e30 em C1:C3, =SOMASE(C1:C3;">=20") retorna50.|O critério inclui20 e30; a soma é50.
''')
put('INFO-B02-S05','excel','Excel: classificação, filtros, seleção e duplicatas','Classificar muda a ordem dos dados; filtrar controla quais registros ficam visíveis. Remover duplicatas altera os dados e depende das colunas escolhidas.','Ocultar uma linha não é apagá-la. Ordenar apenas uma coluna pode romper a associação com as demais.','Antes de ordenar uma tabela de nomes e valores, selecione a estrutura coerente e identifique o cabeçalho.', '''
C|Filtrar uma tabela pode ocultar temporariamente linhas que não atendem ao critério sem apagá-las.|Filtro muda a visualização dos registros, não exige a exclusão física dos dados.
E|Aplicar filtro e remover duplicatas são operações equivalentes e sempre reversíveis pela simples limpeza do filtro.|Remover duplicatas elimina registros conforme critérios; limpar filtro apenas reexibe linhas filtradas.
C|Ao remover duplicatas, escolher uma ou várias colunas modifica o critério de comparação entre linhas.|Uma chave de uma coluna não é necessariamente equivalente à combinação de várias colunas.
E|Ordenar somente a coluna de nomes garante que valores em colunas não incluídas acompanharão cada pessoa.|Ordenação parcial pode desfazer a correspondência entre campos de uma linha.
C|Reconhecer o cabeçalho ao classificar evita que o título da coluna seja tratado como registro comum.|Cabeçalhos e dados têm funções distintas na estrutura da tabela.
E|Uma linha oculta por um filtro foi necessariamente apagada da planilha.|Ocultação visual não implica exclusão do conteúdo.
E|O preenchimento automático tem como única função copiar literalmente uma célula, sem gerar séries.|A ferramenta também pode estender sequências e ajustar referências, dependendo dos dados e das opções.
C|Guardar uma cópia antes de operações de limpeza em massa ajuda a recuperar dados se o critério escolhido estiver errado.|Backup e revisão prévia reduzem o impacto de remoções ou transformações indevidas.
''')
put('INFO-B02-S06','ppt','PowerPoint: slides, layouts, temas, transições e animações','Uma apresentação organiza slides com layouts, temas e objetos. Transição atua entre slides; animação atua sobre objetos.','Alterar o tema não garante conteúdo correto; Slide Mestre apoia consistência visual. Notas do apresentador e conteúdo do slide têm finalidades distintas.','Para padronizar títulos e rodapés, edite o mestre/layout em vez de ajustar dezenas de slides isoladamente.', '''
C|Uma transição controla a passagem entre slides, enquanto uma animação pode atuar sobre um objeto do slide.|Os recursos têm escopos diferentes, embora ambos produzam efeitos visuais.
E|Aplicar animação a uma imagem insere obrigatoriamente uma transição em todos os slides.|Animação de objeto não configura automaticamente a transição de toda a apresentação.
C|O Slide Mestre pode centralizar definições visuais usadas por layouts associados.|Ele ajuda a manter padrões de fontes, elementos e posicionamento em vários slides.
E|O tema de uma apresentação substitui a necessidade de conferir contraste e legibilidade.|Um tema é ponto de partida visual; a qualidade da aplicação e do conteúdo exige revisão.
E|As notas do apresentador são sempre exibidas ao público no mesmo painel do slide projetado.|A exibição depende do modo e da configuração; notas podem servir somente ao apresentador.
C|Inserir um vídeo vinculado pode exigir atenção à disponibilidade do arquivo de origem ao levar a apresentação para outro computador.|Uma dependência externa indisponível pode impedir a reprodução; vincular e incorporar não são operações idênticas.
C|Um layout define a organização de espaços reservados e pode ser alterado sem necessariamente criar um novo arquivo.|Layouts organizam elementos dentro da mesma apresentação.
E|Salvar uma apresentação como PDF preserva obrigatoriamente toda animação interativa e todo vídeo com o mesmo comportamento.|PDF é outra forma de distribuição e não conserva necessariamente recursos multimídia e interatividade do arquivo de apresentação.
''')
put('INFO-B03-S01','winend','Windows7/10 como referência histórica do edital; ciclo de suporte','Windows7 e10 aparecem no edital histórico; estudar suas funções não significa recomendar sistemas sem suporte regular. Interface e suporte variam por edição e programa.','Encerramento de suporte não significa desligamento imediato do computador. Atualização de segurança e simples funcionamento são conceitos diferentes.','Uma máquina com sistema antigo pode continuar ligando, mas isso não prova que recebe manutenção regular de segurança.', '''
C|Um sistema operacional pode continuar funcionando mesmo após o encerramento de seu suporte regular.|O fim do suporte não desliga automaticamente o equipamento; reduz ou encerra serviços e atualizações regulares conforme o ciclo.
E|A presença do Windows7 em um edital histórico obriga o aluno a instalá-lo em seu computador pessoal conectado à Internet.|O programa de estudo pode ser aprendido por documentação e ambiente controlado; a referência histórica não é recomendação de uso inseguro.
C|O suporte regular do Windows10 terminou em14/10/2025, e programas de atualização estendida possuem condições específicas.|A data do ciclo regular e as exceções contratuais devem ser distinguidas; não se deve generalizar cobertura a toda máquina.
E|Se um programa ainda abre no Windows10, isso comprova que o sistema recebe todas as atualizações regulares gratuitas de segurança.|Compatibilidade de execução não demonstra continuidade do suporte regular.
E|Windows e Microsoft Word desempenham a mesma função de sistema operacional.|Windows é sistema operacional; Word é aplicativo de edição de documentos.
C|Ferramentas e telas podem mudar entre edições e versões do Windows, devendo a questão indicar o contexto necessário.|Não é seguro transferir todo comando de uma versão para qualquer outra sem verificar.
C|O estudo de conceitos de arquivos, pastas e permissões permanece útil mesmo quando uma interface antiga deixa de ser recomendada para uso cotidiano.|Conceitos podem ser reaproveitados; detalhes de interface e suporte exigem contextualização.
E|Um programa de suporte estendido transforma automaticamente todas as edições antigas de Windows em sistemas com suporte regular sem prazo.|Extensões têm escopo, elegibilidade e duração definidos; não são suporte regular ilimitado universal.
''')
put('INFO-B03-S02','windows','Explorador de Arquivos: copiar, mover, extensões, atalhos e lixeira','Copiar cria outra ocorrência do conteúdo; mover altera o local. Extensão sugere o formato, mas renomeá-la não converte o conteúdo.','Atalho aponta para um recurso; não equivale a uma cópia independente desse recurso. Lixeira não garante recuperação de toda exclusão.','Renomear foto.jpg para foto.pdf não transforma a imagem em um PDF válido.', '''
C|Renomear a extensão de .jpg para .pdf não realiza, por si, conversão do formato interno do arquivo.|Nome e conteúdo são camadas diferentes; uma conversão requer ferramenta adequada.
E|Criar um atalho de um documento gera necessariamente uma cópia integral e independente de seu conteúdo.|O atalho referencia o alvo; sua existência não substitui o arquivo original.
C|Copiar um arquivo para outra pasta pode manter o original no local de origem.|Cópia e movimentação têm efeitos diferentes sobre a localização do original.
E|A lixeira do Windows garante recuperar qualquer arquivo excluído, inclusive todo arquivo de rede ou de dispositivo removível.|Algumas exclusões não passam pela lixeira local; recuperação não é universal.
C|Mostrar extensões ajuda a identificar um arquivo cujo nome tenta disfarçar um executável como documento.|Extensões ocultas podem facilitar enganos com nomes como relatorio.pdf.exe.
E|Duas pastas diferentes não podem conter arquivos com o mesmo nome.|A identificação inclui o caminho; nomes iguais podem existir em diretórios distintos.
C|Mover um arquivo altera seu local de armazenamento, podendo afetar referências que dependam do caminho anterior.|Programas e atalhos podem precisar localizar novamente o recurso movido.
E|Selecionar um arquivo e executar copiar é suficiente para criar a duplicata na pasta de destino, sem qualquer operação de colagem ou equivalente.|Copiar coloca o conteúdo/referência na área de transferência; a colagem ou operação equivalente efetiva a cópia ao destino.
''')
put('INFO-B03-S03','windows','Configurações, Gerenciador de Tarefas e ferramentas do sistema','Ferramentas do sistema têm funções específicas: gerenciar processos, configurar dispositivos, verificar armazenamento e aplicar atualizações.','Encerrar um processo não equivale a desinstalar o aplicativo. Otimização depende do tipo de unidade e não justifica apagar dados essenciais.','O Gerenciador de Tarefas pode auxiliar a identificar um aplicativo consumindo muitos recursos.', '''
C|O Gerenciador de Tarefas pode mostrar processos em execução e consumo de recursos.|Ele auxilia o diagnóstico de uso de CPU, memória e outros recursos conforme a versão.
E|Encerrar um aplicativo pelo Gerenciador de Tarefas desinstala obrigatoriamente o programa do computador.|Encerrar processo interrompe sua execução; desinstalação é outra operação.
C|Forçar o encerramento de um programa pode causar perda de alterações ainda não salvas.|A interrupção pode impedir o salvamento normal do trabalho.
E|Instalar uma atualização do sistema dispensa verificar se o equipamento e os dados possuem cópia de segurança.|Atualização pode falhar; backup e planejamento de recuperação continuam úteis.
C|As Configurações do Windows reúnem opções de sistema, rede e contas, mas nem todo recurso terá nome idêntico entre versões.|A organização da interface evolui, devendo ser considerado o contexto da questão.
E|Excluir manualmente arquivos desconhecidos da pasta do sistema é um procedimento geral recomendado para acelerar o Windows.|Remoção indevida pode danificar o funcionamento; ferramentas apropriadas e conhecimento são necessários.
C|Um driver permite a interação entre o sistema operacional e determinado hardware.|Drivers são componentes de comunicação e funcionamento do dispositivo no sistema.
E|A desinstalação de um driver e a limpeza de arquivos temporários executam a mesma tarefa técnica.|Remover suporte de hardware é diferente de eliminar dados temporários; os impactos também diferem.
''')
put('INFO-B03-S04','windows','Segurança do Windows: antivírus, firewall e criptografia de unidade','Defender Antivírus procura códigos maliciosos; firewall filtra tráfego conforme regras; BitLocker protege unidades por criptografia, nas edições e condições compatíveis.','Uma proteção não substitui as demais. Criptografia em repouso não impede que alguém com sessão autorizada leia o arquivo.','Um notebook desligado e protegido por criptografia pode oferecer proteção adicional contra leitura direta de seu disco.', '''
C|O firewall pode permitir ou bloquear comunicações conforme regras definidas.|Seu papel é controlar tráfego; não se limita a procurar vírus em arquivos.
E|BitLocker é o nome da ferramenta cujo objetivo principal é classificar emails indesejados.|BitLocker é recurso de criptografia de unidades, não filtro de spam.
E|Manter antivírus ativo torna desnecessário atualizar o sistema e os aplicativos.|Antivírus não corrige todas as vulnerabilidades; atualização e outras medidas continuam necessárias.
C|Criptografar uma unidade ajuda a proteger dados em repouso se o dispositivo for perdido, desde que a proteção esteja corretamente configurada.|A criptografia reduz a leitura não autorizada do armazenamento; configuração e chaves são decisivas.
C|A proteção de uma unidade por BitLocker exige cuidado com a chave de recuperação.|Perder os meios de recuperação pode dificultar ou impedir o acesso legítimo aos dados em certas situações.
E|Um firewall substitui automaticamente qualquer mecanismo de autenticação de usuários.|Filtragem de tráfego e comprovação de identidade têm funções distintas.
C|Um arquivo acessível em uma sessão já autenticada pode continuar sendo lido pelo usuário autorizado apesar da criptografia do disco.|Criptografia em repouso não bloqueia a operação normal autorizada da sessão.
E|As funcionalidades de criptografia têm exatamente a mesma disponibilidade em toda edição e configuração do Windows.|Recursos podem depender de edição, hardware e configuração; a generalização é incorreta.
''')
put('INFO-B04-S01','cert','Fascículo Códigos Maliciosos: vírus, worm, trojan e spyware','Malware é uma categoria ampla. Vírus normalmente depende de código hospedeiro; worms se propagam automaticamente explorando meios disponíveis. Trojan disfarça função maliciosa.','Ransomware descreve uma finalidade de extorsão; spyware coleta informações. Essas classificações não eliminam comportamentos combinados.','Um programa aparentemente útil pode executar ações ocultas e roubar dados.', '''
C|Um worm pode propagar-se automaticamente entre sistemas sem precisar anexar-se a um arquivo hospedeiro como característica definidora.|A propagação autônoma diferencia worms do padrão associado aos vírus.
E|Todo código malicioso precisa que o usuário clique manualmente em cada cópia para se espalhar.|Worms e exploração automática de vulnerabilidades mostram que essa exigência não é universal.
C|Um cavalo de troia pode apresentar função aparentemente legítima enquanto realiza ações maliciosas ocultas.|A dissimulação de finalidade é característica dos trojans.
E|Spyware é um mecanismo criado exclusivamente para impedir a coleta de dados pessoais.|Spyware monitora ou coleta informações sem autorização apropriada; não é mecanismo de privacidade.
C|Vírus pode inserir seu código em um arquivo ou programa hospedeiro e ativar-se quando ele é executado.|Dependência de hospedeiro e execução do código infectado são características clássicas desse tipo.
E|Um arquivo baixado de uma página com HTTPS não pode conter malware.|HTTPS protege o transporte, não certifica que o arquivo é benigno.
C|Atualizar programas pode reduzir a exploração de falhas usadas por códigos maliciosos.|Correções removem vulnerabilidades conhecidas, embora não eliminem todo risco.
E|Categorias de malware são necessariamente exclusivas, de modo que um código que rouba dados jamais pode também criptografar arquivos.|Um código pode combinar funções e técnicas; rótulos classificatórios não impõem exclusividade total.
''')
put('INFO-B04-S02','cert','Fascículos Golpes e Códigos Maliciosos: phishing, ransomware e engenharia social','Engenharia social manipula pessoas para obter ação ou informação; phishing imita comunicação confiável. Ransomware pode bloquear ou cifrar dados e exigir resgate.','Urgência, autoridade aparente e medo não validam a solicitação. Confirmar por canal independente é diferente de responder ao próprio contato suspeito.','Uma mensagem imita o suporte do órgão e exige um código de autenticação sob ameaça de bloquear a conta.', '''
E|Um pedido de senha recebido por mensagem torna-se legítimo se exibir o logotipo oficial da instituição.|Logotipos são facilmente copiados; identidade e canal precisam ser verificados.
C|Confirmar uma solicitação sensível por um canal oficial obtido independentemente da mensagem ajuda a reduzir golpes.|Usar o próprio link ou número suspeito não constitui verificação independente.
C|Uma mensagem que cria urgência para induzir a instalação de aplicativo pode empregar engenharia social.|O ataque pode explorar pressão psicológica para levar a uma ação insegura.
E|Pagar um resgate exigido por ransomware garante a restauração completa dos dados e impede novo ataque.|Não há garantia de recuperação nem de remoção de acessos ou cópias obtidas pelo atacante.
E|Phishing ocorre exclusivamente por email, nunca por mensagem instantânea ou página falsa.|A técnica pode ser veiculada por diversos canais, incluindo mensagens, redes sociais e sites falsos.
C|Backups isolados e testados podem reduzir o impacto de um ataque que criptografe os arquivos de trabalho.|Cópias não atingidas permitem recuperação; manter isolamento e testar restauração é importante.
E|Um remetente com nome de exibição de diretor basta para comprovar que a ordem veio daquela autoridade.|O nome visível pode ser falsificado; endereço e contexto também exigem verificação.
C|Fornecer um código de segunda etapa a um golpista pode permitir que ele complete um acesso indevido.|Códigos de autenticação são segredos de acesso e não devem ser repassados por solicitação suspeita.
''')
put('INFO-B04-S03','auth','Fatores de autenticação e proteção da conta','Autenticação verifica identidade; autorização delimita permissões. Senhas longas e únicas e múltiplos fatores reduzem riscos sem torná-los nulos.','Duas senhas não são necessariamente dois fatores: ambas podem ser algo que se sabe. Privilégio mínimo reduz o alcance de uma conta.','Um usuário pode autenticar-se corretamente e ainda não ter permissão para alterar a folha de pagamento.', '''
C|Um usuário pode autenticar-se no sistema e não ter autorização para editar determinado registro.|Identificação e permissão são controles distintos.
E|Usar duas senhas de conhecimento do usuário constitui necessariamente autenticação com dois fatores independentes.|As duas podem pertencer ao mesmo fator, algo que se sabe; fatores distintos exigem categorias diferentes.
C|Reutilizar a mesma senha em serviços diferentes pode ampliar o impacto de um vazamento.|Credenciais expostas em um serviço podem ser testadas em outros.
E|A ativação de múltiplos fatores elimina qualquer possibilidade de engenharia social.|Golpes podem tentar capturar códigos, autorizações e sessões; múltiplos fatores reduzem, mas não zeram riscos.
C|Conceder apenas as permissões necessárias às tarefas é compatível com o princípio do menor privilégio.|Limitar privilégios reduz ações indevidas e impacto de comprometimentos.
C|Um gerenciador de senhas pode auxiliar a manter credenciais diferentes para diversos serviços.|A ferramenta apoia geração e armazenamento; sua própria proteção também é essencial.
E|Bloquear a tela torna desnecessário manter senha de acesso e cuidado com sessões abertas.|Bloqueio é uma camada; não substitui controles de conta e proteção do ambiente.
E|Autorização é o procedimento que cifra obrigatoriamente todo conteúdo da conta.|Autorização decide acesso a recursos; criptografia protege representação dos dados.
''')
put('INFO-B04-S04','cert','Camadas de proteção: antivírus, firewall e criptografia','Segurança combina controles de finalidades diferentes: detectar códigos, filtrar tráfego e tornar dados ilegíveis sem chave adequada.','Confidencialidade, integridade e disponibilidade têm dimensões distintas; uma única ferramenta não resolve todos os riscos.','Uma organização usa antivírus, regras de rede, atualização e backup como camadas complementares.', '''
E|Criptografar os arquivos torna dispensável qualquer backup, pois a criptografia impede perda de dados.|Criptografia protege confidencialidade, mas não impede falhas, exclusão ou perda de chaves.
C|Um antivírus pode deixar de detectar um código malicioso, razão pela qual outras camadas de proteção continuam necessárias.|Detecção tem limites; atualização, restrição de privilégios e comportamento seguro complementam a proteção.
E|Um firewall é garantia de que todo documento recebido pelo usuário foi revisado e não contém informação falsa.|Firewall controla comunicação; não realiza verificação universal de conteúdo e fatos.
C|Guardar a chave criptográfica com proteção adequada é parte essencial da segurança dos dados cifrados.|Se a chave for exposta, a confidencialidade pode ser comprometida; se perdida, a recuperação pode ficar inviável.
''')
put('INFO-B04-S05','backup','Planejamento, isolamento e testes de backup','Backup é cópia voltada à recuperação. Deve ser periódico, protegido, preferencialmente diversificado e testado; sincronização não garante histórico suficiente.','Cópia no mesmo equipamento pode ser perdida com a origem. Testar restauração é mais informativo do que apenas verificar se um arquivo de backup existe.','Uma cópia desconectada ajuda quando ransomware atinge o computador e os discos permanentemente conectados.', '''
C|Testar a restauração ajuda a verificar se o backup realmente pode ser utilizado para recuperar os dados.|A existência da cópia não prova que ela é legível, completa e restaurável.
E|Guardar a única cópia de segurança no mesmo disco dos arquivos originais elimina o risco de perda por falha física desse disco.|Uma falha do disco pode atingir original e cópia; diversificação e isolamento reduzem esse risco.
C|Um backup offline pode reduzir a exposição da cópia a um ataque que alcance dispositivos conectados.|Desconectar a cópia limita os caminhos de propagação, sem dispensar proteção e verificação.
E|A sincronização que reproduz imediatamente exclusões equivale sempre a um backup com versões recuperáveis.|Sincronização pode replicar o erro; histórico e recuperação precisam ser planejados separadamente.
''')
put('ETI-B01-S01','e','Anexo, I a XIII — regras deontológicas','A ética pública exige atenção à dignidade, ao zelo, à honestidade e ao bem comum. A análise não se esgota na existência de uma proibição legal expressa.','Legalidade e finalidade pública precisam ser examinadas conjuntamente. Publicidade convive com sigilos legalmente protegidos.','Uma decisão formalmente regular pode ser eticamente inadequada se usa a função para favorecer interesse privado.', '''
C|A ausência de proibição literal não torna automaticamente ética uma conduta que desvia a função pública do bem comum.|O Código exige considerar honestidade, finalidade e moralidade, além da análise estritamente formal da legalidade.
E|O servidor deve decidir apenas entre o legal e o ilegal, sem avaliar a honestidade da conduta.|O incisoII inclui o elemento ético e a distinção entre honesto e desonesto.
C|O fim público é componente da análise da moralidade administrativa prevista no Código.|O incisoIII relaciona moralidade ao equilíbrio entre legalidade e finalidade em benefício do bem comum.
E|A remuneração paga com recursos públicos permite tratar usuários como consumidores sem qualquer vínculo com o serviço.|O custeio coletivo reforça a exigência de responsabilidade, moralidade e respeito à comunidade.
C|O Código associa o trabalho do servidor ao bem-estar da comunidade da qual ele próprio participa.|O servidor também integra a sociedade beneficiada pelo êxito do trabalho público.
E|A publicidade de todos os atos é absoluta e o Código proíbe qualquer proteção de informação sigilosa.|O incisoVII admite hipóteses de sigilo conforme a lei; publicidade não elimina proteção legítima.
C|Falsear informação para evitar constrangimento à Administração contraria a exigência ética de verdade.|O incisoVIII protege o direito à verdade mesmo quando a informação contraria interesses da Administração.
C|Negligência repetida no cumprimento de ordens legais pode comprometer o desempenho ético da função.|O incisoXI destaca atenção às ordens legais e os danos dos erros repetidos e do descaso.
E|Uma ausência injustificada é irrelevante à ética, pois apenas a produtividade mensal interessa.|O incisoXII relaciona ausências injustificadas à desmoralização do serviço e à desordem nas relações de trabalho.
E|O decoro é exigível somente dentro do prédio da repartição, sem relação com o comportamento fora dele.|O incisoI abrange o exercício da função e o comportamento fora dela, considerados os reflexos funcionais.
C|Respeitar colegas e cidadãos favorece a cooperação e a realização da atividade pública.|O incisoXIII relaciona harmonia organizacional e respeito à colaboração para a finalidade pública.
E|Se a medida é conveniente para o setor, torna-se dispensável avaliar se é honesta.|Conveniência administrativa não substitui o elemento ético; o incisoII exige examinar a honestidade.
''')
put('ETI-B01-S02','e','Anexo, XIV — deveres fundamentais','Deveres fundamentais incluem cumprir atribuições com zelo e rapidez, prestar contas, respeitar usuários, resistir a pressões indevidas e manter atualização.','Respeitar a hierarquia não significa cumprir ordem ilegal ou silenciar sobre irregularidade. Rapidez não autoriza insegurança ou desvio de finalidade.','O servidor comunica uma pressão para favorecer um interessado e mantém o atendimento impessoal.', '''
C|O dever de respeito à hierarquia convive com a possibilidade de representar contra comprometimento indevido da estrutura estatal.|O incisoXIV,h não transforma hierarquia em proibição de comunicar irregularidades.
E|Para demonstrar lealdade ao superior, o servidor deve ceder a pressão por vantagem indevida.|O incisoXIV,i impõe resistir a pressões por favores indevidos e denunciá-las.
C|Manter-se atualizado sobre normas de serviço e legislação pertinente é um dever ético.|O incisoXIV,q inclui expressamente a atualização necessária à atuação funcional.
E|Retardar prestação de contas é admissível sempre que o servidor tenha muitas tarefas comuns.|O incisoXIV,d proíbe retardar prestação de contas; ela é essencial à gestão de bens e serviços coletivos.
C|Respeitar limitações individuais do usuário é compatível com o dever de urbanidade e de atendimento sem preconceito.|O incisoXIV,g demanda atenção às capacidades e limitações e veda distinções discriminatórias.
C|Facilitar a fiscalização por quem tem competência integra os deveres do servidor.|O incisoXIV,s exige facilitar a fiscalização dos atos e serviços por quem de direito.
E|Cumprir formalidades legais permite exercer a autoridade para finalidade estranha ao interesse público.|O incisoXIV,u veda esse desvio mesmo sem violação legal expressa ou defeito formal.
E|Critério e segurança devem ser abandonados sempre que atrasarem um pouco o atendimento.|O incisoXIV,r reúne critério, segurança e rapidez; não autoriza sacrificar a correção por velocidade.
C|Buscar resolver situações de atraso e filas integra o dever de evitar dano moral ao usuário.|O incisoXIV,b inclui a solução de situações procrastinatórias como prioridade funcional.
C|Comunicar fatos contrários ao interesse público e exigir providências cabíveis é uma atuação prevista no Código.|O incisoXIV,m determina comunicação imediata aos superiores e providências pertinentes.
E|No exercício do direito de greve, a ética dispensa qualquer consideração sobre vida e segurança coletiva.|O incisoXIV,j exige zelar pelas necessidades específicas de defesa da vida e da segurança coletiva.
E|Atualizar conhecimentos e participar de estudos de melhoria do serviço são atividades estranhas aos deveres éticos.|O incisoXIV,o e q abrange melhoria funcional e atualização normativa.
''')
put('ETI-B01-S03','e','Anexo, XV — vedações','O Código veda favorecimento pelo cargo, conivência com erro, manipulação documental, desvio de pessoal e uso de informação privilegiada, entre outras condutas.','Amizade, solidariedade e alegada boa intenção não autorizam violar deveres ou atender interesses particulares com recursos públicos.','Um servidor que acessa informação interna para beneficiar parentes incorre em vedação mesmo sem usar dinheiro do órgão.', '''
E|Usar a influência do cargo para favorecer um amigo é permitido se não houver benefício para o próprio servidor.|O incisoXV,a proíbe favorecimento para si ou para outrem.
C|Ser conivente com infração ética por solidariedade ao colega é conduta vedada.|O incisoXV,c impede que solidariedade sirva de justificativa à conivência.
C|Dificultar deliberadamente o exercício regular de um direito por artifícios pode configurar violação ética.|O incisoXV,d veda procrastinação e dificuldades artificiais que causem dano ao interessado.
E|Solicitar vantagem para um familiar é ético se a vantagem não entrar no patrimônio do servidor.|O incisoXV,g também abrange familiares e outras pessoas; não se restringe a proveito pessoal direto.
C|Alterar indevidamente o teor de documento a encaminhar para providências é vedado.|O incisoXV,h proíbe deturpar ou alterar o conteúdo nessas circunstâncias.
E|Um servidor pode usar informação privilegiada do serviço em favor de terceiros desde que não receba pagamento.|O incisoXV,m veda esse uso em benefício de parentes, amigos ou terceiros, independentemente da justificativa de gratuidade.
E|É permitido retirar bem da repartição para uso particular sempre que haja intenção de devolvê-lo depois.|O incisoXV,l exige autorização legal para retirar bens; intenção de devolver não a substitui.
C|Desviar outro servidor para atender interesse particular contraria uma vedação expressa.|O incisoXV,j protege o emprego da força de trabalho para a finalidade pública.
C|Prejudicar deliberadamente a reputação de cidadão que dependa do serviço é vedado.|O incisoXV,b abrange servidores e cidadãos que deles dependam.
E|Simpatias pessoais podem definir a qualidade do atendimento porque o Código protege a liberdade afetiva do servidor.|O incisoXV,f impede interferência de simpatias, antipatias e interesses pessoais no trato funcional.
C|Recusar, sem justificativa ética, o emprego de avanços técnicos disponíveis à atividade pode contrariar o Código.|O incisoXV,e veda deixar de utilizar os avanços técnicos e científicos ao alcance ou conhecimento para o serviço.
E|Iludir o usuário sobre um procedimento é permitido quando facilita encerrar rapidamente o atendimento.|O incisoXV,i veda iludir ou tentar iludir quem necessita de serviços públicos.
''')
put('ETI-B01-S04','e','Anexo, XXIV — conceito de servidor para apuração ética','Para fins éticos, o conceito de servidor é amplo: vínculo por lei, contrato ou outro ato jurídico e serviço permanente, temporário ou excepcional, inclusive sem remuneração, ligado ao poder estatal.','O conceito do Código não se limita ao ocupante de cargo efetivo; não transforma automaticamente qualquer particular sem vínculo em agente público.','Uma pessoa presta serviço temporário e não remunerado por ato jurídico de vinculação ao órgão; a gratuidade não basta para afastar a apuração ética.', '''
C|A ausência de remuneração não exclui, por si só, a incidência do conceito de servidor utilizado pelo Código para apuração ética.|O incisoXXIV admite prestação sem retribuição financeira, desde que exista o vínculo previsto.
E|Somente o ocupante de cargo efetivo pode ter seu comprometimento ético apurado segundo o conceito do Decreto1.171.|A definição é mais ampla e alcança vínculos legais, contratuais ou decorrentes de outro ato jurídico.
C|Um vínculo contratual de prestação de serviço pode ser relevante para o conceito ético do Código.|O incisoXXIV inclui expressamente o contrato entre as fontes do vínculo.
E|O caráter temporário de uma prestação de serviço impede automaticamente a aplicação do Código.|A definição admite serviços temporários e excepcionais, além dos permanentes.
C|O vínculo indireto com entidade estatal pode estar abrangido pelo conceito previsto para fins de apuração ética.|A definição alcança ligação direta ou indireta ao poder estatal nos termos do incisoXXIV.
E|A mera condição de usuário do serviço público torna qualquer cidadão servidor para fins do Código.|É necessário o vínculo de prestação de serviços previsto; ser destinatário do atendimento não basta.
E|Toda pessoa que entra em uma autarquia assume automaticamente os deveres funcionais de servidor, sem ato jurídico ou serviço prestado.|O conceito depende das condições legais da prestação e do vínculo, não da presença física no órgão.
C|A apuração ética deve examinar as características do vínculo e do serviço, em vez de se limitar ao nome do cargo.|A definição funcional e abrangente do incisoXXIV exige análise do enquadramento concreto.
C|O conceito ético pode alcançar serviços de natureza excepcional, não apenas uma rotina permanente de trabalho.|O incisoXXIV prevê expressamente a natureza excepcional.
E|Se o prestador trabalha em entidade fundacional, sua conduta está necessariamente fora do alcance do conceito do Código.|A definição inclui entidades estatais como fundações e outras formas previstas; não há exclusão automática.
C|Um serviço não remunerado e juridicamente vinculado ao órgão não pode ser tratado como irrelevante à ética somente pela gratuidade.|A remuneração não é requisito universal do conceito ético.
E|A definição usada no Código permite concluir que todo agente abrangido possui exatamente o mesmo regime jurídico de cargos e vantagens.|Abrangência ética não unifica regimes funcionais, direitos remuneratórios ou regras de provimento.
''')
put('ETI-B01-S05','e','Anexo, I,VI e XV,n,p — vida privada e reflexos funcionais','A função pública integra a vida profissional e repercute na vida particular; condutas privadas podem afetar o conceito funcional nos termos do Código.','Isso não cria autorização irrestrita para invadir intimidade nem torna toda preferência pessoal uma infração. É preciso analisar fatos e enquadramento.','A afirmação de que tudo fora do expediente é imune à análise ética é ampla demais.', '''
E|O Código estabelece que nenhum fato da vida privada pode influenciar o conceito funcional do servidor.|O incisoVI reconhece que fatos e atos privados podem acrescer ou diminuir o bom conceito funcional.
C|A análise ética da vida privada deve identificar fatos e sua relevância, sem presumir infração apenas por discordância pessoal.|O Código deve ser aplicado a condutas enquadráveis, respeitando direitos e garantias; diferenças pessoais não bastam.
C|Os primados de dignidade e decoro não são limitados pelo Código ao horário de expediente.|O incisoI menciona comportamento no exercício da função e fora dele.
E|Fora do expediente, o servidor fica autorizado a vincular seu nome a qualquer empreendimento aético sem repercussão prevista no Código.|O incisoXV,p veda atividade profissional aética e ligação a empreendimentos de cunho duvidoso.
E|A referência à vida particular permite desconsiderar toda garantia de intimidade do investigado.|Apuração ética continua sujeita a direitos, contraditório e regras legais; não há autorização geral de devassa.
C|A vedação sobre embriaguez distingue apresentar-se embriagado no serviço de fazê-lo habitualmente fora dele.|O incisoXV,n usa critérios diferentes para o serviço e a habitualidade fora dele.
E|O Código trata apenas de uma punição criminal de comportamentos privados, sem relação com a confiança na função pública.|Seu objeto é ético-funcional; não se confunde com tipificação penal.
C|Alegar que uma atividade profissional ocorre nos fins de semana não resolve, por si, a análise de seu caráter ético.|O momento da atividade não elimina as vedações éticas aplicáveis.
''')
put('ETI-B01-S06','e','Anexo, IX,X,XIV,b,e,g,t — atendimento e bem comum','Atender com cortesia, atenção e respeito às diferenças integra a finalidade pública. Demora injustificada e maus-tratos podem causar dano moral aos usuários.','Prioridades legais não são favorecimento pessoal. Eficiência não autoriza desrespeitar o cidadão ou omitir explicação necessária.','Um usuário com dificuldade de compreensão recebe orientação clara, sem ser ridicularizado ou preterido por preconceito.', '''
C|Adaptar a comunicação às limitações de compreensão do usuário é compatível com o atendimento ético.|O incisoXIV,e e g exige cuidado, aperfeiçoamento da comunicação e respeito às limitações individuais.
E|Se o pedido do cidadão será indeferido, o servidor fica dispensado de agir com urbanidade.|O dever de respeito não depende do resultado favorável do processo.
C|Maus-tratos e descuido com o patrimônio público afetam a comunidade, e não apenas o equipamento ou o usuário imediato.|O incisoIX relaciona a conduta ao dano moral e à contribuição coletiva para o serviço.
E|Criar atraso artificial para desestimular o exercício de um direito é um método aceitável de reduzir filas.|O Código combate procrastinação e veda dificultar direitos por artifícios.
C|Exercer prerrogativas com moderação impede usá-las contra interesses legítimos dos usuários.|O incisoXIV,t determina estrita moderação das prerrogativas funcionais.
E|Tratar melhor um conhecido por simpatia pessoal é equivalente a cumprir uma prioridade prevista em lei.|Preferência pessoal é diferente de prioridade legal; o Código veda interferência de simpatias no atendimento.
C|O dever de rapidez deve ser conciliado com segurança e correção das tarefas.|O incisoXIV,r exige critério, segurança e rapidez, não apenas volume de atendimentos.
E|Filas evitáveis e demora sem justificativa são eticamente neutras desde que o servidor seja educado ao falar.|O incisoX e oXIV,b destacam o dano dos atrasos e o dever de resolver situações procrastinatórias.
''')
put('ETI-B01-S07','e','Anexo,XVI,XVIII e XXII; Decreto6.029,art12,§5º','Comissão de Ética orienta, aconselha e apura condutas. A pena prevista no Código é censura, com fundamentação e ciência do faltoso.','Censura ética não é demissão disciplinar. Encaminhar indícios ou sugerir providência a autoridade competente não equivale a aplicar diretamente outra pena.','A comissão conclui pela falta ética, fundamenta a censura e encaminha aspectos disciplinares à instância competente.', '''
C|A pena aplicável pela Comissão de Ética, segundo o incisoXXII do Código, é censura.|O parecer deve ser fundamentado, assinado pelos integrantes e levado à ciência do faltoso.
E|A Comissão de Ética aplica diretamente demissão estatutária como pena prevista no Decreto1.171.|A pena do Código é censura; sanções disciplinares seguem competência e procedimento próprios.
C|Orientar e aconselhar servidores sobre a relação com pessoas e patrimônio integra a função da comissão.|O incisoXVI atribui à comissão papel preventivo além da análise de condutas censuráveis.
E|A censura pode ser imposta sem fundamentação se todos os integrantes concordarem com a conclusão.|O incisoXXII exige fundamentação no parecer; unanimidade não elimina esse dever.
C|A comissão pode fornecer registros de conduta ética aos organismos responsáveis por procedimentos da carreira.|O incisoXVIII prevê esse fornecimento para instruir procedimentos, inclusive promoções, nos termos do Código.
E|Encaminhar indícios para exame disciplinar significa que a comissão já aplicou a pena disciplinar definitiva.|Encaminhamento e julgamento disciplinar são atos diferentes, com autoridades e garantias próprias.
C|A comunicação de uma censura ao interessado é exigência distinta da assinatura do parecer pelos membros.|O incisoXXII contempla tanto assinatura quanto ciência do faltoso.
E|Se houver componente penal na conduta, toda análise ética se torna automaticamente impossível.|Instâncias podem ter objetos distintos; o simples componente penal não elimina a competência ética e os encaminhamentos adequados.
''')
put('ETI-B02-S01','et','Artigos1,2,5,7,8 e9 — Sistema e Rede de Ética','O Sistema de Gestão da Ética integra a CEP, as comissões do Decreto1.171 e outras comissões equivalentes do Executivo Federal. Integração e cooperação não eliminam competências próprias.','CEP e comissão local têm composição e papel diferentes. A Rede promove cooperação técnica e avaliação, não substitui todas as comissões.','Uma comissão local representa seu órgão na Rede de Ética e realiza orientação dentro de sua competência.', '''
C|O Sistema de Gestão da Ética inclui a CEP e comissões de órgãos e entidades, não se restringindo à comissão central.|O artigo2 enumera a CEP, as comissões do Decreto1.171 e outras comissões equivalentes.
E|A criação do Sistema extinguiu todas as comissões de ética locais e concentrou qualquer atuação na CEP.|O artigo2 preserva a pluralidade de instâncias que integram o Sistema.
C|O Sistema busca integrar órgãos, programas e ações relacionadas à ética pública.|Essa finalidade consta do artigo1 e pressupõe articulação, não isolamento das instâncias.
E|As comissões locais são compostas pelos mesmos sete membros que integram a CEP.|O artigo5 estabelece três titulares e três suplentes nas comissões locais; a CEP tem composição própria.
C|A comissão local atua como instância consultiva de dirigentes e servidores de seu órgão ou entidade.|Essa competência é estabelecida pelo artigo7,I.
C|A Rede de Ética é integrada por representantes das comissões e busca cooperação técnica e avaliação da gestão ética.|O artigo9 define sua composição e finalidade.
E|A Rede de Ética deve reunir-se somente quando ocorrer infração grave, sem periodicidade mínima.|O artigo9,parágrafo único, prevê reunião pelo menos anual em fórum específico.
E|Promover transparência e acesso à informação é incompatível com os objetivos do Sistema de Gestão da Ética.|O artigo1,II, trata esses instrumentos como fundamentais para a gestão ética.
C|Cabe às instâncias superiores constituir comissão e garantir recursos para seu funcionamento.|O artigo8 inclui essas obrigações para a administração direta e indireta.
C|As comissões locais podem recomendar ações de disseminação e treinamento sobre normas éticas.|O artigo7,II,d, lhes atribui recomendar, acompanhar e avaliar essas ações.
E|A participação em um sistema integrado dispensa cada órgão de observar e fazer observar as normas de ética.|O artigo8,I, mantém esse dever nas instâncias superiores dos órgãos e entidades.
E|A comissão local deixa de ter função preventiva porque sua única atribuição é punir condutas já consumadas.|O artigo7 também prevê consulta, orientação, capacitação e disseminação de normas.
''')
put('ETI-B02-S02','et','Artigos3 e4 — composição, mandato e deliberação da CEP','A CEP possui sete brasileiros com idoneidade moral, reputação ilibada e experiência em administração pública, designados pelo Presidente da República. Mandatos são de três anos, não coincidentes, com uma recondução.','Não confundir os sete membros da CEP com os três titulares e três suplentes das comissões locais. Atuação da CEP não gera remuneração aos membros.','Quando há empate em deliberação, a regra do voto de qualidade do presidente precisa ser considerada.', '''
C|A CEP é integrada por sete brasileiros que devem preencher os requisitos previstos no Decreto.|O artigo3 exige idoneidade moral,reputação ilibada e notória experiência em administração pública.
E|Os membros da CEP são eleitos pelos servidores de cada órgão para mandatos anuais.|A designação cabe ao Presidente da República e o mandato ordinário é de três anos.
C|Os mandatos da CEP são não coincidentes, evitando renovação obrigatoriamente simultânea de todos os membros.|O artigo3 prevê expressamente a não coincidência.
E|O Decreto permite reconduções sucessivas ilimitadas dos membros da CEP.|O artigo3 admite uma única recondução.
C|A atuação de membro da CEP não enseja remuneração e é considerada serviço público relevante.|Essa regra consta do artigo3,§1º.
E|O presidente da CEP não participa de deliberações porque exerce somente função representativa externa.|O artigo3,§2º, atribui ao presidente voto de qualidade nas deliberações.
C|A CEP tem competência para escolher seu presidente.|O artigo4,VI, estabelece essa competência do colegiado.
E|É suficiente ser brasileiro para compor a CEP, sem qualquer requisito de experiência ou reputação.|O artigo3 acumula nacionalidade com requisitos de idoneidade,reputação e experiência.
C|A regra inicial de mandatos de um,dois e três anos serve à composição inicial e não muda a duração ordinária prevista.|O artigo3,§3º, trata dos primeiros membros; o caput fixa três anos como mandato ordinário.
E|As comissões locais possuem necessariamente sete titulares e nenhum suplente, seguindo a composição da CEP.|O artigo5 fixa três titulares e três suplentes para as comissões locais.
C|Aprovar o próprio regimento interno é atribuição da CEP.|Essa competência consta do artigo4,V.
E|A nomeação de um membro da CEP torna lícita uma remuneração adicional automática por cada reunião com base no Decreto6.029.|O artigo3,§1º, afasta remuneração pela atuação na CEP.
''')
put('ETI-B02-S03','et','Artigos4,7,11 e12 — competências, legitimados e garantias','A CEP coordena, avalia e supervisiona o Sistema, enquanto comissões locais atuam em seus âmbitos. Cidadãos,agentes,pessoas jurídicas,associações e entidades de classe podem provocar apuração.','Provocar atuação não equivale a condenar o agente; a apuração observa competência e garantias. Atuação de ofício também é possível.','Uma associação apresenta notícia fundamentada de infração ética; não é necessário que seja servidora pública para provocar a comissão.', '''
C|Uma pessoa jurídica de direito privado pode provocar a atuação da CEP ou de comissão de ética nos termos do artigo11.|O dispositivo inclui esse legitimado, além de cidadãos,agentes públicos,associações e entidades de classe.
E|Somente o chefe imediato do agente investigado pode comunicar infração ética à comissão.|O artigo11 estabelece legitimidade ampla, não limitada à chefia.
C|A CEP pode atuar como instância consultiva do Presidente da República e dos Ministros de Estado em matéria ética.|Essa competência consta do artigo4,I.
E|Uma comissão fica impedida de apurar de ofício porque qualquer investigação depende de denúncia do ofendido.|Os artigos4,7 e12 admitem atuação de ofício, conforme a competência.
C|Dirimir dúvidas de interpretação do Código de Ética integra atribuições previstas para a CEP.|O artigo4,III, prevê esse papel em relação ao Decreto1.171.
E|Ao supervisionar o Sistema,a CEP passa a substituir os juízes em todo processo penal de agente público.|Coordenação ética não atribui jurisdição penal; instâncias e competências são distintas.
C|A comissão local pode comunicar à CEP situação que configure possível descumprimento do Código de Conduta da Alta Administração.|O artigo7,IV, prevê supervisão e comunicação dessa natureza.
E|A apresentação de denúncia por um cidadão prova a infração e dispensa a produção de elementos e a defesa.|Provocação inicia análise; não afasta instrução,competência,contraditório e ampla defesa.
''')
put('ETI-B02-S04','et','Artigos10,12,13,14 e16 — apuração e garantias','Apuração ética exige celeridade,imparcialidade,proteção à honra e contraditório. Notificação escrita para manifestação tem prazo de dez dias, também previsto diante de novos elementos após a manifestação inicial.','Reserva do procedimento não elimina vista e conhecimento da imputação pelo investigado. Sigilo legal de documento tem regime próprio.','Se surgem novas provas depois da primeira defesa,o investigado é novamente notificado para se manifestar.', '''
C|O investigado deve ser notificado para manifestação escrita no prazo de dez dias previsto pelo artigo12.|O prazo do caput integra o contraditório no processo de apuração ética.
E|A juntada de novos elementos após a primeira manifestação dispensa ouvir novamente o investigado.|O artigo12,§3º,prevê nova notificação para manifestação em dez dias.
C|A decisão conclusiva deve ser fundamentada após a instrução.|O artigo12,§4º,exige conclusão fundamentada,não simples afirmação de culpa.
E|O caráter reservado do procedimento impede o investigado de saber a acusação até sua conclusão.|O artigo14 assegura conhecer a imputação e ter vista,inclusive antes de notificação formal da investigação.
C|A comissão pode promover diligências e solicitar parecer de especialista para instrução.|O artigo12,§2º,permite essas medidas e a requisição de documentos necessários.
E|Concluído o procedimento,todo documento protegido por sigilo legal se torna irrestritamente público.|O artigo13 preserva o regime de documentos legalmente sigilosos mesmo após o fim da reserva do procedimento.
C|A proteção à identidade do denunciante,sob reserva quando ele assim desejar,é princípio previsto para os trabalhos.|O artigo10,II,contempla essa proteção sem afastar as garantias da pessoa investigada.
E|A comissão pode recusar decisão de sua competência apenas porque o Código não detalhou expressamente o caso.|O artigo16 impede essa escusa e prevê suprir omissões por analogia e princípios,observadas as normas.
''')
put('ETI-B02-S05','et','Artigos6,8,10,12,13,17,18 e20 — apoio, imparcialidade e prestação de informações','Dirigentes devem assegurar condições e recursos às comissões. Órgãos e entidades devem atender prioritariamente suas solicitações e não podem invocar sigilo para recusar documentos necessários à investigação,observadas as regras de proteção.','Transmitir informação à comissão não é autorizá-la a divulgar todo dado sigiloso. Falta de colaboração pode gerar responsabilização.','Um setor entrega documentos necessários à comissão por meio protegido; a reserva acompanha os dados legalmente sigilosos.', '''
C|O titular de órgão ou entidade deve assegurar condições de trabalho para a comissão cumprir suas funções.|O artigo6,I,prevê esse dever,inclusive proteção para que as atribuições dos membros não gerem prejuízo ou dano.
E|A direção pode negar todos os recursos à comissão porque a atuação ética não integra as responsabilidades institucionais.|O artigo8 exige recursos humanos,materiais e financeiros para cumprimento das atribuições.
C|Solicitações da CEP devem receber prioridade das instâncias superiores,nos termos do Decreto.|O artigo8,IV,prevê atendimento prioritário.
E|Invocar genericamente o sigilo permite a qualquer órgão recusar à comissão os documentos necessários à investigação.|O artigo20,§2º,impede a negativa por alegação de sigilo;isso não afasta a proteção legal que a comissão deve preservar.
C|A autoridade competente não pode simplesmente deixar de atender uma solicitação de documento necessário sem observar os deveres de colaboração.|O artigo20 impõe colaboração e prevê consequência para o descumprimento da obrigação de prestar informações.
E|Receber documento sigiloso autoriza a comissão a publicá-lo integralmente para demonstrar transparência.|O artigo13 protege documentos acobertados por sigilo legal;transparência não revoga essa proteção.
C|As decisões éticas devem ser articuladas com as providências institucionais cabíveis,sem impedir exame disciplinar pela instância competente.|O artigo12,§5º,prevê encaminhamentos quando pertinentes;cooperação não transfere toda competência à comissão.
E|Proteger os membros de danos decorrentes de suas atribuições significa conferir imunidade para agir sem imparcialidade.|A proteção funcional convive com a independência e imparcialidade exigidas no artigo10.
''')

# Os enunciados acima são todos redigidos individualmente. Apenas o empacotamento é automático.
def clean(text):
    text=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)', ' ', text)
    text=re.sub(r'(?<=\d)(?=[A-Za-zÀ-ÿ])', ' ', text)
    text=re.sub(r'\b(inciso|artigo)(?=[IVXLC\d])', r'\1 ', text)
    text=re.sub(r'\bdo(?=[IVXLC])', 'do ', text)
    text=re.sub(r',(?=[A-Za-zÀ-ÿ])', ', ', text)
    return text

lessons=[]
scopes={r['id_planejamento']:r for r in PLAN['assuntos'] if r['disciplina'] in ['Informática','Ética']}
assert set(D)==set(scopes),(set(D)^set(scopes))
for pid,row in scopes.items():
    source,loc,core,contrast,example,items=D[pid]
    loc,core,contrast,example=map(clean,(loc,core,contrast,example))
    items=[(a,clean(t),clean(e)) for a,t,e in items]
    assert len(items)==row['meta_questoes_autorais'],(pid,len(items),row['meta_questoes_autorais'])
    lid='v17-'+pid.lower()
    src={**S[source],'locator':loc,'verifiedAt':'2026-10-27'}
    facts=list(dict.fromkeys(e for a,t,e in items))
    # Ensina de forma afirmativa as regras utilizadas na avaliação; não revela sequência de gabaritos.
    rule=core+' '+ ' '.join(facts)
    questions=[]
    # Ordem dos modos não determina gabarito; a interface deverá embaralhar itens e ocultar a fonte até corrigir.
    for i,(answer,text,explanation) in enumerate(items,1):
        qsrc=src
        if pid=='INFO-B02-S04' and i in [1,5]: qsrc={**S['countif'],'verifiedAt':'2026-10-27'}
        if pid=='INFO-B02-S04' and i==6: qsrc={**S['sumifs'],'verifiedAt':'2026-10-27'}
        if pid=='ETI-B01-S05' and i==5: qsrc={**S['et'],'locator':'Artigos10,12 e14 — proteção à honra, contraditório e acesso à imputação','verifiedAt':'2026-10-27'}
        if pid=='ETI-B01-S07' and i in [6,8]: qsrc={**S['et'],'locator':'Artigos12,§5º, e17 — encaminhamento e preservação das competências próprias','verifiedAt':'2026-10-27'}
        if pid=='ETI-B02-S03' and i==8: qsrc={**src,'locator':'Artigo12,caput e§§1º a4º — instrução, contraditório e ampla defesa'}
        if pid=='ETI-B02-S05':
            qloc={1:'Artigo6,I — condições de trabalho e proteção dos integrantes',2:'Artigo8,III — recursos humanos, materiais e financeiros',3:'Artigo8,IV — prioridade às solicitações da CEP',4:'Artigo20,§2º — dever de prestar informação e alegação de sigilo',5:'Artigo20,caput e§1º — colaboração documental e providência por descumprimento',6:'Artigo13,§§2º e3º — preservação do sigilo legal de documentos',7:'Artigos12,§5º, e17 — encaminhamentos às instâncias competentes',8:'Artigos6,I, e10,III — proteção funcional, independência e imparcialidade'}
            qsrc={**src,'locator':clean(qloc[i])}
        questions.append({'id':f'{lid}-q{i:03d}','text':text,'answer':answer,'explanation':explanation,'kind':'autoral','version':1,'difficulty':('basico' if i<=len(items)*.35 else 'intermediario' if i<=len(items)*.8 else 'avancado'),'family':f'{pid}-aspecto-{i:02d}','microtopic':pid,'sourceRef':qsrc,'mode':('reserva' if i%4==0 else 'fixacao' if i%4==1 else 'treino'),'editorialStatus':'conferido-na-elaboracao','reviewedAt':'2026-10-27'})
    lesson_sources=([src,S['countif'],S['sumifs']] if pid=='INFO-B02-S04' else [src])
    for q in questions:
        if q['sourceRef'] not in lesson_sources: lesson_sources.append(q['sourceRef'])
    lessons.append({'id':lid,'d':'info' if pid.startswith('INFO') else 'etica','title':row['assunto'],'core':core,'rule':rule,'example':example,'contrast':contrast,'limit':'A referência curricular é o edital histórico de 2022 retificado. Questões autorais não são itens oficiais. Considere a versão do software ou o dispositivo normativo indicado; não generalize uma regra para contexto diferente.','source':source if source in ['e','et'] else 'info','sources':lesson_sources,'minutes':40,'block':row['bloco'],'planId':pid,'subtopics':facts,'version':1,'questions':questions})
allq=[q for l in lessons for q in l['questions']]
assert len(allq)==280
assert len({q['id'] for q in allq})==280
assert len({q['text'].strip().casefold() for q in allq})==280
assert all(type(q['answer']) is bool for q in allq)
assert sum(len(l['questions']) for l in lessons if l['d']=='info')==160
assert sum(len(l['questions']) for l in lessons if l['d']=='etica')==120
# Verificação aritmética independente dos exemplos de planilha autorais.
assert 3+4*2==11 and (3+4)*2==14 and 10/2*3==15
assert sum(v>4 for v in [2,5,8])==2 and sum(v for v in [2,5,8] if v>4)==13
assert sum(v for v in [10,20,30] if v>=20)==50
result={'lessons':lessons,'sources':list(S.values()),'editorial':{'date':'2026-10-27','author':'JARVIS — elaboração própria','questionCount':280,'lessonCount':35,'status':'conferência de elaboração e validação estrutural; sem revisão independente','method':'280 enunciados e explicações escritos individualmente; Python apenas empacota e valida quotas/IDs/tipos/cálculos','limitations':['Fontes jurídicas Planalto bloquearam consulta; utilizados textos oficiais da Câmara.','Artigos6.029 conferidos no texto disponibilizado pela Câmara; não há declaração de certificação jurídica independente.','Páginas gerais de suporte são referências de navegação; conferir a versão específica para qualquer comando não abrangido nos conceitos do item.','Não contém questões reais nem cópia de banco de terceiros.','Dificuldade é editorial provisória, não calibração psicométrica.']}}
path=ROOT/'data/info-etica.json'
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'file':str(path),'lessons':len(lessons),'questions':len(allq),'C':sum(q['answer'] for q in allq),'E':sum(not q['answer'] for q in allq)},ensure_ascii=False))
