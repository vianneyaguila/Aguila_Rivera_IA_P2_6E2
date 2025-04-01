def ids(grafo, inicio, objetivo, max_profundidad=20):
    """
    Implementación de Iterative Deepening Search (IDS).
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio: Nodo inicial
        objetivo: Nodo a encontrar
        max_profundidad (int): Límite máximo de profundidad a explorar
    
    Returns:
        list: Camino desde inicio a objetivo, o None si no se encuentra
    """
    
    # Función auxiliar para DFS limitada (recursiva)
    def dls(nodo, camino_actual, profundidad):
        # Caso base: nodo objetivo encontrado
        if nodo == objetivo:
            return camino_actual + [nodo]
            
        # Caso base: límite de profundidad alcanzado
        if profundidad <= 0:
            return None
            
        # Explorar vecinos no visitados
        for vecino in grafo[nodo]:
            if vecino not in camino_actual:  # Evita ciclos
                resultado = dls(vecino, camino_actual + [nodo], profundidad - 1)
                if resultado is not None:
                    return resultado
        return None
    
    # Bucle principal: incrementa profundidad iterativamente
    for profundidad in range(max_profundidad + 1):
        resultado = dls(inicio, [], profundidad)
        if resultado is not None:
            return resultado
            
    return None  # Solución no encontrada en el rango de profundidad