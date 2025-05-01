from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos Iris (3 clases, 4 características)
data = load_iris()
X = data.data
y = data.target

# Escalar los datos (normalizar entre 0 y 1)
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Crear el SOM: 7x7 nodos, 4 entradas (dimensión), vecindad gaussiana
som = MiniSom(x=7, y=7, input_len=4, sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, 1000)  # Entrenamiento con 1000 iteraciones

# Visualización: contar cuántos puntos caen en cada nodo
frequencies = np.zeros((7, 7))
for i in range(len(X)):
    x, y_ = som.winner(X[i])
    frequencies[x, y_] += 1

# Graficar mapa de calor
plt.imshow(frequencies, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Número de muestras')
plt.title("Frecuencia de Activación por Nodo del SOM")
plt.show()
