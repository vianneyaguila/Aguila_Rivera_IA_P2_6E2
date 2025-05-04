# Base de hechos inicial
hechos = {"llueve", "nublado"}

# Reglas representadas como (condiciones, conclusión)
reglas = [
    ({"llueve"}, "mojado"),
    ({"mojado", "frío"}, "resfriado"),
    ({"nublado"}, "sin_sol")
]

# Encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos, reglas):
    nuevos = True
    while nuevos:
        nuevos = False
        for condiciones, conclusion in reglas:
            if condiciones.issubset(hechos) and conclusion not in hechos:
                hechos.add(conclusion)
                nuevos = True
                print(f"Derivado: {conclusion}")
    return hechos

# Encadenamiento hacia atrás
def encadenamiento_hacia_atras(objetivo, hechos, reglas):
    if objetivo in hechos:
        return True
    for condiciones, conclusion in reglas:
        if conclusion == objetivo:
            if all(encadenamiento_hacia_atras(c, hechos, reglas) for c in condiciones):
                return True
    return False

# Ejecución del encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
hechos_resultantes = encadenamiento_hacia_adelante(set(hechos), reglas)
print("Hechos finales:", hechos_resultantes)

# Verificación con encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
objetivo = "resfriado"
if encadenamiento_hacia_atras(objetivo, hechos, reglas):
    print(f"El objetivo '{objetivo}' se puede deducir.")
else:
    print(f"El objetivo '{objetivo}' NO se puede deducir.")
