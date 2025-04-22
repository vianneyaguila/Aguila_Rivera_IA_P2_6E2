import numpy as np

class PolicyIteration:
    def __init__(self, states, actions, transitions, rewards, gamma=0.9):
        """
        Inicializa el solver de iteración de políticas.
        
        Args:
            states (list): Lista de estados
            actions (dict): {estado: lista de acciones posibles}
            transitions (dict): {(s,a,s'): probabilidad}
            rewards (dict): {(s,a,s'): recompensa}
            gamma (float): Factor de descuento
        """
        self.states = states
        self.actions = actions
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma
        
    def evaluate_policy(self, policy, tol=1e-6):
        """Evalúa una política dada resolviendo el sistema lineal de ecuaciones."""
        V = {s: 0 for s in self.states}
        while True:
            delta = 0
            for s in self.states:
                v = V[s]
                total = 0
                for a in self.actions[s]:
                    for s_prime in self.states:
                        prob = self.transitions.get((s,a,s_prime), 0)
                        reward = self.rewards.get((s,a,s_prime), 0)
                        total += policy[s][a] * prob * (reward + self.gamma * V[s_prime])
                V[s] = total
                delta = max(delta, abs(v - V[s]))
            if delta < tol:
                break
        return V
    
    def improve_policy(self, V, policy):
        """Mejora la política haciéndola greedy respecto a V."""
        policy_stable = True
        new_policy = {s: {a: 0 for a in self.actions[s]} for s in self.states}
        
        for s in self.states:
            old_action = max(policy[s], key=policy[s].get)
            
            # Encontrar acción greedy
            best_action = None
            best_value = -np.inf
            action_values = {}
            
            for a in self.actions[s]:
                total = 0
                for s_prime in self.states:
                    prob = self.transitions.get((s,a,s_prime), 0)
                    reward = self.rewards.get((s,a,s_prime), 0)
                    total += prob * (reward + self.gamma * V[s_prime])
                action_values[a] = total
                if total > best_value:
                    best_value = total
                    best_action = a
            
            # Asignar probabilidad 1 a la mejor acción
            for a in self.actions[s]:
                new_policy[s][a] = 1 if a == best_action else 0
            
            if best_action != old_action:
                policy_stable = False
                
        return new_policy, policy_stable
    
    def solve(self, max_iter=100, tol=1e-6):
        """Ejecuta el algoritmo de iteración de políticas."""
        # Inicializar política aleatoria
        policy = {s: {a: 1/len(self.actions[s]) for a in self.actions[s]} 
                  for s in self.states}
        
        for i in range(max_iter):
            # Paso 1: Evaluación de política
            V = self.evaluate_policy(policy, tol)
            
            # Paso 2: Mejora de política
            policy, stable = self.improve_policy(V, policy)
            
            if stable:
                print(f"Convergió en {i+1} iteraciones")
                break
                
        return policy, V

# Ejemplo de uso
if __name__ == "__main__":
    # Definir un MDP simple (laberinto 3x3)
    states = [(i,j) for i in range(3) for j in range(3)]
    actions = {s: ['up', 'down', 'left', 'right'] for s in states}
    
    # Transiciones (determinísticas en este ejemplo)
    transitions = {}
    rewards = {}
    for s in states:
        for a in actions[s]:
            i, j = s
            if a == 'up' and i > 0:
                s_prime = (i-1, j)
            elif a == 'down' and i < 2:
                s_prime = (i+1, j)
            elif a == 'left' and j > 0:
                s_prime = (i, j-1)
            elif a == 'right' and j < 2:
                s_prime = (i, j+1)
            else:
                s_prime = s  # Se queda si el movimiento no es posible
                
            transitions[(s, a, s_prime)] = 1.0
            rewards[(s, a, s_prime)] = 10 if s_prime == (2,2) else -1
    
    # Crear solver
    solver = PolicyIteration(states, actions, transitions, rewards)
    
    # Resolver
    optimal_policy, optimal_values = solver.solve()
    
    # Mostrar resultados
    print("\nValores óptimos:")
    for i in range(3):
        for j in range(3):
            print(f"{(i,j)}: {optimal_values[(i,j)]:.2f}", end=" | ")
        print()
    
    print("\nPolítica óptima:")
    for s in states:
        best_action = max(optimal_policy[s], key=optimal_policy[s].get)
        print(f"{s}: {best_action}")