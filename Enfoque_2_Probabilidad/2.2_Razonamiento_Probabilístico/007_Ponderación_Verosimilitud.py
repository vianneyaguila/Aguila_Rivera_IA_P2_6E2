import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class LikelihoodWeighting:
    def __init__(self, red):
        """
        Inicializa el muestreador con una red bayesiana
        
        Args:
            red (dict): Red bayesiana en formato:
                       {'nodo': {'vals': [...], 'prob': [...], 'padres': [...]}}
        """
        self.red = red
        self.orden = self.orden_topologico()
        
    def orden_topologico(self):
        """Determina orden topológico para muestreo"""
        orden = []
        visitados = set()
        
        def dfs(nodo):
            for padre in self.red[nodo].get('padres', []):
                if padre not in visitados:
                    dfs(padre)
            visitados.add(nodo)
            orden.append(nodo)
            
        for nodo in self.red:
            if nodo not in visitados:
                dfs(nodo)
        return orden
    
    def muestrear(self, evidencia, n_muestras=1000):
        """
        Genera muestras ponderadas por verosimilitud
        
        Args:
            evidencia (dict): Valores observados {nodo: valor}
            n_muestras (int): Número de muestras
            
        Returns:
            tuple: (muestras, pesos)
        """
        muestras = []
        pesos = []
        
        for _ in range(n_muestras):
            muestra = {}
            peso = 1.0
            
            for nodo in self.orden:
                if nodo in evidencia:
                    # Fijar evidencia y actualizar peso
                    muestra[nodo] = evidencia[nodo]
                    padres = self.red[nodo].get('padres', [])
                    
                    if not padres:
                        p = self.red[nodo]['prob'][evidencia[nodo]]
                    else:
                        key = tuple(muestra[p] for p in padres)
                        p = self.red[nodo]['prob'][key][evidencia[nodo]]
                    
                    peso *= p
                else:
                    # Muestrear variable no observada
                    padres = self.red[nodo].get('padres', [])
                    
                    if not padres:
                        prob = self.red[nodo]['prob']
                    else:
                        key = tuple(muestra[p] for p in padres)
                        prob = self.red[nodo]['prob'][key]
                    
                    muestra[nodo] = np.random.choice(
                        self.red[nodo]['vals'], 
                        p=prob
                    )
            
            muestras.append(muestra)
            pesos.append(peso)
        
        return muestras, pesos
    
    def estimar_probabilidad(self, consulta, evidencia, n_muestras=1000):
        """
        Estima P(consulta|evidencia)
        
        Args:
            consulta (dict): {variable: valor}
            evidencia (dict): {variable: valor}
            n_muestras (int): Número de muestras
            
        Returns:
            float: Probabilidad estimada
        """
        muestras, pesos = self.muestrear(evidencia, n_muestras)
        var, val = next(iter(consulta.items()))
        
        # Línea corregida con operador ternario dentro de la comprensión
        numerador = sum(w if m[var] == val else 0 for m, w in zip(muestras, pesos))
        denominador = sum(pesos)
        
        return numerador / denominador if denominador > 0 else 0

# ====================================
# EJEMPLO: RED DE ALARMA
# ====================================

# Definir red bayesiana
red_alarma = {
    'Robo': {
        'vals': [0, 1],  # 0=False, 1=True
        'prob': [0.99, 0.01]  # P(Robo)
    },
    'Terremoto': {
        'vals': [0, 1],
        'prob': [0.98, 0.02]  # P(Terremoto)
    },
    'Alarma': {
        'vals': [0, 1],
        'padres': ['Robo', 'Terremoto'],
        'prob': {
            (0,0): [0.999, 0.001],  # P(Alarma|¬R,¬T)
            (0,1): [0.71, 0.29],     # P(Alarma|¬R,T)
            (1,0): [0.06, 0.94],     # P(Alarma|R,¬T)
            (1,1): [0.05, 0.95]      # P(Alarma|R,T)
        }
    }
}

# Crear muestreador
lw = LikelihoodWeighting(red_alarma)

# 1. Estimar P(Robo=1|Alarma=1)
prob = lw.estimar_probabilidad(
    consulta={'Robo': 1},
    evidencia={'Alarma': 1},
    n_muestras=5000
)
print(f"P(Robo=1|Alarma=1) ≈ {prob:.4f}")

# 2. Análisis de muestras
muestras, pesos = lw.muestrear({'Alarma': 1}, 1000)

# Visualizar distribución de pesos
plt.figure(figsize=(10, 5))
plt.hist(pesos, bins=50, density=True)
plt.title("Distribución de pesos de verosimilitud")
plt.xlabel("Peso")
plt.ylabel("Densidad")
plt.show()

# Evolución de la estimación
estimaciones = []
for n in range(1, 1001):
    p = lw.estimar_probabilidad({'Robo': 1}, {'Alarma': 1}, n)
    estimaciones.append(p)

plt.figure(figsize=(10, 5))
plt.plot(estimaciones)
plt.axhline(y=0.284, color='r', linestyle='--', label='Valor teórico')
plt.title("Convergencia de la estimación")
plt.xlabel("Número de muestras")
plt.ylabel("Probabilidad estimada")
plt.legend()
plt.show()