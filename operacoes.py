import matriz3

def exibir_resultado(feedback):
    print(f"{"=" * 30}\n\t{feedback}\n{"=" * 30}")

def multiplicar_matriz_vetor(m,v):
    return [sum(m[i][j]*v[j] for j in range(3)) for i in range(3)]

def start_menu():
    while True:
        print("\n=== FÁBRICA ÓPTICA — CONTROLE DE PRODUÇÃO ===")
        print("1 - Calcular produção de dois modelos")
        print("0 - Sair do programa")
        cmd = input("Escolha uma opção: ")

        if cmd == "1":
            # Consumo por modelo
            metal_a= float(input("Metal usado por modelo A (kg): "))
            plastico_a = float(input("Plástico usado por modelo A (kg): "))
            lente_a = 2

            metal_b = float(input("Metal usado por modelo B (kg): "))
            plastico_b = float(input("Plástico usado por modelo B (kg): "))
            lente_b = 2

            # Estoque disponível
            metal_total = float(input("Metal disponível (kg): "))
            plastico_total = float(input("Plástico disponível (kg): "))
            lente_total = int(input("Lentes disponíveis: "))

            # Montando matriz 3x3 real
            # Coluna 3: apenas para tornar invertível, será usada para ajustar resultado
            matriz = [
                [metal_a, metal_b, 0],
                [plastico_a, plastico_b, 0],
                [lente_a, lente_b, 1]
            ]
            vetor = [metal_total, plastico_total, lente_total]

            inv = matriz3.inversa3x3(matriz)
            if inv is None:
                fb = "Sistema sem solução única!"
                exibir_resultado(fb)
                continue

            resultado = multiplicar_matriz_vetor(inv, vetor)
            qtd_a = int(resultado[0])
            qtd_b = int(resultado[1])

            # Ajustando lentes manualmente
            while qtd_a * lente_a + qtd_b * lente_b > lente_total:
                if qtd_a >= qtd_b:
                    qtd_a -= 1
                else:
                    qtd_b -= 1

            print("\n=== RESULTADO ===")
            print(f"Quantidade de óculos modelo A: {qtd_a}")
            print(f"Quantidade de óculos modelo B: {qtd_b}")
            print("Cálculo concluído!\n")

        elif cmd == "0":
            fb = "Encerrando o sistema!"
            exibir_resultado(fb)
            break
        else:
            fb = "Opção inválida!"
            exibir_resultado(fb)