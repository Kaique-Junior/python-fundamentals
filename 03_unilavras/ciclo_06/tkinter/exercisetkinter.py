import tkinter as tk

def mostrar_mensagem():
    # Pegamos o valor atual guardado na variável do Tkinter
    total_cliques = clique_var.get() 
    total_cliques += 1

    if total_cliques == 1:
        label.config(text="Botão clicado!")
        clique_var.set(1) # Atualiza o valor para o próximo clique
    elif total_cliques == 2:
        label.config(text="Aguardando o clique no botão.")
        clique_var.set(0) # Reseta para zero para recomeçar o ciclo

window = tk.Tk()
window.title("Contador de Cliques")

# Criamos uma variável especial do Tkinter que não se apaga
clique_var = tk.IntVar(value=0)

label = tk.Label(window, text="Aguardando o clique no botão.")
botao = tk.Button(window, text="Clique aqui", command=mostrar_mensagem)

botao.pack(pady=10)
label.pack(pady=10)

window.mainloop()
