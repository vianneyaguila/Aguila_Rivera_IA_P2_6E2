import numpy as np

# Definimos los estados posibles
estados = ['Soleado', 'Lluvioso']

# Probabilidades iniciales de los estados
prob_inicial = {'Soleado': 0.6, 'Lluvioso': 0.4}

# Matriz de transición: probabilidad de pasar de un estado a otro
matriz_transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Matriz de observación: probabilidad de ver una evidencia dado un estado
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

def filtrado(observaciones):
    """
    Realiza el filtrado: actualiza la creencia del estado a medida que llegan observaciones.
    """
    estado_actual = prob_inicial.copy()
    creencias = []  # Guardamos las creencias en cada tiempo

    for i, obs in enumerate(observaciones):
        nueva_prob = {}
        for estado in estados:
            # Paso 1: calcular la probabilidad basada en transición
            suma = sum(estado_actual[prev_estado] * matriz_transicion[prev_estado][estado] for prev_estado in estados)
            # Paso 2: multiplicar por la probabilidad de observación
            nueva_prob[estado] = matriz_observacion[estado][obs] * suma

        # Normalizar
        estado_actual = normalizar(nueva_prob)
        creencias.append(estado_actual.copy())

        print(f"[Filtrado] Después de observar '{obs}', la creencia es: {estado_actual}")

    return creencias

def prediccion(creencia_actual, pasos):
    """
    Realiza predicción: estima la creencia futura sin observaciones nuevas.
    """
    estado_predicho = creencia_actual.copy()

    for paso in range(pasos):
        nueva_prob = {}
        for estado in estados:
            suma = sum(estado_predicho[prev_estado] * matriz_transicion[prev_estado][estado] for prev_estado in estados)
            nueva_prob[estado] = suma

        # Normalizamos aunque no es estrictamente necesario si las matrices son correctas
        estado_predicho = normalizar(nueva_prob)

        print(f"[Predicción] Después de {paso + 1} pasos, la creencia es: {estado_predicho}")

    return estado_predicho

def suavizado(creencias_filtrado, observaciones):
    """
    Realiza suavizado: ajusta las creencias pasadas usando información futura.
    """
    T = len(observaciones)
    futuros = [dict.fromkeys(estados, 1.0)]  # Inicializamos hacia el futuro (todo 1)

    # Vamos hacia atrás desde el final
    for t in range(T - 1, 0, -1):
        futuro_t = {}
        for estado in estados:
            suma = sum(
                matriz_transicion[estado][siguiente_estado] *
                matriz_observacion[siguiente_estado][observaciones[t]] *
                futuros[0][siguiente_estado]
                for siguiente_estado in estados
            )
            futuro_t[estado] = suma

        # Normalizamos y agregamos al principio de la lista
        futuros.insert(0, normalizar(futuro_t))

    # Combinamos creencias filtradas y futuros
    creencias_suavizadas = []
    for t in range(T):
        suavizada = {}
        for estado in estados:
            suavizada[estado] = creencias_filtrado[t][estado] * futuros[t][estado]
        creencias_suavizadas.append(normalizar(suavizada))

        print(f"[Suavizado] En el tiempo {t+1}, la creencia suavizada es: {creencias_suavizadas[-1]}")

    return creencias_suavizadas

# ----- EJECUCIÓN -----

# Lista de observaciones
observaciones = ['Calor', 'Frio', 'Frio']

# Filtrado
creencias_filtrado = filtrado(observaciones)

# Predicción (2 pasos hacia adelante después de la última observación)
creencia_final = creencias_filtrado[-1]
prediccion(creencia_final, 2)

# Suavizado
suavizado(creencias_filtrado, observaciones)
