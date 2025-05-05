import numpy as np
import matplotlib.pyplot as plt

class EpsilonGreedyBandit:
    def __init__(self, num_arms, epsilon=0.1):
        """
        Implementación de bandido multi-brazo con estrategia ε-greedy
        Args:
            num_arms: Número de brazos/máquinas tragamonedas
            epsilon: Probabilidad de exploración (0-1)
        """
        self.num_arms = num_arms
        self.epsilon = epsilon
        self.q_values = np.zeros(num_arms)  # Estimación valor acciones
        self.action_counts = np.zeros(num_arms)  # Conteo selecciones
        
    def choose_action(self):
        """Selecciona acción según política ε-greedy"""
        if np.random.random() < self.epsilon:
            # Exploración: acción aleatoria
            return np.random.randint(self.num_arms)
        else:
            # Explotación: mejor acción estimada
            return np.argmax(self.q_values)
    
    def update(self, action, reward):
        """Actualiza estimaciones con recompensa observada"""
        self.action_counts[action] += 1
        # Actualización incremental (promedio muestral)
        self.q_values[action] += (reward - self.q_values[action]) / self.action_counts[action]
    
    def run_experiment(self, true_means, num_steps=1000):
        """
        Ejecuta experimento completo
        Args:
            true_means: Verdaderas medias de recompensa por acción
            num_steps: Número total de pasos/interacciones
        Returns:
            recompensas: Historial de recompensas obtenidas
            acciones: Historial de acciones seleccionadas
        """
        recompensas = np.zeros(num_steps)
        acciones = np.zeros(num_steps, dtype=int)
        
        for t in range(num_steps):
            # Seleccionar y ejecutar acción
            action = self.choose_action()
            reward = np.random.normal(true_means[action], 1)
            
            # Actualizar estimaciones
            self.update(action, reward)
            
            # Registrar resultados
            recompensas[t] = reward
            acciones[t] = action
            
        return recompensas, acciones

# Configuración experimento
num_arms = 5
true_means = np.array([1.2, 0.8, 1.5, 2.0, 0.5])  # Medias reales desconocidas
epsilon = 0.1
num_steps = 2000

# Ejecución
bandit = EpsilonGreedyBandit(num_arms, epsilon)
rewards, actions = bandit.run_experiment(true_means, num_steps)

# Visualización
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(np.cumsum(rewards) / np.arange(1, num_steps+1), label='Recompensa promedio')
plt.axhline(y=max(true_means), color='r', linestyle='--', label='Óptimo')
plt.xlabel('Pasos')
plt.ylabel('Recompensa promedio acumulada')
plt.legend()

plt.subplot(1, 2, 2)
for arm in range(num_arms):
    plt.plot(np.cumsum(actions == arm) / np.arange(1, num_steps+1), label=f'Brazo {arm+1}')
plt.xlabel('Pasos')
plt.ylabel('Frecuencia de selección')
plt.legend()
plt.tight_layout()
plt.show()