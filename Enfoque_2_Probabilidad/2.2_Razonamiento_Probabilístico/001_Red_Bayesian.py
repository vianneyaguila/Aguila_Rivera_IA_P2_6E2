# Importación de bibliotecas necesarias
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Definición de la estructura de la red
model = BayesianNetwork([
    ('Enfermedad', 'Fiebre'),       # La enfermedad causa fiebre
    ('Enfermedad', 'Dolor'),        # La enfermedad causa dolor
    ('Enfermedad', 'Fatiga'),       # La enfermedad causa fatiga
    ('ActividadFisica', 'Fatiga')   # La actividad física también causa fatiga
])

# 2. Definición de las Tablas de Probabilidad Condicional (CPD)

# CPD para Enfermedad (variable raíz)
cpd_enfermedad = TabularCPD(
    variable='Enfermedad',
    variable_card=3,  # 3 posibles valores: Ninguna, Gripe, COVID
    values=[[0.7], [0.2], [0.1]]  # Probabilidades a priori
)

# CPD para Fiebre (depende de Enfermedad)
cpd_fiebre = TabularCPD(
    variable='Fiebre',
    variable_card=2,  # Sí o No
    values=[
        [0.95, 0.3, 0.1],   # P(Fiebre=No | Enfermedad)
        [0.05, 0.7, 0.9]    # P(Fiebre=Sí | Enfermedad)
    ],
    evidence=['Enfermedad'],
    evidence_card=[3]
)

# CPD para Dolor (depende de Enfermedad)
cpd_dolor = TabularCPD(
    variable='Dolor',
    variable_card=2,
    values=[
        [0.8, 0.2, 0.1],   # P(Dolor=No | Enfermedad)
        [0.2, 0.8, 0.9]     # P(Dolor=Sí | Enfermedad)
    ],
    evidence=['Enfermedad'],
    evidence_card=[3]
)

# CPD para ActividadFisica (variable raíz)
cpd_actividad = TabularCPD(
    variable='ActividadFisica',
    variable_card=2,
    values=[[0.6], [0.4]]  # 60% no hizo actividad, 40% sí
)

# CPD para Fatiga (depende de Enfermedad y ActividadFisica)
cpd_fatiga = TabularCPD(
    variable='Fatiga',
    variable_card=2,
    values=[
        # Ninguna, Gripe, COVID (para Enfermedad)
        [0.9, 0.3, 0.1],  # Actividad=No
        [0.7, 0.1, 0.05], # Actividad=Sí
        [0.1, 0.7, 0.9],  # Actividad=No
        [0.3, 0.9, 0.95]  # Actividad=Sí
    ],
    evidence=['Enfermedad', 'ActividadFisica'],
    evidence_card=[3, 2]
)

# 3. Añadir las CPDs al modelo
model.add_cpds(cpd_enfermedad, cpd_fiebre, cpd_dolor, cpd_actividad, cpd_fatiga)

# 4. Verificar que el modelo es válido
print("El modelo es válido?", model.check_model())

# 5. Crear un motor de inferencia
inferencia = VariableElimination(model)

# 6. Ejemplo de consulta: Probabilidad de COVID dado que hay fiebre y dolor
resultado = inferencia.query(
    variables=['Enfermedad'],
    evidence={'Fiebre': 1, 'Dolor': 1}  # 1 representa "Sí"
)
print("\nProbabilidad de enfermedad dado Fiebre=Sí y Dolor=Sí:")
print(resultado)

# 7. Ejemplo de consulta: Probabilidad de fatiga dado que hizo actividad física
resultado_fatiga = inferencia.query(
    variables=['Fatiga'],
    evidence={'ActividadFisica': 1}
)
print("\nProbabilidad de fatiga dado ActividadFisica=Sí:")
print(resultado_fatiga)