# Importamos la biblioteca math para usar el redondeo
import math

# Definimos las probabilidades base
P_enfermedad = 0.01  # Probabilidad de tener la enfermedad (previa)
P_sintoma_dado_enfermedad = 0.9  # Probabilidad de tener el síntoma si tienes la enfermedad
P_sintoma_dado_no_enfermedad = 0.2  # Probabilidad de tener el síntoma si no tienes la enfermedad

# Función que aplica el Teorema de Bayes
def probabilidad_enfermedad_dado_sintoma():
    # Calculamos la probabilidad total del síntoma
    P_sintoma = (P_sintoma_dado_enfermedad * P_enfermedad) + \
                (P_sintoma_dado_no_enfermedad * (1 - P_enfermedad))

    # Aplicamos el Teorema de Bayes
    P_enfermedad_dado_sintoma = (P_sintoma_dado_enfermedad * P_enfermedad) / P_sintoma

    return round(P_enfermedad_dado_sintoma, 4)

# Ejecutamos la función y mostramos el resultado
resultado = probabilidad_enfermedad_dado_sintoma()
print(f"Probabilidad de tener la enfermedad dado el síntoma: {resultado * 100:.2f}%")
