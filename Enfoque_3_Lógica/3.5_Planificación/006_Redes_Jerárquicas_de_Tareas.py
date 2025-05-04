# HTN simple en Python: Red jerárquica de tareas

# Diccionario que define cómo descomponer tareas abstractas
metodos = {
    "PrepararViaje": ["Empacar", "ComprarBoletos", "ReservarHotel"],
    "Empacar": ["HacerMaleta", "EmpacarRopa"],
    "ComprarBoletos": ["BuscarVuelos", "PagarVuelo"]
}

# Tareas primitivas que no se descomponen más
tareas_primitivas = {"HacerMaleta", "EmpacarRopa", "BuscarVuelos", "PagarVuelo", "ReservarHotel"}

# Plan resultante
plan = []

# Función recursiva que descompone tareas
def planificar(tarea):
    if tarea in tareas_primitivas:
        plan.append(tarea)  # Es una acción que se puede ejecutar
    elif tarea in metodos:
        for subtarea in metodos[tarea]:
            planificar(subtarea)
    else:
        print(f"⚠️ Tarea desconocida: {tarea}")

# Ejecutar planificación para la tarea principal
planificar("PrepararViaje")

# Mostrar plan generado
print("🧳 Plan generado:")
for paso in plan:
    print(" -", paso)
