import numpy as np

# Definición del MDP (grafo)
# Estados: 0, 1, 2 (3 nodos)
# Acciones: 0 (izquierda), 1 (derecha)

# Matriz de transiciones P[s][a][s'] = probabilidad
P = {
    0: {0: {0: 0.5, 1: 0.5}, 1: {1: 0.8, 2: 0.2}},
    1: {0: {0: 0.7, 1: 0.3}, 1: {2: 1.0}},
    2: {0: {2: 1.0}, 1: {2: 1.0}}  # Estado terminal
}

# Recompensas R[s][a][s']
R = {
    0: {0: {0: -1, 1: 0}, 1: {1: 0, 2: 1}},
    1: {0: {0: -1, 1: 0}, 1: {2: 10}},
    2: {0: {2: 0}, 1: {2: 0}}
}

# Hiperparámetros
gamma = 0.9  # Factor de descuento
theta = 1e-6  # Umbral de convergencia

# Inicialización
num_states = 3
num_actions = 2
V = np.zeros(num_states)  # Valores de los estados
policy = np.random.randint(0, num_actions, size=num_states)  # Política aleatoria inicial

# Algoritmo de Policy Iteration
while True:
    # Paso 1: Evaluación de la política
    while True:
        delta = 0
        for s in range(num_states):
            v = V[s]
            a = policy[s]
            # Calcular nuevo valor V(s) = Σ P(s,a,s')[R(s,a,s') + γV(s')]
            new_v = 0
            for s_next in P[s][a]:
                prob = P[s][a][s_next]
                reward = R[s][a][s_next]
                new_v += prob * (reward + gamma * V[s_next])
            V[s] = new_v
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    
    # Paso 2: Mejora de la política
    policy_stable = True
    for s in range(num_states):
        old_action = policy[s]
        # Elegir acción que maximice Σ P(s,a,s')[R(s,a,s') + γV(s')]
        action_values = []
        for a in range(num_actions):
            total = 0
            for s_next in P[s][a]:
                prob = P[s][a][s_next]
                reward = R[s][a][s_next]
                total += prob * (reward + gamma * V[s_next])
            action_values.append(total)
        policy[s] = np.argmax(action_values)
        if old_action != policy[s]:
            policy_stable = False
    
    if policy_stable:
        break

# Resultados
print("Valores óptimos de los estados:")
for s in range(num_states):
    print(f"V({s}) = {V[s]:.2f}")

print("\nPolítica óptima:")
for s in range(num_states):
    print(f"π({s}) = {policy[s]}")