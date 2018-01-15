Cricri é um conjunto de scripts em Python concebido para minimizar os riscos de acesso a informações sensíveis (logins, senhas, números de telefone, por exemplo), principalmente em situações críticas para jornalistas no trabalho de campo.

A ideia é fornecer um dataframe seguro para consultas a informações armazenadas em planilhas criptografadas, sem que haja necessidade de exportá-las para um arquivo aberto ou mesmo expô-las na tela do computador – senhas, por exemplo, são enviadas direto para o clipboard para serem coladas em formulários de login, sendo imediatamente sobrescritas após a operação.

#### SCRIPTS
O conjunto é formado por duas peças principais (cri-gpg.py , cricri-gpg.py) e dois utilitários (cha-gpg.py, cricri-csv-gpg.py).

CRI-GPG - O script cri-gpg.py utiliza a chave pública RSA do usuário para criptografar planilhas geradas em formato-texto ( .csv) ou Excel (.xlsx). A operação deve ser feita num computador seguro, no local de trabalho ou na casa do usuário.

CRICRI-GPG - Em campo, a consulta é feita com o uso da chave privada e a respectiva senha pelo script cricri-gpg.py, que reconstrói a planilha em segundo plano, cria o dataframe e a interface de texto para o usuário num terminal Linux.

Boas práticas de segurança recomendam o armazenamento dos arquivos criptografados, a chave privada e o script numa mesma pasta protegida, de preferência num pendrive inicializável com uma distribuição Linux, Python 3.6+ e os módulos gnupg, pandas, getpass e pyperclip instalados (veja em "requirements.txt"), além de aplicativos essenciais como Tor, e-mail criptografado e chat seguro.

Essa configuração permite ao usuário utilizar o script em qualquer computador, mesmo em locais públicos numa situação de emergência. Para isso, deve dar o boot pelo pendrive, fazer a consulta, encerrar o sistema e desligar a máquina, apagando assim praticamente todos os rastros da operação.

#### UTILITÁRIOS
CHA-GPG - O script cha-gpg.py cria um par de chaves RSA, caso o usuário necessite. Deve ser usado apenas em situações extremas, por conta de fragilidades conhecidas nas chaves RSA geradas em ambiente Python. Se for o caso, recomenda-se que as elas tenham prazo curto de validade e sejam descartadas assim que cumprirem a função a que se destinam.

CRICRI-CSV-GPG - O script cricri-csv-gpg.py completa o kit de campo. Ao invés de gerar um dataframe para consultas, ele limita-se a utilizar a chave privada e a respectiva senha para criar um novo arquivo aberto, em formato csv. Deve ser utilizado apenas nas situações em que o usuário tenha certeza de que o risco de acesso indesejável é praticamente inexistente.


#### SISTEMAS OPERACIONAIS
Na versão atual, ainda em desenvolvimento, Cricri roda em ambiente Linux. Não foi testado em computadores com OSx, mas em tese não há nada que impeça sua utilização.

Ainda não funciona com Windows, por problemas de compatibilidade entre o módulo gnupg e as versões mais recentes do software GnuPG (gpg2), que fornece a infraestrutura para as tarefas de criptografia.

Há outros dois módulos com potencial de uso: pycryptodome e python-gnupg. Ambos rodam nos três sistemas operacionais, mas os testes realizados até aqui não foram satisfatórios, principalmente por problemas na importação de chaves pré-existentes.

#### TODO
- Testes sobre a qualidade da criptografia utilizada são extremamente bem-vindos.

- Testes em ambiente OSx

- Pesquisar soluções para o uso do módulo gnupg em ambiente Windows.

- Desenvolver versões estáveis dos scripts com outros módulos de criptografia, que rodem nos três sistemas operacionais mais usados (em testes: pycryptodome e python-gnupg)

- Pesquisar soluções possíveis para o uso em sistemas Android e iOS
