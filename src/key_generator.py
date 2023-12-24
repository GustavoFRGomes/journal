from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64
import os

def generate_key(passphrase: str, salt: bytes = None) -> bytes:
    if not salt:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_000_000,
        backend=default_backend()
    )

    raw_key = kdf.derive(str.encode(passphrase))
    key = base64.urlsafe_b64encode(raw_key)
    return key

if __name__ == "__main__":
    print("Welcome to key-generator!")

    password = input("Please enter a passphrase to derive the key from: ")
    key = generate_key(password, b'salt')
    print("Generated key: ", base64.urlsafe_b64decode(key))