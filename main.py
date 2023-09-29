from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def load_key(key_file):
    with open(key_file, "rb") as file:
        return file.read()


def save_key(key, key_file):
    with open(key_file, "wb") as file:
        file.write(key)


def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def main():
    print("File Encryption/Decryption Tool")
    print("Options:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        filename = input("Enter the name of the file to encrypt: ")

        key = generate_key()
        key_file = "secret.key"
        save_key(key, key_file)

        # Encrypt the file
        encrypt_file(filename, key)
        print(f"File '{filename}' encrypted successfully.")
        print(key)

    elif choice == "2":
        filename = input("Enter the name of the file to decrypt: ")

        try:
            key_file = "secret.key"
            key = load_key(key_file)

            decrypt_file(filename, key)
            print(f"File '{filename}' decrypted successfully.")
        except FileNotFoundError:
            choice_input_secret_key = input(f"Key file 'secret.key' not found. Wanna put in the secret key manually?. "
                                            f"(Y/n): ")

            if choice_input_secret_key == "y" or "Y":
                key = input("Input the secret key: ")
                decrypt_file(filename, key)
                print(f"File '{filename}' decrypted successfully.")


if __name__ == "__main__":
    main()
