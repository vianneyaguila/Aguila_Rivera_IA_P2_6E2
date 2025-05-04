# Representación de acciones, hechos y niveles de un grafo de planificación

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.effects = set(effects)

    def __repr__(self):
        return self.name

class PlanningGraph:
    def __init__(self, initial_state, actions, goal):
        self.initial_state = set(initial_state)
        self.actions = actions
        self.goal = set(goal)
        self.fact_levels = []  # Niveles de hechos
        self.action_levels = []  # Niveles de acciones

    def expand_graph(self, max_levels=5):
        current_facts = self.initial_state
        for level in range(max_levels):
            self.fact_levels.append(current_facts)
            # Generar acciones aplicables
            applicable = [a for a in self.actions if a.preconditions.issubset(current_facts)]
            self.action_levels.append(applicable)

            # Calcular nuevos hechos
            new_facts = set(current_facts)
            for action in applicable:
                new_facts.update(action.effects)

            # Si los hechos no cambian, el grafo se ha saturado
            if new_facts == current_facts:
                break

            current_facts = new_facts

    def show_graph(self):
        print("GRAFO DE PLANIFICACIÓN")
        for i, facts in enumerate(self.fact_levels):
            print(f"\nNivel de hechos {i}: {facts}")
            if i < len(self.action_levels):
                print(f"Nivel de acciones {i}: {self.action_levels[i]}")

# Definir acciones
hervir = Action("Hervir Agua", ["agua"], ["agua_hervida"])
poner_cafe = Action("Agregar Café", ["agua_hervida", "cafe"], ["cafe_preparado"])
servir = Action("Servir Café", ["cafe_preparado", "taza"], ["taza_llena"])

# Estado inicial y objetivo
estado_inicial = ["agua", "cafe", "taza"]
objetivo = ["taza_llena"]

# Crear grafo y expandirlo
acciones = [hervir, poner_cafe, servir]
grafo = PlanningGraph(estado_inicial, acciones, objetivo)
grafo.expand_graph(max_levels=5)
grafo.show_graph()
