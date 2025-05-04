import re

# Función para skolemizar una expresión lógica
def skolemizar(formula):
    skolem_funcs = []
    var_universales = []
    skolem_index = 0

    # Reemplaza cuantificadores
    while "∃" in formula or "∀" in formula:
        formula = formula.strip()

        if formula.startswith("∀"):
            var = formula[1]
            var_universales.append(var)
            formula = formula[2:].strip()

        elif formula.startswith("∃"):
            var = formula[1]
            skolem_index += 1
            if var_universales:
                # Crea función de Skolem dependiente de variables universales
                skolem_func = f"f{skolem_index}({','.join(var_universales)})"
            else:
                # Si no hay variables universales, solo una constante Skolem
                skolem_func = f"c{skolem_index}"
            skolem_funcs.append((var, skolem_func))
            formula = formula[2:].strip()

    # Reemplaza variables existenciales por funciones Skolem
    for var, skolem_func in skolem_funcs:
        formula = re.sub(rf'\b{var}\b', skolem_func, formula)

    return formula

# Fórmula de entrada
expresion = "∀x ∃y P(x, y)"
print("Expresión original:", expresion)

# Skolemización
skolemizada = skolemizar(expresion)
print("Después de Skolemización:", skolemizada)
