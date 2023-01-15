import os
import random
import string
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

file_path = input('Entrez le chemin du fichier à chiffrer: ')

password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
if os.path.isfile(file_path):
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=16, count=10000)
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, 'rb') as file:
        plaintext = file.read()
        padding_length = 16 - (len(plaintext) % 16)
        plaintext += bytes([padding_length]) * padding_length
        ciphertext = cipher.encrypt(plaintext)
        os.makedirs('encrypted/', exist_ok=True)
        with open(f'encrypted/{os.path.basename(file_path)}', 'wb') as file:
            file.write(ciphertext)
    os.makedirs('Key', exist_ok=True)
    with open('Key/key.bin', 'wb') as file:
        file.write(salt + key)
        print(f'Le fichier {file_path} a été chiffré avec succès et enregistré dans /encrypted/, le mot de passe pour le déchiffrer est : {password}')
else:
    print(f'Le fichier {file_path} n"existe pas')

