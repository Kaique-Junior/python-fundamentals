# Material Radioativo perde metade de sua massa a cada 50 segundos

massa_inicial = float(input("Digite a massa em gramas do material radioativo (Separando os números por . Exemplo: 1.5): "))
massa_final = massa_inicial

# Variáveis definidas
horas = 0
minutos = 0
segundos = 0


while massa_final >= 0.5: # Loop principal que finaliza quando a massa for menor que 0.5
    massa_final = massa_final / 2
    segundos += 50

    if massa_final < 0.5: # Condições para analisar e somar quanto tempo foi necessário para a massa ir abaixo de 0.5g
        while segundos > 60:
            if segundos >= 60:
                minutos += 1
                segundos -= 60

            if minutos >= 60:
                horas += 1
                minutos -= 60

        print(f"\nA massa inicial era de: {massa_inicial:.2f}g")
        print(f"A massa final é de: {massa_final:.2f}g")
        print(f"O tempo necessário para que a massa se torne menor que 0,5 foi de: {horas} Horas | {minutos} minutos | {segundos} segundos\n\n")
        break
                
