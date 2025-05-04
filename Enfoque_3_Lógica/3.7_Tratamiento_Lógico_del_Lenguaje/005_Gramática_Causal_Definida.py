# Reglas de causalidad en forma: 'efecto': ['causa1', 'causa2']
reglas_causales = {
    'llueve': ['nubes', 'baja_presion'],
    'inundacion': ['llueve', 'desbordamiento_rio'],
    'accidente': ['lluvia', 'poca_visibilidad'],
    'corte_electrico': ['inundacion']
}

def evaluar_causalidad(hechos, reglas):
    """
    Evalúa qué efectos se pueden producir según las causas dadas.
    :param hechos: Lista de causas actuales
    :param reglas: Diccionario de reglas causa-efecto
    :return: Lista de efectos producidos
    """
    nuevos_efectos = set()
    hechos_actuales = set(hechos)
    cambiando = True

    while cambiando:
        cambiando = False
        for efecto, causas in reglas.items():
            if efecto not in hechos_actuales and all(c in hechos_actuales for c in causas):
                nuevos_efectos.add(efecto)
                hechos_actuales.add(efecto)
                cambiando = True

    return nuevos_efectos

# Interacción con el usuario
if __name__ == "__main__":
    entrada = input("Ingresa las causas separadas por coma (ej. nubes,baja_presion): ")
    causas_usuario = [c.strip() for c in entrada.lower().split(',')]

    efectos = evaluar_causalidad(causas_usuario, reglas_causales)

    if efectos:
        print("✅ Efectos derivados de tus causas:")
        for e in efectos:
            print(f" - {e}")
    else:
        print("❌ No se derivó ningún efecto con esas causas.")
