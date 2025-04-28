import numpy as np
import matplotlib.pyplot as plt

# ------------ DEFINICIÓN DEL PROBLEMA ------------
# Estado inicial: posición y velocidad
x = np.array([[0],  # Posición inicial
              [1]]) # Velocidad inicial

# Matriz de covarianza inicial (incertidumbre inicial)
P = np.eye(2)

# Modelo de transición de estado (asumimos movimiento uniforme)
dt = 1  # intervalo de tiempo
F = np.array([[1, dt],
              [0, 1]])

# Modelo de observación (solo medimos posición)
H = np.array([[1, 0]])

# Matriz de ruido del proceso (incertidumbre del movimiento)
Q = np.array([[0.001, 0],
              [0, 0.001]])

# Matriz de ruido de medición (incertidumbre del sensor)
R = np.array([[1]])

# Número de pasos
num_steps = 50

# Variables para almacenar resultados
estimaciones = []
mediciones = []

# Simulación de un objeto real moviéndose
pos_real = 0
vel_real = 1
np.random.seed(42)  # Semilla para reproducibilidad

# ------------ CICLO PRINCIPAL DEL FILTRO ------------
for _ in range(num_steps):
    # Simular el movimiento real
    pos_real += vel_real * dt
    # Medición ruidosa de la posición
    medicion = pos_real + np.random.normal(0, 1)
    mediciones.append(medicion)
    
    # ------------- PREDICCIÓN -------------
    # Predicción del siguiente estado
    x = F @ x
    # Predicción de la covarianza del error
    P = F @ P @ F.T + Q

    # ------------- ACTUALIZACIÓN -------------
    # Cálculo de la ganancia de Kalman
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)

    # Actualización del estado con la medición
    z = np.array([[medicion]])
    y = z - H @ x
    x = x + K @ y

    # Actualización de la covarianza
    P = (np.eye(2) - K @ H) @ P

    # Guardar la estimación de posición
    estimaciones.append(x[0, 0])

# ------------ VISUALIZACIÓN DE RESULTADOS ------------
plt.plot(range(num_steps), mediciones, label='Mediciones (ruidosas)', linestyle='dotted')
plt.plot(range(num_steps), estimaciones, label='Estimaciones (Kalman)', linestyle='solid')
plt.plot(range(num_steps), [i for i in range(num_steps)], label='Posición Real', linestyle='dashed')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.legend()
plt.title('Filtro de Kalman: Seguimiento de un objeto en 1D')
plt.grid(True)
plt.show()
