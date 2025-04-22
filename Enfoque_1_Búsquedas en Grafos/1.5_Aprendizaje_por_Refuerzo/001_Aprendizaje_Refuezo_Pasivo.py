import numpy as np

# Definimos el grafo de estados y recompensas (ejemplo simple)
# Estados: 0, 1, 2 (3 nodos)
# Acciones: Seguir política fija (ej: siempre ir al estado 2)
# Recompensas: R(s,a,s')

# Matriz de transición (P[s][a][s'] = probabilidad)
P = {
    0: {0: 0.2, 1: 0.4, 2: 0.4},  # Desde estado 0
    1: {0: 0.1, 1: 0.6, 2: 0.3},  # Desde estado 1
    2: {0: 0.0, 1: 0.0, 2: 1.0}   # Desde estado 2 (absorbente)
}

# Recompensas (R[s][a][s'])
R = {
    0: {0: -1, 1: 0, 2: 1},
    1: {0: -2, 1: 1, 2: 3},
    2: {2: 0}  # Estado absorbente
}

# Política fija (siempre elegir acción que maximice recompensa inmediata)
policy = {
    0: 2,  # En estado 0, elegir acción 2 (ir a estado 2)
    1: 2,  # En estado 1, elegir acción 2 (ir a estado 2)
    2: 2   # En estado 2, quedarse
}

# Hiperparámetros
gamma = 0.9  # Factor de descuento
theta = 1e-6  # Umbral de convergencia

# Inicializar valores de estados (V(s))
V = {0: 0, 1: 0, 2: 0}

# Algoritmo de Iteración de Valores para evaluación de política
def policy_evaluation(V, P, R, policy, gamma, theta):
    while True:
        delta = 0
        for s in V.keys():  # Para cada estado
            v = V[s]
            a = policy[s]  # Acción según política fija
            # Calcular nuevo valor V(s) = Σ P(s,a,s') * [R(s,a,s') + γV(s')]
            new_v = 0
            for s_next in P[s][a]:
                prob = P[s][a][s_next]
                reward = R[s][a][s_next]
                new_v += prob * (reward + gamma * V[s_next])
            V[s] = new_v
            delta = max(delta, abs(v - V[s]))
        if delta < theta:  # Convergencia
            break
    return V

# Ejecutar evaluación
V = policy_evaluation(V, P, R, policy, gamma, theta)
print("Valores de los estados bajo la política fija:")
for s in V:
    print(f"V({s}) = {V[s]:.2f}")