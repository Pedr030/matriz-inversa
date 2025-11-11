class Operacoes:
    def multiplicar_matriz_vetor(m,v):
        return [sum(m[i][j]*v[j] for j in range(3)) for i in range(3)]