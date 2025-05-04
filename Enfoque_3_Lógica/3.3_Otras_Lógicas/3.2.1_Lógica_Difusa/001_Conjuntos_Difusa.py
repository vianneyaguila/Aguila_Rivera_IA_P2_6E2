# Definimos dos conjuntos difusos como diccionarios
A = {"bajo": 0.2, "medio": 0.7, "alto": 0.4}
B = {"bajo": 0.6, "medio": 0.3, "alto": 0.9}

# Unión (max) de A y B
def union_difusa(a, b):
    return {x: max(a[x], b[x]) for x in a}

# Intersección (min) de A y B
def interseccion_difusa(a, b):
    return {x: min(a[x], b[x]) for x in a}

# Complemento de A
def complemento_difuso(a):
    return {x: 1 - a[x] for x in a}

# Mostrar resultados
print("Conjunto A:", A)
print("Conjunto B:", B)

print("\nUnión A ∪ B:", union_difusa(A, B))
print("Intersección A ∩ B:", interseccion_difusa(A, B))
print("Complemento de A:", complemento_difuso(A))
