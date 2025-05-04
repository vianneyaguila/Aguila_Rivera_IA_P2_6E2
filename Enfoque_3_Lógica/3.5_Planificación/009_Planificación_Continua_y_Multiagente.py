import random
import time

# Tareas globales que deben ser completadas
tareas_globales = {"A": False, "B": False, "C": False}

# Plan inicial de cada agente
plan_agente1 = ["A", "B"]
plan_agente2 = ["B", "C"]

# Simula ejecución continua y coordinación
def ejecutar_agente(nombre, plan):
    for tarea in plan:
        # Verifica si la tarea ya fue hecha por otro agente
        if tareas_globales[tarea]:
            print(f"🤖 {nombre}: La tarea {tarea} ya fue realizada. Saltando...")
            continue

        # Simula intento de realizar la tarea
        print(f"🤖 {nombre} intentando realizar: {tarea}")
        time.sleep(random.uniform(0.5, 1.5))  # Simula tiempo de ejecución

        # Probabilidad de éxito o fallo
        if random.random() < 0.8:  # 80% de éxito
            tareas_globales[tarea] = True
            print(f"✅ {nombre} completó la tarea {tarea}.")
        else:
            print(f"❌ {nombre} falló al realizar la tarea {tarea}. Reintentando más tarde...")

# Simulación de ejecución continua
print("🚀 Iniciando planificación continua y multiagente...\n")

# Agentes ejecutan en turnos (en realidad serían paralelos)
for ronda in range(3):
    print(f"\n🔁 Ronda {ronda + 1} de ejecución:")
    ejecutar_agente("Agente1", plan_agente1)
    ejecutar_agente("Agente2", plan_agente2)

print("\n🎯 Estado final de tareas:")
for tarea, completada in tareas_globales.items():
    estado = "Completada" if completada else "Pendiente"
    print(f" - {tarea}: {estado}")
