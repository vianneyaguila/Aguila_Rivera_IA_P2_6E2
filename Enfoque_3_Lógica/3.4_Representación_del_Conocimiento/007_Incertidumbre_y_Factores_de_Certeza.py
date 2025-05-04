# Sistema experto simple con factores de certeza

# Diccionario de síntomas y su factor de certeza
sintomas = {
    "fiebre": 0.8,
    "tos": 0.6,
    "dolor_muscular": 0.7
}

# Reglas del sistema: qué síntomas están asociados con qué enfermedad
reglas = {
    "gripe": {
        "sintomas": ["fiebre", "tos", "dolor_muscular"],
        "factor_base": 0.9  # Qué tan fuerte es esta regla
    }
}

# Función para calcular el factor de certeza combinado
def calcular_fc(enfermedad):
    datos = reglas[enfermedad]
    sintomas_regla = datos["sintomas"]
    fc_base = datos["factor_base"]
    
    # Se usa el mínimo FC de los síntomas presentes
    fc_sintomas = [sintomas[s] for s in sintomas_regla if s in sintomas]
    
    if not fc_sintomas:
        return 0.0
    
    fc_comb = min(fc_sintomas) * fc_base
    return round(fc_comb, 2)

# Interacción
enfermedad = "gripe"
fc = calcular_fc(enfermedad)

print(f"Factor de certeza para {enfermedad}: {fc}")
if fc > 0.7:
    print("Diagnóstico probable.")
elif fc > 0.4:
    print("Diagnóstico posible.")
else:
    print("Diagnóstico poco probable.")
