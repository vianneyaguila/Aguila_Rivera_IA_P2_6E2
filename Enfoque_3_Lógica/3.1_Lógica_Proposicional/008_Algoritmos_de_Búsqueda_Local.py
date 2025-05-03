import random

def crear_tablero(n):
    # Genera una solución inicial aleatoria con una reina por fila
    return [random.randint(0, n - 1) for _ in range(n)]

def calcular_conflictos(tablero):
    # Cuenta el número de pares de reinas que se atacan
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1
    return conflictos

def obtener_vecinos(tablero):
    # Genera todos los vecinos posibles cambiando la posición de cada reina
    vecinos = []
    n = len(tablero)
    for fila in range(n):
        for col in range(n):
            if tablero[fila] != col:
                vecino = list(tablero)
                vecino[fila] = col
                vecinos.append(vecino)
    return vecinos

def hill_climbing(n):
    actual = crear_tablero(n)
    actual_conflictos = calcular_conflictos(actual)

    while True:
        vecinos = obtener_vecinos(actual)
        mejor_vecino = min(vecinos, key=calcular_conflictos)
        mejor_conflictos = calcular_conflictos(mejor_vecino)

        if mejor_conflictos >= actual_conflictos:
            # Óptimo local alcanzado
            return actual, actual_conflictos
        actual = mejor_vecino
        actual_conflictos = mejor_conflictos

def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        print(" ".join("Q" if tablero[fila] == col else "." for col in range(len(tablero))))

# Ejecutar para N = 8
n = 8
solucion, conflictos = hill_climbing(n)
print(f"Tablero encontrado con {conflictos} conflictos:")
imprimir_tablero(solucion)
