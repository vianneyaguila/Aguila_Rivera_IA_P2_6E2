# Importar librerías
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Cargar el dataset de dígitos manuscritos
digitos = load_digits()

# Separar datos e imágenes
X = digitos.data       # Características (imágenes aplanadas)
y = digitos.target     # Etiquetas (número real)

# Separar en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar un modelo de regresión logística
modelo = LogisticRegression(max_iter=2000)
modelo.fit(X_entrenamiento, y_entrenamiento)

# Probar el modelo con una imagen
index = 5  # Puedes cambiar este número para probar otra imagen
imagen = X_prueba[index]
etiqueta_real = y_prueba[index]
prediccion = modelo.predict([imagen])

# Mostrar resultados
plt.gray()
plt.matshow(digitos.images[index])
plt.title(f'Real: {etiqueta_real} / Predicción: {prediccion[0]}')
plt.show()
