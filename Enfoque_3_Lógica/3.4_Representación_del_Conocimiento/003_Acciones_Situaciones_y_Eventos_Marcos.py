# Clase que representa un marco general
class Marco:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.slots = {}
        self.padre = padre  # Herencia de otro marco

    # Agregar o actualizar un slot
    def agregar_slot(self, clave, valor):
        self.slots[clave] = valor

    # Obtener el valor de un slot, buscando también en el marco padre
    def obtener_slot(self, clave):
        if clave in self.slots:
            return self.slots[clave]
        elif self.padre:
            return self.padre.obtener_slot(clave)
        else:
            return None

    # Mostrar información del marco
    def mostrar(self):
        print(f"\nMarco: {self.nombre}")
        for clave, valor in self.slots.items():
            print(f"{clave}: {valor}")

# Crear un marco general para "actividad en restaurante"
marco_restaurante = Marco("Ir al restaurante")
marco_restaurante.agregar_slot("lugar", "Restaurante")
marco_restaurante.agregar_slot("actor", "Cliente")
marco_restaurante.agregar_slot("objetivo", "Comer")
marco_restaurante.agregar_slot("resultado", "Satisfacción")

# Crear un marco específico para "cena en restaurante", que hereda del anterior
marco_cena = Marco("Cena romántica", padre=marco_restaurante)
marco_cena.agregar_slot("hora", "20:00")
marco_cena.agregar_slot("compañía", "Pareja")
marco_cena.agregar_slot("ambiente", "Tranquilo")

# Mostrar marcos
marco_restaurante.mostrar()
marco_cena.mostrar()

# Acceder a slots heredados
print("\n--- Acceso a slots heredados ---")
print("Lugar de la cena:", marco_cena.obtener_slot("lugar"))  # Heredado
print("Objetivo de la cena:", marco_cena.obtener_slot("objetivo"))  # Heredado
