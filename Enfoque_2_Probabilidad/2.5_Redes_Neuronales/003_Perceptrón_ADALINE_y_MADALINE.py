import numpy as np

# Función escalón binaria (para Perceptrón)
def step_function(x):
    return np.where(x >= 0, 1, 0)

# Perceptrón
class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                output = step_function(np.dot(xi, self.weights) + self.bias)
                error = target - output
                self.weights += self.lr * error * xi
                self.bias += self.lr * error

    def predict(self, X):
        return step_function(np.dot(X, self.weights) + self.bias)

# ADALINE
class Adaline:
    def __init__(self, lr=0.01, epochs=20):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        for _ in range(self.epochs):
            output = self.net_input(X)
            error = y - output
            self.weights += self.lr * X.T.dot(error)
            self.bias += self.lr * error.sum()

    def net_input(self, X):
        return np.dot(X, self.weights) + self.bias

    def activation(self, X):
        return self.net_input(X)  # Salida lineal

    def predict(self, X):
        return np.where(self.activation(X) >= 0.5, 1, 0)

# Datos de ejemplo: función AND
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])

# Entrenar y evaluar Perceptrón
print("== Perceptrón ==")
perceptron = Perceptron()
perceptron.fit(X, y)
print("Predicciones:", perceptron.predict(X))

# Entrenar y evaluar ADALINE
print("\n== ADALINE ==")
adaline = Adaline()
adaline.fit(X, y)
print("Predicciones:", adaline.predict(X))
