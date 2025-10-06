def UCS(grafo, inicio, objetivo):
    import heapq

    # cola de prioridad
    cola = []
    heapq.heappush(cola, (0, inicio))  # (costo, nodo)
    visitados = set()
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        costo_actual, nodo = heapq.heappop(cola)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        # si llegamos al objetivo, reconstruimos el camino
        if nodo == objetivo:
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]
            camino.reverse()
            print("Camino encontrado:", camino)
            print("Costo total:", costo_actual)
            return camino

        for vecino, peso in grafo[nodo]:
            if vecino not in visitados:
                nuevo_costo = costo_actual + peso
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = nodo
                    heapq.heappush(cola, (nuevo_costo, vecino))

    print("No se encontró un camino al objetivo.")
    return None