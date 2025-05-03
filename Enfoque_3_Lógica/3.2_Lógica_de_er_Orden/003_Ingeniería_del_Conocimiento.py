# Base de conocimiento (reglas del sistema experto)
reglas = {
    "fiebre y tos": "gripe",
    "dolor de cabeza y fiebre": "infección",
    "tos y dificultad para respirar": "asma",
    "dolor abdominal y náuseas": "intoxicación"
}

# Función para inferir diagnóstico a partir de síntomas
def inferir_diagnostico(entrada_usuario):
    for condicion, diagnostico in reglas.items():
        # Si todos los síntomas de una regla están en la entrada
        sintomas = condicion.split(" y ")
        if all(sintoma in entrada_usuario for sintoma in sintomas):
            return diagnostico
    return "No se pudo determinar un diagnóstico."

# Solicitar síntomas al usuario
print("Ingrese sus síntomas separados por comas (ej. fiebre, tos):")
entrada = input().lower()
entrada_sintomas = [s.strip() for s in entrada.split(",")]

# Inferir diagnóstico
resultado = inferir_diagnostico(entrada_sintomas)

# Mostrar resultado
print("Diagnóstico posible:", resultado)
