import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Chemin complet du fichier à déchiffrer
file_path = input("*.")

# Chemin complet du fichier de clé
key_path = 'Keys/key.bin'

# Lecture de la clé à partir du fichier
with open(key_path, 'rb') as key_file:
    key = key_file.read()

# Initialisation du déchiffreur en mode CTR
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.CTR(os.urandom(16)), backend=backend)
decryptor = cipher.decryptor()

# Lecture des données chiffrées à partir du fichier
with open(file_path, 'rb') as file:
    ciphered_data = file.read()

# Déchiffrement des données
data = decryptor.update(ciphered_data) + decryptor.finalize()

# Ecriture des données déchiffrées dans un nouveau fichier
with open(file_path[:-10], 'wb') as file:
    file.write(data)
