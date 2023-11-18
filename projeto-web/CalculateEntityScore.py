import spacy


nlp = spacy.load('en_core_web_sm')

def entity_in_text(text):
    """Avalia o texto e retorna uma pontuação com base nas entidades nomeadas presentes e na presença de palavras-chave relevantes."""
    doc = nlp(text)
    entity_scores = {
      "CARDINAL": 0.3208,
      "DATE": 0.3807,
      "EVENT": 0.0002,
      "FAC": 0.0003,
      "GPE": 0.0392,
      "LANGUAGE": 0.0002,
      "LAW": 0.0004,
      "LOC": 0.0030,
      "MONEY": 0.0014,
      "NORP": 0.0254,
      "ORDINAL": 0.0097,
      "ORG": 0.1288,
      "PERCENT": 0.0003,
      "PERSON": 0.0630,
      "PRODUCT": 0.0052,
      "QUANTITY": 0.0133,
      "TIME": 0.0079,
      "WORK_OF_ART": 0.0003,
    }
    # Pontuação baseada na frequência
    freq_score = sum(entity_scores.get(ent.label_, 0) for ent in doc.ents)
    recognized_entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return min(max(freq_score, 0), 1) , recognized_entities
  
