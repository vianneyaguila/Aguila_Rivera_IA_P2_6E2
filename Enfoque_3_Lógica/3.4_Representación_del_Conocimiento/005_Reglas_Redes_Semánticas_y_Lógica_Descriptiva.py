# Representación de una red semántica simple con reglas básicas

# Diccionario que simula la red semántica
red_seman = {
    "gato": {"es_un": "mamifero"},
    "mamifero": {"es_un": "animal"},
    "gato": {"tiene": "pelaje"},
    "pez": {"es_un": "animal", "vive_en": "agua"},
}

# Reglas del sistema
def aplicar_reglas(concepto):
    if "es_un" in red_seman.get(concepto, {}):
        superclase = red_seman[concepto]["es_un"]
        print(f"{concepto} es un {superclase}")
        aplicar_reglas(superclase)
    
    if "tiene" in red_seman.get(concepto, {}):
        propiedad = red_seman[concepto]["tiene"]
        print(f"{concepto} tiene {propiedad}")
    
    if "vive_en" in red_seman.get(concepto, {}):
        habitat = red_seman[concepto]["vive_en"]
        print(f"{concepto} vive en {habitat}")

# Ejecución del razonamiento
concepto_input = input("Introduce un concepto (gato o pez): ").lower()
aplicar_reglas(concepto_input)
