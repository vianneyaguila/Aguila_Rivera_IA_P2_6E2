import numpy as np

def logica_difusa(temperatura, humedad):
    """
    Decide si activar el riego en un invernadero basado en reglas difusas.
    
    Parámetros:
        temperatura (float): Valor entre 0 (frío) y 40 (caliente).
        humedad (float): Valor entre 0 (seco) y 100 (húmedo).
    
    Retorna:
        str: Decisión ("Activado", "Desactivado", "Incierto").
    """
    # Funciones de pertenencia difusas (triangulares)
    def membresia_caliente(temp):
        return max(0, min((temp - 25) / 5, 1))  # 25°C a 30°C
    
    def membresia_seco(hum):
        return max(0, min((100 - hum) / 50, 1))  # 0% a 50%
    
    # Evaluar reglas difusas
    activar = min(membresia_caliente(temperatura), membresia_seco(humedad))
    desactivar = 1 - activar  # Regla complementaria
    
    # Tomar decisión
    if activar > 0.7:
        return "Activado"
    elif desactivar > 0.7:
        return "Desactivado"
    else:
        return "Incierto"

# Ejemplo de uso
temp = 28  # °C
hum = 30   # %
decision = logica_difusa(temp, hum)
print(f"Decisión de riego: {decision} (Temperatura: {temp}°C, Humedad: {hum}%)")