def printaMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=' ')
        print()

# Entrega o valor heuristico de uma matriz, considerando a distancia e o custo.
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

# Descobre qual menor valor heuristco dentro da lista de possibilidades(que não foram jogadas ainda) e retorna a matriz desse valor heuristico
def proximoMovimento(jogoAtual, listaExlusao):
    melhorHeuristica = None 
    possibilidades = []
    for possibilidade in testePossiveisMovimentos(jogoAtual, possibilidades):
        heuristica = calculaHeuristica(possibilidade)

        if (melhorHeuristica is None or heuristica < melhorHeuristica) and possibilidade not in listaExlusao:
            melhorHeuristica = heuristica
            proxMovimento = possibilidade
    return proxMovimento


def testePossiveisMovimentos(estado_inicial, possibilidades):

    for linha in range(len(estado_inicial)):
        for coluna in range(len(estado_inicial[linha])):
            if estado_inicial[linha][coluna] == 0:             
                if (linha > 0):
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




def eightpuzle(pontoPartida, resultadoFinal):
    
    
    movimento = pontoPartida
    movimentosPassados = []
    print("Inicio do jogo:\n")
    while movimento != resultadoFinal:
        movimentosPassados.append(movimento)
        printaMatriz(movimento)
        print()
        movimento = proximoMovimento(movimento, movimentosPassados)

    printaMatriz(movimento)
    print("\nO jogo atingiu o resultado final!")

eightpuzle(inicioJogo, fimJogo)
