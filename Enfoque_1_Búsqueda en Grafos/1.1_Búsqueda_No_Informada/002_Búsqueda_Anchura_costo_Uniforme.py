import heapq

def ucs(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda de Costo Uniforme (UCS).
    
    Parámetros:
    - grafo: Diccionario donde grafo[nodo] = [(vecino1, costo1), (vecino2, costo2), ...].
    - inicio: Nodo inicial de la búsqueda.
    - objetivo: Nodo que se desea encontrar.
    
    Retorna:
    - Tupla (camino, costo_total) si existe un camino.
    - (None, 0) si no hay camino.
    """
    # Estructuras auxiliares
    cola_prioridad = []          # Cola de prioridad (min-heap)
    visitados = set()            # Conjunto para nodos ya explorados
    padres = {}                 # Diccionario para reconstruir el camino
    costos = {inicio: 0}        # Costos acumulados desde el inicio
    
    # Inicializar la cola con el nodo inicial (costo 0)
    heapq.heappush(cola_prioridad, (0, inicio))
    padres[inicio] = None
    
    while cola_prioridad:
        # Extraer el nodo con menor costo acumulado
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:  # Si encontramos el objetivo
            # Reconstruir el camino
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return (camino[::-1], costo_actual)  # Invertir camino
        
        if nodo_actual in visitados:
            continue  # Saltar nodos ya procesados (puede haber duplicados en la cola)
        
        visitados.add(nodo_actual)
        
        # Explorar nodos adyacentes
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in visitados:
                nuevo_costo = costos[nodo_actual] + costo
                # Si el vecino no tiene costo registrado o encontramos un camino más barato
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
    
    return (None, 0)  # No se encontró camino

# Ejemplo de grafo ponderado
grafo_ejemplo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Ejecución
inicio = 'A'
objetivo = 'F'
camino, costo = ucs(grafo_ejemplo, inicio, objetivo)
print(f"Camino de {inicio} a {objetivo}: {camino}")
print(f"Costo total: {costo}")