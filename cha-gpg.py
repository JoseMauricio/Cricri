#! python3

import gnupg
import os
import getpass
import shutil

def main():
    if os.path.exists('doctemp'):
            shutil.rmtree('doctemp')

    gpg = gnupg.GPG(homedir='doctemp')

    nome = input('Seu nome: ')
    email = input('Seu email: ')
    validade = input('Data de expiração das chaves (aaaa-mm-dd): ')
    senha = getpass.getpass('Senha: ')
    chave_publica = input('Nome da chave pública (sem extensão): ')
    chave_privada = getpass.getpass('Nome da chave privada (sem extensão): ')

    key_input = gpg.gen_key_input(name_real=nome, name_email=email, expire_date=validade, passphrase=senha, key_type='RSA')

    key = gpg.gen_key(key_input)
    print('\nFingerprint: '+key.fingerprint)

    ascii_armored_public_keys = gpg.export_keys(key)
    ascii_armored_private_keys = gpg.export_keys(key, True)
    with open(chave_publica+'.asc', 'w') as f:
        f.write(ascii_armored_public_keys)
    with open(chave_privada+'.asc', 'w') as f:
        f.write(ascii_armored_private_keys)

    print('\nChaves geradas. Guarde a chave privada em local seguro.')

if __name__ == '__main__':
    main()
