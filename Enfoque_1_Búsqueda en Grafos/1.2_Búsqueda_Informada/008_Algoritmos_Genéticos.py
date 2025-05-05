import random
import numpy as np

class AlgoritmoGenetico:
    def __init__(self, funcion_objetivo, tam_poblacion=50, dim=2, rango=(-10, 10), 
                 prob_cruce=0.8, prob_mutacion=0.1, elitismo=True, max_generaciones=100):
        """
        Inicializa el algoritmo genético
        Args:
            funcion_objetivo: Función a maximizar
            tam_poblacion: Número de individuos
            dim: Dimensión del problema
            rango: Tupla (min, max) para valores iniciales
            prob_cruce: Probabilidad de cruce [0,1]
            prob_mutacion: Probabilidad de mutación [0,1]
            elitismo: Conserva el mejor individuo
            max_generaciones: Criterio de parada
        """
        self.funcion = funcion_objetivo
        self.tam_poblacion = tam_poblacion
        self.dim = dim
        self.rango = rango
        self.prob_cruce = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.elitismo = elitismo
        self.max_gen = max_generaciones
        
    def inicializar_poblacion(self):
        """Genera población inicial aleatoria"""
        return np.random.uniform(self.rango[0], self.rango[1], 
                               (self.tam_poblacion, self.dim))
    
    def evaluar_poblacion(self, poblacion):
        """Evalúa todos los individuos"""
        return np.array([self.funcion(ind) for ind in poblacion])
    
    def seleccion_por_torneo(self, poblacion, fitness, k=3):
        """Selección por torneo de tamaño k"""
        seleccionados = []
        for _ in range(len(poblacion)):
            participantes = random.sample(range(len(poblacion)), k)
            ganador = max(participantes, key=lambda x: fitness[x])
            seleccionados.append(poblacion[ganador])
        return np.array(seleccionados)
    
    def cruce_aritmetico(self, padre1, padre2):
        """Cruce por combinación convexa"""
        alpha = random.random()
        hijo1 = alpha * padre1 + (1-alpha) * padre2
        hijo2 = alpha * padre2 + (1-alpha) * padre1
        return hijo1, hijo2
    
    def mutacion_gaussiana(self, individuo, sigma=0.5):
        """Mutación con ruido gaussiano"""
        mutado = individuo + np.random.normal(0, sigma, size=self.dim)
        return np.clip(mutado, self.rango[0], self.rango[1])
    
    def ejecutar(self):
        """Ejecuta el algoritmo genético"""
        # 1. Inicialización
        poblacion = self.inicializar_poblacion()
        mejor_historico = []
        
        for generacion in range(self.max_gen):
            # 2. Evaluación
            fitness = self.evaluar_poblacion(poblacion)
            mejor_fitness = max(fitness)
            mejor_ind = poblacion[np.argmax(fitness)]
            mejor_historico.append(mejor_fitness)
            
            # 3. Selección
            seleccionados = self.seleccion_por_torneo(poblacion, fitness)
            
            # 4. Cruce
            nueva_poblacion = []
            for i in range(0, self.tam_poblacion-1, 2):
                padre1, padre2 = seleccionados[i], seleccionados[i+1]
                
                if random.random() < self.prob_cruce:
                    hijo1, hijo2 = self.cruce_aritmetico(padre1, padre2)
                else:
                    hijo1, hijo2 = padre1.copy(), padre2.copy()
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            # 5. Mutación
            for i in range(len(nueva_poblacion)):
                if random.random() < self.prob_mutacion:
                    nueva_poblacion[i] = self.mutacion_gaussiana(nueva_poblacion[i])
            
            # 6. Elitismo (opcional)
            if self.elitismo:
                peor_idx = np.argmin([self.funcion(ind) for ind in nueva_poblacion])
                nueva_poblacion[peor_idx] = mejor_ind
            
            poblacion = np.array(nueva_poblacion)
        
        return mejor_ind, mejor_fitness, mejor_historico

# Ejemplo de uso
def funcion_ejemplo(x):
    """Función de ejemplo: Máximo en (0,0)"""
    return -x[0]**2 - x[1]**2  # Sphere function

ag = AlgoritmoGenetico(funcion_ejemplo, tam_poblacion=50, dim=2, 
                      rango=(-10, 10), max_generaciones=100)
mejor_sol, mejor_valor, historial = ag.ejecutar()

print(f"Mejor solución encontrada: {mejor_sol}")
print(f"Valor de la función: {mejor_valor}")
print(f"Evolución del mejor fitness: {historial[:5]}...")