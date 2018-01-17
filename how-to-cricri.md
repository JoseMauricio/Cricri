### Cricri - how-to

#### cri-gpg.py

1 - No terminal Linux, digite:

      python3 cri-gpg.py

 Em pacotes como o Anaconda, em que o Python 3.6 torna-se o padrão para o sistema operacional, digite:
      
      python cri-gpg.py

2 - O primeiro campo que aparece na tela é:

      Arquivo:  

Digite o nome do arquivo que contém a planilha, com a respectiva extensão (.csv ou .xlsx);

3 - O campo seguinte é:

      Arquivo .cri:   

Digite o nome que você deseja dar ao arquivo criptografado. A extensão pode ser qualquer uma, não necessariamente ".cri" como indicado. É recomendável que o nome tenha relação com o arquivo original - "telefones.xlsx.cri", por exemplo, se a planilha a ser criptografada for "telefones.xlsx". Isso facilita a identificação posterior, principalmente se houver mais de um arquivo criptografado na pasta.

4 - O último campo é:

      Chave pública:   

Digite a informação pedida. Lembre-se que o arquivo com a chave pública (com as extensões .asc ou .gpg) tem que estar na mesma pasta que os scripts e as planilhas. O pacote Cricri foi testado com pares de chaves RSA de 2048, 3072 e 4096 bits, geradas pelos softwares do pacote GnuPG (Kleopatra, gpg4Win e gpg2) e OpenSSL. Deve aceitar também chaves do mesmo tipo geradas por outros aplicativos, como o PGP (Symantec), mas convém testar.

5 - O script passa então a criptografar a planilha em segundo plano. No final, imprime na tela "Ok: True" e "status: encryption ok" para indicar que a operação foi bem-sucedida.

6 - Para a digitação do nome do arquivo a ser criptografado e da chave pública, o script oferece três tentativas. Se em todas elas o nome estiver errado ou os arquivos não estiverem disponíveis na mesma pasta em que está o script, ele retornará uma mensagem de erro e se encerrará.

#### cricri-gpg.py

1 - No terminal Linux, digite:

      python3 cricri-gpg.py

Se o Python 3.6 é o padrão, digite:

      python cricri-gpg.py

2 - Digite a informação pedida no primeiro campo:

      Nome do arquivo criptografado:   

3 - O campo seguintes é:

      Chave privada:   

Digite o nome do arquivo, com a extensão (.asc ou .gpg)

4 - Em seguida:

      Senha:   

A senha não aparecerá na tela enquanto você digita. Preste atenção para fazê-lo corretamente.

Os campos para o arquivo criptografado, chave e senha oferecem três tentativas de digitação. A confirmação de que a primeira etapa foi realizada corretamente e a planilha está pronta no dataframe vem com as informações "Ok: True" e "status: decryption ok" impressas na tela.

4 - Abre-se então o primeiro campo para a consulta:

      Quer ver os cabeçalhos das colunas? S para sim e N para continuar:

Digite S se precisar saber que tipo de informação está disponível em cada coluna. O resultado será estampado na tela, ordenadamente: "nome da coluna 1", "nome da coluna 2", "nome da coluna 3" e assim por diante. Acima dos respectivos cabeçalhos, as colunas também serão identificadas por números ("0", "1", "2" etc).

5 - O campo seguinte fornece uma dica:

      O índice para a consulta é a coluna 0, onde estão armazenados os nomes para a pesquisa.

Se a planilha original tiver sido formatada corretamente, a primeira coluna armazenará as informações principais a que todas as outras estarão referenciadas - se for uma agenda, por exemplo, a primeira coluna terá os nomes das pessoas, a que estarão associados os respectivos números de telefone e endereços de e-mail nas colunas seguintes.

6 - O script pede então que você digite o nome que quer consultar:

      Nome:   

Tem que ser exatamente como está na planilha, caso contrário a resposta será:

      Não encontrado. Digite S para nova consulta, N para sair:   

7 - Localizado o nome pelo script, uma nova dica aparece na tela:

      As informações associadas ao nome estão nas colunas seguintes (1, 2, 3 etc).

Lembre-se que o dataframe tomou a primeira coluna como índice para consulta, numerando-a como 0. No exemplo da agenda, é a coluna que armazena os nomes. Em consequência, a coluna em que estão os telefones passou a ser identificada com o número 1 e a que contém os endereços de e-mail, com o número 2.

8 - Novo campo na tela:

      Número da coluna:   

Seguindo o exemplo da agenda, digite 1 para obter o número de telefone, 2 para o endereço de e-mail.

9 - Uma nova informação é estampada, então:

      O resultado está no clipboard. Quer ver aqui na tela? S para sim, N para continuar.

Esse é um dos diferenciais do Cricri. Se você estiver redigindo um e-mail e fez a consulta para obter o endereço, basta um simples ctrl-v para colá-lo no campo "Destinatário", sem a necessidade de exibir o resultado na tela. O mesmo vale para nomes de usuário e senhas em formulários de login.

No exemplo da agenda, se você pediu para o script localizar o número do telefone da pessoa para quem quer ligar, tecle S para vê-lo na tela.

10 - Campo seguinte:

      Digite S para nova consulta, N para sair:   

Se digitar S, o processo inicia-se outra vez, a partir do ítem 5. Lembre-se de que cada nova informação obtida sobrescreve a anterior no clipboard. É o que acontece também quando você opta por sair e encerrar a execução do script.


#### cricri-csv-gpg

1 - No terminal Linux, digite:
      python3 cricri-csv-gpg.py

      (ou "python cricri-csv-gpg.py", sem as aspas).

2 - O fluxo do programa é idêntico ao do cricri-gpg até o ítem 3. O script pede então uma informação adicional:

      Nome do arquivo descriptografado (com a extensão .csv):   

3 - A confirmação de que a planilha foi descriptografada e armazenada novo arquivo aberto é estampada na tela com as informações "Ok: True" e a identificação do caminho até a pasta em que foi armazenada.
