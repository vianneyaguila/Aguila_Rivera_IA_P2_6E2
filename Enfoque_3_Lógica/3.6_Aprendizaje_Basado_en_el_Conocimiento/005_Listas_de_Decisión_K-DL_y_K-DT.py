# Lista de decisión simple (K-Decision List)
# Cada tupla contiene: (condición lambda, resultado)
decision_list = [
    (lambda x: x['edad'] < 18, "menor de edad"),
    (lambda x: x['edad'] < 60, "adulto"),
    (lambda x: True, "adulto mayor")  # por defecto
]

# Función que evalúa la lista sobre una entrada
def clasificar(instancia):
    for regla, resultado in decision_list:
        if regla(instancia):  # si se cumple la condición
            return resultado
    return "desconocido"

# Ejemplo de uso
entrada = {'edad': 72}
print(f"Resultado: {clasificar(entrada)}")
