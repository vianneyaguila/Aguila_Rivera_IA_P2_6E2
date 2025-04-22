import numpy as np

class MDP:
    """Estructura básica de un Proceso de Decisión de Markov."""
    def __init__(self, estados, acciones, recompensas, transiciones, gamma=0.9):
        """
        Args:
            estados (list): Lista de estados posibles.
            acciones (dict): Diccionario {estado: lista de acciones posibles}.
            recompensas (dict): Recompensas R(s,a,s') como {(s,a,s'): valor}.
            transiciones (dict): Probabilidades P(s'|s,a) como {(s,a,s'): prob}.
            gamma (float): Factor de descuento (0 ≤ gamma < 1).
        """
        self.estados = estados
        self.acciones = acciones
        self.recompensas = recompensas
        self.transiciones = transiciones
        self.gamma = gamma

def iteracion_valores(mdp, tol=1e-6, max_iter=1000):
    """
    Implementa el algoritmo de Iteración de Valores.
    
    Args:
        mdp (MDP): Objeto que define el proceso de decisión de Markov.
        tol (float): Tolerancia para la convergencia.
        max_iter (int): Máximo número de iteraciones.
        
    Returns:
        tuple: (V, politica), donde V es el diccionario de valores óptimos
               y politica es la política óptima para cada estado.
    """
    # Inicializar valores arbitrarios (ej. 0 para todos los estados)
    V = {s: 0 for s in mdp.estados}
    
    for _ in range(max_iter):
        delta = 0  # Para medir el cambio máximo en V(s)
        V_nuevo = {}
        
        for s in mdp.estados:
            # Calcular el valor para cada acción posible
            valores_acciones = []
            
            for a in mdp.acciones.get(s, []):
                # Sumar sobre todos los posibles estados siguientes s'
                valor_accion = 0
                for s_prima in mdp.estados:
                    prob = mdp.transiciones.get((s, a, s_prima), 0)
                    recompensa = mdp.recompensas.get((s, a, s_prima), 0)
                    valor_accion += prob * (recompensa + mdp.gamma * V[s_prima])
                
                valores_acciones.append(valor_accion)
            
            # Actualizar V(s) con el máximo valor de acción
            if valores_acciones:
                V_nuevo[s] = max(valores_acciones)
            else:
                V_nuevo[s] = 0  # Estados terminales
            
            # Actualizar delta
            delta = max(delta, abs(V_nuevo[s] - V[s]))
        
        V = V_nuevo.copy()
        
        # Verificar convergencia
        if delta < tol:
            break
    
    # Extraer la política óptima
    politica = {}
    for s in mdp.estados:
        mejor_accion = None
        mejor_valor = -np.inf
        
        for a in mdp.acciones.get(s, []):
            valor_accion = 0
            for s_prima in mdp.estados:
                prob = mdp.transiciones.get((s, a, s_prima), 0)
                recompensa = mdp.recompensas.get((s, a, s_prima), 0)
                valor_accion += prob * (recompensa + mdp.gamma * V[s_prima])
            
            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = a
        
        politica[s] = mejor_accion
    
    return V, politica

# Ejemplo: MDP de 3 estados (Laberinto simple)
if __name__ == "__main__":
    # Definir estados y acciones
    estados = ["A", "B", "C"]
    acciones = {
        "A": ["Ir_B", "Ir_C"],
        "B": ["Ir_A", "Ir_C"],
        "C": []  # Estado terminal (salida)
    }
    
    # Definir recompensas y transiciones
    recompensas = {
        ("A", "Ir_B", "B"): 0,
        ("A", "Ir_C", "C"): 10,  # Llegar a C desde A da recompensa 10
        ("B", "Ir_A", "A"): 0,
        ("B", "Ir_C", "C"): 5    # Llegar a C desde B da recompensa 5
    }
    
    transiciones = {
        ("A", "Ir_B", "B"): 0.8,
        ("A", "Ir_B", "A"): 0.2,  # 20% de fallar y quedarse en A
        ("A", "Ir_C", "C"): 1.0,  # Siempre funciona
        ("B", "Ir_A", "A"): 0.7,
        ("B", "Ir_A", "B"): 0.3,  # 30% de fallar
        ("B", "Ir_C", "C"): 1.0   # Siempre funciona
    }
    
    # Crear MDP
    mdp = MDP(estados, acciones, recompensas, transiciones, gamma=0.9)
    
    # Ejecutar Iteración de Valores
    V_opt, politica_opt = iteracion_valores(mdp)
    
    # Mostrar resultados
    print("Valores óptimos:")
    for s in estados:
        print(f"  {s}: {V_opt[s]:.2f}")
    
    print("\nPolítica óptima:")
    for s in estados:
        print(f"  En {s}: {politica_opt[s]}")