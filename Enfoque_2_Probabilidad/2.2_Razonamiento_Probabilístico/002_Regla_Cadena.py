from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# ======================
# 1. DEFINICIÓN DEL MODELO
# ======================
modelo = BayesianNetwork([
    ('Clima', 'Riego'),       # El clima afecta el riego
    ('Clima', 'Cosecha'),     # El clima afecta la cosecha
    ('Riego', 'Cosecha'),     # El riego afecta la cosecha
    ('TipoSuelo', 'Cosecha')  # El tipo de suelo afecta la cosecha
])

# ======================
# 2. TABLAS DE PROBABILIDAD CONDICIONAL (CPDs)
# ======================

# Clima (Soleado, Nublado, Lluvioso)
cpd_clima = TabularCPD(
    variable='Clima',
    variable_card=3,
    values=[[0.6], [0.3], [0.1]]  # P(Clima)
)

# Riego (Sí, No) - Depende del Clima
cpd_riego = TabularCPD(
    variable='Riego',
    variable_card=2,
    values=[
        # Soleado, Nublado, Lluvioso
        [0.8, 0.5, 0.1],  # P(Riego=No | Clima)
        [0.2, 0.5, 0.9]   # P(Riego=Sí | Clima)
    ],
    evidence=['Clima'],
    evidence_card=[3]
)

# TipoSuelo (Arenoso, Arcilloso)
cpd_suelo = TabularCPD(
    variable='TipoSuelo',
    variable_card=2,
    values=[[0.7], [0.3]]  # P(TipoSuelo)
)

# Cosecha (Buena, Mala) - Depende de Clima, Riego y TipoSuelo
cpd_cosecha = TabularCPD(
    variable='Cosecha',
    variable_card=2,
    values=[
        # Combinaciones de Clima (S,N,L), Riego (N,S), Suelo (Arenoso, Arcilloso)
        [0.9, 0.6, 0.8, 0.3, 0.5, 0.2, 0.7, 0.1, 0.4, 0.05, 0.3, 0.01],  # P(Cosecha=Buena | ...)
        [0.1, 0.4, 0.2, 0.7, 0.5, 0.8, 0.3, 0.9, 0.6, 0.95, 0.7, 0.99]   # P(Cosecha=Mala | ...)
    ],
    evidence=['Clima', 'Riego', 'TipoSuelo'],
    evidence_card=[3, 2, 2]
)

# Añadir CPDs al modelo
modelo.add_cpds(cpd_clima, cpd_riego, cpd_suelo, cpd_cosecha)

# ======================
# 3. INFERENCIA CON REGLA DE LA CADENA
# ======================
inferencia = VariableElimination(modelo)

# Ejemplo 1: Probabilidad conjunta P(Clima=Lluvioso, Riego=Sí, Cosecha=Buena)
prob_conjunta = inferencia.query(
    variables=['Cosecha'],
    evidence={'Clima': 2, 'Riego': 1}  # Lluvioso=2, Sí=1
)

print("Probabilidad de Cosecha=Buena dado Clima=Lluvioso y Riego=Sí:")
print(prob_conjunta)

# Ejemplo 2: Probabilidad de Clima dado Cosecha=Mala
prob_clima = inferencia.query(
    variables=['Clima'],
    evidence={'Cosecha': 1}  # Mala=1
)

print("\nProbabilidad de Clima dado Cosecha=Mala:")
print(prob_clima)