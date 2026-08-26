from pathlib import Path # Biblioteca para que o .txt seja criado na mesma página

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / "logs.txt"

texto = str(input("Escreva um texto: "))

with open(LOG_FILE, "a") as arquivo:
    arquivo.write(f"{texto}\n")

print("\nLog registrado com sucesso! \n\nHISTÓRICO DE LOGS")

with open(LOG_FILE, "r") as arquivo:
    for linha in arquivo:
        print(f"[LOG]: {linha.strip()}")

