from collections import deque

# Clase que representa el nodo de un estado
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # El estado actual
        self.parent = parent  # Nodo padre
        self.action = action  # Acción que llevó a este estado

# Función para generar estados sucesores
def get_successors(state):
    successors = []
    index = state.index(0)  # El espacio vacío (0)
    
    # Posiciones posibles del espacio vacío
    moves = {
        0: [1],
        1: [0, 2],
        2: [1]
    }
    
    for move in moves[index]:
        new_state = state.copy()
        # Intercambia el espacio vacío con el número vecino
        new_state[index], new_state[move] = new_state[move], new_state[index]
        successors.append((new_state, f"Mover {new_state[index]} a posición {index}"))
    
    return successors

# Búsqueda en anchura (Breadth-First Search)
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([Node(initial_state)])
    
    while queue:
        node = queue.popleft()
        if node.state == goal_state:
            return reconstruct_path(node)
        
        visited.add(tuple(node.state))
        
        for successor, action in get_successors(node.state):
            if tuple(successor) not in visited:
                queue.append(Node(successor, parent=node, action=action))
    
    return None

# Función para reconstruir el camino desde el nodo final
def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path

# Estado inicial y meta
initial = [1, 0, 2]  # 0 representa el espacio vacío
goal = [1, 2, 0]

# Ejecutamos la búsqueda
plan = bfs(initial, goal)
print("Plan encontrado:", plan)
