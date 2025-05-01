import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Crear datos linealmente separables
X1, y1 = make_classification(n_samples=100, n_features=2, n_redundant=0,
                             n_informative=2, n_clusters_per_class=1, class_sep=2.0, random_state=1)

# Crear datos NO linealmente separables
X2, y2 = make_classification(n_samples=100, n_features=2, n_redundant=0,
                             n_informative=2, n_clusters_per_class=1, class_sep=0.5, random_state=1)

# Función para graficar los puntos
def plot_data(X, y, title):
    plt.figure(figsize=(6, 5))
    plt.scatter(X[y==0][:, 0], X[y==0][:, 1], color='red', label='Clase 0')
    plt.scatter(X[y==1][:, 0], X[y==1][:, 1], color='blue', label='Clase 1')
    plt.title(title)
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.legend()
    plt.grid(True)
    plt.show()

# Mostrar ambos casos
plot_data(X1, y1, "Datos Linealmente Separables")
plot_data(X2, y2, "Datos NO Linealmente Separables")
