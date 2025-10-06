def DFS(grafo, inici):
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


# 0 = camino, 1 = pared
laberinto = [
    ["0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0"]
]

# convertir el laberinto en un grafo
def laberinto_a_grafo(laberinto):
    grafo = {}
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == "0": # si es un camino
                nodo = (i, j)
                grafo[nodo] = [] # SE AGREGA EL NODO AL GRAFO
                # verificar vecinos (arriba, abajo, izquierda, derecha)
                vecinos = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for vi, vj in vecinos:
                    if 0 <= vi < filas and 0 <= vj < columnas and laberinto[vi][vj] == "0":
                        # si el vecino es un camino lo agregamos al grafo
                        grafo[nodo].append((vi, vj))
    return grafo

grafo_laberinto = laberinto_a_grafo(laberinto)
print("Laberinto:")
for fila in laberinto:
    print(" ".join(fila))
print("Recorrido DFS del laberinto:")
DFS(grafo_laberinto, (0, 0))  # iniciar desde la esquina superior izquierda