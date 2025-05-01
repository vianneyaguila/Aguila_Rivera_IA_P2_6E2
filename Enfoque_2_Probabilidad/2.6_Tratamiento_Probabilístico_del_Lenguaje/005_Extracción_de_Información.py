import re

# Texto de ejemplo
texto = """
El 21 de abril de 2024, Juan Pérez visitó la ciudad de Bogotá para participar en una conferencia internacional.
María López también estuvo presente en el evento que se celebró en el Centro de Convenciones.
"""

# Expresiones regulares para extraer:
# - Fechas (formato día de mes de año)
# - Nombres propios (simplificados como dos palabras con mayúscula inicial)
# - Lugares (simplificados como "ciudad de ..." o "en ...")

# Extraer fechas
fechas = re.findall(r"\d{1,2} de [a-z]+ de \d{4}", texto)

# Extraer nombres (dos palabras que empiezan con mayúscula)
nombres = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+", texto)

# Extraer lugares (ciudad de ... o en ...)
lugares = re.findall(r"(?:ciudad de|en el|en la|en)\s+[A-Z][a-z]+", texto)

# Mostrar resultados
print("Fechas encontradas:")
print(fechas)
print("\nNombres encontrados:")
print(nombres)
print("\nLugares encontrados:")
print(lugares)
