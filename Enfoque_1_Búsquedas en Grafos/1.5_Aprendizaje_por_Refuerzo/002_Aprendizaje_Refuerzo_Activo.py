import numpy as np

# Definición del entorno (grafo)
# Estados: 0, 1, 2 (3 nodos)
# Acciones: 0 (izquierda), 1 (derecha)
# Recompensas: R[s][a]

# Matriz de recompensas R[s][a]
R = {
    0: {0: -1, 1: 0},   # Desde estado 0
    1: {0: -2, 1: 3},   # Desde estado 1
    2: {0: 0, 1: 0}     # Estado terminal
}

# Matriz de transiciones (determinista en este caso)
transitions = {
    0: {0: 0, 1: 1},  # En estado 0, acción 0 lleva a 0, acción 1 lleva a 1
    1: {0: 0, 1: 2},  # En estado 1, acción 0 lleva a 0, acción 1 lleva a 2
    2: {0: 2, 1: 2}   # Estado 2 es terminal
}

# Hiperparámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Probabilidad de exploración (ε-greedy)
episodes = 1000  # Número de episodios de entrenamiento

# Inicializar tabla Q (Q[s][a])
Q = {
    0: {0: 0, 1: 0},
    1: {0: 0, 1: 0},
    2: {0: 0, 1: 0}
}

# Función para elegir acción (ε-greedy)
def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(list(Q[state].keys()))  # Exploración
    else:
        return max(Q[state].items(), key=lambda x: x[1])[0]  # Explotación

# Algoritmo Q-Learning
for episode in range(episodes):
    state = 0  # Estado inicial
    while state != 2:  # Hasta llegar al estado terminal
        action = choose_action(state)
        next_state = transitions[state][action]
        reward = R[state][action]
        
        # Actualizar Q-value: Q(s,a) = Q(s,a) + α [R + γ max Q(s',a') - Q(s,a)]
        best_next_action = max(Q[next_state].items(), key=lambda x: x[1])[0]
        td_target = reward + gamma * Q[next_state][best_next_action]
        td_error = td_target - Q[state][action]
        Q[state][action] += alpha * td_error
        
        state = next_state

# Mostrar política aprendida
print("Política óptima aprendida:")
for s in Q:
    best_action = max(Q[s].items(), key=lambda x: x[1])[0]
    print(f"Estado {s} → Acción {best_action} (Q-value: {Q[s][best_action]:.2f})")