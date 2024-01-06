import argparse
import getpass
import os
from typing import Callable
from functools import partial

from key_generator import generate_key
from encryption_manager import encrypt_file, decrypt_file

def process_all_files_in_directory(directory: str, operation_method: Callable[[str], None]) -> None:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            operation_method(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to Journal CLI")

    parser.add_argument("--directory", "-d", type=str, help="Content Directory, it defaults to a directory in here called content", default=os.getcwd()) #TODO: instead of CWD I should also do that + /content parth
    parser.add_argument("--operation", "-o", choices=["encrypt", "decrypt"], help="Type of operation: encrypt or decrypt are the two values", required=True)
    parser.add_argument("--credentials", "-c", type=str, help="File where we could find the encryption key or passphrase to generate it", default=None) #TODO add the path to the file

    args = parser.parse_args()
    if args.credentials is None:
        args.credentials = getpass.getpass(prompt="Enter passphrase for key generation: ")

    content_directory = args.directory
    operation = args.operation
    key = generate_key(args.credentials, salt=b'saltingrandom')

    method = None
    if args.operation == "encrypt" or args.operation == "e":
        method = partial(encrypt_file, key=key)
    elif operation == "decrypt" or operation == "d":
        method = partial(decrypt_file, key=key)
    else:
        print("Error there is no operation supplied!")

    process_all_files_in_directory(content_directory, method)
