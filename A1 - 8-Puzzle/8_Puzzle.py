def printaMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=' ')
        print()

def calculaHeuristica(matriz):
    erros = 0
    acertos = 0
    posicao = 0
    for linha in matriz:
        for valor in linha:
            posicao += 1
            if valor == posicao:
                acertos += 1
            else:
                erros += 1
    heuristica = posicao - acertos + erros
    return heuristica


def testePossiveisMovimentos(estado_inicial):
    possibilidades = []
    for linha in range(len(estado_inicial)):
        for coluna in range(len(estado_inicial[linha])):
            if estado_inicial[linha][coluna] == 0:             
                if linha > 0:
                    estado = [row[:] for row in estado_inicial]
                    estado[linha][coluna], estado[linha-1][coluna] = estado[linha-1][coluna], estado[linha][coluna]
                    possibilidades.append(estado)
                
                
                if linha < len(estado_inicial) - 1:
                    estado = [row[:] for row in estado_inicial]
                    estado[linha][coluna], estado[linha+1][coluna] = estado[linha+1][coluna], estado[linha][coluna]
                    possibilidades.append(estado)

                
                if coluna > 0:
                    estado = [row[:] for row in estado_inicial]
                    estado[linha][coluna], estado[linha][coluna-1] = estado[linha][coluna-1], estado[linha][coluna]
                    possibilidades.append(estado)

                
                if coluna < len(estado_inicial[linha]) - 1:
                    estado = [row[:] for row in estado_inicial]
                    estado[linha][coluna], estado[linha][coluna+1] = estado[linha][coluna+1], estado[linha][coluna]
                    possibilidades.append(estado)
    return possibilidades




inicioJogo = [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
fimJogo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


for possibilidade in testePossiveisMovimentos(inicioJogo):
    printaMatriz(possibilidade)
    print(calculaHeuristica(possibilidade))
    print()

estado = [row[:] for row in inicioJogo]
print(estado)
