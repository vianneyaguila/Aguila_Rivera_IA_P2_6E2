import numpy as np
import matplotlib.pyplot as plt

def distribucion_objetivo(x):
    """Distribución objetivo: mezcla de dos Gaussianas"""
    return 0.6 * np.exp(-0.5 * ((x - 1)/0.5)**2) + \
           0.4 * np.exp(-0.5 * ((x + 1)/0.8)**2)

def metropolis_hastings(n_iteraciones, x_inicial, propuesta_std):
    """
    Algoritmo de Metropolis-Hastings
    
    Args:
        n_iteraciones (int): Número de muestras a generar
        x_inicial (float): Valor inicial
        propuesta_std (float): Desviación estándar de la propuesta Gaussiana
        
    Returns:
        np.array: Cadena de Markov de muestras
    """
    cadena = [x_inicial]
    x_actual = x_inicial
    
    for _ in range(n_iteraciones):
        # Generar propuesta
        x_propuesto = np.random.normal(x_actual, propuesta_std)
        
        # Calcular razón de aceptación
        ratio = distribucion_objetivo(x_propuesto) / distribucion_objetivo(x_actual)
        probabilidad_aceptacion = min(1, ratio)
        
        # Aceptar o rechazar
        if np.random.rand() < probabilidad_aceptacion:
            x_actual = x_propuesto
        cadena.append(x_actual)
    
    return np.array(cadena)

# Parámetros del algoritmo
n_muestras = 10000
x_inicial = 0.0
propuesta_std = 1.0

# Ejecutar MCMC
muestras = metropolis_hastings(n_muestras, x_inicial, propuesta_std)

# Visualización
plt.figure(figsize=(12, 5))

# Trayectoria de la cadena
plt.subplot(1, 2, 1)
plt.plot(muestras[:1000], alpha=0.6)
plt.title("Primeras 1000 iteraciones de la cadena")
plt.xlabel("Iteración")
plt.ylabel("Valor de x")

# Histograma vs distribución teórica
plt.subplot(1, 2, 2)
x = np.linspace(-4, 4, 1000)
plt.plot(x, distribucion_objetivo(x), 'r-', label='Distribución Objetivo')
plt.hist(muestras[500:], bins=50, density=True, alpha=0.6, label='Muestras MCMC')
plt.title("Distribución de las muestras")
plt.legend()
plt.show()