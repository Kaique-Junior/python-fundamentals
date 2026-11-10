# Nome Completo: Kaique Junior da Silva Oliveira
# Período: 2º período
# Atividade: Mão na Massa - Matrizes

def somar_vendas(planilha):
    soma_total = 0  # acumulador
    for venda in planilha:
        # Multiplica quantidade pelo valor unitário e soma ao total
        soma_total += venda[2] * venda[3]
    return soma_total

def produto_mais_vendido(planilha):
    mais_vendido = None
    quantidade_maxima = 0

    for venda in planilha:
        # Verifica se a quantidade atual é maior que a máxima registrada
        if venda[2] > quantidade_maxima:
            quantidade_maxima = venda[2]
            mais_vendido = venda[1]
            
    return mais_vendido  # Retorna após verificar toda a lista

def valor_medio_vendas(planilha):
    total = somar_vendas(planilha)
    numero_vendas = len(planilha)
    
    # Evita divisão por zero se a planilha estiver vazia
    if numero_vendas == 0:
        return 0
    return total / numero_vendas
   
def encontrar_cliente_gastou_mais(planilha):
    cliente_mais_gastador = None
    gasto_maximo = 0

    for venda in planilha:
        gasto = venda[2] * venda[3]  # Calcula o total da compra individual
        if gasto > gasto_maximo:
            gasto_maximo = gasto
            cliente_mais_gastador = venda[0]
            
    return cliente_mais_gastador
    
def ordenar_por_nome_do_produto(planilha):
    return sorted(planilha, key=lambda x: x[1])

# Planilha de Vendas
planilha = [
    ["Kaique", "SmartPhone", 1, 1000],
    ["Brenda", "TV", 1, 1500],
    ["Monique", "Fone", 2, 50],
    ["Fábio", "Impressora", 4, 1500],
    ["Roberta", "Notebook", 2, 3500],
    ["Junior", "Impressora", 1, 1500],
    ["Julia", "SmartPhone", 2, 1000],
    ["Monique", "Fone", 5, 50]
]

# Execução e exibição dos resultados
valor_total_vendas = somar_vendas(planilha)

print(f'Total de vendas: R$ {valor_total_vendas:.2f}')
print(f'Produto mais vendido: {produto_mais_vendido(planilha)}')
print(f'Valor médio: R$ {valor_medio_vendas(planilha):.2f}')
print(f'Cliente que mais gastou: {encontrar_cliente_gastou_mais(planilha)}\n')

print("Planilha Original:", planilha)
print("Planilha Ordenada:", ordenar_por_nome_do_produto(planilha))