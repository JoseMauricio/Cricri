#! python3

import gnupg
import shutil
import os
import getpass
import pandas as pd
import pyperclip
import sys

def main():
    arquivo_cri = input('Nome do arquivo criptografado: ')
    x = 1
    while os.path.exists(arquivo_cri) == False:
        arquivo_cri = input(f'Arquivo não-encontrado.\nTente de novo ({x+1}/3):\nNome do arquivo para criptografar: ')
        x += 1
        if x == 3:
            print('Arquivo não encontrado.')
            sys.exit()

    # recria a pasta de trabalho do gpg
    if os.path.exists('doctemp'):
        shutil.rmtree('doctemp')
    gpg = gnupg.GPG(homedir='doctemp')

    key = getpass.getpass('Chave privada: ')
    x = 1
    while os.path.exists(key) == False:
        key = getpass.getpass(f'Chave não encontrada.\nTente de novo ({x+1}/3):\nNome da chave privada: ')
        x += 1
        if x == 3:
            print('Chave não encontrada')
            sys.exit()

    key_data = open(key).read()
    import_result = gpg.import_keys(key_data)

    # descriptografa o arquivo
    senha = getpass.getpass('Senha: ')

    with open(arquivo_cri, 'r') as f:
        descri = gpg.decrypt_file(f, passphrase=senha)

    print('ok: ', descri.ok)
    print('status: ', descri.status)

    x = 1
    while descri.ok == False:
        senha = getpass.getpass(f'Senha errada.\nTente de novo ({x+1}/3) Senha: ')

        with open(arquivo_cri, 'r') as f:
            descri = gpg.decrypt_file(f, passphrase=senha)
            print('ok: ', descri.ok)
            print('status: ', descri.status)

        x += 1

        if x == 3:
            print('Problema com a senha.')
            sys.exit()

    # prepara a planilha e cria um dataframe para a consulta
    descri = descri.data.decode('utf8')
    descri = str(descri)
    descri = descri.strip("'").split('\n')

    planilha = []
    for linha in descri:
        linha = linha.split(",")
        planilha.append(linha)

    df = pd.DataFrame(planilha)
    #df.set_index(0, inplace=True)
    header = (input('\nQuer ver os cabeçalhos das colunas? S para sim, N para continuar: ')).upper()
    if header == 'S':
        print()
        print(df.head(1))

    df.set_index(0, inplace=True)

    def consulta():
        print('\nO índice para a consulta é a coluna 0, em que estão os nomes para a pesquisa.')
        nome = input('\nNome: ')
        if nome not in df.index:
            print('Não encontrado')

        else:
            print('\nAs informações associadas ao nome estão nas colunas seguintes (1, 2, 3 etc).')
            campo = input('\nNúmero da coluna: ')
            result = df.loc[nome,[int(campo)]]
            result = str(result)
            result = result.split()
            pyperclip.copy(result[1])

            mostra_resultado = (input('''\nO resultado está no clipboard.
            \nQuer ver aqui na tela? S para sim, N para continuar: ''')).upper()

            if mostra_resultado == 'S':
                print(result[1])

    consulta()

    def nova_consulta():
        nova_consulta = (input('\nS para nova consulta, N para sair: ')).upper()

        while nova_consulta == 'S':
            consulta()
            nova_consulta = (input('\nS para nova consulta, N para sair: ')).upper()

    nova_consulta()

    input('\nTecle <enter> para terminar...')
    pyperclip.copy('Xô Urubu!')
    shutil.rmtree('doctemp')


if __name__ == '__main__':
    main()
