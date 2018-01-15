#! python3

import gnupg
import shutil
import os
import sys
import getpass

if os.path.exists('doctemp'):
    shutil.rmtree('doctemp')

gpg = gnupg.GPG(homedir='doctemp')

arquivo_cri = input('Nome do arquivo criptografado: ')
x = 1
while os.path.exists(arquivo_cri) == False:
    arquivo_cri = input(f'Arquivo não-encontrado.\nTente de novo ({x+1}/3):\nNome do arquivo criptografado: ')
    x += 1
    if x == 3:
        print('Arquivo não encontrado.')
        sys.exit()

arquivo_out = input('Nome do arquivo descriptografado (com a extensão .csv): ')

key = getpass.getpass('Nome da chave privada: ')
x = 1
while os.path.exists(key) == False:
    key = getpass.getpass(f'Chave não encontrada.\nTente de novo ({x+1}/3):\nNome da chave privada: ')
    x += 1
    if x == 3:
        print('Chave não encontrada')
        sys.exit()

key_data = open(key).read()
import_result = gpg.import_keys(key_data)

senha = getpass.getpass('Senha: ')

with open(arquivo_cri, 'rb') as f:
    descri = gpg.decrypt_file(f, passphrase=senha, output=arquivo_out)

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


if os.path.exists(arquivo_out) == True:
    print('\nArquivo gerado: '+os.path.realpath(arquivo_out))
