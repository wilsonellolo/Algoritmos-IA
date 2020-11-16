
def sucesores(nodo_actual):
    if nodo_actual == 'a':
        return [['b'], ['c'], ['d']]
    if nodo_actual == 'b':
        return [['e'], ['c']]
    if nodo_actual == 'c':
        return [['e'], ['g'], ['f']]
    if nodo_actual == 'd':
        return [['c'], ['f']]
    if nodo_actual == 'e':
        return [['g']]
    if nodo_actual == 'f':
        return [['g']]
    # if nodo_actual == 'g':
    #     return [[]]


def museo(nodo_inicio, nodo_fin):
    no_sol = 0
    lista = [[nodo_inicio]]
    while lista:
        nodo_actual = lista.pop(0)
        # print(nodo_actual)
        if nodo_actual[0] == nodo_fin:
            no_sol += 1
            print(nodo_actual[:][::-1])
            print("SOLUCION")
        temp = sucesores(nodo_actual[0])
        # temp.reverse()
        # print(temp)
        if temp:
            for x in temp:
                x.extend(nodo_actual)
            lista.extend(temp)
            # print(lista)
    print("TOTAL: " + str(no_sol)+" SOLUCIONES")


museo('a', 'g')
