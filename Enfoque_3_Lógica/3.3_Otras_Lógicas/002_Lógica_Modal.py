# Representa un mundo posible
class Mundo:
    def __init__(self, nombre, proposiciones):
        self.nombre = nombre
        self.proposiciones = proposiciones  # proposiciones verdaderas en este mundo
        self.accesibles = []  # mundos que son accesibles desde este

    def agregar_accesible(self, otro_mundo):
        self.accesibles.append(otro_mundo)

# Operador ◻ (necesariamente): la proposición debe ser verdadera en todos los mundos accesibles
def necesariamente(mundo_actual, proposicion):
    for mundo in mundo_actual.accesibles:
        if proposicion not in mundo.proposiciones:
            return False
    return True

# Operador ◇ (posiblemente): basta que sea verdadera en al menos un mundo accesible
def posiblemente(mundo_actual, proposicion):
    for mundo in mundo_actual.accesibles:
        if proposicion in mundo.proposiciones:
            return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos mundos con proposiciones verdaderas
    mundo1 = Mundo("M1", ["p", "q"])
    mundo2 = Mundo("M2", ["p"])
    mundo3 = Mundo("M3", ["q"])

    # Definimos accesibilidad
    mundo1.agregar_accesible(mundo2)
    mundo1.agregar_accesible(mundo3)

    # Usuario elige una proposición
    proposicion = input("Ingrese una proposición (por ejemplo: p, q): ")

    # Evaluamos en el mundo1
    print(f"En el mundo {mundo1.nombre}...")
    if necesariamente(mundo1, proposicion):
        print(f"◻️ La proposición '{proposicion}' es necesariamente verdadera.")
    else:
        print(f"❌ La proposición '{proposicion}' NO es necesariamente verdadera.")

    if posiblemente(mundo1, proposicion):
        print(f"◇ La proposición '{proposicion}' es posiblemente verdadera.")
    else:
        print(f"❌ La proposición '{proposicion}' NO es posiblemente verdadera.")
