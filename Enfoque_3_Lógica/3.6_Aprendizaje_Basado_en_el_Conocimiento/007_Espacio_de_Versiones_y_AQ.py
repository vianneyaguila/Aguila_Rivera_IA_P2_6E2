# Representamos las hipótesis como listas de atributos. "?" es general, "∅" es vacío (no válido)
def inicializar_hipotesis(n):
    return ['∅'] * n  # hipótesis específica inicial

def generalizar(hipo, ejemplo):
    for i in range(len(hipo)):
        if hipo[i] == '∅':
            hipo[i] = ejemplo[i]
        elif hipo[i] != ejemplo[i]:
            hipo[i] = '?'
    return hipo

def es_consistente(hipo, ejemplo):
    for h, e in zip(hipo, ejemplo):
        if h != '?' and h != e:
            return False
    return True

# Datos de entrada
positivos = [['rojo', 'pequeño', 'ligero'], ['rojo', 'grande', 'ligero']]
negativos = [['verde', 'pequeño', 'ligero']]

# Inicialización
S = inicializar_hipotesis(3)
G = ['?', '?', '?']  # hipótesis más general posible

# Actualizar S con positivos
for ej in positivos:
    S = generalizar(S, ej)

# Verificar consistencia con negativos
for ej in negativos:
    if es_consistente(S, ej):
        print("Error: hipótesis específica S cubre un negativo.")

# Mostrar resultado
print("Hipótesis más específica (S):", S)
print("Hipótesis más general (G):", G)
