from pgmpy.models import BayesianNetwork
import networkx as nx
import matplotlib.pyplot as plt

def visualizar_red(red, titulo):
    """
    Visualiza la estructura de una red bayesiana
    """
    G = nx.DiGraph()
    G.add_edges_from(red.edges())
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', 
            font_size=12, font_weight='bold', arrowsize=20)
    plt.title(titulo)
    plt.show()

def encontrar_manto_markov(red, nodo):
    """
    Encuentra y visualiza el Manto de Markov de un nodo
    """
    # Identificar componentes del manto
    padres = set(red.get_parents(nodo))
    hijos = set(red.get_children(nodo))
    padres_de_hijos = set()
    
    for hijo in hijos:
        padres_de_hijos.update(red.get_parents(hijo))
    
    manto = padres.union(hijos).union(padres_de_hijos)
    manto.discard(nodo)  # Eliminar el nodo mismo si está presente
    
    # Visualización especial
    G = nx.DiGraph()
    G.add_edges_from(red.edges())
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 7))
    
    # Colorear nodos
    node_colors = []
    for node in G.nodes():
        if node == nodo:
            node_colors.append('red')  # Nodo objetivo
        elif node in manto:
            node_colors.append('orange')  # Manto de Markov
        else:
            node_colors.append('lightgray')  # Otros nodos
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors, 
            node_size=2500, font_size=12, font_weight='bold',
            edge_color='gray', arrowsize=20)
    
    plt.title(f"Manto de Markov para el nodo '{nodo}'")
    plt.show()
    
    return manto

# ====================================
# EJEMPLO PRÁCTICO: SISTEMA MÉDICO
# ====================================

# Crear red bayesiana
red_medica = BayesianNetwork([
    ('Genética', 'Cancer'),        # La genética influye en el cáncer
    ('Fumar', 'Cancer'),           # Fumar influye en el cáncer
    ('Cancer', 'Fatiga'),          # El cáncer causa fatiga
    ('Cancer', 'Dolor'),           # El cáncer causa dolor
    ('Ejercicio', 'Fatiga'),       # El ejercicio afecta la fatiga
    ('Edad', 'PresionAlta'),       # La edad afecta la presión
    ('PresionAlta', 'Dolor')       # La presión alta causa dolor
])

# Visualizar red completa
visualizar_red(red_medica, "Red Médica Completa")

# Encontrar y visualizar manto de Markov para 'Cancer'
manto_cancer = encontrar_manto_markov(red_medica, 'Cancer')
print(f"\nManto de Markov para 'Cancer': {manto_cancer}")

# Encontrar y visualizar manto de Markov para 'Fatiga'
manto_fatiga = encontrar_manto_markov(red_medica, 'Fatiga')
print(f"\nManto de Markov para 'Fatiga': {manto_fatiga}")