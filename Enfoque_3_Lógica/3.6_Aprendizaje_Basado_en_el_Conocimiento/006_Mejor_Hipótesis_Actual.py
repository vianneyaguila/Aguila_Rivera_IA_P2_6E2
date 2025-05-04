# Representamos hipótesis como listas de atributos, donde "?" significa "cualquier valor"
# Este es un ejemplo del algoritmo "Find-S" adaptado lógicamente

def find_best_hypothesis(positivos):
    # Inicializamos con la hipótesis más específica posible
    hipotesis = positivos[0].copy()
    
    for ejemplo in positivos:
        for i in range(len(hipotesis)):
            if hipotesis[i] != ejemplo[i]:
                hipotesis[i] = "?"  # generalizamos

    return hipotesis

# Ejemplos positivos (atributos de instancias: cielo, temperatura, humedad)
ejemplos_positivos = [
    ["soleado", "caliente", "alta"],
    ["soleado", "caliente", "media"],
    ["soleado", "caliente", "baja"]
]

# Ejecutamos la función
mejor_hipotesis = find_best_hypothesis(ejemplos_positivos)
print("Mejor hipótesis actual:", mejor_hipotesis)
