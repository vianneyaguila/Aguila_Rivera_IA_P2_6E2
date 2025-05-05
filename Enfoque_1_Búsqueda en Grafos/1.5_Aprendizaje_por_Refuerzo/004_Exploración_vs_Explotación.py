import numpy as np

# Entorno simple: 3 estados (0, 1, 2) y 2 acciones (0, 1)
# Recompensas R[s][a]
R = {
    0: {0: -1, 1: 2},   # Estado 0: acción 0 → -1, acción 1 → +2
    1: {0: 0, 1: 10},   # Estado 1: acción 0 → 0, acción 1 → +10 (óptima)
    2: {0: 0, 1: 0}     # Estado terminal
}

# Transiciones (deterministas)
transitions = {
    0: {0: 0, 1: 1},  # Estado 0: acción 0 → estado 0, acción 1 → estado 1
    1: {0: 0, 1: 2},  # Estado 1: acción 0 → estado 0, acción 1 → estado 2 (terminal)
    2: {0: 2, 1: 2}   # Estado terminal
}

# Hiperparámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.2  # Probabilidad de exploración (20%)
episodes = 1000  # Número de episodios

# Inicializar tabla Q (Q[s][a] = 0)
Q = {
    0: {0: 0, 1: 0},
    1: {0: 0, 1: 0},
    2: {0: 0, 1: 0}
}

# Función ε-greedy para elegir acción
def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice([0, 1])  # Exploración aleatoria
    else:
        return max(Q[state].items(), key=lambda x: x[1])[0]  # Mejor acción según Q

# Entrenamiento con Q-Learning + ε-greedy
for episode in range(episodes):
    state = 0  # Estado inicial
    while state != 2:  # Hasta llegar al terminal
        action = choose_action(state)
        next_state = transitions[state][action]
        reward = R[state][action]
        
        # Actualizar Q(s,a): Q(s,a) = Q(s,a) + α [R + γ max Q(s',a') - Q(s,a)]
        best_next_action = max(Q[next_state].items(), key=lambda x: x[1])[0]
        td_target = reward + gamma * Q[next_state][best_next_action]
        td_error = td_target - Q[state][action]
        Q[state][action] += alpha * td_error
        
        state = next_state

# Resultados
print("Tabla Q final:")
for s in Q:
    print(f"Estado {s}: Acción 0 = {Q[s][0]:.2f}, Acción 1 = {Q[s][1]:.2f}")

print("\nPolítica óptima aprendida:")
for s in Q:
    best_action = max(Q[s].items(), key=lambda x: x[1])[0]
    print(f"Estado {s} → Acción {best_action} (Q = {Q[s][best_action]:.2f})")