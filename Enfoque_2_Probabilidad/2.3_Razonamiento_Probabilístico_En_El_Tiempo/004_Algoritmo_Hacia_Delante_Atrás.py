import numpy as np

# Definimos los estados ocultos
estados = ['Soleado', 'Lluvioso']

# Definimos las probabilidades iniciales
prob_inicial = {'Soleado': 0.6, 'Lluvioso': 0.4}

# Definimos la matriz de transición de estados
matriz_transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Definimos la matriz de observación
matriz_observacion = {
    'Soleado': {'Calor': 0.8, 'Frio': 0.2},
    'Lluvioso': {'Calor': 0.3, 'Frio': 0.7}
}

def normalizar(distribucion):
    """
    Normaliza un diccionario de probabilidades para que sumen 1.
    """
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}

def adelante(observaciones):
    """
    Fase hacia adelante: calcula probabilidad hasta cada paso.
    """
    alpha = []  # Lista que guarda las creencias en cada tiempo
    estado_actual = {}

    # Primer paso: usar la probabilidad inicial
    for estado in estados:
        estado_actual[estado] = prob_inicial[estado] * matriz_observacion[estado][observaciones[0]]

    estado_actual = normalizar(estado_actual)
    alpha.append(estado_actual)

    # Pasos siguientes
    for t in range(1, len(observaciones)):
        nuevo_estado = {}
        for estado in estados:
            suma = sum(alpha[t-1][prev_estado] * matriz_transicion[prev_estado][estado] for prev_estado in estados)
            nuevo_estado[estado] = matriz_observacion[estado][observaciones[t]] * suma

        nuevo_estado = normalizar(nuevo_estado)
        alpha.append(nuevo_estado)

    return alpha

def atras(observaciones):
    """
    Fase hacia atrás: calcula probabilidad de evidencias futuras.
    """
    beta = []  # Lista que guarda la información hacia atrás
    estado_actual = dict.fromkeys(estados, 1.0)  # Inicializamos en 1

    beta.insert(0, estado_actual)

    for t in range(len(observaciones) - 1, 0, -1):
        nuevo_estado = {}
        for estado in estados:
            suma = sum(
                matriz_transicion[estado][siguiente_estado] *
                matriz_observacion[siguiente_estado][observaciones[t]] *
                beta[0][siguiente_estado]
                for siguiente_estado in estados
            )
            nuevo_estado[estado] = suma

        nuevo_estado = normalizar(nuevo_estado)
        beta.insert(0, nuevo_estado)

    return beta

def adelante_atras(observaciones):
    """
    Algoritmo hacia adelante-atrás: combina fase adelante y atrás.
    """
    alpha = adelante(observaciones)
    beta = atras(observaciones)

    suavizado = []
    for t in range(len(observaciones)):
        estado_t = {}
        for estado in estados:
            estado_t[estado] = alpha[t][estado] * beta[t][estado]
        suavizado.append(normalizar(estado_t))

        print(f"[Adelante-Atrás] Tiempo {t+1}, Creencia suavizada: {suavizado[-1]}")

    return suavizado

# ----- EJECUCIÓN -----
observaciones = ['Calor', 'Frio', 'Frio']
adelante_atras(observaciones)
