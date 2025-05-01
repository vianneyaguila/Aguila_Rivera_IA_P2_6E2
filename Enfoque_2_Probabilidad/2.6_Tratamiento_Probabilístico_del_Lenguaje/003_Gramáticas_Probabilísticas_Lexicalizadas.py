import nltk
from nltk import ProbabilisticProduction, Nonterminal, induce_pcfg
from nltk.tree import Tree

# Simulación de una gramática lexicalizada (simplificada)
productions = []

# Reglas con palabras como cabezas léxicas anotadas
productions.append(ProbabilisticProduction(Nonterminal('S'), [Nonterminal('VP_ver')], prob=1.0))
productions.append(ProbabilisticProduction(Nonterminal('VP_ver'), ['ver', Nonterminal('NP_perro')], prob=1.0))
productions.append(ProbabilisticProduction(Nonterminal('NP_perro'), ['el', 'perro'], prob=1.0))

# Crear la gramática a partir de las producciones
grammar = induce_pcfg(Nonterminal('S'), productions)

# Parser probabilístico con la gramática definida
parser = nltk.ViterbiParser(grammar)

# Frase a analizar
sentence = ['ver', 'el', 'perro']

# Mostrar análisis
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
