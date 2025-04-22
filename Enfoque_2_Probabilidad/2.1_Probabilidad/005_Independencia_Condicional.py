import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

class ConditionalIndependenceAnalyzer:
    def __init__(self):
        """Inicializa el analizador con estructuras de datos vacías"""
        self.model = None
        self.inference_engine = None
    
    def create_medical_diagnosis_model(self):
        """
        Crea una red bayesiana de ejemplo para diagnóstico médico que demuestra 
        independencia condicional entre síntomas dada la enfermedad.
        
        Estructura:
           Enfermedad -> Síntoma1
           Enfermedad -> Síntoma2
        """
        # Definir estructura del modelo
        self.model = BayesianNetwork([('Enfermedad', 'Fiebre'), 
                                    ('Enfermedad', 'Dolor')])
        
        # Definir probabilidades condicionales (CPDs)
        cpd_enfermedad = TabularCPD(
            variable='Enfermedad',
            variable_card=2,  # 0: No enfermo, 1: Enfermo
            values=[[0.9], [0.1]]  # P(Enfermo=0)=90%, P(Enfermo=1)=10%
        )
        
        cpd_fiebre = TabularCPD(
            variable='Fiebre',
            variable_card=2,  # 0: No fiebre, 1: Fiebre
            values=[
                [0.8, 0.1],  # P(Fiebre=0|Enfermedad=0), P(Fiebre=0|Enfermedad=1)
                [0.2, 0.9]   # P(Fiebre=1|Enfermedad=0), P(Fiebre=1|Enfermedad=1)
            ],
            evidence=['Enfermedad'],
            evidence_card=[2]
        )
        
        cpd_dolor = TabularCPD(
            variable='Dolor',
            variable_card=2,  # 0: No dolor, 1: Dolor
            values=[
                [0.7, 0.05],  # P(Dolor=0|Enfermedad=0), P(Dolor=0|Enfermedad=1)
                [0.3, 0.95]    # P(Dolor=1|Enfermedad=0), P(Dolor=1|Enfermedad=1)
            ],
            evidence=['Enfermedad'],
            evidence_card=[2]
        )
        
        # Añadir CPDs al modelo
        self.model.add_cpds(cpd_enfermedad, cpd_fiebre, cpd_dolor)
        
        # Verificar consistencia del modelo
        if not self.model.check_model():
            raise ValueError("El modelo contiene inconsistencias")
        
        # Inicializar motor de inferencia
        self.inference_engine = VariableElimination(self.model)
    
    def visualize_model(self):
        """Visualiza la estructura de la red bayesiana"""
        if self.model is None:
            raise ValueError("Primero debe crear un modelo")
            
        nx_graph = nx.DiGraph()
        nx_graph.add_edges_from(self.model.edges())
        
        pos = nx.spring_layout(nx_graph)
        plt.figure(figsize=(8, 6))
        nx.draw(nx_graph, pos, with_labels=True, 
                node_size=3000, node_color='skyblue', 
                font_size=12, font_weight='bold', arrowsize=20)
        plt.title("Red Bayesiana: Independencia Condicional", fontsize=14)
        plt.show()
    
    def test_conditional_independence(self, var1, var2, given):
        """
        Prueba si var1 es independiente de var2 dado 'given'
        
        Args:
            var1 (str): Nombre primera variable
            var2 (str): Nombre segunda variable
            given (list): Lista de variables de condicionamiento
            
        Returns:
            bool: True si son condicionalmente independientes
        """
        if self.model is None:
            raise ValueError("Primero debe crear un modelo")
            
        return self.model.is_active_trail(var1, var2, observed=given)
    
    def demonstrate_independence(self):
        """
        Demuestra independencia condicional mediante:
        1. Mostrar que síntomas son dependientes marginalmente
        2. Mostrar que son independientes dada la enfermedad
        """
        if self.inference_engine is None:
            raise ValueError("Motor de inferencia no inicializado")
        
        # 1. Probabilidad conjunta sin condicionar
        joint_no_condition = self.inference_engine.query(
            variables=['Fiebre', 'Dolor'], 
            joint=True
        )
        print("\nDistribución conjunta SIN condicionar:")
        print(joint_no_condition)
        
        # 2. Probabilidad conjunta dada enfermedad
        joint_given_disease0 = self.inference_engine.query(
            variables=['Fiebre', 'Dolor'], 
            evidence={'Enfermedad': 0},
            joint=True
        )
        print("\nDistribución conjunta DADO Enfermedad=0:")
        print(joint_given_disease0)
        
        joint_given_disease1 = self.inference_engine.query(
            variables=['Fiebre', 'Dolor'], 
            evidence={'Enfermedad': 1},
            joint=True
        )
        print("\nDistribución conjunta DADO Enfermedad=1:")
        print(joint_given_disease1)
        
        # 3. Factorización para verificar independencia
        print("\nVerificación de independencia condicional:")
        print("Fiebre ⊥ Dolor | Enfermedad?:", 
              self.test_conditional_independence('Fiebre', 'Dolor', ['Enfermedad']))
        
        # 4. Mostrar que no son marginalmente independientes
        print("Fiebre ⊥ Dolor (sin condicionar)?:", 
              self.test_conditional_independence('Fiebre', 'Dolor', []))

# Ejemplo de uso completo
if __name__ == "__main__":
    analyzer = ConditionalIndependenceAnalyzer()
    
    # 1. Crear modelo de diagnóstico médico
    analyzer.create_medical_diagnosis_model()
    
    # 2. Visualizar estructura del modelo
    analyzer.visualize_model()
    
    # 3. Demostrar independencia condicional
    analyzer.demonstrate_independence()