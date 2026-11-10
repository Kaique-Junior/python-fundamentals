import threading
import queue
import time
import random

# Nome completo: Kaique Junior da Silva Oliveira
# Período: 2º Período

# Cores para deixar vísivel cada caixa específico
RESET = "\033[0m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"

# Função executada por cada thread(caixa)
def processar_caixa(nome_caixa, fila):
    
    # Continua a funcionar enquanto tiver clientes na fila
    while not fila.empty():
        
        # Obtem o próximo cliente da fila
        cliente = fila.get()
        
        # Imprime uma mensagem indicando que a caixa está atendendo o cliente
        print(f"[{nome_caixa}] atendendo o {cliente}...")
        
        # Simula o tempo de atendimento de forma aleatória (de 1 a 5 segundos)
        tempo_atendimento = random.randint(1, 5)
        time.sleep(tempo_atendimento)
        
        # Imprime uma mensagem indicando que foi finalizado o atendimento e o quanto tempo foi preciso
        print(f"[{nome_caixa}] atendeu o {cliente} em {tempo_atendimento} segundos.")
        
        # Informa a fila que terminou
        fila.task_done()

# Fluxo Principal
# Cria três filas (uma para cada caixa)
filas_caixas = [queue.Queue(), queue.Queue(), queue.Queue()]
nomes_caixas = [f"{AMARELO}Caixa 1{RESET}", f"{VERDE}Caixa 2{RESET}", f"{AZUL}Caixa 3{RESET}"]

# Lista de Clientes
clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]

# Adiciona os clientes aleatoriamente nas filas dos caixas
for cliente in clientes:
    indice_caixa_aleatorio = random.randint(0, 2)
    filas_caixas[indice_caixa_aleatorio].put(cliente)
    print(f"{cliente} esta na fila do {nomes_caixas[indice_caixa_aleatorio]}.")

print("\n=== Início do Atendimento ===\n")

# Inicia as três threads, uma para cada caixa, chamando a função processar_caixa
threads_ativas = []
for i in range(3):
    # Passamos o nome da caixa e a sua respectiva fila como argumentos (args)
    t = threading.Thread(target=processar_caixa, args=(nomes_caixas[i], filas_caixas[i]))
    threads_ativas.append(t)
    t.start()

# Espera até que todas as compras sejam processadas (todas as threads finalizem)
for t in threads_ativas:
    t.join()

# Imprime uma mensagem no terminal indicando que todas as compras foram processadas e finalizadas
print("\n=== Fim do Atendimento ===")
print("Todas as compras foram finalizadas nos caixas.")