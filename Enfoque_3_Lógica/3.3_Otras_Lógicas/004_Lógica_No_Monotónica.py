# Conjunto de hechos
hechos = {
    "es_pajaro": True,
    "es_pingüino": False  # Cambia esto a True para ver cómo cambia la inferencia
}

# Función que simula una regla por defecto (no monotónica)
def puede_volar(hechos):
    if hechos.get("es_pingüino", False):
        return False  # Excepción: los pingüinos no vuelan
    elif hechos.get("es_pajaro", False):
        return True  # Por defecto, los pájaros vuelan
    else:
        return None  # No se sabe

# Mostrar resultados
if __name__ == "__main__":
    print("Inferencia no monotónica:")
    resultado = puede_volar(hechos)

    if resultado is True:
        print("→ Conclusión: Puede volar.")
    elif resultado is False:
        print("→ Conclusión: No puede volar.")
    else:
        print("→ Conclusión: No se puede determinar.")
