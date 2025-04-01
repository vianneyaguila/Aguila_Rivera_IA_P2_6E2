import math
import random
import numpy as np

def simulated_annealing_tsp(distancias, temp_inicial=1000, enfriamiento=0.95, iter_por_temp=100, temp_final=0.1):
    """
    Resuelve el TSP usando Temple Simulado
    Args:
        distancias: Matriz nxn de distancias entre ciudades
        temp_inicial: Temperatura inicial
        enfriamiento: Factor de enfriamiento (0.8-0.99 típico)
        iter_por_temp: Iteraciones por temperatura
        temp_final: Temperatura final para detenerse
    Returns:
        tuple: (mejor_ruta, mejor_costo, historial_costos)
    """
    n = len(distancias)
    # 1. Solución inicial aleatoria
    ruta_actual = random.sample(range(n), n)
    costo_actual = calcular_costo(ruta_actual, distancias)
    
    mejor_ruta = ruta_actual.copy()
    mejor_costo = costo_actual
    historial = [costo_actual]
    
    T = temp_inicial
    while T > temp_final:
        for _ in range(iter_por_temp):
            # 2. Generar vecino (intercambio 2-opt aleatorio)
            i, j = sorted(random.sample(range(1, n), 2))
            ruta_vecina = ruta_actual[:i] + ruta_actual[i:j][::-1] + ruta_actual[j:]
            costo_vecino = calcular_costo(ruta_vecina, distancias)
            
            # 3. Calcular diferencia de costo
            delta = costo_vecino - costo_actual
            
            # 4. Criterio de aceptación
            if delta < 0 or random.random() < math.exp(-delta / T):
                ruta_actual, costo_actual = ruta_vecina, costo_vecino
                # 5. Actualizar mejor solución
                if costo_actual < mejor_costo:
                    mejor_ruta, mejor_costo = ruta_actual.copy(), costo_actual
        
        historial.append(mejor_costo)
        # 6. Enfriar
        T *= enfriamiento
    
    return mejor_ruta, mejor_costo, historial

def calcular_costo(ruta, distancias):
    """Calcula la distancia total de una ruta"""
    return sum(distancias[ruta[i]][ruta[(i+1)%len(ruta)]] for i in range(len(ruta)))

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de distancias de ejemplo (5 ciudades)
    distancias = np.array([
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 40],
        [20, 25, 30, 0, 50],
        [25, 30, 40, 50, 0]
    ])
    
    ruta, costo, historial = simulated_annealing_tsp(distancias)
    print(f"Mejor ruta: {ruta}")
    print(f"Distancia total: {costo}")
    print(f"Evolución de costos: {historial[:10]}...")  # Primeros 10 valores