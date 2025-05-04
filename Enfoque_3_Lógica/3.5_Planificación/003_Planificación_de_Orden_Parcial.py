# Clase que representa una acción
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.effects = set(effects)

# Clase que representa el plan parcialmente ordenado
class PartialOrderPlan:
    def __init__(self):
        self.actions = []
        self.orderings = []  # tuplas (a1, a2) -> a1 antes que a2
        self.causes = []     # enlaces causales: (a1, cond, a2)

    def add_action(self, action):
        self.actions.append(action)

    def add_ordering(self, before, after):
        self.orderings.append((before, after))

    def add_causal_link(self, supporter, condition, supported):
        self.causes.append((supporter, condition, supported))
        self.add_ordering(supporter, supported)  # Enlace causa una restricción de orden

    def show_plan(self):
        print("Acciones en el plan:")
        for a in self.actions:
            print(f"- {a.name}")
        print("\nOrdenamientos necesarios:")
        for b, a in self.orderings:
            print(f"{b.name} → {a.name}")
        print("\nEnlaces causales:")
        for sup, cond, supd in self.causes:
            print(f"{sup.name} ---{cond}---> {supd.name}")

# Ejemplo: hacer café
# Acciones
hervir_agua = Action("Hervir Agua", [], ["agua_hervida"])
poner_cafe = Action("Poner Café", ["agua_hervida"], ["cafe_listo"])
servir = Action("Servir Café", ["cafe_listo"], ["taza_llena"])

# Crear plan
plan = PartialOrderPlan()
plan.add_action(hervir_agua)
plan.add_action(poner_cafe)
plan.add_action(servir)

# Establecer relaciones de causalidad y orden parcial
plan.add_causal_link(hervir_agua, "agua_hervida", poner_cafe)
plan.add_causal_link(poner_cafe, "cafe_listo", servir)

# Mostrar el plan
plan.show_plan()
