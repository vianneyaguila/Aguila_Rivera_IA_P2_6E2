# SATPLAN Simulado sin librerías externas

# Definimos acciones como diccionarios con precondiciones y efectos
acciones = {
    "Mover_AB_0": {
        "precondiciones": {"At_A_0"},
        "efectos": {"At_B_1"}
    }
}

# Estado inicial y meta
estado_inicial = {"At_A_0"}
objetivo = {"At_B_1"}

# Función que verifica si las precondiciones están en el estado actual
def precondiciones_cumplidas(estado, precondiciones):
    return precondiciones.issubset(estado)

# Simulación del plan
estado_actual = set(estado_inicial)
plan = []

# Simulamos un paso de planificación
for nombre_accion, detalles in acciones.items():
    if precondiciones_cumplidas(estado_actual, detalles["precondiciones"]):
        estado_actual.update(detalles["efectos"])
        plan.append(nombre_accion)

# Verificamos si se cumplió el objetivo
if objetivo.issubset(estado_actual):
    print("✅ Plan encontrado:")
    for paso in plan:
        print(" -", paso)
else:
    print("❌ No se encontró un plan válido.")
