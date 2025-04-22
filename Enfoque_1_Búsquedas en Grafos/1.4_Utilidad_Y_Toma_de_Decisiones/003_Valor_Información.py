import numpy as np

class ValorInformacion:
    """Calcula el Valor de la Información (VOI) para una decisión."""
    def __init__(self, estados, acciones, utilidades, prob_a_priori):
        """
        Args:
            estados (list): Posibles estados del mundo (ej. ["Enfermo", "Sano"]).
            acciones (list): Decisiones posibles (ej. ["Tratar", "No tratar"]).
            utilidades (dict): Utilidad U(a,s) para cada acción y estado.
            prob_a_priori (dict): Probabilidad inicial P(s) de cada estado.
        """
        self.estados = estados
        self.acciones = acciones
        self.utilidades = utilidades
        self.prob_a_priori = prob_a_priori

    def utilidad_esperada_sin_info(self):
        """Calcula la utilidad esperada sin información adicional."""
        mejor_utilidad = -np.inf
        mejor_accion = None

        for a in self.acciones:
            utilidad = 0
            for s in self.estados:
                utilidad += self.prob_a_priori[s] * self.utilidades[(a, s)]
            
            if utilidad > mejor_utilidad:
                mejor_utilidad = utilidad
                mejor_accion = a

        return mejor_accion, mejor_utilidad

    def utilidad_esperada_con_info(self, evidencias, prob_evidencia_dado_estado):
        """
        Calcula la utilidad esperada si obtenemos información adicional.
        
        Args:
            evidencias (list): Posibles resultados de la observación (ej. ["Test+", "Test-"]).
            prob_evidencia_dado_estado (dict): P(e|s) para cada evidencia y estado.
        """
        # Paso 1: Calcular P(e) para cada evidencia
        prob_evidencia = {e: 0 for e in evidencias}
        for e in evidencias:
            for s in self.estados:
                prob_evidencia[e] += self.prob_a_priori[s] * prob_evidencia_dado_estado[(e, s)]

        # Paso 2: Calcular P(s|e) usando Bayes: P(s|e) = P(e|s) * P(s) / P(e)
        prob_estado_dado_evidencia = {}
        for e in evidencias:
            for s in self.estados:
                if prob_evidencia[e] > 0:
                    prob_estado_dado_evidencia[(s, e)] = (
                        prob_evidencia_dado_estado[(e, s)] * self.prob_a_priori[s] / prob_evidencia[e]
                    )
                else:
                    prob_estado_dado_evidencia[(s, e)] = 0

        # Paso 3: Para cada evidencia e, encontrar la mejor acción a|e
        utilidad_total = 0
        for e in evidencias:
            mejor_utilidad_e = -np.inf
            for a in self.acciones:
                utilidad = 0
                for s in self.estados:
                    utilidad += prob_estado_dado_evidencia[(s, e)] * self.utilidades[(a, s)]
                
                if utilidad > mejor_utilidad_e:
                    mejor_utilidad_e = utilidad
            
            utilidad_total += prob_evidencia[e] * mejor_utilidad_e

        return utilidad_total

    def calcular_voi(self, evidencias, prob_evidencia_dado_estado):
        """Calcula el Valor de la Información (VOI)."""
        _, util_sin_info = self.utilidad_esperada_sin_info()
        util_con_info = self.utilidad_esperada_con_info(evidencias, prob_evidencia_dado_estado)
        return max(0, util_con_info - util_sin_info)  # VOI no puede ser negativo

# Ejemplo: ¿Vale la pena hacer un test médico?
if __name__ == "__main__":
    # Definir estados, acciones y utilidades
    estados = ["Enfermo", "Sano"]
    acciones = ["Tratar", "No tratar"]
    utilidades = {
        ("Tratar", "Enfermo"): 90,    # Tratar a un enfermo es muy útil
        ("Tratar", "Sano"): -10,       # Tratar a un sano tiene costo
        ("No tratar", "Enfermo"): -70, # No tratar a un enfermo es grave
        ("No tratar", "Sano"): 0       # No tratar a un sano es neutral
    }
    prob_a_priori = {"Enfermo": 0.2, "Sano": 0.8}  # 20% de prevalencia

    # Crear calculador de VOI
    voi_calculator = ValorInformacion(estados, acciones, utilidades, prob_a_priori)

    # Definir posibles resultados de un test (evidencias)
    evidencias = ["Test+", "Test-"]
    # Probabilidad P(e|s): Sensibilidad y especificidad del test
    prob_evidencia_dado_estado = {
        ("Test+", "Enfermo"): 0.9,  # Sensibilidad (90%)
        ("Test-", "Enfermo"): 0.1,
        ("Test+", "Sano"): 0.2,      # Falsos positivos (20%)
        ("Test-", "Sano"): 0.8       # Especificidad (80%)
    }

    # Calcular VOI
    voi = voi_calculator.calcular_voi(evidencias, prob_evidencia_dado_estado)
    print(f"Valor de la Información (VOI) del test médico: {voi:.2f}")

    # Interpretación
    if voi > 0:
        print("El test vale la pena porque mejora la decisión.")
    else:
        print("El test no aporta valor suficiente para justificar su uso.")