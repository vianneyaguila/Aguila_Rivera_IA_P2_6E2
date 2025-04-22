import numpy as np
from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Crear modelo de Red Bayesiana Dinámica
def crear_modelo_clima():
    # Definir estructura de la DBN
    dbn = DBN()
    
    # Nodos para tiempo t
    dbn.add_nodes_from(['Lluvia_t', 'Nubes_t'])
    # Nodos para tiempo t+1
    dbn.add_nodes_from(['Lluvia_t+1', 'Nubes_t+1'])
    
    # Arcos intra-tiempo (en t)
    dbn.add_edge('Nubes_t', 'Lluvia_t')
    # Arcos inter-tiempo (de t a t+1)
    dbn.add_edge('Lluvia_t', 'Lluvia_t+1')
    dbn.add_edge('Nubes_t', 'Nubes_t+1')
    
    # Definir CPDs (Tablas de Probabilidad Condicional)
    
    # CPD inicial para Nubes (t=0)
    cpd_nubes = TabularCPD(
        variable='Nubes_t',
        variable_card=2,  # 0: Pocas nubes, 1: Muchas nubes
        values=[[0.7], [0.3]]  # P(Nubes_t)
    )
    
    # CPD para Lluvia dado Nubes (t=0)
    cpd_lluvia = TabularCPD(
        variable='Lluvia_t',
        variable_card=2,  # 0: No llueve, 1: Llueve
        evidence=['Nubes_t'],
        evidence_card=[2],
        values=[[0.8, 0.2],  # P(Lluvia=0|Nubes)
                [0.2, 0.8]]  # P(Lluvia=1|Nubes)
    )
    
    # CPD de transición para Nubes (t+1 dado t)
    cpd_trans_nubes = TabularCPD(
        variable='Nubes_t+1',
        variable_card=2,
        evidence=['Nubes_t'],
        evidence_card=[2],
        values=[[0.6, 0.3],  # P(Nubes_t+1=0|Nubes_t)
                [0.4, 0.7]]  # P(Nubes_t+1=1|Nubes_t)
    )
    
    # CPD de transición para Lluvia (t+1 dado t)
    cpd_trans_lluvia = TabularCPD(
        variable='Lluvia_t+1',
        variable_card=2,
        evidence=['Lluvia_t'],
        evidence_card=[2],
        values=[[0.7, 0.3],  # P(Lluvia_t+1=0|Lluvia_t)
                [0.3, 0.7]]  # P(Lluvia_t+1=1|Lluvia_t)
    )
    
    # Añadir CPDs al modelo
    dbn.add_cpds(cpd_nubes, cpd_lluvia, cpd_trans_nubes, cpd_trans_lluvia)
    
    # Verificar modelo
    assert dbn.check_model()
    
    return dbn

# Ejemplo de uso
if __name__ == "__main__":
    # Crear modelo
    modelo = crear_modelo_clima()
    print("Modelo DBN creado correctamente")
    
    # Realizar inferencia
    inferencia = DBNInference(modelo)
    
    # Filtrado: P(Lluvia_t=1 | observaciones)
    # Supongamos que observamos Muchas nubes en t=0
    filtrado = inferencia.forward_inference(
        variables=['Lluvia_t'],
        evidence=[('Nubes_t', 1)]
    )
    print("\nProbabilidad de lluvia en t=0 dado Nubes_t=1:")
    print(filtrado['Lluvia_t'].values)
    
    # Predicción: P(Lluvia_t+1=1 | observaciones)
    prediccion = inferencia.forward_inference(
        variables=['Lluvia_t+1'],
        evidence=[('Nubes_t', 1)]
    )
    print("\nProbabilidad de lluvia en t=1 dado Nubes_t=1:")
    print(prediccion['Lluvia_t+1'].values)
    
    # Suavizado: P(Lluvia_t=1 | observaciones hasta t+1)
    # Supongamos que en t+1 observamos Lluvia_t+1=1
    suavizado = inferencia.backward_inference(
        variables=['Lluvia_t'],
        evidence=[('Nubes_t', 1), ('Lluvia_t+1', 1)]
    )
    print("\nProbabilidad de lluvia en t=0 dado Nubes_t=1 y Lluvia_t+1=1:")
    print(suavizado['Lluvia_t'].values)