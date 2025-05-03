# Importamos herramientas de lógica simbólica
from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent, to_cnf, satisfiable

# Definimos variables proposicionales
p, q = symbols('p q')

# Fórmulas para analizar
formula1 = Not(Or(p, q))             # ¬(p ∨ q)
formula2 = And(Not(p), Not(q))       # (¬p ∧ ¬q)

# 1. Verificar Equivalencia
es_equivalente = Equivalent(formula1, formula2)

# 2. Verificar Validez
validez = satisfiable(Not(es_equivalente)) == False

# 3. Verificar Satisfacibilidad
satisfacible = satisfiable(formula1)

# Mostrar resultados
print("Fórmula 1: ¬(p ∨ q)")
print("Fórmula 2: (¬p ∧ ¬q)")

print("\n¿Son equivalentes?:", es_equivalente)
print("¿La equivalencia es válida?:", validez)
print("¿La Fórmula 1 es satisfacible?:", satisfacible)
