# Base de conocimiento: hechos observados
hechos_observados = ["no_enciende", "bateria_nueva"]

# Reglas de diagnóstico (diagnóstico inverso)
def diagnosticar(hechos):
    posibles_causas = []

    # Reglas causales representadas como condiciones lógicas
    if "no_enciende" in hechos and "bateria_nueva" in hechos:
        posibles_causas.append("problema_motor")

    if "no_enciende" in hechos and "luces_debilitadas" in hechos:
        posibles_causas.append("bateria_descargada")

    if "frenos_no_responden" in hechos:
        posibles_causas.append("frenos_fallando")

    if "humo_motor" in hechos:
        posibles_causas.append("sobrecalentamiento")

    if not posibles_causas:
        posibles_causas.append("diagnóstico_desconocido")

    return posibles_causas

# Diagnóstico basado en los hechos ingresados
resultado = diagnosticar(hechos_observados)

# Mostrar el resultado
print("Posibles causas del problema:")
for causa in resultado:
    print("- " + causa)
