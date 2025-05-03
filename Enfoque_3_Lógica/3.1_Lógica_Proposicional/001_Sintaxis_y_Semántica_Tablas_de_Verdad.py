import itertools

# Evaluador de expresiones lógicas usando tablas de verdad
def tabla_de_verdad(expresion, variables):
    # Obtener todas las combinaciones posibles de valores de verdad
    combinaciones = list(itertools.product([False, True], repeat=len(variables)))
    
    # Imprimir encabezado
    print(" | ".join(variables) + " | Resultado")
    print("-" * (len(variables) * 6 + 12))
    
    # Evaluar la expresión para cada combinación
    for valores in combinaciones:
        contexto = dict(zip(variables, valores))  # Empareja variables con sus valores
        resultado = eval(expresion, {}, contexto)  # Evalúa la expresión en ese contexto
        valores_str = " | ".join(['V' if v else 'F' for v in valores])
        print(f"{valores_str} |    {'V' if resultado else 'F'}")

# Variables lógicas a usar
variables = ['p', 'q']
# Expresión lógica usando operadores de Python: and, or, not
expresion = "(p and q) or (not p)"

# Llamamos a la función
tabla_de_verdad(expresion, variables)
