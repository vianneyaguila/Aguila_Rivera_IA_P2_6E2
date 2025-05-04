import numpy as np
from sklearn.linear_model import LinearRegression

# Nodo del árbol M5
class NodoM5:
    def __init__(self, profundidad=0, max_profundidad=2):
        self.atributo = None
        self.umbral = None
        self.hoja = False
        self.modelo = None
        self.izquierda = None
        self.derecha = None
        self.profundidad = profundidad
        self.max_profundidad = max_profundidad

    # Entrenamiento del árbol
    def entrenar(self, X, y):
        if self.profundidad >= self.max_profundidad or len(set(y)) == 1:
            # Si llegamos al límite o no hay variación, entrenamos regresión lineal
            self.modelo = LinearRegression()
            self.modelo.fit(X, y)
            self.hoja = True
            return

        # Elegimos el mejor atributo y umbral para dividir
        mejor_mse = float("inf")
        for atributo in range(X.shape[1]):
            umbrales = np.unique(X[:, atributo])
            for umbral in umbrales:
                izquierda = y[X[:, atributo] <= umbral]
                derecha = y[X[:, atributo] > umbral]

                if len(izquierda) == 0 or len(derecha) == 0:
                    continue

                mse = (np.var(izquierda) * len(izquierda) + np.var(derecha) * len(derecha)) / len(y)
                if mse < mejor_mse:
                    mejor_mse = mse
                    self.atributo = atributo
                    self.umbral = umbral

        if self.atributo is None:
            self.modelo = LinearRegression()
            self.modelo.fit(X, y)
            self.hoja = True
            return

        # Dividimos y entrenamos ramas recursivamente
        izquierda_idx = X[:, self.atributo] <= self.umbral
        derecha_idx = X[:, self.atributo] > self.umbral
        self.izquierda = NodoM5(self.profundidad + 1, self.max_profundidad)
        self.derecha = NodoM5(self.profundidad + 1, self.max_profundidad)
        self.izquierda.entrenar(X[izquierda_idx], y[izquierda_idx])
        self.derecha.entrenar(X[derecha_idx], y[derecha_idx])

    # Predicción
    def predecir(self, x):
        if self.hoja:
            return self.modelo.predict(x.reshape(1, -1))[0]
        if x[self.atributo] <= self.umbral:
            return self.izquierda.predecir(x)
        else:
            return self.derecha.predecir(x)

# Datos de prueba (sintéticos): X -> características, y -> variable continua
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([2.2, 2.8, 3.6, 4.5, 8.0, 8.4, 9.1, 10.0])

# Crear y entrenar el árbol
arbol = NodoM5(max_profundidad=2)
arbol.entrenar(X, y)

# Probar una predicción
nueva_instancia = np.array([4.5])
prediccion = arbol.predecir(nueva_instancia)
print(f"Predicción para {nueva_instancia[0]}: {prediccion:.2f}")
