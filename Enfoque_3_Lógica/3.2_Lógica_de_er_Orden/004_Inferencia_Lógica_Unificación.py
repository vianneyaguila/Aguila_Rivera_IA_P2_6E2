# Función de unificación básica entre dos términos
def unificar(x, y, sustituciones=None):
    if sustituciones is None:
        sustituciones = {}

    if x == y:
        return sustituciones

    # Si x es una variable
    if isinstance(x, str) and x.islower():
        return unificar_variable(x, y, sustituciones)

    # Si y es una variable
    if isinstance(y, str) and y.islower():
        return unificar_variable(y, x, sustituciones)

    # Si ambos son listas (términos complejos)
    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for xi, yi in zip(x, y):
            sustituciones = unificar(xi, yi, sustituciones)
            if sustituciones is None:
                return None
        return sustituciones

    return None  # No se puede unificar

# Función auxiliar para unificar variables
def unificar_variable(var, x, sustituciones):
    if var in sustituciones:
        return unificar(sustituciones[var], x, sustituciones)
    elif x in sustituciones:
        return unificar(var, sustituciones[x], sustituciones)
    else:
        sustituciones[var] = x
        return sustituciones

# Ejemplo de uso
termino1 = ['padre', 'X', 'Juan']
termino2 = ['padre', 'Pedro', 'Y']

resultado = unificar(termino1, termino2)

# Mostrar resultado
if resultado:
    print("Unificación exitosa. Sustituciones encontradas:")
    for k, v in resultado.items():
        print(f"{k} = {v}")
else:
    print("No se pudo unificar los términos.")
