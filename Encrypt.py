import os
import random
import string
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

# Demander à l'utilisateur de saisir le chemin du fichier à chiffrer
file_path = input('Entrez le chemin du fichier à chiffrer: ')

# Générer un mot de passe aléatoire de 16 caractères
password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

# Vérifier que le fichier existe
if os.path.isfile(file_path):
    # Utiliser PBKDF2 pour générer une clé de chiffrement à partir du mot de passe
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=16, count=10000)
    # Créer un objet Cipher AES en mode CBC
    cipher = AES.new(key, AES.MODE_CBC)

    # Ouvrir le fichier en mode binaire
    with open(file_path, 'rb') as file:
        # Lire le contenu du fichier
        plaintext = file.read()
        # Ajouter des octets de remplissage si nécessaire
        padding_length = 16 - (len(plaintext) % 16)
        plaintext += bytes([padding_length]) * padding_length
        # Chiffrer le contenu du fichier
        ciphertext = cipher.encrypt(plaintext)
        # Créer un dossier pour stocker les fichiers chiffrés
        os.makedirs('encrypted/', exist_ok=True)
        # Écrire le contenu chiffré dans un nouveau fichier
        with open(f'encrypted/{os.path.basename(file_path)}', 'wb') as file:
            file.write(ciphertext)
    # Créer un dossier pour stocker la clé de chiffrement
    os.makedirs('Key', exist_ok=True)
    # Écrire la clé de chiffrement dans un fichier
    with open('Key/key.bin', 'wb') as file:
        file.write(salt + key)
        print(f'Le fichier {file_path} a été chiffré avec succès et enregistré dans /encrypted/, le mot de passe pour le déchiffrer est : {password}')
else:
    print(f'Le fichier {file_path} n"existe pas')

