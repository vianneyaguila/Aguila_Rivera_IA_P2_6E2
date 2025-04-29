# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Cargamos un dataset de ejemplo (cáncer de mama)
data = datasets.load_breast_cancer()
X = data.data      # Características
y = data.target    # Etiquetas (0 = maligno, 1 = benigno)

# Normalizamos los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Creamos el modelo SVM con núcleo RBF (radial basis function)
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')

# Entrenamos el modelo
svm_rbf.fit(X_train, y_train)

# Realizamos predicciones
y_pred = svm_rbf.predict(X_test)

# Mostramos resultados
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))
