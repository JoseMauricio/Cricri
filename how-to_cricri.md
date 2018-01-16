### Cricri - how-to

#### cri-gpg.py

1 - No terminal Linux, digite "python3 cri-gpg.py" sem as aspas (em pacotes como o Anaconda, em que o Python 3.6 passa a ser o padrão para o sistema operacional, digite "python cri-gpg.py").

2 - No primeiro campo que surge na tela...

      "Arquivo:  "

... digite o nome do arquivo que contém a planilha, com a respectiva extensão (.csv ou .xlsx);

3 - No campo seguinte...

      "Arquivo .cri:   "

... digite o nome que você deseja dar ao arquivo criptografado. A extensão pode ser qualquer uma, não necessariamente ".cri" como indicado. É recomendável que o nome tenha relação com o arquivo original - "telefones.xlsx.cri", por exemplo, se a planilha a ser criptografa for "telefones.xlsx". Isso facilita a identificação posterior, principalmente se houver mais de um arquivo criptografado na pasta.

4 - No último campo...

      "Chave pública:   "

... digite a informação pedida. Lembre-se que o arquivo com a chave pública (com as extensões .asc ou .gpg) tem de estar na mesma pasta que os scripts e as planilhas. O pacote Cricri foi testado com pares de chaves RSA geradas pelos softwares GnuPG (Kleopatra ou gpg), PGP (Symantec) e OpenSSL.

5 - O script passa então a criptografar a planilha em segundo plano. No final, ele imprime na tela "Ok: True" e "status: encryption ok" para indicar que a operação foi bem-sucedida.

6 - Para a digitação do nome do arquivo a ser criptografado e da chave pública a ser utilizada, o script oferece três tentativas. Se em todas elas o nome estiver errado ou os arquivos não estiverem no local adequado, ele se encerrará.

#### cricri-gpg.py

1 - No terminal Linux, digite "python3 cricri-gpg.py" (ou "python cricri-gpg.py" como descrito acima).

2 - Digite a informação pedida no primeiro campo:

      "Nome do arquivo criptografado:   "

3 - Os campos seguintes...

      "Nome da chave privada:   "

      "Senha:   "

... bem como o anterior, também oferecem três tentativas de digitação. A confirmação de que a primeira etapa foi realizada corretamente e a planilha está pronta no dataframe vem com as informações "Ok: True" e "status: decryption ok" impressas na tela.

4 - Abre-se então o primeiro campo para a consulta:

      "Quer ver os cabeçalhos das colunas? S para sim e N para continuar:    ".

Digite S se precisar saber que tipo de informação está disponível em cada coluna. O resultado será estampado na tela, ordenadamente: "nome da coluna 1", "nome da coluna 2", "nome da coluna 3" e assim por diante. Acima dos respectivos cabeçalhos, as colunas também serão identificadas por números ("0", "1", "2" etc).

5 - O campo seguinte começa com uma dica:

      "O índice para a consulta é a coluna 0, onde estão armazenados os nomes para a pesquisa".

Se a planilha original tiver sido formatada corretamente, a primeira coluna armazenará a informação principal a que todas as outras estarão referenciadas - se for uma agenda, por exemplo, a primeira coluna terá os nomes das pessoas a que estarão associados os respectivos números de telefone e endereços de e-mail nas colunas seguintes.

6 - O script pede então que você digite o nome que quer consultar:

      "Digite o nome:   "

Tem que ser exatamente como está na planilha, caso contrário a resposta será:

      "Não encontrado. Digite S para nova consulta, N para sair:   "

7 - Identificado o nome pelo script, uma nova dica aparece na tela:

      "As informações associadas ao nome estão nas colunas seguintes (1, 2, 3 etc)."

Lembre-se que o dataframe tomou a primeira coluna como índice para consulta, numerando-a como "0". No exemplo da agenda, é a que armazena os nomes. Por extensão, a coluna em que estão os números de telefone passou a ser identificada com o número 1 e a que contém os endereços de e-mail, com o número 2.

8 - Novo campo na tela:

      "Digite o número da coluna:   "

Seguindo o exemplo, digite 1 para obter o número de telefone, 2 para o endereço de e-mail.

9 - Uma nova informação é estampada, então:

      "O resultado está no clipboard. Quer ver aqui na tela? S para sim, N para continuar."

Esse é um dos diferenciais do Cricri. Se você estiver redigindo um e-mail e pesquisou pelo endereço, basta um simples ctrl-v para colá-lo no campo "Destinatário", sem a necessidade de exibir o resultado na tela. O mesmo vale para nomes de usuário e senhas em formulários de login.

No exemplo da agenda, se você pediu para o script localizar o número do telefone da pessoa para quem quer ligar, tecle S para vê-lo na tela.

10 - Campo seguinte:

      "Digite S para nova consulta, N para sair:   "

Se digitar S, o processo inicia-se outra vez, a partir do ítem 5. Lembre-se de que cada nova informação obtida sobrescreve a anterior no clipboard. É o que acontece também quando você opta por sair e encerrar o script.


#### cricri-csv-gpg

1 - No terminal Linux, digite "python 3 cricri-csv-gpg.py" (ou "python cricri-csv-gpg.py").

2 - O fluxo do programa é idêntico ao do cricri-gpg até o ítem 3. O script pede então uma informação adicional:

      "Nome do arquivo descriptografado (com a extensão .csv):   "

3 - A confirmação de que a planilha foi descriptografada no novo arquivo é estampada na tela com as informações "Ok: True" e a identificação do caminho até a pasta em que foi armazenada.
