import random

# Plan inicial: tareas que el agente debe realizar
plan_original = ["Tarea1", "Tarea2", "Tarea3"]

# Replanificación simple: plan alternativo si ocurre un fallo
plan_alternativo = ["RevisarEstado", "TareaBackup", "Continuar"]

# Simula ejecución del plan con vigilancia y replanificación
def ejecutar_plan(plan):
    for paso in plan:
        print(f"🔄 Ejecutando: {paso}")
        # Simulamos una falla aleatoria en una tarea
        if random.random() < 0.3:  # 30% de probabilidad de fallo
            print(f"❌ Falló la ejecución de: {paso}")
            return False
        print(f"✅ {paso} completada.")
    return True

# Ejecutar y vigilar
print("🚀 Iniciando ejecución del plan...")
exito = ejecutar_plan(plan_original)

# Si falla, se replanifica
if not exito:
    print("🔁 Replanificando...")
    ejecutar_plan(plan_alternativo)
else:
    print("🎯 Plan completado sin errores.")
