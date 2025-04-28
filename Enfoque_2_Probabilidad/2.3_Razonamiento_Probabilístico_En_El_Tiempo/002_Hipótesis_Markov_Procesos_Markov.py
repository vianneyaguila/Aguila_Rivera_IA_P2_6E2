import random

# Definimos los estados posibles
estados = ["Soleado", "Lluvioso", "Nublado"]

# Definimos la matriz de transición
# Cada fila representa el estado actual, y las columnas representan el siguiente estado
# Los valores representan la probabilidad de pasar de un estado a otro
matriz_transicion = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.1, "Nublado": 0.1},
    "Lluvioso": {"Soleado": 0.2, "Lluvioso": 0.6, "Nublado": 0.2},
    "Nublado": {"Soleado": 0.3, "Lluvioso": 0.3, "Nublado": 0.4}
}

def siguiente_estado(estado_actual):
    """
    Dado el estado actual, elige el siguiente estado basado en las probabilidades de transición.
    """
    probabilidad = random.random()  # Genera un número aleatorio entre 0 y 1
    suma = 0
    for estado_siguiente, prob in matriz_transicion[estado_actual].items():
        suma += prob
        if probabilidad <= suma:
            return estado_siguiente

def simular_proceso_markov(estado_inicial, pasos):
    """
    Simula el proceso de Markov dado un estado inicial y número de pasos.
    """
    estado_actual = estado_inicial
    print(f"Estado inicial: {estado_actual}")
    for i in range(pasos):
        estado_actual = siguiente_estado(estado_actual)
        print(f"Paso {i+1}: {estado_actual}")

# Ejecución de la simulación
# El usuario puede cambiar el estado inicial y número de pasos si lo desea
simular_proceso_markov("Soleado", 10)
