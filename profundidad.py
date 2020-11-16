

# 1,2,3
# 4,5,6
# 7,8,9
# ir de 1->9
# 1 ->2
# 1 ->4
# 1 ->5
# sucesores de 1 es 2, 4 y 5
# asi con 2 y los demas
# se mete 2, 4 y 5
# 2 no es 9 se pasa al siguien hijo de dos y asi hasta que
# no hayan mas hijos y luego va para arriba.

def sucesores(nodo_actual):
    if nodo_actual == 1:
        return [2, 4, 5]
    if nodo_actual == 2:
        return [1, 3, 4, 5, 6]
    if nodo_actual == 3:
        return [2, 5, 6]
    if nodo_actual == 4:
        return [1, 2, 5, 7]
    if nodo_actual == 5:
        return [1, 2, 3, 4, 6, 7, 8, 9]
    if nodo_actual == 6:
        return [2, 3, 5, 8, 9]
    if nodo_actual == 7:
        return [4, 5, 8]
    if nodo_actual == 8:
        return [4, 5, 6, 7, 9]
    if nodo_actual == 9:
        return [5, 6, 8]


def anchura(nodo_inicio, nodo_fin):
    lista = [nodo_inicio]
    while lista:
        nodo_actual = lista.pop(0)
        print(nodo_actual)
        if nodo_actual == nodo_fin:
            return print("Solución", nodo_actual)
        temp = sucesores(nodo_actual)
        # temp.reverse()
        print(temp)
        if temp:
            temp.extend(lista)  # solo estas lineas cambian
            lista = temp  # Solo estas lineas cambian
            print(lista)
    print("No-SOLUCIÓN")


anchura(1, 9)
