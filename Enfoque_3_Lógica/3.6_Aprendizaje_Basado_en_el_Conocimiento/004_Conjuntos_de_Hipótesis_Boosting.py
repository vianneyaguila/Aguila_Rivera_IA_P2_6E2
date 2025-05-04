from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Crear un conjunto de datos de clasificación sintético
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=1)

# 2. Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Crear el modelo base (un árbol débil)
modelo_base = DecisionTreeClassifier(max_depth=1)

# 4. Crear el modelo de Boosting (AdaBoost con 50 estimadores)
modelo_boosting = AdaBoostClassifier(base_estimator=modelo_base, n_estimators=50, learning_rate=1.0, random_state=42)

# 5. Entrenar el modelo con el conjunto de entrenamiento
modelo_boosting.fit(X_train, y_train)

# 6. Predecir resultados en el conjunto de prueba
y_pred = modelo_boosting.predict(X_test)

# 7. Evaluar la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo AdaBoost: {accuracy:.2f}")
