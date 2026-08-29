# Desafio 1

# Váriaveis
salario_minimo = 1192.40
hora_extra = 10

nome = str(input("\nInforme o nome do funcionário: "))
horas_extra_trabalhadas = float(input(f"Informe quantas horas extras {nome.upper()} trabalhou:"))

salario_extra = hora_extra * horas_extra_trabalhadas
salario_bruto = 3 * salario_minimo + salario_extra

# Desconto do INSS
if salario_bruto > 2000:
    salario_descontado_INSS = salario_bruto * (12/100)
else:
    salario_descontado_INSS = salario_bruto * (5/100)

# Desconto do Imposto de Renda 20% > R$2500
if salario_bruto > 2500:
    salario_descontado_IR = salario_bruto * (20/100)
else:
    salario_descontado_IR = 0

# Soma dos Descontos
descontos = salario_descontado_INSS + salario_descontado_IR

# Valor Liquido
salario_liquido = salario_bruto - descontos

print(f"\nNome do Funcionário: {nome}")
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário Liquido: R${salario_liquido:.2f}")