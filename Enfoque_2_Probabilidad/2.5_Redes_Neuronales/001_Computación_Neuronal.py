import numpy as np
import matplotlib.pyplot as plt

# Función sigmoide: convierte valores en probabilidades (entre 0 y 1)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la sigmoide: necesaria para ajustar pesos
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada (XOR)
entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

# Salidas esperadas para XOR (0, 1, 1, 0)
salidas = np.array([[0], [1], [1], [0]])

# Inicialización aleatoria de pesos y sesgos
np.random.seed(42)
pesos = 2 * np.random.random((2, 1)) - 1
sesgo = np.random.random()

# Tasa de aprendizaje
alpha = 0.5

# Entrenamiento de la red
for i in range(10000):
    # Propagación hacia adelante
    entrada_neta = np.dot(entradas, pesos) + sesgo
    salida_predicha = sigmoid(entrada_neta)

    # Cálculo del error
    error = salidas - salida_predicha

    # Ajuste de pesos usando retropropagación
    ajustes = alpha * np.dot(entradas.T, error * sigmoid_derivative(salida_predicha))
    pesos += ajustes
    sesgo += alpha * np.sum(error * sigmoid_derivative(salida_predicha))

# Mostrar resultados finales
print("Salidas predichas después del entrenamiento:")
print(np.round(salida_predicha, 2))
