import numpy as np
import matplotlib.pyplot as plt

# Parámetros para la distribución normal
media_x = 0     # Centro en el eje X
media_y = 0     # Centro en el eje Y
desviacion = 1  # Desviación estándar (dispersión de los puntos)
num_puntos = 500  # Número de puntos a generar

# Generar coordenadas X e Y aleatorias con distribución normal
x = np.random.normal(loc=media_x, scale=desviacion, size=num_puntos)
y = np.random.normal(loc=media_y, scale=desviacion, size=num_puntos)

# Crear un gráfico de dispersión
plt.figure(figsize=(6, 6))
plt.scatter(x, y, alpha=0.6, color='blue', label='Puntos simulados')
plt.title('Simulación de Partículas en Distribución Normal')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
