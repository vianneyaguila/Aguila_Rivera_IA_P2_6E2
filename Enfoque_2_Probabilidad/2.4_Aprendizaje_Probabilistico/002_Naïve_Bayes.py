# Importamos defaultdict para contar palabras automáticamente
from collections import defaultdict

# Creamos la clase del clasificador Naive Bayes
class NaiveBayesClassifier:
    def __init__(self):
        # Inicializamos contadores para clases y atributos
        self.contar_clases = defaultdict(int)
        self.contar_atributos = defaultdict(lambda: defaultdict(int))
        self.total_muestras = 0

    def entrenar(self, datos):
        """
        Entrena el clasificador con una lista de (atributos, clase)
        """
        for atributos, clase in datos:
            self.contar_clases[clase] += 1
            for atributo in atributos:
                self.contar_atributos[clase][atributo] += 1
            self.total_muestras += 1

    def predecir(self, atributos):
        """
        Predice la clase de un nuevo conjunto de atributos
        """
        mejor_clase = None
        mejor_probabilidad = -1

        for clase in self.contar_clases:
            # Calculamos probabilidad inicial de la clase
            probabilidad = self.contar_clases[clase] / self.total_muestras
            for atributo in atributos:
                # Multiplicamos por la probabilidad del atributo dado la clase (suavizado Laplace)
                probabilidad *= (self.contar_atributos[clase][atributo] + 1) / \
                                (sum(self.contar_atributos[clase].values()) + len(self.contar_atributos[clase]))
            if probabilidad > mejor_probabilidad:
                mejor_probabilidad = probabilidad
                mejor_clase = clase

        return mejor_clase

# ---------------------
# PRUEBA DEL CLASIFICADOR
# ---------------------

# Conjunto de datos de ejemplo
datos_entrenamiento = [
    (["dinero", "urgente", "gana"], "spam"),
    (["dinero", "gratis", "promoción"], "spam"),
    (["reunión", "proyecto", "mañana"], "no_spam"),
    (["actualización", "de", "proyecto"], "no_spam")
]

# Crear el clasificador
clasificador = NaiveBayesClassifier()

# Entrenar con los datos
clasificador.entrenar(datos_entrenamiento)

# Clasificar un nuevo correo
nuevo_mensaje = ["dinero", "urgente", "oferta"]
resultado = clasificador.predecir(nuevo_mensaje)

# Mostrar el resultado
print(f"El mensaje se clasifica como: {resultado}")
