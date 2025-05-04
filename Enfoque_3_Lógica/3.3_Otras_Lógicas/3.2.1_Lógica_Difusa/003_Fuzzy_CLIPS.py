# Definimos funciones de pertenencia para el conjunto difuso "temperatura"
def temperatura_frio(t):
    if t <= 15:
        return 1.0
    elif 15 < t < 25:
        return (25 - t) / 10
    else:
        return 0.0

def temperatura_calor(t):
    if t >= 30:
        return 1.0
    elif 20 < t < 30:
        return (t - 20) / 10
    else:
        return 0.0

# Reglas tipo "Fuzzy CLIPS" implementadas en Python
def fuzzy_rules(temp):
    frio = temperatura_frio(temp)
    calor = temperatura_calor(temp)

    # Reglas:
    # SI temperatura ES frio -> ventilador lento (20%)
    # SI temperatura ES calor -> ventilador rápido (80%)
    # Promedio ponderado difuso

    if frio + calor == 0:
        return 50  # Valor neutro si no hay pertenencia

    velocidad = (frio * 20 + calor * 80) / (frio + calor)
    return velocidad

# Interfaz con el usuario
if __name__ == "__main__":
    try:
        temp = float(input("Ingrese la temperatura actual en °C: "))
        vel = fuzzy_rules(temp)
        print(f"Velocidad recomendada del ventilador: {vel:.2f}%")
    except ValueError:
        print("Por favor, ingrese un número válido.")
