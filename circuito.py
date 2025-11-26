import matriz3

def exibir_resultado(feedback):
    print(f"{"=" * 30}\n\t{feedback}\n{"=" * 30}")

def start_menu():
    while True:
        print("\n=== ANÁLISE DE CIRCUITO ELÉTRICO ===")
        print("Calcular correntes em circuito com 3 malhas")
        print("Lei de Kirchhoff: R₁I₁ + R₂I₂ + R₃I₃ = V")
        
        print("\n1 - Analisar circuito")
        print("0 - Sair do programa")
        cmd = input("Escolha uma opção: ")

        if cmd == "1":
            print("\n=== DADOS DO CIRCUITO ===")
            
            # Malha 1
            print("\nMalha 1:")
            r11 = float(input("Resistência R11 (Ω): "))
            r12 = float(input("Resistência R12 (Ω): "))
            r13 = float(input("Resistência R13 (Ω): "))
            v1 = float(input("Tensão V1 (V): "))
            
            # Malha 2
            print("\nMalha 2:")
            r21 = float(input("Resistência R21 (Ω): "))
            r22 = float(input("Resistência R22 (Ω): "))
            r23 = float(input("Resistência R23 (Ω): "))
            v2 = float(input("Tensão V2 (V): "))
            
            # Malha 3
            print("\nMalha 3:")
            r31 = float(input("Resistência R31 (Ω): "))
            r32 = float(input("Resistência R32 (Ω): "))
            r33 = float(input("Resistência R33 (Ω): "))
            v3 = float(input("Tensão V3 (V): "))
            
            # Validação básica
            if any(r <= 0 for r in [r11,r12,r13,r21,r22,r23,r31,r32,r33]):
                fb = "Todas as resistências devem ser positivas!"
                exibir_resultado(fb)
                continue

            # Debug: mostrar dados de entrada
            print(f"\nSistema de equações:")
            print(f"Malha 1: {r11}I₁ + {r12}I₂ + {r13}I₃ = {v1}V")
            print(f"Malha 2: {r21}I₁ + {r22}I₂ + {r23}I₃ = {v2}V")
            print(f"Malha 3: {r31}I₁ + {r32}I₂ + {r33}I₃ = {v3}V")
            
            # Matriz de resistências
            matriz = [
                [r11, r12, r13],
                [r21, r22, r23],
                [r31, r32, r33]
            ]
            vetor = [v1, v2, v3]
            
            print(f"\nMatriz de resistências: {matriz}")
            print(f"Vetor de tensões: {vetor}")

            inv = matriz3.inversa3x3(matriz)
            if inv is None:
                fb = "Erro: Circuito mal formado (sistema sem solução única)!"
                exibir_resultado(fb)
                continue
                
            # Inversão da matriz
            resultado = [sum(inv[i][j] * vetor[j] for j in range(3)) for i in range(3)]
            print(f"\nResultado bruto: {resultado}")
                
            i1 = resultado[0]
            i2 = resultado[1]
            i3 = resultado[2]
            
            print(f"\nResultado da análise:")
            print(f"I₁: {i1:.3f}A, I₂: {i2:.3f}A, I₃: {i3:.3f}A")

            print("\n=== RESULTADO ===")
            print(f"Corrente na malha 1 (I₁): {i1:.3f}A")
            print(f"Corrente na malha 2 (I₂): {i2:.3f}A")
            print(f"Corrente na malha 3 (I₃): {i3:.3f}A")
            
            # Verificação (substituir de volta nas equações)
            print(f"\nVerificação:")
            check1 = r11*i1 + r12*i2 + r13*i3
            check2 = r21*i1 + r22*i2 + r23*i3
            check3 = r31*i1 + r32*i2 + r33*i3
            print(f"Malha 1: {check1:.3f}V (esperado: {v1}V)")
            print(f"Malha 2: {check2:.3f}V (esperado: {v2}V)")
            print(f"Malha 3: {check3:.3f}V (esperado: {v3}V)")
            print("Análise concluída!\n")

        elif cmd == "0":
            fb = "Encerrando o sistema!"
            exibir_resultado(fb)
            break
        else:
            fb = "Opção inválida!"
            exibir_resultado(fb)