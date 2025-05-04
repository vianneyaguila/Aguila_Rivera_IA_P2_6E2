# Simulación de razonamiento por defecto y no monotónico

# Base de conocimientos
aves = {
    "loro": {"vuela": True},
    "pingüino": {"vuela": False},  # Excepción
    "avestruz": {"vuela": False},  # Excepción
    "gallina": {},  # No se especifica
    "canario": {}   # No se especifica
}

# Función para determinar si un ave puede volar
def puede_volar(ave):
    info = aves.get(ave.lower(), {})
    if "vuela" in info:
        return info["vuela"]
    else:
        # Regla por defecto: si no se sabe lo contrario, se asume que vuela
        return True

# Interacción con el usuario
nombre_ave = input("Introduce el nombre de un ave: ")
resultado = puede_volar(nombre_ave)

if resultado:
    print(f"Se asume que el {nombre_ave} puede volar.")
else:
    print(f"Se sabe que el {nombre_ave} no puede volar.")
