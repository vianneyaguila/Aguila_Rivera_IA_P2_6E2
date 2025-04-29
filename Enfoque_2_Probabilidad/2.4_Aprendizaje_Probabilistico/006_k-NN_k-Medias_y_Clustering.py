# Importamos librerías necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargamos el dataset Iris (muy común en IA)
iris = load_iris()
X = iris.data      # Datos de entrada (4 características)
y = iris.target    # Etiquetas de clase

# Escalamos los datos para mejorar el rendimiento de los algoritmos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividimos los datos en entrenamiento y prueba para k-NN
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# ==============================
# ALGORITMO k-NN
# ==============================

# Creamos un clasificador k-NN con k=3 vecinos
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el clasificador con los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizamos predicciones usando el conjunto de prueba
y_pred = knn.predict(X_test)

# Mostramos la precisión del modelo k-NN
print("Precisión del clasificador k-NN:", knn.score(X_test, y_test))

# ==============================
# ALGORITMO k-MEANS
# ==============================

# Creamos el modelo k-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Ajustamos el modelo a los datos escalados
kmeans.fit(X_scaled)

# Obtenemos las etiquetas de los clusters
labels = kmeans.labels_

# ==============================
# VISUALIZACIÓN usando solo matplotlib
# ==============================

# Creamos una figura para graficar
plt.figure(figsize=(8, 5))

# Usamos un ciclo para graficar cada cluster con diferente color
colors = ['red', 'green', 'blue']

for i in range(3):
    plt.scatter(X_scaled[labels == i, 0], X_scaled[labels == i, 1], 
                color=colors[i], label=f'Cluster {i}')

# Configuramos el gráfico
plt.title("Agrupamiento con k-Means (Iris Dataset)")
plt.xlabel("Característica 1 (escalada)")
plt.ylabel("Característica 2 (escalada)")
plt.legend()
plt.grid(True)
plt.show()
