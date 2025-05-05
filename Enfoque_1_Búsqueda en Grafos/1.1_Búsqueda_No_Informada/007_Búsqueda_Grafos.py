from collections import deque

def bfs(grafo, inicio, objetivo):
    """
    Búsqueda en Anchura (BFS) para encontrar camino más corto en grafos no ponderados.
    
    Args:
        grafo: Dict {nodo: [vecinos]}
        inicio: Nodo inicial
        objetivo: Nodo destino
    
    Returns:
        Lista con el camino o None si no existe
    """
    cola = deque([(inicio, [inicio])])  # (nodo_actual, camino)
    visitados = set()
    
    while cola:
        nodo, camino = cola.popleft()
        
        if nodo == objetivo:
            return camino
            
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
    
    return None

def dfs(grafo, inicio, objetivo):
    """
    Búsqueda en Profundidad (DFS) para exploración completa del grafo.
    
    Args:
        grafo: Dict {nodo: [vecinos]}
        inicio: Nodo inicial
        objetivo: Nodo destino
    
    Returns:
        Lista con el camino o None si no existe
    """
    pila = [(inicio, [inicio])]  # (nodo_actual, camino)
    visitados = set()
    
    while pila:
        nodo, camino = pila.pop()
        
        if nodo == objetivo:
            return camino
            
        if nodo not in visitados:
            visitados.add(nodo)
            # Añadir en orden inverso para procesar de izquierda a derecha
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
    
    return None