import numpy as np
from scipy.stats import multivariate_normal

# Algoritmo EM para un modelo de mezcla de dos Gaussianas
class EM_GMM:
    def __init__(self, k, n_iter=100):
        self.k = k              # Número de componentes (clusters)
        self.n_iter = n_iter     # Número de iteraciones
        self.pesos = None        # Pesos de cada componente
        self.medias = None       # Medias de las Gaussianas
        self.covarianzas = None  # Matrices de covarianza de las Gaussianas

    def inicializar(self, X):
        """
        Inicializa los parámetros de forma aleatoria
        """
        n_muestras, n_caracteristicas = X.shape
        self.pesos = np.ones(self.k) / self.k
        self.medias = X[np.random.choice(n_muestras, self.k, False)]
        self.covarianzas = np.array([np.eye(n_caracteristicas)] * self.k)

    def ajustar(self, X):
        """
        Ejecuta el algoritmo EM sobre los datos
        """
        self.inicializar(X)

        for _ in range(self.n_iter):
            # E-step: calcular las responsabilidades
            responsabilidades = np.zeros((X.shape[0], self.k))
            for i in range(self.k):
                responsabilidades[:, i] = self.pesos[i] * multivariate_normal(
                    self.medias[i], self.covarianzas[i]
                ).pdf(X)
            responsabilidades /= responsabilidades.sum(axis=1, keepdims=True)

            # M-step: actualizar parámetros
            Nk = responsabilidades.sum(axis=0)
            self.pesos = Nk / X.shape[0]
            self.medias = (responsabilidades.T @ X) / Nk[:, np.newaxis]
            for i in range(self.k):
                x_centrada = X - self.medias[i]
                self.covarianzas[i] = (responsabilidades[:, i][:, np.newaxis] * x_centrada).T @ x_centrada
                self.covarianzas[i] /= Nk[i]

    def predecir(self, X):
        """
        Asigna cada punto al cluster más probable
        """
        responsabilidades = np.zeros((X.shape[0], self.k))
        for i in range(self.k):
            responsabilidades[:, i] = self.pesos[i] * multivariate_normal(
                self.medias[i], self.covarianzas[i]
            ).pdf(X)
        return np.argmax(responsabilidades, axis=1)

# -------------------
# PRUEBA DEL EM-GMM
# -------------------

if __name__ == "__main__":
    # Generamos datos de prueba
    np.random.seed(42)
    X1 = np.random.normal(0, 1, (100, 2))  # Cluster 1
    X2 = np.random.normal(5, 1, (100, 2))  # Cluster 2
    X = np.vstack((X1, X2))  # Unimos los datos

    # Crear modelo EM-GMM
    modelo = EM_GMM(k=2, n_iter=50)

    # Entrenar el modelo
    modelo.ajustar(X)

    # Predecir los clusters
    clusters = modelo.predecir(X)

    # Mostrar resultados
    print("Clusters asignados:", clusters)
