# Clase que representa un agente con creencias
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.creencias = {}  # Diccionario de creencias

    # Agregar o actualizar una creencia
    def actualizar_creencia(self, proposicion, valor):
        print(f"{self.nombre} ahora cree que '{proposicion}' es {valor}")
        self.creencias[proposicion] = valor

    # Consultar una creencia
    def cree(self, proposicion):
        return self.creencias.get(proposicion, None)

    # Tomar una decisión simple basada en creencias
    def decidir(self):
        if self.cree("llueve"):
            print(f"{self.nombre} decide llevar paraguas.")
        elif self.cree("soleado"):
            print(f"{self.nombre} decide usar gafas de sol.")
        else:
            print(f"{self.nombre} no sabe qué clima hace, así que se queda en casa.")

# Crear un agente
agente = Agente("Ana")

# Mostrar decisiones basadas en sus creencias
agente.decidir()

# Simular eventos que cambian sus creencias
agente.actualizar_creencia("llueve", True)
agente.decidir()

agente.actualizar_creencia("llueve", False)
agente.actualizar_creencia("soleado", True)
agente.decidir()
