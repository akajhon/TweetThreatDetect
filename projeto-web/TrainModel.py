import pandas as pd
from CalculateContextScore import cybersecurity_context, normalize_value, text_to_vector
from CalculateEntityScore import entity_in_text
from LoadModel import predizerSentimento
import numpy as np
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from tqdm import tqdm
import pickle
# =====================================================================================
# ============================= RANDOM FOREST + WORD2VEC ==============================
# =====================================================================================

with open('glossary_fortinet.txt', 'r') as f:
    cybersecurity_words = [line.strip() for line in f.readlines()]

def loadRandomForestModel(input):
    with open('./Random-Forest/random_forest_model.pkl', 'rb') as model_file:
        loaded_rf_model = pickle.load(model_file)

    y_pred = loaded_rf_model.predict(input)
    prob_first_class = y_pred[0]

    y_pred = loaded_rf_model.predict_proba(input)
    prob_second_class = y_pred[0][1]
    return prob_first_class , prob_second_class

def loadSvmModel(input):
    vector = text_to_vector(input)
    with open('./Svm/svm_model.pkl', 'rb') as model_file:
        loaded_svm_model = pickle.load(model_file)
        
    pred_range = loaded_svm_model.predict_proba([vector])
    prob_second_class = pred_range[0][1]
   # y_pred = loaded_rf_model.predict(input)
    return prob_second_class

def extrairDados(input):
    all_vectors = []
    sentiment , average_prediction , positive_probability, negative_probability = predizerSentimento(input)
    entity_score , recognized_entities                                          = entity_in_text(input)
    context_score , percent_similarity                                          = cybersecurity_context(input)
    vector                                                                      = text_to_vector(input)
    svmModel                                                                    = loadSvmModel(input)
    
    sentiment_array     = np.array([average_prediction])
    entity_score_array  = np.array([entity_score])
    context_score_array = np.array([context_score])
    svmModel_array = np.array([svmModel])
    
    full_vector = np.concatenate((vector, sentiment_array, entity_score_array, context_score_array, svmModel_array), axis=None)
    all_vectors.append(full_vector)
    
    prob_threat, prob_percent = loadRandomForestModel(all_vectors)

    return sentiment, recognized_entities, average_prediction, positive_probability, negative_probability, percent_similarity, prob_threat, prob_percent

extrairDados("i hate English")
