# Dominio de discurso: conjunto de personas con edades
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 32},
    {"nombre": "Sofía", "edad": 19},
    {"nombre": "Carlos", "edad": 17}
]

# Cuantificador universal: ¿Todas las personas son mayores de edad?
def cuantificador_universal(lista, predicado):
    return all(predicado(x) for x in lista)

# Cuantificador existencial: ¿Existe alguna persona menor de edad?
def cuantificador_existencial(lista, predicado):
    return any(predicado(x) for x in lista)

# Predicado: persona es mayor de edad
es_mayor_de_edad = lambda persona: persona["edad"] >= 18

# Uso de los cuantificadores
todos_mayores = cuantificador_universal(personas, es_mayor_de_edad)
alguien_menor = cuantificador_existencial(personas, lambda p: p["edad"] < 18)

# Resultados
print("¿Todas las personas son mayores de edad?", todos_mayores)
print("¿Existe alguna persona menor de edad?", alguien_menor)
