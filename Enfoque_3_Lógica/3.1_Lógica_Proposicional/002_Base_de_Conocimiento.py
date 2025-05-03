# Base de conocimiento simple con inferencia encadenada hacia adelante

# Hechos iniciales
base_de_conocimiento = {
    "es_humano(socrates)": True,
}

# Reglas de inferencia (forma simplificada)
reglas = [
    {
        "si": ["es_humano(X)"],
        "entonces": "es_mortal(X)"
    }
]

# Función para aplicar reglas sobre hechos
def inferir(bc, reglas):
    nuevos_hechos = {}
    for regla in reglas:
        for hecho in bc:
            if regla["si"][0].startswith("es_humano(") and hecho.startswith("es_humano("):
                x = hecho[10:-1]  # extrae el valor X de 'es_humano(X)'
                nuevo_hecho = regla["entonces"].replace("X", x)
                if nuevo_hecho not in bc:
                    nuevos_hechos[nuevo_hecho] = True
    return nuevos_hechos

# Aplicamos inferencia
nuevos = inferir(base_de_conocimiento, reglas)
base_de_conocimiento.update(nuevos)

# Mostramos el resultado
print("Hechos en la base de conocimiento:")
for hecho in base_de_conocimiento:
    print("-", hecho)
