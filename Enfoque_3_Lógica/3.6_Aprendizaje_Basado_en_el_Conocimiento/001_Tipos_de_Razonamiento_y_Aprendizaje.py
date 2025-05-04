# Definimos la base de conocimientos con hechos iniciales
hechos = {"llueve", "nublado"}

# Definimos reglas como tuplas: (condiciones, conclusión)
reglas = [
    ({"llueve", "nublado"}, "llevar paraguas"),
    ({"sin paraguas", "llueve"}, "mojarse"),
    ({"llevar paraguas"}, "no mojarse"),
    ({"sol"}, "salir sin paraguas")
]

# Motor de inferencia
def motor_inferencia(hechos, reglas):
    nuevos_hechos = hechos.copy()
    cambios = True

    while cambios:
        cambios = False
        for condiciones, conclusion in reglas:
            if condiciones.issubset(nuevos_hechos) and conclusion not in nuevos_hechos:
                nuevos_hechos.add(conclusion)
                cambios = True  # Se produjo una deducción
                print(f"Regla aplicada: Si {condiciones} entonces {conclusion}")
    return nuevos_hechos

# Ejecutamos el motor
resultado = motor_inferencia(hechos, reglas)

# Mostramos los hechos deducidos
print("\nHechos finales:")
for hecho in resultado:
    print(f"- {hecho}")
