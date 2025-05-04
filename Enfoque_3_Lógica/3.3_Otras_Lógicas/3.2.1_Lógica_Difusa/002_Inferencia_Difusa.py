# Definimos funciones de pertenencia manualmente
def temperatura_baja(temp):
    if temp <= 15:
        return 1.0
    elif 15 < temp < 25:
        return (25 - temp) / 10
    else:
        return 0.0

def temperatura_alta(temp):
    if temp >= 30:
        return 1.0
    elif 20 < temp < 30:
        return (temp - 20) / 10
    else:
        return 0.0

# Inferencia difusa con dos reglas simples
def inferencia_difusa(temp):
    bajo = temperatura_baja(temp)
    alto = temperatura_alta(temp)

    # Reglas:
    # Si la temperatura es baja, velocidad del ventilador es lenta (valor bajo)
    # Si la temperatura es alta, velocidad del ventilador es rápida (valor alto)

    # Salida difusa (promedio ponderado)
    velocidad = (bajo * 20 + alto * 80) / (bajo + alto) if (bajo + alto) != 0 else 50

    return velocidad

# Interacción con el usuario
if __name__ == "__main__":
    temp = float(input("Ingresa la temperatura actual (°C): "))
    velocidad_resultado = inferencia_difusa(temp)
    print(f"Velocidad del ventilador sugerida: {velocidad_resultado:.2f} %")
