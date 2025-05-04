# Definimos una función que aplica una regla por defecto
def razonamiento_por_defecto(factores):
    # Si se sabe explícitamente que no puede volar
    if factores.get("no_vuela", False):
        return "Conclusión: No puede volar (excepción detectada)."
    # Si se sabe que es un pájaro, pero no se indica que no vuele
    elif factores.get("es_pajaro", False):
        return "Conclusión: Puede volar (por defecto)."
    # Si no hay información suficiente
    else:
        return "Conclusión: No se puede determinar."

# Entrada principal del programa
if __name__ == "__main__":
    # Diccionario de hechos. Puedes cambiar estos valores.
    hechos = {
        "es_pajaro": True,
        "no_vuela": False  # Cambiar a True para activar la excepción
    }

    print("Lógica por defecto aplicada:")
    resultado = razonamiento_por_defecto(hechos)
    print(resultado)
