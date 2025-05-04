import math
from collections import Counter

# Función para calcular entropía
def calcular_entropia(datos):
    etiquetas = [fila[-1] for fila in datos]
    contador = Counter(etiquetas)
    total = len(datos)
    entropia = 0
    for freq in contador.values():
        p = freq / total
        entropia -= p * math.log2(p)
    return entropia

# Función para dividir datos según un atributo
def dividir_datos(datos, indice_atributo, valor):
    return [fila for fila in datos if fila[indice_atributo] == valor]

# ID3 - construir el árbol de decisión
def id3(datos, atributos, etiquetas_atributos):
    etiquetas = [fila[-1] for fila in datos]
    if len(set(etiquetas)) == 1:
        return etiquetas[0]  # Caso base: todas las etiquetas iguales

    if not atributos:
        return Counter(etiquetas).most_common(1)[0][0]  # mayoría

    entropia_base = calcular_entropia(datos)
    mejor_ganancia = -1
    mejor_atributo = None

    for i in atributos:
        valores = set([fila[i] for fila in datos])
        entropia_condicional = 0
        for v in valores:
            subconjunto = dividir_datos(datos, i, v)
            p = len(subconjunto) / len(datos)
            entropia_condicional += p * calcular_entropia(subconjunto)
        ganancia = entropia_base - entropia_condicional

        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_atributo = i

    if mejor_atributo is None:
        return Counter(etiquetas).most_common(1)[0][0]

    arbol = {etiquetas_atributos[mejor_atributo]: {}}
    valores = set([fila[mejor_atributo] for fila in datos])
    nuevos_atributos = [i for i in atributos if i != mejor_atributo]

    for v in valores:
        subconjunto = dividir_datos(datos, mejor_atributo, v)
        arbol[etiquetas_atributos[mejor_atributo]][v] = id3(
            subconjunto, nuevos_atributos, etiquetas_atributos)

    return arbol

# Ejemplo de datos (juego de tenis)
datos = [
    ["soleado", "calor", "alta", "falso", "no"],
    ["soleado", "calor", "alta", "verdadero", "no"],
    ["nublado", "calor", "alta", "falso", "sí"],
    ["lluvioso", "templado", "alta", "falso", "sí"],
    ["lluvioso", "frío", "normal", "falso", "sí"],
    ["lluvioso", "frío", "normal", "verdadero", "no"],
    ["nublado", "frío", "normal", "verdadero", "sí"],
    ["soleado", "templado", "alta", "falso", "no"],
    ["soleado", "frío", "normal", "falso", "sí"],
]

etiquetas_atributos = ["clima", "temperatura", "humedad", "viento"]
atributos = list(range(len(etiquetas_atributos)))

# Construimos el árbol
arbol = id3(datos, atributos, etiquetas_atributos)

# Mostrar el árbol generado
import pprint
pprint.pprint(arbol)
