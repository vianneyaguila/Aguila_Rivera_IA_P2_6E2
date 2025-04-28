import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
dt = 1.0           # Intervalo de tiempo (s)
F = np.array([[1, dt], [0, 1]])  # Matriz de transición (posición y velocidad)
H = np.array([[1, 0]])           # Matriz de observación (solo posición)
Q = np.diag([0.1, 0.01])        # Ruido del proceso (incertidumbre del modelo)
R = np.array([[10]])             # Ruido de medición (covarianza)
iteraciones = 50   # Número de pasos

# Estado inicial: [posición, velocidad]
x_est = np.array([[0], [0]])     
P_est = np.diag([100, 100])     # Covarianza inicial (alta incertidumbre)

# Almacenar resultados
posiciones_reales = []
mediciones = []
estimaciones = []

# Simular movimiento real y mediciones ruidosas
pos_real = 0
vel_real = 0.5
for _ in range(iteraciones):
    pos_real += vel_real * dt
    pos_real += np.random.normal(0, 0.1)  # Ruido del proceso
    z = pos_real + np.random.normal(0, np.sqrt(R[0,0]))  # Medición ruidosa
    
    posiciones_reales.append(pos_real)
    mediciones.append(z)
    
    # --- PREDICCIÓN ---
    x_pred = F @ x_est
    P_pred = F @ P_est @ F.T + Q
    
    # --- ACTUALIZACIÓN ---
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_est = x_pred + K @ (z - H @ x_pred)
    P_est = (np.eye(2) - K @ H) @ P_pred
    
    estimaciones.append(x_est[0, 0])

# Graficar resultados
plt.plot(posiciones_reales, label='Posición Real', linestyle='--')
plt.scatter(range(iteraciones), mediciones, color='red', label='Mediciones', alpha=0.5)
plt.plot(estimaciones, color='green', label='Estimación Kalman')
plt.legend()
plt.xlabel('Tiempo (pasos)')
plt.ylabel('Posición')
plt.title('Filtro de Kalman 1D: Estimación vs Mediciones')
plt.show()