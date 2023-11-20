import numpy as np
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)
with open('./resources/glossary_fortinet.txt', 'r') as f:
    cybersecurity_words = [line.strip() for line in f.readlines()]

def cybersecurity_context(text):
    """Calcula o contexto de cibersegurança do texto com base na similaridade com termos do glossário."""
    text_vector = text_to_vector(text)
    similarities = []

    for glossary_vector in glossary_vectors.values():
        if text_vector is not None and glossary_vector is not None:
            similarity = cosine_similarity(text_vector, glossary_vector)
            similarities.append(similarity)
            
    if similarities:
        average_similarity    = np.mean(similarities)
        normalized_similarity = normalize_value(average_similarity, 0, 1)

        return min(max(normalized_similarity, 0), 1)  , min(max(normalized_similarity, 0), 100)
    else:
        return 0

def normalize_value(x, min_value, max_value, new_min=0, new_max=1):
    """Normaliza um valor x no intervalo [min_value, max_value] para um novo intervalo [new_min, new_max]."""
    if x < min_value or x > max_value:
        #print(f"Warning: Value {x} is out of bounds [{min_value}, {max_value}]. Clamping it.")
        x = max(min(x, max_value), min_value)  # Alternativa para manter x nos limites sem usar if/else
    normalized_x = new_min + ((new_max - new_min) * (x - min_value)) / (max_value - min_value)
    return normalized_x

def cosine_similarity(vector1, vector2):
    """Calcula a similaridade de cosseno entre dois vetores."""
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    
    if not norm_vector1 or not norm_vector2:  # Evitando divisão por zero
        return 0

    dot_product = np.dot(vector1, vector2)
    similarity  = dot_product / (norm_vector1 * norm_vector2)
    return similarity

def get_word_vectors(text):
    """Retorna os vetores das palavras no texto que estão presentes no modelo."""
    word_vectors = []
    for word in text.split():
        if word in model:
            word_vectors.append(model[word])
    return word_vectors

def text_to_vector(text):
    """Converte o texto em um vetor médio dos vetores das palavras."""
    word_vectors = get_word_vectors(text)
    if not word_vectors:
        return np.zeros(300)
    return np.mean(word_vectors, axis=0)

glossary_vectors = {
    term: text_to_vector(term).squeeze()
    for term in cybersecurity_words
}