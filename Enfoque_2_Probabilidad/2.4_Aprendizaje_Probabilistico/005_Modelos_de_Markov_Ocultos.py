# Importamos librerías necesarias
import numpy as np
from hmmlearn import hmm

# Paso 1: Definimos las observaciones (por ejemplo, 0 = "sol", 1 = "lluvia")
observaciones = np.array([[0], [1], [0], [1], [0]]).reshape(-1, 1)

# Paso 2: Creamos el modelo HMM
modelo = hmm.MultinomialHMM(n_components=2, random_state=42)

# Paso 3: Definimos manualmente los parámetros del modelo
modelo.startprob_ = np.array([0.6, 0.4])  # Probabilidad inicial de cada estado
modelo.transmat_ = np.array([
    [0.7, 0.3],  # Probabilidad de transición entre estados
    [0.4, 0.6]
])
modelo.emissionprob_ = np.array([
    [0.9, 0.1],  # Estado 0: alta probabilidad de observar "sol"
    [0.2, 0.8]   # Estado 1: alta probabilidad de observar "lluvia"
])

# Paso 4: Calculamos la secuencia de estados más probable
logprob, estados_ocultos = modelo.decode(observaciones, algorithm="viterbi")

# Paso 5: Mostramos el resultado
print("Secuencia observada:", observaciones.ravel())
print("Secuencia de estados ocultos inferida:", estados_ocultos)
