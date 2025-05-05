import numpy as np
from itertools import product

class NashEquilibrium:
    """Calcula equilibrios de Nash en juegos bipersonales de suma no nula."""
    
    def __init__(self, payoff_matrix_A, payoff_matrix_B):
        """
        Args:
            payoff_matrix_A: Matriz de pagos para el jugador A (filas = estrategias A)
            payoff_matrix_B: Matriz de pagos para el jugador B (columnas = estrategias B)
        """
        self.payoff_A = np.array(payoff_matrix_A)
        self.payoff_B = np.array(payoff_matrix_B)
        self.n_strategies_A = self.payoff_A.shape[0]
        self.n_strategies_B = self.payoff_A.shape[1]
        
    def find_pure_nash(self):
        """Encuentra todos los equilibrios de Nash puros."""
        nash_equilibria = []
        
        # Verificar todas las combinaciones de estrategias
        for s_a in range(self.n_strategies_A):
            for s_b in range(self.n_strategies_B):
                is_nash = True
                
                # Verificar si A no puede mejorar
                current_payoff_A = self.payoff_A[s_a, s_b]
                for alt_s_a in range(self.n_strategies_A):
                    if self.payoff_A[alt_s_a, s_b] > current_payoff_A:
                        is_nash = False
                        break
                
                if is_nash:
                    # Verificar si B no puede mejorar
                    current_payoff_B = self.payoff_B[s_a, s_b]
                    for alt_s_b in range(self.n_strategies_B):
                        if self.payoff_B[s_a, alt_s_b] > current_payoff_B:
                            is_nash = False
                            break
                
                if is_nash:
                    nash_equilibria.append((s_a, s_b))
        
        return nash_equilibria
    
    def find_mixed_nash(self, tol=1e-6, max_iter=1000):
        """
        Aproxima equilibrios de Nash mixtos usando iteración de mejor respuesta.
        Retorna estrategias mixtas para ambos jugadores.
        """
        # Inicializar estrategias mixtas aleatorias
        mixed_A = np.random.rand(self.n_strategies_A)
        mixed_A /= mixed_A.sum()
        mixed_B = np.random.rand(self.n_strategies_B)
        mixed_B /= mixed_B.sum()
        
        for _ in range(max_iter):
            # Jugador B responde óptimamente a A
            expected_payoff_B = mixed_A @ self.payoff_B
            best_B = np.zeros_like(mixed_B)
            best_B[np.argmax(expected_payoff_B)] = 1
            
            # Jugador A responde óptimamente a B
            expected_payoff_A = self.payoff_A @ mixed_B
            best_A = np.zeros_like(mixed_A)
            best_A[np.argmax(expected_payoff_A)] = 1
            
            # Verificar convergencia
            if (np.linalg.norm(mixed_A - best_A) < tol and 
                np.linalg.norm(mixed_B - best_B) < tol):
                break
                
            mixed_A = best_A
            mixed_B = best_B
        
        return mixed_A, mixed_B

# Ejemplo: Dilema del Prisionero
if __name__ == "__main__":
    # Matrices de pagos: (Confesar, Callar)
    # Jugador A (filas), Jugador B (columnas)
    payoff_A = np.array([
        [-5, 0],    # A Confiesa
        [-10, -1]    # A Calla
    ])
    
    payoff_B = np.array([
        [-5, -10],  # B Confiesa
        [0, -1]     # B Calla
    ])
    
    game = NashEquilibrium(payoff_A, payoff_B)
    
    # Encontrar equilibrios puros
    pure_nash = game.find_pure_nash()
    print("Equilibrios puros de Nash:", pure_nash)
    
    # Encontrar equilibrio mixto
    mixed_A, mixed_B = game.find_mixed_nash()
    print("\nEstrategia mixta para Jugador A:", mixed_A)
    print("Estrategia mixta para Jugador B:", mixed_B)