from collections import deque

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda Bidireccional usando BFS en ambas direcciones.
    
    Args:
        grafo (dict): Diccionario de listas de adyacencia
        inicio: Nodo inicial
        objetivo: Nodo objetivo
    
    Returns:
        list: Camino completo desde inicio a objetivo, o None si no existe
    """
    # Verificación rápida de casos triviales
    if inicio == objetivo:
        return [inicio]
    
    # Estructuras para la búsqueda hacia adelante (desde inicio)
    cola_adelante = deque([inicio])
    padres_adelante = {inicio: None}
    visitados_adelante = {inicio}
    
    # Estructuras para la búsqueda hacia atrás (desde objetivo)
    cola_atras = deque([objetivo])
    padres_atras = {objetivo: None}
    visitados_atras = {objetivo}
    
    # Nodo de intersección (cuando se encuentren las búsquedas)
    interseccion = None
    
    while cola_adelante and cola_atras and not interseccion:
        # Búsqueda hacia adelante (un nivel)
        nivel_actual_adelante = len(cola_adelante)
        for _ in range(nivel_actual_adelante):
            nodo = cola_adelante.popleft()
            
            for vecino in grafo[nodo]:
                if vecino not in visitados_adelante:
                    padres_adelante[vecino] = nodo
                    visitados_adelante.add(vecino)
                    cola_adelante.append(vecino)
                    
                    # Verificar intersección
                    if vecino in visitados_atras:
                        interseccion = vecino
                        break
            if interseccion:
                break
                
        # Búsqueda hacia atrás (un nivel) si no hay intersección aún
        if not interseccion:
            nivel_actual_atras = len(cola_atras)
            for _ in range(nivel_actual_atras):
                nodo = cola_atras.popleft()
                
                for vecino in grafo[nodo]:
                    if vecino not in visitados_atras:
                        padres_atras[vecino] = nodo
                        visitados_atras.add(vecino)
                        cola_atras.append(vecino)
                        
                        # Verificar intersección
                        if vecino in visitados_adelante:
                            interseccion = vecino
                            break
                if interseccion:
                    break
                    
    # Reconstruir camino completo si hay intersección
    if interseccion:
        # Construir primera parte del camino (inicio -> intersección)
        camino_adelante = []
        nodo = interseccion
        while nodo is not None:
            camino_adelante.append(nodo)
            nodo = padres_adelante[nodo]
        camino_adelante.reverse()
        
        # Construir segunda parte (intersección -> objetivo)
        camino_atras = []
        nodo = padres_atras[interseccion]  # Evitar duplicar la intersección
        while nodo is not None:
            camino_atras.append(nodo)
            nodo = padres_atras[nodo]
        
        # Combinar ambos caminos
        camino_completo = camino_adelante + camino_atras
        return camino_completo
    
    return None  # No hay camino