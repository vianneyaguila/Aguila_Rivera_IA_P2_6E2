# Sistema Experto Simple para Diagnóstico de Fallas en PC

# Reglas del sistema (reglas del conocimiento)
reglas = [
    {
        "condiciones": ["no_enciende", "cables_conectados"],
        "conclusion": "problema_fuente_poder"
    },
    {
        "condiciones": ["enciende", "no_hay_imagen"],
        "conclusion": "problema_tarjeta_video"
    },
    {
        "condiciones": ["enciende", "imagen_ok", "no_arranca_sistema"],
        "conclusion": "problema_disco_duro"
    }
]

# Preguntas al usuario para generar hechos
preguntas = {
    "no_enciende": "¿La computadora no enciende? (s/n): ",
    "cables_conectados": "¿Están los cables bien conectados? (s/n): ",
    "enciende": "¿La computadora enciende? (s/n): ",
    "no_hay_imagen": "¿No hay imagen en pantalla? (s/n): ",
    "imagen_ok": "¿Hay imagen en pantalla? (s/n): ",
    "no_arranca_sistema": "¿El sistema operativo no arranca? (s/n): "
}

# Función para obtener hechos del usuario
def obtener_hechos():
    hechos = []
    for clave, pregunta in preguntas.items():
        respuesta = input(pregunta).strip().lower()
        if respuesta == 's':
            hechos.append(clave)
    return hechos

# Motor de inferencia
def inferir(hechos):
    conclusiones = []
    for regla in reglas:
        if all(cond in hechos for cond in regla["condiciones"]):
            conclusiones.append(regla["conclusion"])
    return conclusiones

# Ejecución del sistema experto
print("=== SISTEMA EXPERTO: DIAGNÓSTICO DE PC ===")
hechos_usuario = obtener_hechos()
resultado = inferir(hechos_usuario)

if resultado:
    for conclusion in resultado:
        print(f"⚠ Posible falla detectada: {conclusion.replace('_', ' ').upper()}")
else:
    print("✅ No se pudo detectar una falla con la información proporcionada.")
