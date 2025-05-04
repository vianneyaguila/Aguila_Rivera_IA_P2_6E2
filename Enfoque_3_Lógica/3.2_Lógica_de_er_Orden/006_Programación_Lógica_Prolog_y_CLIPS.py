# Base de conocimiento con hechos y reglas simuladas
hechos = {"animal(perro)", "animal(gato)", "tiene_pelo(perro)", "tiene_pelo(gato)"}

reglas = [
    ("animal(X) and tiene_pelo(X)", "mamifero(X)"),
    ("mamifero(X) and tiene_garras(X)", "felino(X)")
]

# Función para extraer variable X
def obtener_valor(variable, hecho):
    if "(" in hecho and ")" in hecho:
        predicado, valor = hecho.split("(")
        valor = valor.replace(")", "")
        if predicado == variable:
            return valor
    return None

# Simulación de inferencia hacia adelante
def inferencia_hacia_adelante(hechos, reglas):
    nuevos_hechos = set(hechos)
    derivaciones = set()

    for regla in reglas:
        condicion, conclusion = regla
        if "and" in condicion:
            pred1, pred2 = condicion.split(" and ")

            for h1 in hechos:
                for h2 in hechos:
                    if pred1.split("(")[0] in h1 and pred2.split("(")[0] in h2:
                        var1 = h1[h1.find("(")+1:h1.find(")")]
                        var2 = h2[h2.find("(")+1:h2.find(")")]
                        if var1 == var2:
                            concl_pred = conclusion.replace("X", var1)
                            if concl_pred not in nuevos_hechos:
                                nuevos_hechos.add(concl_pred)
                                derivaciones.add(concl_pred)
    
    return nuevos_hechos, derivaciones

# Ejecutar inferencia
nuevos_hechos, inferidos = inferencia_hacia_adelante(hechos, reglas)

# Mostrar resultados
print("Hechos iniciales:")
print(hechos)
print("\nNuevos hechos inferidos:")
print(inferidos)
print("\nBase de hechos final:")
print(nuevos_hechos)
