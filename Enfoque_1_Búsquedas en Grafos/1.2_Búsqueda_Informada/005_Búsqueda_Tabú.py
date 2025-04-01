import random
import math
from copy import deepcopy

class TabuSearch:
    def __init__(self, distancias, tam_tabu=10, max_iter=100):
        """
        Inicializa el solver TSP con Búsqueda Tabú
        Args:
            distancias: Matriz de distancias entre ciudades
            tam_tabu: Tamaño de la lista tabú
            max_iter: Máximo de iteraciones
        """
        self.distancias = distancias
        self.tam_tabu = tam_tabu
        self.max_iter = max_iter
        self.n = len(distancias)
        
    def costo_ruta(self, ruta):
        """Calcula la distancia total de una ruta"""
        return sum(self.distancias[ruta[i]][ruta[(i+1)%self.n]] for i in range(self.n))
    
    def generar_vecinos(self, ruta):
        """Genera vecinos mediante intercambio 2-opt"""
        vecinos = []
        for i in range(1, self.n-1):
            for j in range(i+1, self.n):
                if j-i == 1: continue  # No intercambiar adyacentes
                vecino = ruta.copy()
                vecino[i], vecino[j] = vecino[j], vecino[i]  # Swap
                vecinos.append((vecino, (i, j)))  # Guarda el movimiento
        return vecinos
    
    def resolver(self):
        """Ejecuta la Búsqueda Tabú"""
        # Solución inicial aleatoria
        mejor_ruta = random.sample(range(self.n), self.n)
        mejor_costo = self.costo_ruta(mejor_ruta)
        
        # Variables de seguimiento
        ruta_actual = mejor_ruta.copy()
        lista_tabu = []
        historial_costos = []
        
        for _ in range(self.max_iter):
            # Generar vecinos y evaluarlos
            vecinos = self.generar_vecinos(ruta_actual)
            mejor_vecino = None
            mejor_costo_vecino = float('inf')
            mejor_movimiento = None
            
            for vecino, movimiento in vecinos:
                costo = self.costo_ruta(vecino)
                
                # Verificar si el movimiento es tabú
                es_tabu = movimiento in lista_tabu or movimiento[::-1] in lista_tabu
                
                # Criterio de aspiración (aceptar si es mejor global)
                if (costo < mejor_costo_vecino) and (not es_tabu or costo < mejor_costo):
                    mejor_vecino = vecino
                    mejor_costo_vecino = costo
                    mejor_movimiento = movimiento
            
            # Actualizar solución
            if mejor_vecino is not None:
                ruta_actual = mejor_vecino
                lista_tabu.append(mejor_movimiento)
                
                # Mantener tamaño de lista tabú
                if len(lista_tabu) > self.tam_tabu:
                    lista_tabu.pop(0)
                
                # Actualizar mejor solución global
                if mejor_costo_vecino < mejor_costo:
                    mejor_ruta = mejor_vecino.copy()
                    mejor_costo = mejor_costo_vecino
            
            historial_costos.append(mejor_costo)
        
        return mejor_ruta, mejor_costo, historial_costos

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de distancias (ejemplo con 5 ciudades)
    distancias = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 40],
        [20, 25, 30, 0, 50],
        [25, 30, 40, 50, 0]
    ]
    
    ts = TabuSearch(distancias, tam_tabu=5, max_iter=50)
    ruta, costo, historial = ts.resolver()
    
    print(f"Mejor ruta encontrada: {ruta}")
    print(f"Distancia total: {costo}")
    print(f"Evolución de costos: {historial}")