# Definimos una acción en STRIPS con precondiciones, efectos positivos y negativos
class Action:
    def __init__(self, name, preconditions, add_effects, del_effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.add_effects = set(add_effects)
        self.del_effects = set(del_effects)

    def is_applicable(self, state):
        # Verifica si las precondiciones están en el estado actual
        return self.preconditions.issubset(state)

    def apply(self, state):
        # Aplica los efectos al estado actual y retorna un nuevo estado
        new_state = state.copy()
        new_state -= self.del_effects
        new_state |= self.add_effects
        return new_state

# Función que encuentra un plan simple hacia el objetivo
def plan(initial_state, goal_state, actions):
    state = set(initial_state)
    plan_steps = []

    while not goal_state.issubset(state):
        applicable_action = None
        for action in actions:
            if action.is_applicable(state) and not goal_state.issubset(state):
                applicable_action = action
                break

        if not applicable_action:
            raise Exception("No se puede encontrar un plan.")

        state = applicable_action.apply(state)
        plan_steps.append(applicable_action.name)

    return plan_steps

# Ejemplo de uso

# Estado inicial y objetivo
initial_state = {"robot_en_A", "caja_en_A"}
goal_state = {"caja_en_B"}

# Definimos una acción para mover la caja de A a B
mover_caja = Action(
    name="mover_caja_A_B",
    preconditions={"robot_en_A", "caja_en_A"},
    add_effects={"caja_en_B"},
    del_effects={"caja_en_A"}
)

# Lista de acciones posibles
acciones = [mover_caja]

# Ejecutar el planificador
resultado = plan(initial_state, goal_state, acciones)
print("Plan encontrado:", resultado)
