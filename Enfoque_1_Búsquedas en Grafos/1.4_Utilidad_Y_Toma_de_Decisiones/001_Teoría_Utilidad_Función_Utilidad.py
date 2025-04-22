import numpy as np

class AgenteUtilidad:
    def __init__(self, factores_importancia):
        """
        Inicializa el agente con los pesos para cada factor de decisión.
        
        Args:
            factores_importancia (dict): Diccionario con los pesos de cada factor.
                Ejemplo: {'tiempo': 0.6, 'costo': 0.3, 'comodidad': 0.1}
        """
        self.factores = factores_importancia
        # Normalizamos los pesos para que sumen 1
        total = sum(factores_importancia.values())
        self.pesos = {k: v/total for k, v in factores_importancia.items()}
    
    def normalizar(self, valores):
        """
        Normaliza los valores de un factor para que estén en el rango [0,1].
        
        Args:
            valores (list or np.array): Valores a normalizar.
            
        Returns:
            np.array: Valores normalizados.
        """
        min_val = np.min(valores)
        max_val = np.max(valores)
        if max_val == min_val:
            return np.ones_like(valores)  # Todos iguales, misma utilidad
        return (valores - min_val) / (max_val - min_val)
    
    def calcular_utilidad(self, opciones):
        """
        Calcula la utilidad para cada opción basada en los factores ponderados.
        
        Args:
            opciones (list of dict): Lista de opciones, cada una es un diccionario
                con los valores para cada factor. Ejemplo:
                [{'tiempo': 30, 'costo': 100, 'comodidad': 3},
                 {'tiempo': 45, 'costo': 80, 'comodidad': 4}]
                
        Returns:
            dict: Utilidad total para cada opción y utilidades parciales por factor.
        """
        # Convertimos a estructura numpy para cálculo eficiente
        factores = list(self.pesos.keys())
        num_opciones = len(opciones)
        
        # Extraemos los valores para cada factor
        datos = {f: np.zeros(num_opciones) for f in factores}
        for i, opcion in enumerate(opciones):
            for f in factores:
                datos[f][i] = opcion.get(f, 0)  # 0 si el factor no está presente
        
        # Normalizamos cada factor (mayor valor es mejor)
        # Para factores donde menor es mejor (como tiempo), invertimos después
        datos_norm = {f: self.normalizar(datos[f]) for f in factores}
        
        # Invertimos factores donde menor es mejor (como tiempo)
        for f in ['tiempo', 'costo']:  # Ejemplo de factores donde menos es mejor
            if f in datos_norm:
                datos_norm[f] = 1 - datos_norm[f]
        
        # Calculamos utilidad total ponderada
        utilidades = np.zeros(num_opciones)
        for f in factores:
            utilidades += self.pesos[f] * datos_norm[f]
        
        # Preparamos resultado detallado
        resultado = {
            'utilidad_total': utilidades,
            'utilidades_parciales': {f: datos_norm[f] for f in factores}
        }
        
        return resultado
    
    def mejor_opcion(self, opciones):
        """
        Selecciona la opción con mayor utilidad.
        
        Args:
            opciones (list of dict): Lista de opciones a evaluar.
            
        Returns:
            int: Índice de la mejor opción.
            dict: Detalles de utilidades calculadas.
        """
        resultado = self.calcular_utilidad(opciones)
        mejor_idx = np.argmax(resultado['utilidad_total'])
        return mejor_idx, resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos la importancia de cada factor para el agente
    factores_importancia = {
        'tiempo': 0.6,    # Muy importante
        'costo': 0.3,      # Moderadamente importante
        'comodidad': 0.1   # Poco importante
    }
    
    # Creamos el agente
    agente = AgenteUtilidad(factores_importancia)
    
    # Definimos las opciones disponibles (rutas en este caso)
    opciones_rutas = [
        {'tiempo': 30, 'costo': 100, 'comodidad': 3},  # Ruta rápida pero cara
        {'tiempo': 45, 'costo': 80, 'comodidad': 4},    # Ruta intermedia
        {'tiempo': 60, 'costo': 50, 'comodidad': 2}     # Ruta lenta pero barata
    ]
    
    # Encontramos la mejor opción
    mejor_idx, utilidades = agente.mejor_opcion(opciones_rutas)
    
    # Mostramos resultados
    print(f"Mejor opción: Ruta {mejor_idx + 1}")
    print(f"Utilidad total: {utilidades['utilidad_total'][mejor_idx]:.2f}")
    print("\nDetalles de utilidades:")
    for i, opcion in enumerate(opciones_rutas):
        print(f"\nRuta {i+1}:")
        print(f"  - Atributos: {opcion}")
        print(f"  - Utilidad total: {utilidades['utilidad_total'][i]:.2f}")
        for f in factores_importancia:
            print(f"  - Utilidad {f}: {utilidades['utilidades_parciales'][f][i]:.2f} (peso: {agente.pesos[f]:.2f})")