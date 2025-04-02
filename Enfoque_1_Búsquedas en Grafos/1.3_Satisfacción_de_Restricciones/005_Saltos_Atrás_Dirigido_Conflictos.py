def conflict_directed_backjumping(csp, asignacion={}, nivel=0, conflictos=None):
    """
    Implementa CBJ para resolver un CSP.
    
    Args:
        csp (dict): Diccionario con variables, dominios y restricciones.
        asignacion (dict): Asignación parcial actual.
        nivel (int): Nivel actual de profundidad en la búsqueda.
        conflictos (dict): Diccionario de conjuntos de conflicto por variable.
    
    Returns:
        dict: Asignación solución o None si no hay solución.
    """
    if conflictos is None:
        conflictos = {v: set() for v in csp["variables"]}
    
    if len(asignacion) == len(csp["variables"]):
        return asignacion  # Solución encontrada
    
    var = seleccionar_variable_no_asignada(csp, asignacion)
    for valor in ordenar_valores(csp, var, asignacion):
        if es_consistente(var, valor, asignacion, csp["restricciones"]):
            asignacion[var] = valor
            resultado = conflict_directed_backjumping(csp, asignacion, nivel + 1, conflictos)
            if resultado is not None:
                return resultado
            del asignacion[var]  # Backtrack estándar
        else:
            # Registrar variables en conflicto
            nuevas_variables_conflicto = obtener_variables_conflicto(var, valor, asignacion, csp["restricciones"])
            conflictos[var].update(nuevas_variables_conflicto)
    
    # Determinar el nivel de salto (máxima profundidad de las variables en conflicto)
    if conflictos[var]:
        max_nivel_conflicto = max([nivel for v in conflictos[var] for nivel in [list(asignacion.keys()).index(v)]])
        return None  # Indica que se debe saltar al max_nivel_conflicto
    
    return None

def seleccionar_variable_no_asignada(csp, asignacion):
    """
    Heurística: Selecciona la variable con menor dominio restante (MRV).
    """
    variables_no_asignadas = [v for v in csp["variables"] if v not in asignacion]
    return min(variables_no_asignadas, key=lambda v: len(csp["dominios"][v]))

def ordenar_valores(csp, var, asignacion):
    """
    Heurística: Ordena valores por Least Constraining Value (LCV).
    """
    def contar_conflictos(valor):
        return sum(1 for v in asignacion 
                   if not es_consistente(var, valor, asignacion, csp["restricciones"]))
    
    return sorted(csp["dominios"][var], key=contar_conflictos)

def es_consistente(var, valor, asignacion, restricciones):
    """
    Verifica si var=valor es consistente con la asignación actual.
    """
    for (v1, v2), restr in restricciones.items():
        if v1 == var and v2 in asignacion and not restr(valor, asignacion[v2]):
            return False
        elif v2 == var and v1 in asignacion and not restr(asignacion[v1], valor):
            return False
    return True

def obtener_variables_conflicto(var, valor, asignacion, restricciones):
    """
    Retorna variables en asignación que causan conflicto con var=valor.
    """
    conflicto = set()
    for (v1, v2), restr in restricciones.items():
        if v1 == var and v2 in asignacion and not restr(valor, asignacion[v2]):
            conflicto.add(v2)
        elif v2 == var and v1 in asignacion and not restr(asignacion[v1], valor):
            conflicto.add(v1)
    return conflicto

# Ejemplo de uso
if __name__ == "__main__":
    # Definir CSP: 3 variables (A, B, C) con dominios {1, 2, 3} y restricciones A != B != C
    csp = {
        "variables": ["A", "B", "C"],
        "dominios": {"A": {1, 2, 3}, "B": {1, 2, 3}, "C": {1, 2, 3}},
        "restricciones": {
            ("A", "B"): lambda a, b: a != b,
            ("B", "C"): lambda b, c: b != c,
            ("A", "C"): lambda a, c: a != c
        }
    }
    
    solucion = conflict_directed_backjumping(csp)
    print("Solución:", solucion)