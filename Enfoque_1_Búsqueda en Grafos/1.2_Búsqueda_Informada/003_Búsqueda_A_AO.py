import heapq #módulo de Python queque permite usar una cola de prioridad implementada
# En un montón, el elemento con menor valor siempre está al principio.
# no es una palabra reservada como printo while. Es una librería externa estándar de Python, por eso necesitas importarla explícitamente antes de usar sus funciones como heapq.heappusho heapq.heappop.

def a_star(grafo, inicio, objetivo, heuristica):
    """
    Implementación del algoritmo A*
    grafo: Diccionario {nodo: {vecino: costo}}
    inicio, objetivo: Nodos inicial y final
    heuristica: Función h(n) que estima distancia al objetivo
    """
    frontera = []
    heapq.heappush(frontera, (0 + heuristica(inicio, objetivo), 0, inicio, [inicio]))
    visitados = set()
    
    while frontera:
        _, g_actual, actual, camino = heapq.heappop(frontera)
        
        if actual == objetivo:
            return camino
            
        if actual not in visitados:
            visitados.add(actual)
            for vecino, costo in grafo[actual].items():
                if vecino not in visitados:
                    g_nuevo = g_actual + costo
                    f_nuevo = g_nuevo + heuristica(vecino, objetivo)
                    heapq.heappush(frontera, (f_nuevo, g_nuevo, vecino, camino + [vecino]))
    
    return None

# Ejemplo de uso
def distancia_euclidiana(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

grafo_ejemplo = {
    (0,0): {(0,1): 1, (1,0): 1},
    (0,1): {(0,0): 1, (1,1): 1.5},
    (1,0): {(0,0): 1, (1,1): 1},
    (1,1): {(0,1): 1.5, (1,0): 1}
}

camino = a_star(grafo_ejemplo, (0,0), (1,1), distancia_euclidiana)
print("Camino A*:", camino)


def ao_star(grafo_and_or, inicio, objetivo, heuristica):
    """
    Implementación básica de AO* para grafos AND-OR
    grafo_and_or: Diccionario con estructura especial:
        {'OR': {nodo: [opciones]}, 'AND': {nodo: [[requisitos]]}}
    """
    solucion = {}
    expandido = set()
    
    def costo(nodo):
        if nodo == objetivo:
            return 0
        if nodo in grafo_and_or['OR']:
            return min(heuristica(opcion, objetivo) + costo(opcion) 
                   for opcion in grafo_and_or['OR'][nodo])
        elif nodo in grafo_and_or['AND']:
            return sum(heuristica(req, objetivo) + costo(req) 
                   for conjunto in grafo_and_or['AND'][nodo] 
                   for req in conjunto)
    
    # Búsqueda principal (simplificada)
    nodo_actual = inicio
    while nodo_actual != objetivo:
        if nodo_actual in expandido:
            break
            
        expandido.add(nodo_actual)
        
        if nodo_actual in grafo_and_or['OR']:
            # Selecciona la mejor opción OR
            mejor_opcion = min(grafo_and_or['OR'][nodo_actual], 
                             key=lambda x: heuristica(x, objetivo) + costo(x))
            solucion[nodo_actual] = mejor_opcion
            nodo_actual = mejor_opcion
        elif nodo_actual in grafo_and_or['AND']:
            # Expande todos los requisitos AND
            for conjunto in grafo_and_or['AND'][nodo_actual]:
                for req in conjunto:
                    if req not in solucion:
                        solucion.update(ao_star(grafo_and_or, req, objetivo, heuristica))
    
    return solucion