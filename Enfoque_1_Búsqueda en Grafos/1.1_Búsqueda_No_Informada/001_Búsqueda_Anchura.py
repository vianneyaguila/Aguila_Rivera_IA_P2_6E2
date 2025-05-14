from collections import deque # "cola de doble extremo") desde el módulo  
#Es una estructura de datos parecida a una lista , pero más eficiente para agregar o quitar elementos al principio o al final .
#Ideal para implementar colas y pilas de forma eficiente.

def bfs(grafo, inicio, objetivo):
    """
    Implementación de Búsqueda en Anchura (BFS).
    
    Parámetros:
    - grafo: Diccionario que representa el grafo (lista de adyacencia).
    - inicio: Nodo inicial de la búsqueda.
    - objetivo: Nodo que se desea encontrar.
    
    Retorna:
    - Camino desde el inicio hasta el objetivo (si existe).
    - None si no hay camino.
    """
    # Estructuras auxiliares
    cola = deque()          # Cola para nodos a explorar (FIFO)
    visitados = set()       # Conjunto para nodos ya visitados
    padres = {}             # Diccionario para reconstruir el camino
    
    cola.append(inicio)     # Inicializar la cola con el nodo inicial
    visitados.add(inicio)   # Marcar como visitado
    padres[inicio] = None   # El nodo inicial no tiene padre
    
    while cola:             # Mientras haya nodos por explorar
        nodo_actual = cola.popleft()  # Extraer el primer nodo de la cola
        
        if nodo_actual == objetivo:    # Si encontramos el objetivo
            # Reconstruir el camino
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]       # Invertir para mostrar inicio -> objetivo
        
        # Explorar nodos adyacentes no visitados
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)
                padres[vecino] = nodo_actual  # Registrar el padre del vecino
    
    return None  # No se encontró camino

# Ejemplo de grafo (lista de adyacencia)
grafo_ejemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecución
inicio = 'A'
objetivo = 'F'
resultado = bfs(grafo_ejemplo, inicio, objetivo)
print(f"Camino de {inicio} a {objetivo}: {resultado}")  