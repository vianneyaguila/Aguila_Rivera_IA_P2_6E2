import heapq

def a_star(grafo, inicio, objetivo, heuristica):
    # Inicialización: cola de prioridad (f, g, nodo, camino)
    cola = []
    heapq.heappush(cola, (0 + heuristica(inicio, objetivo), 0, inicio, [inicio]))
    visitados = set()

    while cola:
        _, g_actual, nodo_actual, camino = heapq.heappop(cola)

        if nodo_actual == objetivo:
            return camino  # Solución encontrada

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for vecino, costo in grafo[nodo_actual].items():
                if vecino not in visitados:
                    g_nuevo = g_actual + costo
                    f_nuevo = g_nuevo + heuristica(vecino, objetivo)
                    heapq.heappush(cola, (f_nuevo, g_nuevo, vecino, camino + [vecino]))

    return None  # No hay solución

# Ejemplo de heurística (distancia Manhattan para un grid)
def heuristica_manhattan(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# Grafo de ejemplo (coordenadas y costos)
grafo_ejemplo = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

inicio = (0, 0)
objetivo = (1, 1)
camino = a_star(grafo_ejemplo, inicio, objetivo, heuristica_manhattan)
print("Camino encontrado:", camino)