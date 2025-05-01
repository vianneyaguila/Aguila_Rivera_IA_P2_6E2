# Diccionario de probabilidades de traducción palabra a palabra
probabilidades_traduccion = {
    "hola": {"hello": 0.9, "hi": 0.1},
    "mundo": {"world": 1.0},
    "buenos": {"good": 0.8, "nice": 0.2},
    "días": {"morning": 1.0},
    "amigo": {"friend": 1.0}
}

# Frase en español a traducir
frase_entrada = "hola mundo buenos días amigo"

# Separar la frase en palabras
palabras = frase_entrada.lower().split()

# Inicializar lista para la frase traducida
traduccion = []

# Traducir palabra por palabra eligiendo la traducción más probable
for palabra in palabras:
    if palabra in probabilidades_traduccion:
        traduccion_prob = probabilidades_traduccion[palabra]
        mejor_traduccion = max(traduccion_prob, key=traduccion_prob.get)
        traduccion.append(mejor_traduccion)
    else:
        # Si no se encuentra la palabra, dejarla igual
        traduccion.append(palabra)

# Mostrar la traducción
frase_traducida = " ".join(traduccion)
print("Frase original:", frase_entrada)
print("Traducción (estimada):", frase_traducida)
