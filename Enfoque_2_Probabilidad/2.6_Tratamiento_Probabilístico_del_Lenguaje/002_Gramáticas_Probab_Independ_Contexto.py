import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Definición de la gramática PCFG
grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det Noun [0.5] | 'Juan' [0.5]
  VP -> Verb NP [1.0]
  Det -> 'el' [1.0]
  Noun -> 'gato' [0.5] | 'perro' [0.5]
  Verb -> 've' [1.0]
""")

# Crear el parser usando el algoritmo de Viterbi (probabilístico)
parser = ViterbiParser(grammar)

# Frase de ejemplo a analizar
sentence = ['Juan', 've', 'el', 'perro']

# Analizar la frase y mostrar los árboles sintácticos
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
