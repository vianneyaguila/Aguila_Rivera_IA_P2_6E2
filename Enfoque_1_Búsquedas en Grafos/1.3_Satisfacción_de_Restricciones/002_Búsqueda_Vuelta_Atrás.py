def es_seguro(tablero, fila, col, n):
    """
    Verifica si es seguro colocar una reina en la posición (fila, col)
    en un tablero de ajedrez de tamaño n x n.
    
    Args:
        tablero: Matriz que representa el tablero
        fila: Fila donde se quiere colocar la reina
        col: Columna donde se quiere colocar la reina
        n: Tamaño del tablero
    
    Returns:
        True si es seguro, False si no lo es
    """
    # Verifica la fila hacia la izquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    
    # Verifica la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verifica la diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_n_reinas(tablero, col, n, soluciones):
    """
    Función recursiva principal que resuelve el problema de las N reinas usando backtracking.
    
    Args:
        tablero: Matriz que representa el tablero
        col: Columna actual que se está considerando
        n: Tamaño del tablero
        soluciones: Lista para almacenar todas las soluciones encontradas
    """
    # Caso base: si todas las reinas están colocadas
    if col >= n:
        # Guardamos una copia de la solución actual
        soluciones.append([fila[:] for fila in tablero])
        return
    
    # Consideramos esta columna y probamos colocar la reina en todas las filas una por una
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            # Colocamos la reina en (i, col)
            tablero[i][col] = 1
            
            # Recursión para colocar el resto de las reinas
            resolver_n_reinas(tablero, col + 1, n, soluciones)
            
            # Si colocar la reina en (i, col) no lleva a una solución, la quitamos (backtrack)
            tablero[i][col] = 0

def n_reinas(n):
    """
    Función principal que resuelve el problema de las N reinas.
    
    Args:
        n: Número de reinas y tamaño del tablero (n x n)
    
    Returns:
        Lista con todas las soluciones posibles
    """
    # Inicializamos el tablero vacío
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    soluciones = []
    
    # Comenzamos desde la columna 0
    resolver_n_reinas(tablero, 0, n, soluciones)
    
    return soluciones

# Ejemplo de uso
soluciones = n_reinas(4)
print(f"Número de soluciones encontradas: {len(soluciones)}")
for i, sol in enumerate(soluciones, 1):
    print(f"Solución {i}:")
    for fila in sol:
        print(fila)
    print()