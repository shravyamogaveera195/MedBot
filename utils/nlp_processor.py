import nltk
import re
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
nltk.download('wordnet',quiet=True)
nltk.download('punkt_tab',quiet=True)

symptom_columns=joblib.load('model/symptom_columns.pkl')
SYMPTOM_SYNONYMS = {
    'tired': 'fatigue',
    'tiredness': 'fatigue',
    'exhausted': 'fatigue',
    'temperature': 'high_fever',
    'high temperature': 'high_fever',
    'throwing up': 'vomiting',
    'puking': 'vomiting',
    'runny nose': 'runny_nose',
    'stuffy nose': 'congestion',
    'belly ache': 'stomach_pain',
    'tummy ache': 'stomach_pain',
    'belly pain': 'stomach_pain',
    'hurts': 'pain',
    'hurt': 'pain',
    'dizzy': 'dizziness',
    'shivering': 'chills',
    'shaking': 'chills',
    'scratching': 'itching',
    'rash': 'skin_rash',
    'swollen': 'swelling',
    'cannot sleep': 'insomnia',
    'cant sleep': 'insomnia',
    'cant breathe': 'breathlessness',
    'cannot breathe': 'breathlessness',
    'short of breath': 'breathlessness',
    'weight loss': 'weight_loss',
    'losing weight': 'weight_loss',
    'lose weight': 'weight_loss',
    'yellow eyes': 'yellowing_of_eyes',
    'yellow skin': 'yellowish_skin',
    'back ache': 'back_pain',
    'back hurts': 'back_pain',
    'chest pain': 'chest_pain',
    'chest hurts': 'chest_pain',
    'sore throat': 'throat_irritation',
    'throat hurts': 'throat_irritation',
}

def extract_symptoms(user_input):
    '''
    extract sympotms from natural language
    returns: list of matched symptom names
    '''
    text=user_input.lower()
    text=re.sub(r'[^a-zA-Z\s]','',text)
    text=text.strip()

    for phrase, symptom in SYMPTOM_SYNONYMS.items():
        if phrase in text:
            text=text.replace(phrase,symptom.replace('_',''))

    tokens=word_tokenize(text)

    #remove stopwords but keep medically relavent words
    stop_words=set(stopwords.words('english'))
    keep_words={'no','not','loss','high','low','severe','mild','chronic'}
    stop_words=stop_words-keep_words

    tokens=[t for t in tokens if t not in stop_words]

    #lemmatize
    lemmatizer=WordNetLemmatizer()
    tokens=[lemmatizer.lemmatize(t) for t in tokens]

    #matching the symptoms
    detected=[]

    for token in tokens:
        #direct match
        if token in symptom_columns:
            detected.append(token)
        else:
            #partial match
            for symptom in symptom_columns:
                parts=symptom.split('_')
                if token in parts:
                    if symptom not in detected:
                        detected.append(symptom)
    return list(set(detected))

def build_input_vector(detected_symptoms):
    '''
    convert detected symptoms to binary vector 
    '''
    import pandas as pd
    vector=pd.Dataframe(0,index=[0],columns=symptom_columns)
    for symptom in vector.columns:
        vector[symptom]=1
    return vector