import numpy as np

# Función sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Datos de entrada (XOR simplificado)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Salidas esperadas
y = np.array([[0], [1], [1], [0]])

# Inicialización aleatoria de pesos
np.random.seed(42)
input_weights = np.random.rand(2, 3)  # 2 entradas -> 3 neuronas ocultas
hidden_weights = np.random.rand(3, 1)  # 3 ocultas -> 1 salida

# Tasa de aprendizaje
lr = 0.5

# Entrenamiento
for epoch in range(10000):
    # FORWARD
    hidden_input = np.dot(X, input_weights)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, hidden_weights)
    final_output = sigmoid(final_input)

    # Cálculo del error
    error = y - final_output

    if epoch % 1000 == 0:
        print(f"Epoch {epoch} - Error promedio: {np.mean(np.abs(error)):.4f}")

    # BACKWARD
    d_output = error * sigmoid_deriv(final_output)
    d_hidden = d_output.dot(hidden_weights.T) * sigmoid_deriv(hidden_output)

    # Actualización de pesos
    hidden_weights += hidden_output.T.dot(d_output) * lr
    input_weights += X.T.dot(d_hidden) * lr

# Resultado final
print("\nSalida final después del entrenamiento:")
print(final_output)
