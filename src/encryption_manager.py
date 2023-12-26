from cryptography.fernet import Fernet
import sys

def encrypt_file(file_path: str, key: bytes):
    """ Encrypt a file using the provided key """
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path: str, key: bytes):
    """ Decrypt a file using the provided key """
    fernet = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <encrypt/decrypt> <key> <file_path>")
        sys.exit(1)

    operation = sys.argv[1]
    key = sys.argv[2]
    file_path = sys.argv[3]

    if operation == 'encrypt':
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif operation == 'decrypt':
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid operation.")
        sys.exit(1)