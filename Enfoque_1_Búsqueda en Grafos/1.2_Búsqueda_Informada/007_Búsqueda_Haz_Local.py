import heapq
from math import inf

def beam_search(grafo, inicio, objetivo, heuristica, k=3, max_iter=100):
    """
    Implementación de Beam Search para encontrar camino en grafo
    Args:
        grafo: Diccionario de adyacencia {nodo: [vecinos]}
        inicio: Nodo inicial
        objetivo: Nodo destino
        heuristica: Función h(n) que estima distancia al objetivo
        k: Tamaño del haz
        max_iter: Máximo de iteraciones
    Returns:
        Lista con el camino encontrado o None
    """
    # Estructura para almacenar nodos: (heurística, camino)
    haz_actual = [(heuristica(inicio, objetivo), [inicio])]
    
    for _ in range(max_iter):
        siguiente_haz = []
        
        # Expandir todos los nodos del haz actual
        for h_valor, camino in haz_actual:
            nodo_actual = camino[-1]
            
            if nodo_actual == objetivo:
                return camino  # Solución encontrada
                
            for vecino in grafo[nodo_actual]:
                if vecino not in camino:  # Evitar ciclos
                    nuevo_camino = camino + [vecino]
                    nuevo_h_valor = heuristica(vecino, objetivo)
                    siguiente_haz.append((nuevo_h_valor, nuevo_camino))
        
        if not siguiente_haz:
            break  # No hay más nodos por expandir
            
        # Seleccionar los k mejores caminos
        siguiente_haz.sort()  # Ordenar por heurística
        haz_actual = siguiente_haz[:k]
    
    return None  # No se encontró solución

# Ejemplo de heurística (distancia Manhattan para grid 2D)
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

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
camino = beam_search(grafo, inicio=(0,0), objetivo=(2,2), 
                    heuristica=manhattan, k=2)
print("Camino encontrado:", camino)