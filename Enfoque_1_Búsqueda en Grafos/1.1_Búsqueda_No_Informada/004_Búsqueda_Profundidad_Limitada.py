def dls_iterativo(grafo, inicio, objetivo, limite):
    """
    Implementación iterativa de DLS usando stack.
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio: Nodo inicial
        objetivo: Nodo a encontrar
        limite (int): Profundidad máxima permitida
    
    Returns:
        list: Camino desde inicio a objetivo, o None si no se encuentra
    """
    pila = [(inicio, [inicio], limite)]  # (nodo, camino, profundidad_restante)
    visitados = set()
    
    while pila:
        nodo, camino, profundidad = pila.pop()
        
        if nodo == objetivo:
            return camino
            
        if profundidad > 0 and nodo not in visitados:
            visitados.add(nodo)
            # Añadimos vecinos en orden inverso para procesar de izquierda a derecha
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino], profundidad - 1))
    
    return None