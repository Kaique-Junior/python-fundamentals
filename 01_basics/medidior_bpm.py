# Monitor de Sinais Vitais

total_medicoes = 0
soma_bpm = 0
maior_100bpm = 0
media_bpm = 0

print("--- SISTEMA HOME CARE: MONITOR DE BPM ---")
while True:

    try:
        batimento = int(input("Digite o BPM do paciente (ou 0 para encerrar): "))
    except ValueError:
        print("[ERRO!] Digite apenas números inteiros!")
        continue

    if batimento > 0:

        total_medicoes = total_medicoes + 1 # contador
        soma_bpm = soma_bpm + batimento # acomulador

        if batimento >= 100:
            maior_100bpm = maior_100bpm + 1 # contador

    else:
        media_bpm = soma_bpm / total_medicoes # acomulador
        
        print("\n--- RELATÓRIO DO TURNO ---")
        print(f"Total de medições: {total_medicoes}")
        print(f"Média de BPM: {media_bpm:.1f}")
        print(f"Alertas (>100 BPM): {maior_100bpm}")
        break

