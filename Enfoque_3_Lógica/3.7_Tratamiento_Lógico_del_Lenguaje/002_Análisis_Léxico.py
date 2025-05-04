import re

# Lista de palabras clave simuladas (como si fuera un lenguaje de programación)
palabras_clave = {'if', 'else', 'while', 'return', 'int', 'float', 'print'}

def analizador_lexico(codigo):
    """
    Función que analiza léxicamente una línea de código.
    Retorna una lista de tuplas con (token, tipo)
    """
    tokens = []
    # Patrón general para separar palabras, números, operadores y paréntesis
    patron = r'[\w]+|[=+\-*/(){};]'
    partes = re.findall(patron, codigo)

    for parte in partes:
        if parte in palabras_clave:
            tokens.append((parte, "Palabra clave"))
        elif parte.isdigit():
            tokens.append((parte, "Número entero"))
        elif re.match(r'^[a-zA-Z_]\w*$', parte):
            tokens.append((parte, "Identificador"))
        elif parte in "=+-*/(){};":
            tokens.append((parte, "Símbolo"))
        else:
            tokens.append((parte, "Desconocido"))

    return tokens

# Interacción con el usuario
if __name__ == "__main__":
    linea = input("Introduce una línea de código: ")
    resultado = analizador_lexico(linea)
    print("\nTokens encontrados:")
    for token, tipo in resultado:
        print(f"{token} -> {tipo}")
