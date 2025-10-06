
def DFS_recursivo(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    # procesar el nodo
    print(nodo)
    visitados.add(nodo)
    # para cada vecino del nodo
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            DFS_recursivo(grafo, vecino, visitados)
    return visitados
