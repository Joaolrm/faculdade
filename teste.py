cidades = {
    'A': [('C', 2), ('D', 3)],
    'C': [('D', 1), ('E', 4), ('F', 6)],
    'D': [('E', 1), ('G', 5)],
    'E': [('B', 5), ('F', 2)],
    'F': [('B', 3)],
    'G': [('E', 2), ('B', 9)],
    'H': [('A', 4), ('D', 3)],
    'I': [('H', 3), ('J', 6)],
    'J': [('A', 5)]
    # você pode adicionar mais valores aqui 
}
heuristica = {
    'A': 7, 'C': 5, 'D': 7, 'E': 3, 'F': 2,
    'G': 6, 'H': 8, 'I': 9, 'J': 10, 'B':0
}

print(cidades)

for c in cidades:
    # print(cidades[c])
    index = 0
    for x in c:
        print(cidades[c][index])
        index = index + 1
        print(index)


