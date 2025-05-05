import random

def minimos_conflictos(n, max_iter=1000):
    """
    Resuelve el problema de N-Reinas usando el algoritmo de mínimos conflictos.
    
    Args:
        n (int): Tamaño del tablero y número de reinas.
        max_iter (int): Máximo número de iteraciones permitidas.
    
    Returns:
        list: Solución como lista de posiciones por columna, o None si no se encontró solución.
    """
    # 1. Inicialización aleatoria
    solucion = [random.randint(0, n-1) for _ in range(n)]
    
    for _ in range(max_iter):
        # 2. Encontrar reinas en conflicto
        reinas_conflicto = [i for i in range(n) if calcular_conflictos(solucion, i, solucion[i]) > 0]
        
        # Si no hay conflictos, solución encontrada
        if not reinas_conflicto:
            return solucion
        
        # 3. Seleccionar una reina en conflicto aleatoriamente
        col = random.choice(reinas_conflicto)
        
        # 4. Encontrar el movimiento que minimiza conflictos
        min_conflictos = float('inf')
        mejores_posiciones = []
        
        for fila in range(n):
            num_conflictos = calcular_conflictos(solucion, col, fila)
            if num_conflictos < min_conflictos:
                min_conflictos = num_conflictos
                mejores_posiciones = [fila]
            elif num_conflictos == min_conflictos:
                mejores_posiciones.append(fila)
        
        # 5. Mover a una posición óptima aleatoria
        solucion[col] = random.choice(mejores_posiciones)
    
    # Si se agotaron las iteraciones
    return None

def calcular_conflictos(solucion, col, fila):
    """
    Calcula el número de reinas que atacan a (col, fila).
    
    Args:
        solucion (list): Arreglo con posiciones actuales de las reinas.
        col (int): Columna de la reina a evaluar.
        fila (int): Fila de la reina a evaluar.
    
    Returns:
        int: Número de conflictos.
    """
    conflictos = 0
    for otra_col in range(len(solucion)):
        if otra_col == col:
            continue  # No comparar consigo misma
        
        otra_fila = solucion[otra_col]
        if otra_fila == fila or abs(otra_fila - fila) == abs(otra_col - col):
            conflictos += 1
    
    return conflictos

# Ejemplo de uso
if __name__ == "__main__":
    n = 8  # Tamaño del tablero (8x8)
    solucion = minimos_conflictos(n)
    
    if solucion:
        print("Solución encontrada:")
        for fila in range(n):
            linea = ['Q' if solucion[col] == fila else '.' for col in range(n)]
            print(' '.join(linea))
    else:
        print(f"No se encontró solución en {n}x{n} después del máximo de iteraciones.")