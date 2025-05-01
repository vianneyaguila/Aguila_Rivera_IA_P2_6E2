from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Generar un conjunto de datos no lineal (forma de media luna)
X, y = make_moons(n_samples=300, noise=0.2, random_state=42)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo MLP
# hidden_layer_sizes=(10, 5): dos capas ocultas con 10 y 5 neuronas
mlp = MLPClassifier(hidden_layer_sizes=(10, 5), activation='relu', solver='adam', max_iter=1000, random_state=1)

# Entrenar el modelo
mlp.fit(X_train, y_train)

# Evaluar el modelo
y_pred = mlp.predict(X_test)
print("=== Informe de Clasificación ===")
print(classification_report(y_test, y_pred))

# Graficar resultados
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k')
plt.title("Predicciones del MLP en Datos de Prueba")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()
