 # Base de conocimientos inicial
conocimiento = {
    "llueve": False,
    "tengo_paraguas": True,
    "hace_frio": True
}

# Reglas del agente lógico (condición -> acción)
reglas = [
    ("llueve and tengo_paraguas", "salir_con_paraguas"),
    ("llueve and not tengo_paraguas", "no_salir"),
    ("hace_frio", "usar_abrigo")
]

# Función de inferencia
def inferir_acciones(conocimiento, reglas):
    acciones = []

    for condicion, accion in reglas:
        # Convertimos los valores de conocimiento en variables locales
        contexto = conocimiento.copy()

        try:
            if eval(condicion, {}, contexto):
                acciones.append(accion)
        except Exception as e:
            print("Error evaluando la condición:", condicion, e)

    return acciones

# Función principal del agente lógico
def agente_logico():
    print("Percepciones iniciales:")
    for clave, valor in conocimiento.items():
        print(f"{clave} = {valor}")

    acciones = inferir_acciones(conocimiento, reglas)

    print("\nAcciones deducidas por el agente:")
    for acc in acciones:
        print(f"- {acc}")

# Ejecutar el agente
agente_logico()
