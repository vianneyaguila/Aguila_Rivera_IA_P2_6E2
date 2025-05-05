import numpy as np
from itertools import product

class TigerPOMDP:
    """Implementa el clásico problema POMDP del tigre."""
    
    def __init__(self, gamma=0.95):
        # Estados: tigre a la izquierda (0) o derecha (1)
        self.states = [0, 1]  
        # Acciones: escuchar (0), abrir izquierda (1), abrir derecha (2)
        self.actions = [0, 1, 2]  
        # Observaciones: oír tigre izquierda (0) o derecha (1)
        self.observations = [0, 1]  
        self.gamma = gamma
        
        # Recompensas: R(s,a)
        self.R = {
            (0, 0): -1,  # Escuchar tiene costo
            (1, 0): -1,
            (0, 1): -100 if s == 0 else 10,  # Abrir puerta con tigre
            (0, 2): 10 if s == 0 else -100,
            (1, 1): 10 if s == 1 else -100,
            (1, 2): -100 if s == 1 else 10
        }
        
        # Transiciones: después de abrir, se reinicia aleatoriamente
        self.T = np.zeros((len(self.states), len(self.actions), len(self.states)))
        for s, a, s_prime in product(self.states, self.actions, self.states):
            if a == 0:  # Escuchar no cambia el estado
                self.T[s,a,s_prime] = 1 if s == s_prime else 0
            else:  # Abrir puerta reinicia el problema
                self.T[s,a,s_prime] = 0.5  # Probabilidad uniforme
        
        # Observaciones: O(o|s',a)
        self.O = np.zeros((len(self.states), len(self.actions), len(self.observations)))
        for s_prime, a, o in product(self.states, self.actions, self.observations):
            if a == 0:  # Escuchar da observación correcta con 85% de probabilidad
                self.O[s_prime,a,o] = 0.85 if s_prime == o else 0.15
            else:  # Otras acciones dan observaciones no informativas
                self.O[s_prime,a,o] = 0.5
    
    def update_belief(self, b, a, o):
        """Actualiza la creencia usando la regla de Bayes."""
        new_b = np.zeros(len(self.states))
        for s_prime in self.states:
            total = 0
            for s in self.states:
                total += self.T[s,a,s_prime] * b[s]
            new_b[s_prime] = self.O[s_prime,a,o] * total
        
        # Normalizar
        if new_b.sum() > 0:
            new_b /= new_b.sum()
        else:
            new_b = np.array([0.5, 0.5])  # Creencia por defecto si no hay información
            
        return new_b
    
    def value_iteration(self, horizon=10, tol=1e-6):
        """Algoritmo de iteración de valores para POMDP (aproximado)."""
        # Discretización del espacio de creencias
        belief_points = [np.array([1,0]), np.array([0,1]), np.array([0.5,0.5])]
        
        # Inicializar valores alpha-vectors
        alpha_vectors = []
        for a in self.actions:
            alpha = np.array([self.R[(s,a)] for s in self.states])
            alpha_vectors.append((alpha, a))
        
        for _ in range(horizon):
            new_alpha_vectors = []
            
            for a in self.actions:
                # Para cada acción posible
                for o in self.observations:
                    # Para cada observación posible
                    updated_alphas = []
                    for alpha, _ in alpha_vectors:
                        new_alpha = np.zeros(len(self.states))
                        for s in self.states:
                            total = 0
                            for s_prime in self.states:
                                total += self.T[s,a,s_prime] * self.O[s_prime,a,o] * alpha[s_prime]
                            new_alpha[s] = self.R[(s,a)] + self.gamma * total
                        updated_alphas.append(new_alpha)
                    
                    # Conservar el mejor alpha-vector para esta (a,o)
                    best_alpha = max(updated_alphas, key=lambda vec: min(np.dot(vec, b) for b in belief_points))
                    new_alpha_vectors.append((best_alpha, a))
            
            # Eliminar vectores dominados
            alpha_vectors = self.prune_vectors(new_alpha_vectors)
        
        return alpha_vectors
    
    def prune_vectors(self, vectors):
        """Elimina alpha-vectors dominados."""
        kept_vectors = []
        for i, (alpha_i, a_i) in enumerate(vectors):
            dominated = False
            for j, (alpha_j, a_j) in enumerate(vectors):
                if i != j and np.all(alpha_j >= alpha_i):
                    dominated = True
                    break
            if not dominated:
                kept_vectors.append((alpha_i, a_i))
        return kept_vectors
    
    def get_policy(self, alpha_vectors):
        """Deriva una política de los alpha-vectors."""
        def policy(b):
            best_value = -np.inf
            best_action = None
            for alpha, a in alpha_vectors:
                value = np.dot(alpha, b)
                if value > best_value:
                    best_value = value
                    best_action = a
            return best_action
        return policy

# Ejemplo de uso
if __name__ == "__main__":
    pomdp = TigerPOMDP()
    
    print("Ejecutando iteración de valores aproximada...")
    alpha_vectors = pomdp.value_iteration(horizon=5)
    policy = pomdp.get_policy(alpha_vectors)
    
    # Simular interacción
    b = np.array([0.5, 0.5])  # Creencia inicial uniforme
    print("\nSimulación:")
    for t in range(5):
        a = policy(b)
        action_names = ["Escuchar", "Abrir izquierda", "Abrir derecha"]
        print(f"Paso {t+1}: Creencia={b}, Acción={action_names[a]}")
        
        # Simular observación (aquí elegimos arbitrariamente)
        o = 0 if b[0] > 0.7 else 1 if b[1] > 0.7 else np.random.choice([0,1])
        obs_names = ["Oír tigre izquierda", "Oír tigre derecha"]
        print(f"  Observación: {obs_names[o]}")
        
        b = pomdp.update_belief(b, a, o)