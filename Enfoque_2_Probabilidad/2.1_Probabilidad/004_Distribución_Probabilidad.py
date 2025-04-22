import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, beta, expon
from sklearn.neighbors import KernelDensity

class ProbabilityDistributionAnalyzer:
    def __init__(self, data=None):
        """
        Analizador avanzado de distribuciones de probabilidad
        
        Args:
            data (array-like): Datos para estimación no paramétrica
        """
        self.data = np.array(data) if data is not None else None
        self.fitted_distributions = {}
        
    def fit_parametric(self, dist_type, params):
        """
        Ajusta una distribución paramétrica conocida
        
        Args:
            dist_type (str): Tipo de distribución ('normal', 'poisson', 'beta', 'expon')
            params (dict): Parámetros de la distribución
        """
        if dist_type == 'normal':
            self.fitted_distributions['normal'] = norm(loc=params['mean'], scale=params['std'])
        elif dist_type == 'poisson':
            self.fitted_distributions['poisson'] = poisson(mu=params['lambda'])
        elif dist_type == 'beta':
            self.fitted_distributions['beta'] = beta(a=params['alpha'], b=params['beta'])
        elif dist_type == 'expon':
            self.fitted_distributions['expon'] = expon(scale=1/params['lambda'])
        else:
            raise ValueError("Distribución no soportada")
    
    def fit_nonparametric(self, bandwidth=0.5, kernel='gaussian'):
        """
        Estimación no paramétrica usando KDE (Kernel Density Estimation)
        
        Args:
            bandwidth (float): Ancho de banda para suavizado
            kernel (str): Tipo de kernel ('gaussian', 'tophat', 'epanechnikov')
        """
        if self.data is None:
            raise ValueError("Se requieren datos para estimación no paramétrica")
            
        kde = KernelDensity(bandwidth=bandwidth, kernel=kernel)
        kde.fit(self.data.reshape(-1, 1))
        self.fitted_distributions['kde'] = kde
    
    def plot_distributions(self, x_range=None, plot_data=True):
        """
        Visualiza las distribuciones ajustadas
        
        Args:
            x_range (tuple): Rango (min, max) para evaluación
            plot_data (bool): Si mostrar histograma de datos
        """
        if not self.fitted_distributions:
            raise ValueError("No hay distribuciones ajustadas")
            
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Determinar rango automático si no se especifica
        if x_range is None:
            if self.data is not None:
                x_min, x_max = self.data.min(), self.data.max()
                x_range = (x_min - 0.1*(x_max-x_min), x_max + 0.1*(x_max-x_min))
            else:
                x_range = (-10, 10)  # Default para distribuciones sin datos
        
        x = np.linspace(x_range[0], x_range[1], 1000)
        
        # Graficar datos si existen
        if plot_data and self.data is not None:
            ax.hist(self.data, bins=30, density=True, alpha=0.5, 
                   color='gray', label='Datos observados')
        
        # Graficar cada distribución ajustada
        for name, dist in self.fitted_distributions.items():
            if name == 'kde':
                log_prob = dist.score_samples(x.reshape(-1, 1))
                y = np.exp(log_prob)
                label = 'KDE (no paramétrico)'
            else:
                if hasattr(dist, 'pdf'):
                    y = dist.pdf(x)
                else:
                    y = dist.pmf(x)
                label = f'{name.capitalize()} (paramétrico)'
            
            ax.plot(x, y, lw=2, label=label)
        
        ax.set_title('Comparación de Distribuciones de Probabilidad', fontsize=14)
        ax.set_xlabel('Valor', fontsize=12)
        ax.set_ylabel('Densidad/Probabilidad', fontsize=12)
        ax.legend()
        ax.grid(True)
        plt.show()
    
    def calculate_probability(self, interval, dist_name='kde'):
        """
        Calcula P(a < X < b) para una distribución
        
        Args:
            interval (tuple): Intervalo (a, b)
            dist_name (str): Nombre de distribución a usar
            
        Returns:
            float: Probabilidad en el intervalo
        """
        if dist_name not in self.fitted_distributions:
            raise ValueError("Distribución no encontrada")
            
        dist = self.fitted_distributions[dist_name]
        a, b = interval
        
        if dist_name == 'kde':
            # Integración numérica para KDE
            x = np.linspace(a, b, 1000)
            log_prob = dist.score_samples(x.reshape(-1, 1))
            prob = np.trapz(np.exp(log_prob), x)
        else:
            if hasattr(dist, 'cdf'):
                prob = dist.cdf(b) - dist.cdf(a)
            else:
                # Para discretas, sumar PMF en rango
                x_vals = np.arange(np.ceil(a), np.floor(b)+1)
                prob = np.sum([dist.pmf(x) for x in x_vals])
        
        return prob

# Ejemplo de uso completo
if __name__ == "__main__":
    # Generar datos sintéticos (mezcla de normales)
    np.random.seed(42)
    data = np.concatenate([
        np.random.normal(loc=0, scale=1, size=500),
        np.random.normal(loc=5, scale=1.5, size=300)
    ])
    
    # Crear analizador
    analyzer = ProbabilityDistributionAnalyzer(data)
    
    # Ajustar distribuciones paramétricas
    analyzer.fit_parametric('normal', {'mean': np.mean(data), 'std': np.std(data)})
    analyzer.fit_parametric('expon', {'lambda': 1/np.mean(data)})
    
    # Ajustar KDE no paramétrico
    analyzer.fit_nonparametric(bandwidth=0.3)
    
    # Visualizar comparación
    analyzer.plot_distributions(x_range=(-5, 10))
    
    # Calcular probabilidad en intervalo
    interval = (2, 4)
    prob_kde = analyzer.calculate_probability(interval, 'kde')
    prob_norm = analyzer.calculate_probability(interval, 'normal')
    
    print(f"\nProbabilidad P({interval[0]} < X < {interval[1]}):")
    print(f"- KDE: {prob_kde:.4f} ({prob_kde:.2%})")
    print(f"- Normal: {prob_norm:.4f} ({prob_norm:.2%})")