# Diccionario con palabras ambiguas y sus posibles significados
significados = {
    'banco': ['asiento para sentarse', 'institución financiera'],
    'bateria': ['instrumento musical', 'fuente de energía'],
    'ratón': ['animal', 'dispositivo de computadora']
}

def detectar_ambiguedad(oracion, diccionario):
    """
    Detecta si la oración contiene palabras ambiguas y muestra sus posibles significados.
    :param oracion: texto ingresado por el usuario
    :param diccionario: palabras ambiguas con significados
    :return: resultados de ambigüedad encontrados
    """
    palabras = oracion.lower().split()
    ambiguas = {}

    for palabra in palabras:
        if palabra in diccionario:
            ambiguas[palabra] = diccionario[palabra]

    return ambiguas

# Interacción con el usuario
if __name__ == "__main__":
    entrada = input("Escribe una oración: ")
    resultado = detectar_ambiguedad(entrada, significados)

    if resultado:
        print("\n⚠️ Palabras ambiguas encontradas:")
        for palabra, sentidos in resultado.items():
            print(f" - '{palabra}' puede significar:")
            for s in sentidos:
                print(f"   • {s}")
    else:
        print("✅ No se detectaron ambigüedades léxicas.")
