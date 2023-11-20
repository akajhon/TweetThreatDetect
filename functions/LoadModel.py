import numpy
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from sklearn.metrics import classification_report, accuracy_score
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import statistics
# ===================================================================================== #
lemmatizer = WordNetLemmatizer()

# Defining regex patterns.
urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|(www\.)[^ ]*)"
userPattern       = '@[^\s]+'
hashtagPattern    = '#[^\s]+'
alphaPattern      = "[^a-z0-9<>]"
sequencePattern   = r"(.)\1\1+"
seqReplacePattern = r"\1\1"

def predizerSentimento(input):
    with open('./models/Sentiment-BiLSTM/Tokenizer.pickle', 'rb') as file:
        tokenizer = pickle.load(file)
        
    words = word_tokenize(input)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # Use o tokenizador para obter as sequências
    sequences = tokenizer.texts_to_sequences([' '.join(lemmatized_words)])
    sequences = pad_sequences(sequences, maxlen=60)
    
    model = tf.keras.models.load_model('./models/Sentiment-BiLSTM')
        
    predictions = model.predict(sequences)
    sentiment_labels , prediction = [], []
    
    for pred in predictions:
        if pred > 0.5:
            sentiment_labels.append('Negativo')
            prediction.append(pred[0])
        else:
            sentiment_labels.append('Positivo')
            prediction.append(pred[0])

    average_prediction = numpy.mean(prediction)
    average = statistics.mean([0 if s == 'Positivo' else 1 for s in sentiment_labels])
    label = 'Negativo' if average > 0.5 else 'Positivo'
    
    #Para dados de gráfico
    positive_probability = (1 - average_prediction) * 100
    negative_probability = average_prediction * 100

    return label , average_prediction , positive_probability , negative_probability
    
def limpezaTweet(tweet):
    # Tansform all the tweets to LowerCase
    tweet = tweet.lower()

    # Remove Emojis
    emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
    tweet = emoji_pattern.sub(r'', tweet)

    # Strip all URLs
    tweet = re.sub(urlPattern,'',tweet)

    # Remove mentions
    tweet = re.sub(userPattern,'', tweet)
    # Remove Hashtags from the end of the sentence
    tweet = re.sub(r'(\s+#[\w-]+)+\s*$', '', tweet).strip()

    # Remove the # symbol from hashtags in the middle of the sentence
    tweet = re.sub(r'#([\w-]+)', r'\1', tweet).strip()

    # Replace 3 or more consecutive letters by 2 letter.
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)

    # Remove Multiple Spaces
    tweet = re.sub(r"\s\s+", " ", tweet)

    # Remove NUmbers
    tweet = re.sub(r'\d+', '', tweet)

    # Remove non-alphanumeric and symbols
    tweet = re.sub(alphaPattern, ' ', tweet)

    # Adding space on either side of '/' to seperate words (After replacing URLS).
    tweet = re.sub(r'/', ' / ', tweet)
    # Lemmatize the text
    words = word_tokenize(tweet)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    #lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    tweet = ' '.join(lemmatized_words)

    return tweet
# ===================================================================================== #