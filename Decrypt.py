import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from getpass import getpass

file_path = input('Entrez le chemin du fichier à déchiffrer: ')
password = getpass('Entrez le mot de passe pour déchiffrer le fichier: ')

if os.path.isfile(file_path):
    with open('Key/key.bin', 'rb') as file:
        key_file = file.read()
        salt = key_file[:16]
        key = key_file[16:]
    key = PBKDF2(password, salt, dkLen=16, count=10000)
    cipher = AES.new(key, AES.MODE_CBC)

    with open(file_path, 'rb') as file:
        ciphertext = file.read()
        plaintext = cipher.decrypt(ciphertext)
        padding_length = plaintext[-1]
        plaintext = plaintext[:-padding_length]
        os.makedirs('decrypted/', exist_ok=True)
        with open(f'decrypted/{os.path.basename(file_path)}', 'wb') as file:
            file.write(plaintext)
    print(f'Le fichier {file_path} a été déchiffré avec succès et enregistré dans decrypted/.')
else:
    print(f"Le fichier {file_path} n'existe pas ou vous avez entré un mauvais mot de passe")
