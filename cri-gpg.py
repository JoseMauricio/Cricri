#! python3

import gnupg
import shutil
import os
import pandas as pd
import getpass
import sys

def main():
    # cria o diretório de trabalho do gpg e importa a chave pública
    if os.path.isdir('doctemp'):
        shutil.rmtree('doctemp')
    gpg = gnupg.GPG(homedir='doctemp')

    arquivo_in = input('Arquivo: ')
    x = 1
    while os.path.exists(arquivo_in) == False:
        arquivo_cri = input(f'Arquivo não-encontrado.\nTente de novo ({x+1}/3):\nNome do arquivo para criptografar: ')
        x += 1
        if x == 3:
            print('Arquivo não encontrado.')
            sys.exit()

    arquivo_cri = input('Arquivo .cri: ')

    chave_publica = getpass.getpass('Chave pública: ')
    x = 1
    while os.path.exists(chave_publica) == False:
        chave_publica = getpass.getpass(f'Chave não encontrada.\nTente de novo ({x+1}/3):\nNome da chave: ')
        if x == 3:
            print('Chave não encontrada')
            sys.exit()

    key_data = open(chave_publica).read()
    key = gpg.import_keys(key_data)

    def cri():
        # prepara a planilha para a criptografia
        if arquivo_in.split('.')[1] == 'xlsx':
            temp = pd.ExcelFile(arquivo_in)
            planilha = temp.sheet_names[0]
            df = temp.parse(planilha)
        else:
            planilha = arquivo_in
            df = pd.read_csv(planilha)

        #df.rename(columns={(df.columns[0]):0}, inplace=True)
        df.set_index(df.columns[0], inplace=True)
        df.to_csv('temp.csv', sep=',', encoding='utf-8')
        arquivo = 'temp.csv'

        # criptografa a planilha e remove o diretório de trabalho
        with open(arquivo, 'rb') as f:
            status = gpg.encrypt(f, key.results[0]['fingerprint'], output=arquivo_cri)
        print('ok: ', status.ok)
        print('status: ', status.status)

        shutil.rmtree('doctemp')
        os.remove('temp.csv')

    cri()

if __name__ == '__main__':
    main()
