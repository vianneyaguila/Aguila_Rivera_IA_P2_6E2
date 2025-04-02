from typing import List, Dict, Optional

class CSP:
    def __init__(self, variables: List[str], dominios: Dict[str, List[int]]):
        """
        Inicializa un CSP genérico
        Args:
            variables: Lista de nombres de variables
            dominios: Diccionario {variable: lista de valores posibles}
        """
        self.variables = variables
        self.dominios = dominios
        self.restricciones = {v: [] for v in variables}
    
    def agregar_restriccion(self, funcion_restriccion, variables: List[str]):
        """
        Añade una restricción al CSP
        Args:
            funcion_restriccion: Función que evalúa si la restricción se cumple
            variables: Lista de variables involucradas en la restricción
        """
        for var in variables:
            if var not in self.variables:
                raise ValueError(f"Variable {var} no definida")
            self.restricciones[var].append((funcion_restriccion, variables))
    
    def consistente(self, variable: str, asignacion: Dict[str, int]) -> bool:
        """
        Verifica si un valor propuesto para una variable es consistente
        Args:
            variable: Variable a verificar
            asignacion: Asignación actual de variables
        Returns:
            bool: True si es consistente con todas las restricciones
        """
        for restriccion, variables in self.restricciones[variable]:
            # Filtra variables ya asignadas relevantes para esta restricción
            vars_asignadas = {v: asignacion[v] for v in variables if v in asignacion}
            if not restriccion(vars_asignadas):
                return False
        return True
    
    def backtracking_search(self, asignacion: Dict[str, int] = {}) -> Optional[Dict[str, int]]:
        """
        Implementa backtracking recursivo para resolver el CSP
        Args:
            asignacion: Asignación parcial actual
        Returns:
            Dict: Asignación completa solución o None si no hay solución
        """
        # 1. Verificar si la asignación está completa
        if len(asignacion) == len(self.variables):
            return asignacion
        
        # 2. Seleccionar variable no asignada (heurística: MRV)
        no_asignadas = [v for v in self.variables if v not in asignacion]
        var = min(no_asignadas, key=lambda v: len(self.dominios[v]))
        
        # 3. Probar valores del dominio (heurística: LCV)
        for valor in self.dominios[var]:
            asignacion_prueba = asignacion.copy()
            asignacion_prueba[var] = valor
            
            if self.consistente(var, asignacion_prueba):
                resultado = self.backtracking_search(asignacion_prueba)
                if resultado is not None:
                    return resultado
        
        return None

def resolver_sudoku(tablero: List[List[int]]) -> Optional[List[List[int]]]:
    """
    Resuelve un Sudoku usando CSP
    Args:
        tablero: Matriz 9x9 con 0 en casillas vacías
    Returns:
        Matriz 9x9 resuelta o None si no tiene solución
    """
    # 1. Inicializar CSP
    variables = [f"{i}{j}" for i in range(9) for j in range(9)]
    dominios = {v: list(range(1, 10)) if tablero[int(v[0])][int(v[1])] == 0 
               else tablero[int(v[0])][int(v[1])] for v in variables}
    
    csp = CSP(variables, dominios)
    
    # 2. Añadir restricciones de fila, columna y subcuadrícula 3x3
    for i in range(9):
        # Restricciones de fila
        vars_fila = [f"{i}{j}" for j in range(9)]
        csp.agregar_restriccion(lambda a: len(set(a.values())) == len(a), vars_fila)
        
        # Restricciones de columna
        vars_col = [f"{j}{i}" for j in range(9)]
        csp.agregar_restriccion(lambda a: len(set(a.values())) == len(a), vars_col)
    
    # Restricciones de subcuadrícula 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            vars_cuad = [f"{i+x}{j+y}" for x in range(3) for y in range(3)]
            csp.agregar_restriccion(lambda a: len(set(a.values())) == len(a), vars_cuad)
    
    # 3. Resolver
    solucion = csp.backtracking_search()
    
    if solucion is None:
        return None
    
    # 4. Convertir solución a matriz 9x9
    resultado = [[0]*9 for _ in range(9)]
    for var, val in solucion.items():
        i, j = map(int, var)
        resultado[i][j] = val
    
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Sudoku difícil (0 = vacío)
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    solucion = resolver_sudoku(sudoku)
    
    if solucion:
        print("Solución encontrada:")
        for fila in solucion:
            print(fila)
    else:
        print("No se encontró solución")