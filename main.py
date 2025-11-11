import  matriz3
from operacoes import Operacoes

while True:
    print("\n=== FÁBRICA ÓPTICA — CONTROLE DE PRODUÇÃO ===")
    print("1 - Calcular produção de dois modelos")
    print("0 - Sair do programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Consumo por modelo
        metal_A = float(input("Metal usado por modelo A (kg): "))
        plastico_A = float(input("Plástico usado por modelo A (kg): "))
        lente_A = int(input("Lentes usadas por modelo A (mínimo 2): "))
        if lente_A < 2:
            print("❌ Cada óculos precisa de pelo menos 2 lentes!"); continue

        metal_B = float(input("Metal usado por modelo B (kg): "))
        plastico_B = float(input("Plástico usado por modelo B (kg): "))
        lente_B = int(input("Lentes usadas por modelo B (mínimo 2): "))
        if lente_B < 2:
            print("❌ Cada óculos precisa de pelo menos 2 lentes!"); continue

        # Estoque disponível
        metal_total = float(input("Metal disponível (kg): "))
        plastico_total = float(input("Plástico disponível (kg): "))
        lente_total = int(input("Lentes disponíveis: "))

        # Montando matriz 3x3 real
        # Coluna 3: apenas para tornar invertível, será usada para ajustar resultado
        matriz = [
            [metal_A, metal_B, 0],
            [plastico_A, plastico_B, 0],
            [lente_A, lente_B, 1]
        ]
        vetor = [metal_total, plastico_total, lente_total]

        inv = matriz3.inversa3x3(matriz)
        if inv is None:
            print("❌ Sistema sem solução única!"); continue

        resultado = Operacoes.multiplicar_matriz_vetor(inv, vetor)
        Q_A = int(resultado[0])
        Q_B = int(resultado[1])

        # Ajustando lentes manualmente
        while Q_A*lente_A + Q_B*lente_B > lente_total:
            if Q_A >= Q_B:
                Q_A -= 1
            else:
                Q_B -= 1

        print("\n=== RESULTADO ===")
        print(f"Quantidade de óculos modelo A: {Q_A}")
        print(f"Quantidade de óculos modelo B: {Q_B}")
        print("✅ Cálculo concluído!\n")

    elif opcao == "0":
        print("Encerrando o sistema... 👓"); break
    else:
        print("⚠ Opção inválida! Digite 1 ou 0.")