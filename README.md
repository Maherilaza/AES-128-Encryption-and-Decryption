# AES File Encryption and Decryption

> This program provides a basic example of how to encrypt and decrypt a file using the AES 128 bit algorithm in Python.

## Requirements
. os    
. random    
. string    
. Crypto.Cipher 
. Crypto.Protocol.KDF   

> You can install these modules using pip by running `pip install pycrypto` or `pip install cryptography`

## Usage

## Encryption

To encrypt a file, run the script and provide the path to the file you want to encrypt. The program will then prompt you to enter a password, which will be used as the encryption key. The encrypted file will be saved in a folder named encrypted with the same file name.

## Decryption

To decrypt a file, run the script and provide the path to the encrypted file. The program will then prompt you to enter the password used to encrypt the file. The decrypted file will be saved in a folder named decrypted with the same file name.

## Note

It is important to note that this is just a basic example and it is important to ensure that the security of the password is handled appropriately by using secure password generation methods. It is also important to backup your original files before encrypting them and to store the password in a safe place. It is important to check if the paths to your folders are correct and if you have the necessary permissions to create folders and files.