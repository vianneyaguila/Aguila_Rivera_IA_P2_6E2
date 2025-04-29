# Importamos la librería necesaria
from collections import defaultdict

# Creamos una clase para nuestro Clasificador Bayesiano
class ClasificadorBayesiano:
    def __init__(self):
        # Diccionarios para contar ocurrencias de palabras en cada categoría
        self.spam_palabras = defaultdict(int)
        self.no_spam_palabras = defaultdict(int)
        self.total_spam = 0
        self.total_no_spam = 0

    def entrenar(self, correos):
        # Entrenamos el modelo con una lista de tuplas (correo, etiqueta)
        for texto, es_spam in correos:
            palabras = texto.lower().split()
            if es_spam:
                for palabra in palabras:
                    self.spam_palabras[palabra] += 1
                    self.total_spam += 1
            else:
                for palabra in palabras:
                    self.no_spam_palabras[palabra] += 1
                    self.total_no_spam += 1

    def predecir(self, correo):
        # Clasifica un nuevo correo como Spam o No Spam
        palabras = correo.lower().split()
        prob_spam = 1
        prob_no_spam = 1
        
        for palabra in palabras:
            # Probabilidades condicionadas
            prob_spam *= (self.spam_palabras[palabra] + 1) / (self.total_spam + 2)
            prob_no_spam *= (self.no_spam_palabras[palabra] + 1) / (self.total_no_spam + 2)
        
        # Devolvemos la categoría con mayor probabilidad
        return "Spam" if prob_spam > prob_no_spam else "No Spam"

# --------------------------
# PRUEBA DEL CLASIFICADOR
# --------------------------

# Datos de entrenamiento: lista de (texto, es_spam)
correos_entrenamiento = [
    ("Gana dinero rápido", True),
    ("Oferta exclusiva ahora", True),
    ("Reunión del proyecto mañana", False),
    ("Actualización de tu cuenta", False)
]

# Crear una instancia del clasificador
clasificador = ClasificadorBayesiano()

# Entrenar el clasificador
clasificador.entrenar(correos_entrenamiento)

# Probar con un nuevo correo
nuevo_correo = "Gana una oferta exclusiva ahora"
resultado = clasificador.predecir(nuevo_correo)

# Mostrar el resultado
print(f"El correo se clasifica como: {resultado}")
