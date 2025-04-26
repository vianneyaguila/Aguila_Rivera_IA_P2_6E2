import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from functools import reduce

class BayesianUpdater:
    def __init__(self, prior_dist, likelihood_func):
        """
        Sistema avanzado de actualización bayesiana iterativa
        
        Args:
            prior_dist (dict): Distribución a priori en formato {'valores': [], 'probabilidades': []}
            likelihood_func (function): Función que calcula P(D|H) para cualquier dato D
        """
        self.prior = prior_dist
        self.likelihood = likelihood_func
        self.posterior_history = []
        self.evidence_history = []
        
        # Validar distribución inicial
        self._validate_distribution(self.prior)
        
    def _validate_distribution(self, dist):
        """Valida que la distribución sea válida"""
        if not np.isclose(sum(dist['probabilidades']), 1.0, atol=1e-6):
            raise ValueError("Las probabilidades deben sumar 1")
        if len(dist['valores']) != len(dist['probabilidades']):
            raise ValueError("Valores y probabilidades deben tener misma longitud")
    
    def update(self, observed_data):
        """
        Realiza actualización bayesiana con nuevo dato observado
        
        Args:
            observed_data: Dato observado para actualizar creencias
        """
        # Calcular verosimilitudes para cada hipótesis
        likelihoods = np.array([self.likelihood(observed_data, h) 
                              for h in self.prior['valores']])
        
        # Calcular términos no normalizados (prior * likelihood)
        unnormalized_posterior = self.prior['probabilidades'] * likelihoods
        
        # Calcular evidencia (P(D))
        evidence = np.sum(unnormalized_posterior)
        
        # Normalizar para obtener posterior
        posterior = unnormalized_posterior / evidence
        
        # Guardar histórico
        self.posterior_history.append({
            'valores': self.prior['valores'],
            'probabilidades': posterior
        })
        self.evidence_history.append(evidence)
        
        # Actualizar prior para próxima iteración
        self.prior['probabilidades'] = posterior
    
    def plot_evolution(self, true_value=None):
        """Visualiza la evolución de las creencias"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Gráfico 1: Distribuciones inicial, intermedia y final
        iterations = len(self.posterior_history)
        for i in [0, iterations//2, -1]:
            dist = self.prior if i == 0 else self.posterior_history[i]
            label = 'Prior' if i == 0 else f'Iteración {i+1}'
            ax1.plot(dist['valores'], dist['probabilidades'], 
                    label=label, lw=2)
        
        if true_value is not None:
            ax1.axvline(true_value, color='black', linestyle='--', 
                       label='Valor verdadero')
        ax1.set_title('Evolución de Creencias', fontsize=14)
        ax1.set_xlabel('Hipótesis', fontsize=12)
        ax1.set_ylabel('Probabilidad', fontsize=12)
        ax1.legend()
        ax1.grid(True)
        
        # Gráfico 2: Máxima probabilidad a posteriori (MAP) por iteración
        map_estimates = [dist['valores'][np.argmax(dist['probabilidades'])] 
                        for dist in self.posterior_history]
        ax2.plot(range(1, iterations+1), map_estimates, 'o-')
        if true_value is not None:
            ax2.axhline(true_value, color='red', linestyle='--', 
                       label='Valor verdadero')
        ax2.set_title('Estimación MAP por Iteración', fontsize=14)
        ax2.set_xlabel('Iteración', fontsize=12)
        ax2.set_ylabel('Estimación MAP', fontsize=12)
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def get_current_beliefs(self):
        """Devuelve la distribución de creencias actual"""
        return self.prior
    
    def get_evidence_history(self):
        """Devuelve el histórico de valores de evidencia"""
        return self.evidence_history

# Función de verosimilitud para ejemplo médico
def medical_likelihood(observed_test, disease_prevalence):
    """
    Calcula P(Test|Disease) para un test diagnóstico
    
    Args:
        observed_test (bool): Resultado del test (True = positivo)
        disease_prevalence (float): Prevalencia de la enfermedad (hipótesis)
        
    Returns:
        float: Probabilidad del resultado del test dada la prevalencia
    """
    sensitivity = 0.95  # P(Test+ | Enfermo)
    specificity = 0.90  # P(Test- | Sano)
    
    if observed_test:
        return sensitivity * disease_prevalence + (1 - specificity) * (1 - disease_prevalence)
    else:
        return (1 - sensitivity) * disease_prevalence + specificity * (1 - disease_prevalence)

# Ejemplo de uso completo
if __name__ == "__main__":
    # Configurar hipótesis sobre prevalencia de enfermedad
    hypotheses = np.linspace(0, 1, 100)  # De 0% a 100%
    initial_probs = np.ones_like(hypotheses) / len(hypotheses)  # Prior uniforme
    
    # Crear actualizador bayesiano
    updater = BayesianUpdater(
        prior_dist={'valores': hypotheses, 'probabilidades': initial_probs},
        likelihood_func=lambda data, h: medical_likelihood(data, h)
    )
    
    # Simular secuencia de resultados de tests
    np.random.seed(42)
    test_results = [True, True, False, True, False, False, True]
    true_prevalence = 0.3  # Valor "verdadero" para comparación
    
    # Realizar actualizaciones secuenciales
    for i, result in enumerate(test_results, 1):
        updater.update(result)
        print(f"\nDespués de {i} tests ({'Positivo' if result else 'Negativo'}):")
        current_beliefs = updater.get_current_beliefs()
        map_estimate = current_beliefs['valores'][np.argmax(current_beliefs['probabilidades'])]
        print(f"Estimación MAP de prevalencia: {map_estimate:.2%}")
    
    # Visualizar evolución completa
    updater.plot_evolution(true_value=true_prevalence)
    
    # Mostrar evidencia (P(D)) para cada paso
    print("\nEvidencia (P(D)) por iteración:")
    for i, ev in enumerate(updater.get_evidence_history(), 1):
        print(f"Iteración {i}: {ev:.6f}")