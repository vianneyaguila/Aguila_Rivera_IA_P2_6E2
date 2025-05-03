def es_seguro(tablero, fila, col, n):
    # Verifica si es seguro colocar una reina en tablero[fila][col]

    # Verifica esta columna en filas anteriores
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # Verifica diagonal izquierda superior
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verifica diagonal derecha superior
    i, j = fila - 1, col + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def resolver_n_reinas(tablero, fila, n):
    # Caso base: si todas las reinas están colocadas
    if fila == n:
        return True

    # Prueba colocar una reina en cada columna de esta fila
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1  # Coloca reina
            if resolver_n_reinas(tablero, fila + 1, n):
                return True  # Si solución encontrada, termina
            tablero[fila][col] = 0  # Backtrack: quita reina

    return False  # No se pudo colocar reina en esta fila

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if x == 1 else "." for x in fila))

# Tamaño del tablero
n = 8
tablero = [[0] * n for _ in range(n)]

if resolver_n_reinas(tablero, 0, n):
    print(f"Solución para {n} reinas:")
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")
