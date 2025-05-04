# Ejemplo educativo: simulación simplificada de FOIL
# Aprende reglas tipo "if condición then clase"

def foil(examples, attributes):
    rules = []
    positives = [e for e in examples if e['clase'] == "yes"]
    negatives = [e for e in examples if e['clase'] == "no"]

    while positives:
        rule = []
        covered = positives[:]
        remaining_negatives = negatives[:]
        
        while remaining_negatives:
            best_attr = None
            best_gain = 0

            for attr in attributes:
                # Filtrar positivos y negativos que cumplen con el literal
                pos_cover = [e for e in covered if e[attr]]
                neg_cover = [e for e in remaining_negatives if e[attr]]

                # Ganancia: proporción de positivos sobre total
                if len(pos_cover) + len(neg_cover) == 0:
                    continue
                gain = len(pos_cover) / (len(pos_cover) + len(neg_cover))

                if gain > best_gain:
                    best_gain = gain
                    best_attr = attr

            if not best_attr:
                break

            rule.append(best_attr)
            covered = [e for e in covered if e[best_attr]]
            remaining_negatives = [e for e in remaining_negatives if not e[best_attr]]

        rules.append(rule)
        positives = [e for e in positives if not all(e[attr] for attr in rule)]

    return rules

# Datos de ejemplo: cada ejemplo es un diccionario de atributos con la clase final
examples = [
    {'calvo': True,  'gafas': False, 'bata': True,  'clase': 'yes'},
    {'calvo': True,  'gafas': True,  'bata': True,  'clase': 'yes'},
    {'calvo': False, 'gafas': True,  'bata': True,  'clase': 'no'},
    {'calvo': False, 'gafas': False, 'bata': False, 'clase': 'no'},
    {'calvo': True,  'gafas': False, 'bata': False, 'clase': 'yes'},
]

# Lista de atributos que se pueden usar
attributes = ['calvo', 'gafas', 'bata']

# Ejecutar FOIL
reglas = foil(examples, attributes)

# Mostrar resultados
for i, r in enumerate(reglas):
    condiciones = " AND ".join(r)
    print(f"Regla {i+1}: IF {condiciones} THEN yes")
