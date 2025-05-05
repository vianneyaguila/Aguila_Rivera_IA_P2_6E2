import numpy as np
from itertools import product

class RedBayesiana:
    def __init__(self, estructura, cpts):
        """
        Inicializa la red bayesiana.
        
        Args:
            estructura (dict): Diccionario de dependencias padre-hijo
            cpts (dict): Tablas de probabilidad condicional
        """
        self.estructura = estructura
        self.cpts = cpts
        self.variables = list(estructura.keys())
    
    def inferencia_por_corte(self, query, evidence, cut_vars, n_samples=10000):
        """
        Realiza inferencia aproximada por acondicionamiento del corte.
        
        Args:
            query (str): Variable a consultar
            evidence (dict): Evidencia observada {var: valor}
            cut_vars (list): Variables para el corte
            n_samples (int): Número de muestras para aproximación
            
        Returns:
            dict: Distribución de probabilidad aproximada para la query
        """
        # Paso 1: Muestreo de las variables de corte
        cut_samples = self._muestreo_corte(cut_vars, evidence, n_samples)
        
        # Paso 2: Inferencia en cada componente condicionada
        resultados = []
        for cut_values in cut_samples:
            # Combinar evidencia con valores del corte
            nuevo_evidence = {**evidence, **dict(zip(cut_vars, cut_values))}
            
            # Inferencia exacta en el subgrafo condicionado
            prob = self._inferencia_exacta(query, nuevo_evidence)
            resultados.append(prob)
        
        # Paso 3: Promediar resultados
        return np.mean(resultados, axis=0)
    
    def _muestreo_corte(self, cut_vars, evidence, n_samples):
        """Genera muestras para las variables de corte."""
        # Implementación simplificada: muestreo directo con evidencia
        samples = []
        for _ in range(n_samples):
            sample = {}
            for var in self.variables:
                if var in evidence:
                    sample[var] = evidence[var]
                else:
                    # Muestreo basado en padres (simplificado)
                    padres = self.estructura[var]
                    if not padres:
                        sample[var] = np.random.choice(list(self.cpts[var].keys()))
                    else:
                        valores_padres = tuple(sample[p] for p in padres)
                        probs = self.cpts[var][valores_padres]
                        sample[var] = np.random.choice(list(probs.keys()), p=list(probs.values()))
            
            # Solo mantener valores para variables de corte
            samples.append(tuple(sample[var] for var in cut_vars))
        return samples
    
    def _inferencia_exacta(self, query, evidence):
        """Inferencia exacta simplificada para subgrafos pequeños."""
        # Implementación naive para demostración
        vars_restantes = [v for v in self.variables if v not in evidence]
        distribucion = {}
        
        for combinacion in product(*[list(self.cpts[v].keys()) for v in vars_restantes]):
            escenario = {**dict(zip(vars_restantes, combinacion)), **evidence}
            prob = 1.0
            for var in self.variables:
                padres = self.estructura[var]
                valores_padres = tuple(escenario[p] for p in padres) if padres else ()
                prob *= self.cpts[var][valores_padres].get(escenario[var], 0.0)
            
            if escenario[query] not in distribucion:
                distribucion[escenario[query]] = 0.0
            distribucion[escenario[query]] += prob
        
        # Normalizar
        total = sum(distribucion.values())
        return {k: v/total for k, v in distribucion.items()}

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una red bayesiana simple (Alarma -> Robo | Terremoto)
    estructura = {
        'Robo': [],
        'Terremoto': [],
        'Alarma': ['Robo', 'Terremoto']
    }
    
    cpts = {
        'Robo': {(): {'T': 0.001, 'F': 0.999}},
        'Terremoto': {(): {'T': 0.002, 'F': 0.998}},
        'Alarma': {
            ('T', 'T'): {'T': 0.95, 'F': 0.05},
            ('T', 'F'): {'T': 0.94, 'F': 0.06},
            ('F', 'T'): {'T': 0.29, 'F': 0.71},
            ('F', 'F'): {'T': 0.001, 'F': 0.999}
        }
    }
    
    rb = RedBayesiana(estructura, cpts)
    
    # Realizar inferencia con acondicionamiento del corte (usando Alarma como corte)
    resultado = rb.inferencia_por_corte(
        query='Robo',
        evidence={'Terremoto': 'F'},
        cut_vars=['Alarma'],
        n_samples=1000
    )
    
    print("Distribución aproximada de Robo dado Terremoto=F:")
    print(resultado)