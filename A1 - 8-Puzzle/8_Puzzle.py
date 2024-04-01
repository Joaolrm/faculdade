def printaMatriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=' ')
        print()

def calculaHeuristica(matriz):
    erros = 0
    acertos = 0
    posicao = 0
    for linha in matriz:
        for valor in linha:
            posicao += 1
            # print (posicao)
            if valor == posicao:
                acertos += 1
            else:
                erros += 1
    erros = erros + (posicao - acertos)
    return (erros - acertos)


estado_inicial = [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
printaMatriz(estado_inicial)

print(calculaHeuristica(estado_inicial))
printaMatriz(estado_inicial)
