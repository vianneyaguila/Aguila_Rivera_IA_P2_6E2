import random

# Simulamos un entorno incierto: ¿dónde están las llaves?
ubicacion_llaves = random.choice(["cajon", "mochila"])

# Plan condicional del agente
def plan_condicional():
    print("🔍 Buscando llaves para abrir la puerta...")

    # Acción de observar el cajón
    print("🧭 Revisando el cajón...")
    if ubicacion_llaves == "cajon":
        print("✅ Encontré las llaves en el cajón.")
        abrir_puerta()
    else:
        print("❌ No hay llaves en el cajón. Revisando la mochila...")
        if ubicacion_llaves == "mochila":
            print("✅ Encontré las llaves en la mochila.")
            abrir_puerta()
        else:
            print("🚫 No encontré las llaves en ningún lugar.")

# Acción final
def abrir_puerta():
    print("🚪 Usando las llaves para abrir la puerta... ¡Hecho!")

# Ejecutamos el plan
plan_condicional()
