from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Conjunto de documentos (corpus)
documents = [
    "La inteligencia artificial está transformando la industria.",
    "Los sistemas de recuperación de información utilizan modelos probabilísticos.",
    "La recuperación de datos permite encontrar información relevante.",
    "Los modelos estadísticos son claves en la inteligencia artificial moderna."
]

# Consulta del usuario
query = "modelos de recuperación de información"

# Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Transformar documentos y consulta en vectores TF-IDF
doc_vectors = vectorizer.fit_transform(documents + [query])

# Separar la consulta del resto
query_vector = doc_vectors[-1]
doc_vectors = doc_vectors[:-1]

# Calcular similitud del coseno (simula la probabilidad de relevancia)
similarities = cosine_similarity(query_vector, doc_vectors).flatten()

# Mostrar documentos ordenados por similitud
ranked_docs = sorted(zip(similarities, documents), reverse=True)

# Mostrar resultados
print("Documentos más relevantes para la consulta:\n")
for score, doc in ranked_docs:
    print(f"Relevancia: {score:.2f} | Documento: {doc}")
