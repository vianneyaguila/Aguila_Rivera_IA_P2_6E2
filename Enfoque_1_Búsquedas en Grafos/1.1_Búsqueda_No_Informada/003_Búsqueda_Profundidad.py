def dfs_iterativo(grafo, inicio, objetivo):
    """
    Implementación iterativa de DFS usando stack.
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio: Nodo de inicio
        objetivo: Nodo a encontrar
    
    Returns:
        list: Camino desde inicio a objetivo, o None si no existe
    """
    pila = [(inicio, [inicio])]  # Almacena (nodo, camino)
    visitados = set()
    
    while pila:
        nodo, camino = pila.pop()  # LIFO
        
        if nodo == objetivo:
            return camino
            
        if nodo not in visitados:
            visitados.add(nodo)
            # Añade vecinos en orden inverso para procesar de izquierda a derecha
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
    
    return None