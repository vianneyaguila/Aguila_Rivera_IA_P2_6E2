import numpy as np

class NodoChance:
    """Nodo que representa una variable aleatoria (incertidumbre)."""
    def __init__(self, nombre, valores, probabilidades):
        """
        Args:
            nombre (str): Nombre del nodo (ej. "Fiebre").
            valores (list): Posibles valores (ej. ["Alta", "Baja"]).
            probabilidades (dict): Probabilidades condicionales.
        """
        self.nombre = nombre
        self.valores = valores
        self.probabilidades = probabilidades

    def prob(self, valor, evidencia=None):
        """Retorna P(valor | evidencia)."""
        if evidencia is None:
            return self.probabilidades.get(valor, 0)
        else:
            # Si hay padres, se usa probabilidad condicional
            key = tuple(evidencia.items())
            return self.probabilidades.get(key, {}).get(valor, 0)

class NodoDecision:
    """Nodo que representa una decisión posible."""
    def __init__(self, nombre, opciones):
        """
        Args:
            nombre (str): Nombre de la decisión (ej. "Tratamiento").
            opciones (list): Acciones posibles (ej. ["Antibiótico", "Reposo"]).
        """
        self.nombre = nombre
        self.opciones = opciones

class NodoUtilidad:
    """Nodo que asigna utilidad a combinaciones de decisiones y eventos."""
    def __init__(self, nombre, valores_utilidad):
        """
        Args:
            nombre (str): Nombre del nodo (ej. "Utilidad_Paciente").
            valores_utilidad (dict): Utilidad para cada combinación.
        """
        self.nombre = nombre
        self.valores_utilidad = valores_utilidad

    def utilidad(self, decision, estado):
        """Retorna la utilidad dada una decisión y un estado."""
        key = (decision, tuple(estado.items()))
        return self.valores_utilidad.get(key, 0)

class RedDecision:
    """Red de Decisión que conecta nodos de chance, decisión y utilidad."""
    def __init__(self):
        self.nodos_chance = {}
        self.nodos_decision = {}
        self.nodos_utilidad = {}

    def agregar_nodo_chance(self, nodo):
        self.nodos_chance[nodo.nombre] = nodo

    def agregar_nodo_decision(self, nodo):
        self.nodos_decision[nodo.nombre] = nodo

    def agregar_nodo_utilidad(self, nodo):
        self.nodos_utilidad[nodo.nombre] = nodo

    def mejor_decision(self, evidencia=None):
        """
        Encuentra la decisión con máxima utilidad esperada.
        
        Args:
            evidencia (dict): Evidencia observada (ej. {"Fiebre": "Alta"}).
            
        Returns:
            tuple: (mejor_opcion, utilidad_esperada)
        """
        if evidencia is None:
            evidencia = {}

        mejor_opcion = None
        max_utilidad = -np.inf

        # Para cada posible decisión
        for decision_nodo in self.nodos_decision.values():
            for opcion in decision_nodo.opciones:
                utilidad_total = 0

                # Calcular utilidad esperada para esta decisión
                for utilidad_nodo in self.nodos_utilidad.values():
                    # Sumar sobre todos los estados posibles
                    for estado in self._generar_estados(evidencia):
                        prob_estado = self._probabilidad_estado(estado, evidencia)
                        utilidad = utilidad_nodo.utilidad(opcion, estado)
                        utilidad_total += prob_estado * utilidad

                # Actualizar mejor decisión
                if utilidad_total > max_utilidad:
                    max_utilidad = utilidad_total
                    mejor_opcion = opcion

        return mejor_opcion, max_utilidad

    def _generar_estados(self, evidencia):
        """Genera combinaciones de estados posibles."""
        # Implementación simplificada (en realidad requiere enumeración más compleja)
        estados = [{}]  # Caso base
        for nombre, nodo in self.nodos_chance.items():
            if nombre not in evidencia:
                nuevos_estados = []
                for estado in estados:
                    for valor in nodo.valores:
                        nuevo_estado = estado.copy()
                        nuevo_estado[nombre] = valor
                        nuevos_estados.append(nuevo_estado)
                estados = nuevos_estados
        return estados

    def _probabilidad_estado(self, estado, evidencia):
        """Calcula P(estado | evidencia)."""
        prob = 1.0
        for nombre, valor in estado.items():
            if nombre in self.nodos_chance:
                nodo = self.nodos_chance[nombre]
                prob *= nodo.prob(valor, evidencia)
        return prob

# Ejemplo: Diagnóstico Médico
if __name__ == "__main__":
    # 1. Definir nodos de chance (incertidumbre)
    fiebre = NodoChance(
        nombre="Fiebre",
        valores=["Alta", "Baja"],
        probabilidades={"Alta": 0.3, "Baja": 0.7}
    )

    infeccion = NodoChance(
        nombre="Infección",
        valores=["Bacteriana", "Viral", "Ninguna"],
        probabilidades={
            ("Alta",): {"Bacteriana": 0.6, "Viral": 0.3, "Ninguna": 0.1},
            ("Baja",): {"Bacteriana": 0.1, "Viral": 0.2, "Ninguna": 0.7}
        }
    )

    # 2. Definir nodo de decisión (tratamiento)
    tratamiento = NodoDecision(
        nombre="Tratamiento",
        opciones=["Antibiótico", "Antiviral", "Reposo"]
    )

    # 3. Definir nodo de utilidad (beneficio del paciente)
    utilidad_paciente = NodoUtilidad(
        nombre="Utilidad_Paciente",
        valores_utilidad={
            ("Antibiótico", ("Fiebre", "Alta", "Infección", "Bacteriana")): 90,
            ("Antibiótico", ("Fiebre", "Alta", "Infección", "Viral")): 30,
            ("Antibiótico", ("Fiebre", "Alta", "Infección", "Ninguna")): 10,
            ("Antiviral", ("Fiebre", "Alta", "Infección", "Viral")): 80,
            ("Antiviral", ("Fiebre", "Alta", "Infección", "Bacteriana")): 20,
            ("Reposo", ("Fiebre", "Alta", "Infección", "Viral")): 70,
            ("Reposo", ("Fiebre", "Alta", "Infección", "Bacteriana")): 40,
            # ... (completar para todas las combinaciones)
        }
    )

    # 4. Construir red de decisión
    red = RedDecision()
    red.agregar_nodo_chance(fiebre)
    red.agregar_nodo_chance(infeccion)
    red.agregar_nodo_decision(tratamiento)
    red.agregar_nodo_utilidad(utilidad_paciente)

    # 5. Tomar decisión basada en evidencia (ej. fiebre alta)
    mejor_opcion, utilidad = red.mejor_decision(evidencia={"Fiebre": "Alta"})
    print(f"Mejor decisión: {mejor_opcion} (Utilidad esperada: {utilidad:.2f})")