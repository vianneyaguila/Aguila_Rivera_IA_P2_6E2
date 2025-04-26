import numpy as np
from itertools import product

class Factor:
    def __init__(self, variables, card, values):
        """
        Inicializa un factor probabilístico
        
        Args:
            variables (list): Nombres de variables en el factor
            card (list): Cardinalidad de cada variable
            values (np.array): Valores de probabilidad
        """
        self.variables = variables
        self.card = card
        self.values = np.array(values).reshape(card)
    
    def __mul__(self, other):
        """Multiplicación de factores (producto punto)"""
        # Implementación de multiplicación de factores
        pass
    
    def marginalize(self, var):
        """Marginaliza una variable del factor"""
        # Implementación de marginalización
        pass

class RedBayesiana:
    def __init__(self):
        self.factores = []
        self.variables = set()
    
    def agregar_factor(self, variables, card, values):
        """Añade un factor a la red"""
        self.factores.append(Factor(variables, card, values))
        self.variables.update(variables)
    
    def eliminar_variable(self, var, orden_eliminacion):
        """
        Elimina una variable mediante marginalización
        
        Args:
            var (str): Variable a eliminar
            orden_eliminacion (list): Orden preferente para operaciones
        """
        # 1. Seleccionar factores que contienen la variable
        factores_relevantes = [f for f in self.factores if var in f.variables]
        
        # 2. Multiplicar factores relevantes
        producto = factores_relevantes[0]
        for f in factores_relevantes[1:]:
            producto *= f
        
        # 3. Marginalizar la variable
        marginal = producto.marginalize(var)
        
        # 4. Actualizar lista de factores
        self.factores = [f for f in self.factores if var not in f.variables]
        self.factores.append(marginal)
    
    def inferencia(self, consulta, evidencia={}, orden_eliminacion=None):
        """
        Realiza inferencia por eliminación de variables
        
        Args:
            consulta (dict): Variable y valor a consultar
            evidencia (dict): Evidencia observada
            orden_eliminacion (list): Orden sugerido para eliminar variables
            
        Returns:
            float: Probabilidad normalizada
        """
        # Implementación completa del algoritmo
        pass

# ====================================
# EJEMPLO: SISTEMA DE ALARMA
# ====================================

# Crear red bayesiana
red = RedBayesiana()

# Añadir factores (CPTs)
red.agregar_factor(['Robo'], [2], [0.01, 0.99])  # P(Robo)
red.agregar_factor(['Terremoto'], [2], [0.02, 0.98])  # P(Terremoto)
red.agregar_factor(['Robo', 'Terremoto', 'Alarma'], [2, 2, 2], [
    # P(Alarma|Robo,Terremoto)
    [0.95, 0.05], [0.94, 0.06], [0.29, 0.71], [0.001, 0.999]
])

# Realizar inferencia
resultado = red.inferencia(
    consulta={'Robo': 1},  # 1 = True
    evidencia={'Alarma': 1},
    orden_eliminacion=['Terremoto']
)

print(f"P(Robo=True|Alarma=True) = {resultado:.4f}")