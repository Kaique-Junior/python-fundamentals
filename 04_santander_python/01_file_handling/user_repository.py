from pathlib import Path
import json

BASE_DIR = Path(__file__).parent
USER_FILE = BASE_DIR / "users.json"

if USER_FILE.exists():
    with open(USER_FILE, "r") as arquivo:
        usuarios = json.load(arquivo)
else:
    usuarios = []

num_id = 0

for users in usuarios:
    num_id = num_id + 1

print("--- Cadastro de Usuário ---\n")

nome_usuario = str(input("Informe o nome do Usuário: "))
email_usuario = str(input("Informe o email do Usuário: "))

novo_usuario = {
    "id": num_id,
    "nome": nome_usuario,
    "email": email_usuario,
}

usuarios.append(novo_usuario)

with open(USER_FILE, "w") as arquivo:
    json.dump(usuarios, arquivo, indent=4)

print(f"\nO usuário {nome_usuario.upper()} foi cadastrado!\n")