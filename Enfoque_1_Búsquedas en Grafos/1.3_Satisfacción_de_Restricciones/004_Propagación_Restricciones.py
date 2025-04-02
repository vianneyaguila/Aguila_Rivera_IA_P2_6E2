from collections import deque

def AC3(csp, dominios, restricciones):
    """
    Implementa el algoritmo AC-3 para propagación de restricciones.
    
    Args:
        csp (dict): Diccionario de variables y sus dominios iniciales.
        restricciones (dict): Restricciones entre pares de variables.
    
    Returns:
        bool: True si se logra consistencia de arco, False si algún dominio queda vacío.
    """
    # Inicializar cola con todos los arcos (X, Y) y (Y, X) para restricciones binarias
    cola = deque()
    for (X, Y) in restricciones:
        cola.append((X, Y))
        cola.append((Y, X))
    
    while cola:
        (Xi, Xj) = cola.popleft()
        
        # Intentar reducir el dominio de Xi
        if revisar_dominio(Xi, Xj, dominios, restricciones):
            # Si el dominio de Xi queda vacío, el CSP no tiene solución
            if not dominios[Xi]:
                return False
            
            # Reintroducir arcos (Xk, Xi) donde Xk es vecino de Xi (excepto Xj)
            for Xk in csp:
                if Xk != Xi and Xk != Xj and (Xk, Xi) in restricciones:
                    cola.append((Xk, Xi))
    
    return True  # CSP es arco-consistente

def revisar_dominio(Xi, Xj, dominios, restricciones):
    """
    Elimina valores de Xi que no tienen apoyo en Xj.
    
    Args:
        Xi (str): Variable origen.
        Xj (str): Variable destino.
        dominios (dict): Dominios actuales de las variables.
        restricciones (dict): Restricciones entre variables.
    
    Returns:
        bool: True si se modificó el dominio de Xi, False en caso contrario.
    """
    modificado = False
    
    # Para cada valor en el dominio de Xi
    for x in list(dominios[Xi]):
        # Verificar si existe al menos un valor en Xj que satisfaga la restricción
        soporte_valido = any(
            restricciones[(Xi, Xj)](x, y) for y in dominios[Xj]
        )
        
        # Si no hay soporte, eliminar x de Xi
        if not soporte_valido:
            dominios[Xi].remove(x)
            modificado = True
    
    return modificado

# Ejemplo de uso
if __name__ == "__main__":
    # Definición del CSP: 3 variables (A, B, C) con dominios iniciales
    csp = {"A", "B", "C"}
    dominios = {
        "A": {1, 2, 3},
        "B": {1, 2, 3},
        "C": {1, 2, 3}
    }
    
    # Restricciones: A != B, B != C, A != C
    restricciones = {
        ("A", "B"): lambda a, b: a != b,
        ("B", "A"): lambda b, a: b != a,
        ("B", "C"): lambda b, c: b != c,
        ("C", "B"): lambda c, b: c != b,
        ("A", "C"): lambda a, c: a != c,
        ("C", "A"): lambda c, a: c != a
    }
    
    # Ejecutar AC-3
    if AC3(csp, dominios, restricciones):
        print("Dominios después de AC-3:")
        for var in dominios:
            print(f"{var}: {dominios[var]}")
    else:
        print("No hay solución.")