def BFS(grafo, inici):
    cola = [] 
    visitados = set()

    # encolar el nodo inicial
    cola.append(inici) # A
    while cola: # mientras la cola no esté vacía
        nodo = cola.pop(0) # desencolar el primer nodo
        # procesar el nodo
        if nodo not in visitados:
            print(nodo)
            visitados.add(nodo)
            # para cada vecino del nodo
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                # si el vecino no ha sido visitado
                    cola.append(vecino)

