# Kaique Junior da Silva Oliveira
# Período 2

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task_name = task_name_entry.get()
    task_priority = priority_combobox.get()

    if task_name and task_priority:
        task_list.insert('', tk.END, values=(task_name, task_priority, 'Não Concluída'))
        task_name_entry.delete(0, tk.END)
        priority_combobox.set('')
    else:
        messagebox.showwarning('Aviso', 'Digite o nome e selecione a prioridade da tarefa!')

def update_task():
    selected_item = task_list.selection()

    if selected_item:
        selected_item = selected_item[0]
        updated_task_name = task_name_entry.get()
        updated_task_priority = priority_combobox.get()

        if updated_task_name and updated_task_priority:
            task_list.item(selected_item, values=(updated_task_name, updated_task_priority, 'Não Concluída'))
            task_name_entry.delete(0, tk.END)
            priority_combobox.set('')
        else:
            messagebox.showwarning('Aviso', 'Digite o nome e selecione a prioridade atualizada da tarefa!')
    else:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa para atualizar!')

def delete_task():
    selected_item = task_list.selection()

    if selected_item:
        selected_item = selected_item[0]
        task_list.delete(selected_item)
        task_name_entry.delete(0, tk.END)
        priority_combobox.set('')
    else:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa para excluir!')

def toggle_completed():
    selected_item = task_list.selection()

    if selected_item:
        selected_item = selected_item[0]
        item_values = task_list.item(selected_item, 'values')
        current_status = item_values[2]

        new_status = 'Concluída' if current_status == 'Não Concluída' else 'Não Concluída'
        task_list.item(selected_item, values=(item_values[0], item_values[1], new_status))
    else:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa para concluir!')

# Configurar a janela principal e estilos
window = tk.Tk()
window.title('Lista de Tarefas com Prioridade')

style = ttk.Style()
style.configure('TButton', padding=10, relief='raised', font=('Helvetica', 12))
style.configure('TEntry', padding=10, font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

# Definir cores personalizadas e estilos de botões
bg_color = '#f0f0f0'

button_bg_colors = {
    'Inserir': '#4caf50',
    'Alterar': '#2196f3',
    'Deletar': '#f44336',
    'Concluir': '#ff9800'
}

button_fg_color = 'white'

for action, bg_color in button_bg_colors.items():
    style.configure(f'{action}.TButton', background=bg_color, foreground=button_fg_color)

# Rótulos e entradas de texto
task_name_label = ttk.Label(window, text='Nome da Tarefa:', background=bg_color)
task_name_label.grid(row=0, column=0, padx=10, pady=5)
task_name_entry = ttk.Entry(window, width=30, font=('Helvetica', 12))
task_name_entry.grid(row=0, column=1, padx=10, pady=5)

priority_label = ttk.Label(window, text='Prioridade:', background=bg_color)
priority_label.grid(row=1, column=0, padx=10, pady=5)
priorities = ['Alta', 'Média', 'Baixa']
priority_combobox = ttk.Combobox(window, values=priorities, state='readonly', width=27, font=('Helvetica', 12))
priority_combobox.grid(row=1, column=1, padx=10, pady=5)

# Botões
button_frame = ttk.Frame(window)
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

insert_button = ttk.Button(button_frame, text='Inserir', command=add_task, style='Inserir.TButton')
update_button = ttk.Button(button_frame, text='Alterar', command=update_task, style='Alterar.TButton')
delete_button = ttk.Button(button_frame, text='Deletar', command=delete_task, style='Deletar.TButton')
complete_button = ttk.Button(button_frame, text='Concluir', command=toggle_completed, style='Concluir.TButton')

insert_button.grid(row=0, column=0, padx=5)
update_button.grid(row=0, column=1, padx=5)
delete_button.grid(row=1, column=0, padx=5)
complete_button.grid(row=1, column=1, padx=5)

# Tabela para exibir tarefas
columns = ('Tarefa', 'Prioridade', 'Status')

task_list = ttk.Treeview(window, columns=columns, show='headings', height=10)

task_list.heading('Tarefa', text='Tarefa')
task_list.heading('Prioridade', text='Prioridade')
task_list.heading('Status', text='Status')

task_list.grid(row=3, column=0, columnspan=4, padx=10, pady=5)

task_list.column('Status', width=100)
task_list.heading('Status', text='Status')

window.mainloop()