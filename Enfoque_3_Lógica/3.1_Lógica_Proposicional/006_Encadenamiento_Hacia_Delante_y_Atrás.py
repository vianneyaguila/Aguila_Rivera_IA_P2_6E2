# Base de hechos iniciales
hechos = {"llueve", "nubes"}

# Base de reglas (premisas => conclusión)
reglas = [
    ({"llueve"}, "suelo_mojado"),
    ({"nubes"}, "posibilidad_lluvia"),
    ({"suelo_mojado", "frio"}, "resbaloso"),
    ({"posibilidad_lluvia"}, "llevar_paraguas")
]

# Encadenamiento hacia adelante
def encadenamiento_adelante(hechos, reglas):
    nuevos_hechos = set(hechos)
    aplicado = True

    while aplicado:
        aplicado = False
        for premisas, conclusion in reglas:
            if premisas.issubset(nuevos_hechos) and conclusion not in nuevos_hechos:
                nuevos_hechos.add(conclusion)
                aplicado = True
    return nuevos_hechos

# Encadenamiento hacia atrás
def encadenamiento_atras(meta, hechos, reglas):
    if meta in hechos:
        return True
    for premisas, conclusion in reglas:
        if conclusion == meta:
            if all(encadenamiento_atras(p, hechos, reglas) for p in premisas):
                return True
    return False

# Pruebas
print("Encadenamiento hacia adelante:")
resultado = encadenamiento_adelante(hechos, reglas)
print("Hechos inferidos:", resultado)

print("\nEncadenamiento hacia atrás:")
meta = "llevar_paraguas"
resultado2 = encadenamiento_atras(meta, hechos, reglas)
print(f"¿Se puede inferir '{meta}'?:", resultado2)
