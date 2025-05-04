# Definimos una gramática regular para el lenguaje que reconoce cadenas que contienen "a" y "b"
# según las reglas:
# S -> aS | bS | ε (cadena vacía)

import re

def validar_cadena(cadena):
    """
    Esta función valida si una cadena pertenece al lenguaje definido por la gramática regular:
    S -> aS | bS | ε, es decir, cualquier combinación de 'a' y 'b' (incluyendo cadena vacía).
    """
    patron = re.compile(r'^[ab]*$')  # Expresión regular: cualquier cantidad de 'a' o 'b'
    if patron.fullmatch(cadena):
        return True
    else:
        return False

# Interacción con el usuario
if __name__ == "__main__":
    entrada = input("Introduce una cadena con letras 'a' y 'b': ")
    if validar_cadena(entrada):
        print("✅ La cadena pertenece al lenguaje definido.")
    else:
        print("❌ La cadena NO pertenece al lenguaje definido.")
