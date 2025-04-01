import random
import math

def hill_climbing(func, vecinos, x0, max_iter=1000):
    """
    Implementación básica de ascensión de colinas para maximización
    Args:
        func: Función a maximizar
        vecinos: Función que genera vecinos de un estado
        x0: Estado inicial
        max_iter: Máximo de iteraciones permitidas
    Returns:
        Tupla (mejor estado encontrado, valor de la función)
    """
    actual = x0
    valor_actual = func(actual)
    
    for _ in range(max_iter):
        # Generar vecinos y evaluarlos
        vecinos_generados = vecinos(actual)
        if not vecinos_generados:  # Si no hay más vecinos
            break
            
        # Seleccionar el mejor vecino
        mejor_vecino = max(vecinos_generados, key=func)
        valor_vecino = func(mejor_vecino)
        
        # Criterio de parada (no hay mejora)
        if valor_vecino <= valor_actual:
            break
            
        # Moverse al mejor vecino
        actual, valor_actual = mejor_vecino, valor_vecino
    
    return actual, valor_actual

# Ejemplo 1: Maximizar función cuadrática simple
def f1(x):
    return -x**2 + 4*x  # Máximo en x=2 (valor=4)

def vecinos1(x, paso=0.1):
    return [x + paso, x - paso]  # Vecinos izquierda/derecha

# Ejemplo 2: Optimización en espacio discreto (problema de mochila simplificado)
items = [(2,3), (3,4), (4,5), (5,6)]  # (peso, valor)
capacidad = 8

def f2(solucion):
    peso = sum(items[i][0] for i in solucion)
    if peso > capacidad:
        return -float('inf')  # Solución inválida
    return sum(items[i][1] for i in solucion)

def vecinos2(solucion):
    vecinos = []
    # Vecino 1: Añadir un elemento no incluido
    for i in range(len(items)):
        if i not in solucion:
            vecinos.append(solucion + [i])
    # Vecino 2: Quitar un elemento incluido
    for i in range(len(solucion)):
        nuevo = solucion.copy()
        nuevo.pop(i)
        vecinos.append(nuevo)
    return vecinos

# Ejecución
print("Ejemplo 1 (continuo):")
sol, val = hill_climbing(f1, vecinos1, x0=0.0)
print(f"Máximo encontrado en x={sol:.2f}, f(x)={val:.2f}")

print("\nEjemplo 2 (discreto):")
sol, val = hill_climbing(f2, vecinos2, x0=[], max_iter=50)
print(f"Mejor solución: {sol}, Valor total: {val}")