from itertools import product
import numpy as np

class RedBayesiana:
    def __init__(self):
        self.nodos = {}
        self.relaciones = []
    
    def agregar_nodo(self, nombre, valores, cpt):
        """
        Añade un nodo a la red con su tabla de probabilidad condicional (CPT)
        
        Args:
            nombre (str): Nombre del nodo
            valores (list): Valores posibles del nodo
            cpt (dict): Tabla de probabilidad condicional
        """
        self.nodos[nombre] = {'valores': valores, 'cpt': cpt}
    
    def agregar_relacion(self, padre, hijo):
        """
        Establece una relación padre-hijo entre nodos
        
        Args:
            padre (str): Nodo padre
            hijo (str): Nodo hijo
        """
        self.relaciones.append((padre, hijo))
    
    def _es_compatible(self, instancia, evidencia):
        """
        Verifica si una instancia es compatible con la evidencia
        
        Args:
            instancia (dict): Asignación de valores a variables
            evidencia (dict): Evidencia observada
            
        Returns:
            bool: True si es compatible, False si no
        """
        for var, val in evidencia.items():
            if instancia.get(var) != val:
                return False
        return True
    
    def _get_padres(self, nodo):
        """
        Obtiene los padres de un nodo
        
        Args:
            nodo (str): Nombre del nodo
            
        Returns:
            list: Lista de padres del nodo
        """
        return [p for (p, h) in self.relaciones if h == nodo]
    
    def _calcular_probabilidad_conjunta(self, instancia):
        """
        Calcula la probabilidad conjunta para una instancia específica
        
        Args:
            instancia (dict): Asignación completa de valores
            
        Returns:
            float: Probabilidad conjunta
        """
        prob = 1.0
        for nodo in self.nodos:
            padres = self._get_padres(nodo)
            if not padres:  # Nodo raíz
                prob *= self.nodos[nodo]['cpt'].get(instancia[nodo], 0)
            else:
                # Construir clave para CPT
                key = tuple(instancia[p] for p in padres)
                prob *= self.nodos[nodo]['cpt'].get(key, {}).get(instancia[nodo], 0)
        return prob
    
    def inferencia_por_enumeracion(self, consulta, evidencia={}):
        """
        Realiza inferencia por enumeración
        
        Args:
            consulta (dict): Variable a consultar y su valor deseado
            evidencia (dict): Evidencia observada
            
        Returns:
            float: Probabilidad normalizada
        """
        # Obtener variables ocultas (todas excepto consulta y evidencia)
        vars_ocultas = [n for n in self.nodos if n not in consulta and n not in evidencia]
        
        # Generar todas las posibles combinaciones de variables ocultas
        valores_ocultas = [self.nodos[v]['valores'] for v in vars_ocultas]
        combinaciones = product(*valores_ocultas)
        
        # Calcular probabilidades no normalizadas
        prob_consulta = 0.0
        prob_total = 0.0
        
        var_consulta, val_consulta = next(iter(consulta.items()))
        
        for comb in combinaciones:
            # Crear instancia completa
            instancia = evidencia.copy()
            instancia.update(zip(vars_ocultas, comb))
            instancia.update(consulta)
            
            # Calcular probabilidad conjunta
            prob_conjunta = self._calcular_probabilidad_conjunta(instancia)
            
            # Acumular según si coincide con la consulta
            if instancia[var_consulta] == val_consulta:
                prob_consulta += prob_conjunta
            prob_total += prob_conjunta
        
        # Normalizar
        return prob_consulta / prob_total if prob_total > 0 else 0.0

# ====================================
# EJEMPLO: SISTEMA DE DIAGNÓSTICO MÉDICO
# ====================================

# Crear red bayesiana
red = RedBayesiana()

# Definir nodos y probabilidades
red.agregar_nodo('Enfermedad', ['Ninguna', 'Gripe', 'COVID'], 
                 {'Ninguna': 0.7, 'Gripe': 0.2, 'COVID': 0.1})

red.agregar_nodo('Fiebre', ['No', 'Si'], {
    ('Ninguna',): {'No': 0.9, 'Si': 0.1},
    ('Gripe',): {'No': 0.3, 'Si': 0.7},
    ('COVID',): {'No': 0.1, 'Si': 0.9}
})

red.agregar_nodo('Tos', ['No', 'Si'], {
    ('Ninguna',): {'No': 0.7, 'Si': 0.3},
    ('Gripe',): {'No': 0.4, 'Si': 0.6},
    ('COVID',): {'No': 0.1, 'Si': 0.9}
})

# Establecer relaciones
red.agregar_relacion('Enfermedad', 'Fiebre')
red.agregar_relacion('Enfermedad', 'Tos')

# ====================================
# CONSULTAS DE INFERENCIA
# ====================================

# Consulta 1: P(Enfermedad=COVID | Fiebre=Si)
resultado1 = red.inferencia_por_enumeracion(
    consulta={'Enfermedad': 'COVID'},
    evidencia={'Fiebre': 'Si'}
)
print(f"P(Enfermedad=COVID | Fiebre=Si) = {resultado1:.4f}")

# Consulta 2: P(Fiebre=Si | Tos=Si)
resultado2 = red.inferencia_por_enumeracion(
    consulta={'Fiebre': 'Si'},
    evidencia={'Tos': 'Si'}
)
print(f"P(Fiebre=Si | Tos=Si) = {resultado2:.4f}")