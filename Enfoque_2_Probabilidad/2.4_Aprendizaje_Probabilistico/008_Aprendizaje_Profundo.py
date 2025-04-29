# Importamos la librería numpy para operaciones numéricas
import numpy as np

# Definimos la función de activación (sigmoide) y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Creamos un conjunto de datos de entrada (X) y salidas esperadas (y)
# Ejemplo: aprender a reconocer el patrón OR lógico
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [1]])

# Inicializamos pesos aleatoriamente
np.random.seed(1)  # Para reproducibilidad
pesos = 2 * np.random.random((2, 1)) - 1

# Definimos el número de épocas (veces que entrenamos sobre todo el dataset)
epocas = 10000

# Entrenamiento
for i in range(epocas):
    # Propagación hacia adelante
    entrada = X
    salida = sigmoid(np.dot(entrada, pesos))
    
    # Calculamos el error
    error = y - salida
    
    # Calculamos el ajuste (delta)
    ajuste = error * sigmoid_derivative(salida)
    
    # Actualizamos los pesos
    pesos += np.dot(entrada.T, ajuste)

# Mostramos los resultados finales
print("Resultados después del entrenamiento:")
print(salida)
