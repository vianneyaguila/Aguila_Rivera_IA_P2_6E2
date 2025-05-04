# Sistema lógico que diagnostica fiebre y da una explicación

def diagnosticar(paciente):
    # Información relevante: temperatura corporal
    temperatura = paciente['temperatura']
    
    # Reglas lógicas
    if temperatura > 38:
        explicacion = f"Se detectó fiebre porque la temperatura ({temperatura}°C) es mayor a 38°C."
        return "Fiebre", explicacion
    else:
        explicacion = f"No se detectó fiebre porque la temperatura ({temperatura}°C) está dentro del rango normal."
        return "No fiebre", explicacion

# Ejemplo de entrada
paciente1 = {'nombre': 'Luis', 'temperatura': 39.2}
paciente2 = {'nombre': 'Ana', 'temperatura': 36.7}

# Diagnóstico con explicación
diagnostico1, razon1 = diagnosticar(paciente1)
diagnostico2, razon2 = diagnosticar(paciente2)

# Resultados
print(f"{paciente1['nombre']} → Diagnóstico: {diagnostico1}")
print("Explicación:", razon1)

print(f"{paciente2['nombre']} → Diagnóstico: {diagnostico2}")
print("Explicación:", razon2)
