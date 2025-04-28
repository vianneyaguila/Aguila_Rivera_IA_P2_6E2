import numpy as np

# Definir parámetros del HMM
estados = ['Soleado', 'Lluvioso']          # Estados ocultos
observaciones = ['Paraguas', 'NoParaguas'] # Observaciones

# Matriz de transición (A): Soleado -> Soleado: 0.7, Lluvioso -> Lluvioso: 0.6
A = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Matriz de emisión (B): Soleado emite 'NoParaguas' con 0.9 de probabilidad
B = np.array([[0.1, 0.9],  # Paraguas, NoParaguas desde Soleado
              [0.8, 0.2]]) # Paraguas, NoParaguas desde Lluvioso

# Distribución inicial (π): Empieza en Soleado con 0.6 de probabilidad
pi = np.array([0.6, 0.4])

def viterbi(obs, A, B, pi):
    T = len(obs)                  # Longitud de la secuencia de observaciones
    N = A.shape[0]                # Número de estados ocultos
    delta = np.zeros((T, N))      # Almacena probabilidades máximas
    psi = np.zeros((T, N), dtype=int) # Almacena índices de estados previos
    
    # Paso 1: Inicialización (t=0)
    delta[0] = pi * B[:, obs[0]]  # π_i * b_i(o_1)
    
    # Paso 2: Recursión (t=1 a T-1)
    for t in range(1, T):
        for j in range(N):
            trans_prob = delta[t-1] * A[:, j]  # Probabilidades de transición
            psi[t, j] = np.argmax(trans_prob)  # Mejor estado previo
            delta[t, j] = trans_prob[psi[t, j]] * B[j, obs[t]]  # Actualizar delta
    
    # Paso 3: Backtracking para obtener la secuencia de estados
    path = np.zeros(T, dtype=int)
    path[-1] = np.argmax(delta[-1])  # Estado final más probable
    for t in range(T-2, -1, -1):
        path[t] = psi[t+1, path[t+1]]  # Reconstruir camino óptimo
    
    return [estados[i] for i in path]

# Ejemplo de uso
# Mapear observaciones a índices: 'Paraguas'=0, 'NoParaguas'=1
obs_seq = [0, 0, 1]  # Ejemplo: [Paraguas, Paraguas, NoParaguas]

secuencia_optima = viterbi(obs_seq, A, B, pi)
print("Secuencia óptima de estados:", secuencia_optima)