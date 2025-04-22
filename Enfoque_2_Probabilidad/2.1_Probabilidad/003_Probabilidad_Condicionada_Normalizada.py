import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

class BayesianNormalizer:
    def __init__(self, prior_distributions):
        """
        Sistema bayesiano para probabilidades condicionadas con normalización automática
        
        Args:
            prior_distributions (dict): Diccionario con formas de los priores
                Ejemplo: {'A': {'mean': 0, 'std': 1}, 'B': {'mean': 5, 'std': 2}}
        """
        self.priors = prior_distributions
        self.evidence_history = []
        self.current_posteriors = None
        
    def compute_likelihood(self, data, hypothesis):
        """
        Calcula P(Data|Hypothesis) usando distribución normal
        
        Args:
            data (float): Valor observado
            hypothesis (str): Clave del hipótesis (debe existir en priors)
            
        Returns:
            float: Valor de verosimilitud
        """
        params = self.priors[hypothesis]
        return norm.pdf(data, loc=params['mean'], scale=params['std'])
    
    def update_beliefs(self, observed_data):
        """
        Actualiza todas las probabilidades condicionadas usando Bayes y normaliza
        
        Args:
            observed_data (float): Nuevo dato observado
        """
        self.evidence_history.append(observed_data)
        
        # Paso 1: Calcular términos no normalizados
        unnormalized = {}
        marginal = 0.0
        
        for hypo in self.priors:
            # P(Hypo) * P(Data|Hypo)
            prior = 1.0 / len(self.priors)  # Prior uniforme simplificado
            likelihood = self.compute_likelihood(observed_data, hypo)
            unnormalized[hypo] = prior * likelihood
            marginal += unnormalized[hypo]  # Acumular para P(Data)
        
        # Paso 2: Normalizar (Teorema de Bayes completo)
        self.current_posteriors = {
            hypo: (unnormalized[hypo] / marginal if marginal > 0 else 0)
            for hypo in self.priors
        }
    
    def plot_distributions(self, observed_value=None):
        """Visualiza priors, likelihoods y posteriors"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Gráfico 1: Distribuciones de los priors
        x = np.linspace(-10, 15, 1000)
        for hypo, params in self.priors.items():
            dist = norm(params['mean'], params['std'])
            ax1.plot(x, dist.pdf(x), label=f'Prior {hypo}')
        
        if observed_value is not None:
            ax1.axvline(observed_value, color='black', linestyle='--', label='Dato observado')
        ax1.set_title('Distribuciones a Priori y Dato')
        ax1.legend()
        ax1.grid(True)
        
        # Gráfico 2: Probabilidades posteriores (si existen)
        if self.current_posteriors:
            hypotheses = list(self.current_posteriors.keys())
            probabilities = list(self.current_posteriors.values())
            
            ax2.bar(hypotheses, probabilities, color=['blue', 'orange', 'green'])
            ax2.set_ylim(0, 1)
            ax2.set_title('Probabilidades Posteriores Normalizadas')
            ax2.grid(True)
            ax2.set_ylabel('P(Hipótesis|Dato)')
        
        plt.tight_layout()
        plt.show()

# Ejemplo de uso completo
if __name__ == "__main__":
    # Definir tres hipótesis competidoras con distribuciones normales
    priors_config = {
        'H1': {'mean': 0, 'std': 1},  # Hipótesis 1: Media baja
        'H2': {'mean': 5, 'std': 2},   # Hipótesis 2: Media moderada
        'H3': {'mean': 10, 'std': 3}   # Hipótesis 3: Media alta
    }
    
    bayes_system = BayesianNormalizer(priors_config)
    
    # Simular datos observados (verdadero valor alrededor de 4)
    np.random.seed(42)
    simulated_data = np.random.normal(loc=4, scale=1.5, size=3)
    
    # Procesar cada dato secuencialmente
    for i, data_point in enumerate(simulated_data, 1):
        print(f"\nActualización con dato {i}: {data_point:.2f}")
        bayes_system.update_beliefs(data_point)
        bayes_system.plot_distributions(data_point)
        
        # Mostrar resultados numéricos
        print("Probabilidades posteriores:")
        for hypo, prob in bayes_system.current_posteriors.items():
            print(f"{hypo}: {prob:.4f} ({prob:.2%})")