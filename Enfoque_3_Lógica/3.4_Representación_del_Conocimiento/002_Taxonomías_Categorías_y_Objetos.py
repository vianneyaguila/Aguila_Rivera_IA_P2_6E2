# Clase base para categorías (clases)
class Categoria:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.propiedades = {}

    def agregar_propiedad(self, clave, valor):
        self.propiedades[clave] = valor

    def obtener_propiedad(self, clave):
        if clave in self.propiedades:
            return self.propiedades[clave]
        elif self.padre:
            return self.padre.obtener_propiedad(clave)
        else:
            return None

# Clase para objetos (instancias)
class Objeto:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def describir(self):
        print(f"\nObjeto: {self.nombre}")
        for prop in ["es_ser_vivo", "puede_volar", "tiene_pelo"]:
            valor = self.categoria.obtener_propiedad(prop)
            print(f"{prop.replace('_', ' ').capitalize()}: {valor}")

# Crear la jerarquía de categorías
animal = Categoria("Animal")
animal.agregar_propiedad("es_ser_vivo", True)

mamifero = Categoria("Mamífero", padre=animal)
mamifero.agregar_propiedad("tiene_pelo", True)

ave = Categoria("Ave", padre=animal)
ave.agregar_propiedad("puede_volar", True)

# Crear objetos
perro = Objeto("Perro", mamifero)
pingüino = Objeto("Pingüino", ave)

# Mostrar descripción
perro.describir()
pingüino.describir()
