import numpy as np
import matplotlib.pyplot as plt

# Función Sigmoide: salida entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función Tangente Hiperbólica: salida entre -1 y 1
def tanh(x):
    return np.tanh(x)

# Función ReLU (Rectified Linear Unit): salida de 0 si x<0, y x si x>=0
def relu(x):
    return np.maximum(0, x)

# Rango de valores de entrada
x = np.linspace(-10, 10, 100)

# Aplicar funciones
y_sigmoid = sigmoid(x)
y_tanh = tanh(x)
y_relu = relu(x)

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y_sigmoid, label="Sigmoid", color='blue')
plt.plot(x, y_tanh, label="Tanh", color='red')
plt.plot(x, y_relu, label="ReLU", color='green')

plt.title("Comparación de Funciones de Activación")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
