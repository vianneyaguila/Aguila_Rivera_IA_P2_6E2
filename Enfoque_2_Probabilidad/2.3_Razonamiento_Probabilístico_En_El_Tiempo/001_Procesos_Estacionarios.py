# Importación de librerías
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf

# Parámetros del proceso
np.random.seed(42)
n = 500  # Número de observaciones
phi = 0.6  # Coeficiente AR (debe ser <1 para estacionariedad)

# Generación de proceso AR(1) estacionario
errores = np.random.normal(0, 1, n)
serie = np.zeros(n)
for t in range(1, n):
    serie[t] = phi * serie[t-1] + errores[t]

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(serie, color='blue')
plt.title('Proceso AR(1) Estacionario')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()

# Test de Dickey-Fuller Aumentado (ADF)
result = adfuller(serie)
print(f'ADF Statistic: {result[0]:.4f}')
print(f'p-value: {result[1]:.4f}')
print('Valores Críticos:')
for key, value in result[4].items():
    print(f'\t{key}: {value:.4f}')

# Función de Autocorrelación (ACF)
plot_acf(serie, lags=40, alpha=0.05)
plt.show()