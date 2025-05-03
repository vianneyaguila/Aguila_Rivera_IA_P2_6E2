# Simulación de inferencia lógica proposicional usando Modus Ponens

# Base de conocimientos: proposiciones conocidas
base_conocimiento = {
    "p": True,  # Se conoce que "p" es verdadera
    "p -> q": True  # Se conoce que "si p entonces q" es verdadera
}

# Función para aplicar Modus Ponens
def aplicar_modus_ponens(base):
    if "p" in base and base["p"] == True:
        if "p -> q" in base and base["p -> q"] == True:
            base["q"] = True  # Se infiere que "q" es verdadera
            print("Se ha inferido que 'q' es verdadera usando Modus Ponens.")
        else:
            print("No se encuentra la implicación 'p -> q' en la base.")
    else:
        print("No se encuentra 'p' como verdadera en la base.")

# Llamada a la función de inferencia
aplicar_modus_ponens(base_conocimiento)

# Mostrar resultados
print("\nEstado final de la base de conocimiento:")
for proposicion, valor in base_conocimiento.items():
    estado = "Verdadero" if valor else "Falso"
    print(f"{proposicion}: {estado}")
