import numpy as np

class GridWorldMDP:
    """Implementa un MDP para navegación en un grid 4x4."""
    
    def __init__(self, size=4, gamma=0.9):
        """
        Args:
            size (int): Tamaño del grid (size x size)
            gamma (float): Factor de descuento
        """
        self.size = size
        self.gamma = gamma
        self.actions = ['up', 'down', 'left', 'right']
        
        # Estados terminales (esquinas)
        self.terminal_states = [(0,0), (size-1, size-1)]
        
        # Recompensas: +10 en (0,0), -10 en (3,3), -1 en otros
        self.rewards = {}
        for i in range(size):
            for j in range(size):
                if (i,j) == (0,0):
                    self.rewards[(i,j)] = 10
                elif (i,j) == (size-1, size-1):
                    self.rewards[(i,j)] = -10
                else:
                    self.rewards[(i,j)] = -1
    
    def get_states(self):
        """Retorna lista de todos los estados posibles."""
        return [(i,j) for i in range(self.size) for j in range(self.size)]
    
    def get_actions(self, state):
        """Retorna acciones posibles para un estado dado."""
        if state in self.terminal_states:
            return []  # No hay acciones en estados terminales
        return self.actions
    
    def transition(self, state, action):
        """
        Modela la función de transición P(s'|s,a).
        Retorna lista de tuplas (probabilidad, nuevo_estado, recompensa).
        """
        i, j = state
        
        # Determinista en este ejemplo (80% éxito, 20% aleatorio)
        if action == 'up':
            new_i, new_j = max(i-1, 0), j
        elif action == 'down':
            new_i, new_j = min(i+1, self.size-1), j
        elif action == 'left':
            new_i, new_j = i, max(j-1, 0)
        elif action == 'right':
            new_i, new_j = i, min(j+1, self.size-1)
        
        # Recompensa del nuevo estado
        reward = self.rewards[(new_i, new_j)]
        
        # 80% probabilidad de éxito, 20% de movimiento aleatorio
        transitions = [
            (0.8, (new_i, new_j), reward),
            (0.2/3, *self.transition(state, np.random.choice(
                [a for a in self.actions if a != action]))[0][1:])
        ]
        
        return transitions
    
    def value_iteration(self, tol=1e-6):
        """Implementa el algoritmo de Iteración de Valores."""
        states = self.get_states()
        V = {s: 0 for s in states}
        
        while True:
            delta = 0
            new_V = {}
            
            for s in states:
                if s in self.terminal_states:
                    new_V[s] = 0
                    continue
                
                max_value = -np.inf
                for a in self.get_actions(s):
                    expected_value = 0
                    for prob, s_prime, reward in self.transition(s, a):
                        expected_value += prob * (reward + self.gamma * V[s_prime])
                    
                    if expected_value > max_value:
                        max_value = expected_value
                
                new_V[s] = max_value
                delta = max(delta, abs(new_V[s] - V[s]))
            
            V = new_V
            if delta < tol:
                break
        
        # Extraer política óptima
        policy = {}
        for s in states:
            if s in self.terminal_states:
                policy[s] = None
                continue
            
            best_action = None
            best_value = -np.inf
            
            for a in self.get_actions(s):
                action_value = 0
                for prob, s_prime, reward in self.transition(s, a):
                    action_value += prob * (reward + self.gamma * V[s_prime])
                
                if action_value > best_value:
                    best_value = action_value
                    best_action = a
            
            policy[s] = best_action
        
        return V, policy

# Ejemplo de uso
if __name__ == "__main__":
    # Crear MDP de grid 4x4
    mdp = GridWorldMDP(size=4)
    
    # Ejecutar Iteración de Valores
    optimal_values, optimal_policy = mdp.value_iteration()
    
    # Mostrar resultados
    print("Valores óptimos:")
    for i in range(4):
        for j in range(4):
            print(f"({i},{j}): {optimal_values[(i,j)]:.2f}", end=" | ")
        print()
    
    print("\nPolítica óptima:")
    for i in range(4):
        for j in range(4):
            print(f"({i},{j}): {optimal_policy[(i,j)]}", end=" | ")
        print()