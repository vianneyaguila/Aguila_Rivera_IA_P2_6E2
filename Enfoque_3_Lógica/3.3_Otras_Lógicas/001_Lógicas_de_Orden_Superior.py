# Definimos una función que representa un predicado de primer orden
def es_mayor_que_5(x):
    return x > 5

def es_par(x):
    return x % 2 == 0

# Función de orden superior: toma una lista de predicados y evalúa una propiedad común
def todos_satisfacen(propiedad, predicados, valor):
    """
    Evalúa si todos los predicados cumplen con una propiedad determinada para un valor dado.
    propiedad: una función que actúa sobre un predicado
    predicados: lista de funciones
    valor: valor con el que se prueba cada predicado
    """
    for pred in predicados:
        if not propiedad(pred, valor):
            return False
    return True

# Propiedad: que el predicado sea verdadero para cierto valor
def verdadero_para_valor(predicado, valor):
    return predicado(valor)

# Interacción principal
if __name__ == "__main__":
    predicados = [es_mayor_que_5, es_par]
    valor = int(input("Ingrese un número para evaluar los predicados: "))
    
    resultado = todos_satisfacen(verdadero_para_valor, predicados, valor)
    
    if resultado:
        print("✅ Todos los predicados son verdaderos para el valor dado.")
    else:
        print("❌ No todos los predicados son verdaderos para el valor dado.")
