# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Paso 1: Generar datos artificiales
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Paso 2: Crear el modelo de K-Means
kmeans = KMeans(n_clusters=4, random_state=0)

# Paso 3: Ajustar el modelo a los datos
kmeans.fit(X)

# Paso 4: Obtener las etiquetas predichas
y_kmeans = kmeans.predict(X)

# Paso 5: Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Mostrar los centros de los clusters
centros = kmeans.cluster_centers_
plt.scatter(centros[:, 0], centros[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("Agrupamiento No Supervisado con K-Means")
plt.show()
