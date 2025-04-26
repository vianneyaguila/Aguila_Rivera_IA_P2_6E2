import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class Muestreador:
    def __init__(self, red):
        """
        Inicializa el muestreador con una red bayesiana
        
        Args:
            red (dict): Representación de la red bayesiana
                       Ej: {'A': {'vals': [0,1], 'prob': [0.3,0.7]},
                           'B': {'vals': [0,1], 'prob': [[0.9,0.1], [0.4,0.6]],
                                 'padres': ['A']}}
        """
        self.red = red
        self.orden = self.orden_topologico()
        
    def orden_topologico(self):
        """Determina orden topológico para muestreo directo"""
        # Implementación simplificada
        return sorted(self.red.keys())
    
    def muestreo_directo(self, n_muestras=1000):
        """
        Genera muestras mediante muestreo directo
        
        Args:
            n_muestras (int): Número de muestras a generar
            
        Returns:
            list: Muestras generadas
        """
        muestras = []
        for _ in range(n_muestras):
            muestra = {}
            for nodo in self.orden:
                padres = self.red[nodo].get('padres', [])
                if not padres:  # Nodo raíz
                    prob = self.red[nodo]['prob']
                else:
                    # Obtener configuración de padres
                    key = tuple(muestra[p] for p in padres)
                    prob = self.red[nodo]['prob'][key]
                
                # Muestrear valor
                muestra[nodo] = np.random.choice(
                    self.red[nodo]['vals'], 
                    p=prob
                )
            muestras.append(muestra)
        return muestras
    
    def muestreo_rechazo(self, evidencia, n_muestras=1000):
        """
        Muestreo por rechazo dada evidencia
        
        Args:
            evidencia (dict): Valores observados {nodo: valor}
            n_muestras (int): Intentos de muestreo
            
        Returns:
            list: Muestras aceptadas
        """
        muestras_aceptadas = []
        intentos = 0
        
        while len(muestras_aceptadas) < n_muestras and intentos < 10*n_muestras:
            intentos += 1
            muestra = {}
            # Generar muestra candidata (podría optimizarse)
            for nodo in self.orden:
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
            
            # Verificar consistencia con evidencia
            aceptar = all(muestra[n] == v for n, v in evidencia.items())
            if aceptar:
                muestras_aceptadas.append(muestra)
        
        tasa_aceptacion = len(muestras_aceptadas)/intentos if intentos > 0 else 0
        print(f"Tasa de aceptación: {tasa_aceptacion:.2%}")
        return muestras_aceptadas

# ====================================
# EJEMPLO: SISTEMA DE ALARMA
# ====================================

# Definir red bayesiana (Robo -> Alarma <- Terremoto)
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
            (0,0): [0.999, 0.001],  # P(Alarma|¬Robo,¬Terremoto)
            (0,1): [0.71, 0.29],    # P(Alarma|¬Robo,Terremoto)
            (1,0): [0.06, 0.94],    # P(Alarma|Robo,¬Terremoto)
            (1,1): [0.05, 0.95]     # P(Alarma|Robo,Terremoto)
        }
    }
}

# Crear muestreador
muestreador = Muestreador(red_alarma)

# 1. Muestreo directo para estimar P(Alarma=1)
muestras = muestreador.muestreo_directo(5000)
p_alarma = sum(m['Alarma'] for m in muestras)/len(muestras)
print(f"P(Alarma=1) estimada: {p_alarma:.4f}")

# 2. Muestreo por rechazo para P(Robo=1|Alarma=1)
muestras_cond = muestreador.muestreo_rechazo({'Alarma': 1}, 1000)
if muestras_cond:
    p_robo = sum(m['Robo'] for m in muestras_cond)/len(muestras_cond)
    print(f"P(Robo=1|Alarma=1) estimada: {p_robo:.4f}")
else:
    print("No se generaron muestras válidas")

# Visualización
def plot_estimaciones(muestras, titulo):
    """Visualiza histograma de muestras"""
    plt.figure(figsize=(10, 5))
    plt.hist([m['Alarma'] for m in muestras], bins=[-0.5,0.5,1.5], density=True)
    plt.xticks([0,1], ['False', 'True'])
    plt.title(titulo)
    plt.ylabel('Densidad estimada')
    plt.show()

plot_estimaciones(muestras, "Distribución marginal de Alarma (Muestreo Directo)")