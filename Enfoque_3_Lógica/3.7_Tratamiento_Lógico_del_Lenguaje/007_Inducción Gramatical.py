# Ejemplos positivos (lenguaje válido)
ejemplos_positivos = ["ab", "aabb", "aaabbb", "aaaabbbb"]

def inducir_gramatica(ejemplos):
    """
    Intenta inducir una regla simple tipo a^n b^n a partir de los ejemplos dados.
    """
    reglas = []
    for cadena in ejemplos:
        # Verifica si la cadena solo contiene 'a's seguidas de 'b's
        a_count = 0
        b_count = 0
        i = 0
        while i < len(cadena) and cadena[i] == 'a':
            a_count += 1
            i += 1
        while i < len(cadena) and cadena[i] == 'b':
            b_count += 1
            i += 1

        if i == len(cadena) and a_count == b_count and a_count > 0:
            reglas.append(f"S -> {'a ' * a_count} {'b ' * b_count}")
        else:
            reglas.append(f"# No válida: {cadena}")
    return reglas

# Interacción con el usuario
if __name__ == "__main__":
    print("📘 Inducción de gramática para lenguaje a^n b^n")
    resultados = inducir_gramatica(ejemplos_positivos)
    
    for idx, r in enumerate(resultados):
        print(f"Ejemplo {idx + 1}: {r}")
