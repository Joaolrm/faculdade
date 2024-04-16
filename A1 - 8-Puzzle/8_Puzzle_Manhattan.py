def printaMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=' ')
        print()


def gerarTuplasIncorretosCorretos(matriz):
    valorCorreto = 0
    tuplasIncorretos = []
    tuplasCorretos = []
    countLine = 0
    countColuna = 0
    for linha in matriz:
        countLine += 1
        countColuna = 0
        for valor in linha:
            countColuna += 1
            valorCorreto += 1
            tuplasCorretos.append((valorCorreto, countLine, countColuna))
            if valor != valorCorreto and valor != 0:
                tuplasIncorretos.append((valor, countLine, countColuna))

    return (tuplasIncorretos, tuplasCorretos)

# Entrega o valor heuristico de uma matriz, considerando a distancia e o custo.
def calculaHeuristica(matriz):
    tuplasIncorretos, tuplasCorretos = gerarTuplasIncorretosCorretos(matriz)
    heuristica = 0
    for tuplaIncorreta in tuplasIncorretos:
        tuplaCorreta = tuplasCorretos[tuplaIncorreta[0]-1]
        distanciaLinhas = 0
        distanciaColunas = 0
        if tuplaIncorreta[1] > tuplaCorreta[1]:
            distanciaLinhas += tuplaIncorreta[1]-tuplaCorreta[1]

        if tuplaIncorreta[1] < tuplaCorreta[1]:
            distanciaLinhas += tuplaCorreta[1]-tuplaIncorreta[1]


        if tuplaIncorreta[2] > tuplaCorreta[2]:
            distanciaColunas += tuplaIncorreta[2]-tuplaCorreta[2]

        if tuplaIncorreta[2] < tuplaCorreta[2]:
            distanciaColunas += tuplaCorreta[2]-tuplaIncorreta[2]

        heuristica += distanciaLinhas + distanciaColunas        

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

# inicioJogo = [[4, 1, 3], 
#               [7, 2, 0], 
#               [8, 6, 5]]

# inicioJogo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# inicioJogo = [[1, 2, 3, 0], 
#               [5, 7, 8, 4], 
#               [9, 6, 10, 11], 
#               [13, 14, 15, 12]]
# fimJogo = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]





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
