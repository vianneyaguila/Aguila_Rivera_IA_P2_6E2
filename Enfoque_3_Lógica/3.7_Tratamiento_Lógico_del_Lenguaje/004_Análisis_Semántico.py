# Análisis sintáctico de frases simples tipo: sujeto + verbo + objeto

# Listas de palabras válidas por categoría
sujetos = ['yo', 'tú', 'él', 'ella']
verbos = ['como', 'amas', 've', 'mira']
objetos = ['manzana', 'película', 'libro', 'cielo']

def analizar_oracion(oracion):
    """
    Función que analiza la estructura de una oración simple.
    Devuelve si la oración es sintácticamente válida.
    """
    palabras = oracion.lower().split()  # Separamos en palabras y pasamos a minúsculas
    if len(palabras) != 3:
        return False, "❌ La oración no tiene exactamente 3 palabras."

    sujeto, verbo, objeto = palabras

    if sujeto in sujetos and verbo in verbos and objeto in objetos:
        return True, "✅ Oración sintácticamente válida."
    else:
        return False, "❌ Estructura inválida. Revise sujeto, verbo u objeto."

# Interacción con el usuario
if __name__ == "__main__":
    entrada = input("Escribe una oración simple (sujeto verbo objeto): ")
    valido, mensaje = analizar_oracion(entrada)
    print(mensaje)
