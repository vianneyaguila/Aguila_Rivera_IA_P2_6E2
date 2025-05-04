# Definimos una clase base para todos los conceptos
class Concepto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = {}

    def agregar_propiedad(self, clave, valor):
        self.propiedades[clave] = valor

    def obtener_propiedad(self, clave):
        return self.propiedades.get(clave, "Desconocido")

# Clases específicas que heredan de Concepto
class Animal(Concepto):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.agregar_propiedad("es_ser_vivo", True)

class Ave(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.agregar_propiedad("puede_volar", True)

class Pez(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.agregar_propiedad("vive_en_agua", True)

# Inferencia básica sobre la ontología
def razonamiento(animal):
    print(f"\nInformación sobre: {animal.nombre}")
    print("¿Es ser vivo?", animal.obtener_propiedad("es_ser_vivo"))
    print("¿Puede volar?", animal.obtener_propiedad("puede_volar"))
    print("¿Vive en agua?", animal.obtener_propiedad("vive_en_agua"))

# Ejecución
if __name__ == "__main__":
    pajaro = Ave("Canario")
    pez = Pez("Salmón")
    animal_generico = Animal("Criatura")

    razonamiento(pajaro)
    razonamiento(pez)
    razonamiento(animal_generico)
