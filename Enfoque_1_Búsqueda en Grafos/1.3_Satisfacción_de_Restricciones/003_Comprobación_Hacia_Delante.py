def forward_checking(sudoku, fila, col, num, dominios):
    """
    Realiza comprobación hacia delante: elimina 'num' de los dominios de las celdas relacionadas.
    
    Args:
        sudoku (list): Matriz 9x9 representando el tablero.
        fila (int): Fila de la celda actual.
        col (int): Columna de la celda actual.
        num (int): Número que se quiere asignar.
        dominios (dict): Diccionario con dominios posibles de cada celda.
    
    Returns:
        bool: True si la asignación es válida, False si deja un dominio vacío.
    """
    # Copia temporal de dominios para revertir cambios si falla
    dominios_temp = {k: v.copy() for k, v in dominios.items()}
    
    # Eliminar 'num' de las celdas en la misma fila, columna y cuadrante
    for i in range(9):
        # Misma fila
        if (fila, i) in dominios and num in dominios[(fila, i)]:
            dominios[(fila, i)].remove(num)
            if not dominios[(fila, i)]:  # Si el dominio queda vacío
                dominios.update(dominios_temp)  # Revertir cambios
                return False
        
        # Misma columna
        if (i, col) in dominios and num in dominios[(i, col)]:
            dominios[(i, col)].remove(num)
            if not dominios[(i, col)]:
                dominios.update(dominios_temp)
                return False
    
    # Mismo cuadrante 3x3
    cuadrante_fila, cuadrante_col = fila // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            celda = (cuadrante_fila + i, cuadrante_col + j)
            if celda in dominios and num in dominios[celda]:
                dominios[celda].remove(num)
                if not dominios[celda]:
                    dominios.update(dominios_temp)
                    return False
    
    return True  # Asignación válida

def resolver_sudoku(sudoku):
    """
    Resuelve el Sudoku usando Forward Checking + Backtracking.
    
    Args:
        sudoku (list): Tablero 9x9 (0 = vacío).
    
    Returns:
        bool: True si encontró solución, False si no.
    """
    # Inicializar dominios: celdas vacías pueden ser 1-9
    dominios = {}
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                dominios[(i, j)] = set(range(1, 10))
    
    # Aplicar restricciones iniciales (números fijos)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                if not forward_checking(sudoku, i, j, sudoku[i][j], dominios):
                    return False  # Sudoku inválido
    
    # Función auxiliar recursiva
    def backtrack():
        if not dominios:  # Todas las celdas asignadas
            return True
    
        # Seleccionar la celda con menor dominio (heurística MRV)
        celda = min(dominios.keys(), key=lambda k: len(dominios[k]))
        fila, col = celda
        valores = list(dominios[celda])
        
        for num in valores:
            sudoku[fila][col] = num
            dominios_antes = {k: v.copy() for k, v in dominios.items()}
            del dominios[celda]  # Celda ya asignada
            
            # Forward Checking
            if forward_checking(sudoku, fila, col, num, dominios):
                if backtrack():  # Llamada recursiva
                    return True
            
            # Backtrack si falla
            sudoku[fila][col] = 0
            dominios[celda] = dominios_antes[celda]
            dominios.update({k: v for k, v in dominios_antes.items() if k != celda})
        
        return False
    
    return backtrack()

# Ejemplo de uso
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

if resolver_sudoku(sudoku):
    print("Solución encontrada:")
    for fila in sudoku:
        print(fila)
else:
    print("No hay solución.")