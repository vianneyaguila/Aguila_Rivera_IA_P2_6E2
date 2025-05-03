from sympy import symbols
from sympy.logic.boolalg import to_cnf, Or, And, Not
from sympy.logic.inference import satisfiable

# 1. Definimos proposiciones
p, q = symbols('p q')

# 2. Fórmula original
formula = Not(Or(p, q))  # ¬(p ∨ q)

# 3. Convertimos a Forma Normal Conjuntiva (FNC)
fnc = to_cnf(formula, simplify=True)

# 4. Verificamos satisfacibilidad (¿es contradictoria?)
es_satisfacible = satisfiable(fnc)

# 5. Mostramos resultados
print("Fórmula original:", formula)
print("Forma Normal Conjuntiva (FNC):", fnc)
print("¿Es satisfacible?:", es_satisfacible)
