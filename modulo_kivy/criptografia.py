from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(filename, key):
    with open(filename, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(filename + ".encrypted", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Gerar a chave e salvar em algum lugar seguro
key = generate_key()

# Nome do arquivo que você deseja criptografar
nome_arquivo = "texto.txt"

# Criptografar o arquivo
encrypt_file(nome_arquivo, key)
print(key)