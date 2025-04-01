from queue import PriorityQueue

def greedy_best_first_search(grafo, inicio, objetivo, heuristica):
    """
    Implementación de GBFS para encontrar camino en un grafo
    Args:
        grafo: Diccionario de adyacencia {nodo: [vecinos]}
        inicio: Nodo inicial
        objetivo: Nodo destino
        heuristica: Función h(n) que estima distancia al objetivo
    Returns:
        Lista con el camino encontrado o None
    """
    frontera = PriorityQueue()  # Cola priorizada por h(n)
    frontera.put (heuristica(inicio, objetivo), inicio)  # (h(n), nodo)
    procedencia = {inicio: None}  # Para reconstruir camino
    visitados = set()  # Nodos ya expandidos

    while not frontera.empty():
        _, actual = frontera.get()  # Extrae nodo con menor h(n)

        if actual == objetivo:  # Solución encontrada
            # Reconstrucción del camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = procedencia[actual]
            return camino[::-1]  # Invierte para orden correcto

        visitados.add(actual)  # Marca como visitado

        for vecino in grafo[actual]:
            if vecino not in visitados and vecino not in procedencia:
                # Calcula h(n) para el vecino y lo añade a frontera
                h_valor = heuristica(vecino, objetivo)
                frontera.put((h_valor, vecino))
                procedencia[vecino] = actual  # Registra relación padre-hijo

    return None  # No se encontró solución

# Ejemplo de heurística (distancia Manhattan para grid 2D)
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Grafo de ejemplo (laberinto simple)
grafo = {
    (0,0): [(0,1), (1,0)],
    (0,1): [(0,0), (0,2), (1,1)],
    (0,2): [(0,1), (1,2)],
    (1,0): [(0,0), (1,1)],
    (1,1): [(1,0), (0,1), (1,2)],
    (1,2): [(1,1), (0,2), (2,2)],
    (2,2): [(1,2)]
}

# Ejecución
inicio = (0,0)
objetivo = (2,2)
camino = greedy_best_first_search(grafo, inicio, objetivo, manhattan)
print("Camino encontrado:", camino)