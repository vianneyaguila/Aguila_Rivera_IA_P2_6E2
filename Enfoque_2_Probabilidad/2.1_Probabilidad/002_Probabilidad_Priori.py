import numpy as np

class BayesUpdater:
    def __init__(self, prior_prob):
        """
        Inicializa el actualizador bayesiano con probabilidad a priori
        
        Args:
            prior_prob (float): Probabilidad inicial P(Hipótesis)
        """
        self.prior = prior_prob
        self.posterior = prior_prob  # Inicialmente igual al prior
        
    def update(self, likelihood, marginal):
        """
        Actualiza la probabilidad usando el teorema de Bayes
        
        Args:
            likelihood (float): P(Evidencia|Hipótesis)
            marginal (float): P(Evidencia)
        """
        # Aplicar teorema de Bayes: P(H|E) = P(E|H)*P(H)/P(E)
        self.posterior = (likelihood * self.prior) / marginal
        # El nuevo prior será este posterior para la próxima actualización
        self.prior = self.posterior
        
    def get_probability(self):
        """Devuelve la probabilidad actual"""
        return self.posterior

# Ejemplo: Diagnóstico de enfermedad rara
if __name__ == "__main__":
    # Probabilidad a priori: 1% de la población tiene la enfermedad
    enfermedad_prior = 0.01
    bayes = BayesUpdater(enfermedad_prior)
    
    # Parámetros del test:
    # - Sensibilidad (P(Test+|Enfermo)) = 95%
    # - Especificidad (P(Test-|Sano)) = 90%
    # Por tanto, P(Test+|Sano) = 10%
    
    # Primera evidencia: test positivo
    likelihood_positivo = 0.95  # P(Test+|Enfermo)
    marginal_positivo = (0.95 * 0.01) + (0.10 * 0.99)  # P(Test+)
    
    bayes.update(likelihood_positivo, marginal_positivo)
    print(f"Probabilidad después de 1er test positivo: {bayes.get_probability():.2%}")
    
    # Segunda evidencia: segundo test positivo
    bayes.update(likelihood_positivo, marginal_positivo)
    print(f"Probabilidad después de 2do test positivo: {bayes.get_probability():.2%}")