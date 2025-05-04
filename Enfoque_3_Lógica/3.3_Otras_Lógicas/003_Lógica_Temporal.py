# Lista de estados del sistema a lo largo del tiempo
estados = [
    {"p": True, "q": False},
    {"p": True, "q": False},
    {"p": True, "q": True},
    {"p": False, "q": True},
]

# Función que evalúa "siempre p" (G p)
def siempre(prop):
    return all(estado.get(prop, False) for estado in estados)

# Función que evalúa "eventualmente q" (F q)
def eventualmente(prop):
    return any(estado.get(prop, False) for estado in estados)

# Función que evalúa "p hasta que q" (p U q)
def hasta_que(p, q):
    for estado in estados:
        if estado.get(q, False):
            return True
        if not estado.get(p, False):
            return False
    return False

# Interacción con el usuario
if __name__ == "__main__":
    print("Evaluando fórmulas temporales sobre una secuencia de estados:\n")

    print("1. Siempre p (G p):", "✅" if siempre("p") else "❌")
    print("2. Eventualmente q (F q):", "✅" if eventualmente("q") else "❌")
    print("3. p hasta que q (p U q):", "✅" if hasta_que("p", "q") else "❌")
