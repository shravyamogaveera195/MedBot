import joblib
import pandas as pd

#loading models
model = joblib.load('model/random_forest.pkl')
le=joblib.load('model/label_encoder.pkl')
severity_dict=joblib.load('model/severity_dict.pkl')

#loading disease info into file
desc_df=pd.read_csv('data/symptom_Description.csv')
precaution_df=pd.read_csv('data/symptom_precaution.csv')

desc_dict=dict(zip(desc_df['Disease'],desc_df['Description']))

def get_precautions(disease):
    row=precaution_df[precaution_df['Disease']==disease]
    if len(row)==0:
        return['Consult a doctor']
    precautions=[]
    for i in range(1,5):
        col= f'Precaution_{i}'
        if col in row.columns:
            val=row[col].values[0]
            if pd.notna(val):
                precautions.append(val)
    return precautions

def calculate_severity(detected_symptoms):
    '''
    calculates the overall severity score
    '''
    total=0
    for symptom in detected_symptoms:
        total+=severity_dict.get(symptom,1)
    avg=total/max(len(detected_symptoms),1)

    if avg>=5:
        return "HIGH","🔴"
    elif avg>=3:
        return "MEDIUM","🟠"
    else:
        return "LOW","🟢"

def predict_disease(input_vector):
    '''
    confidence threshold + fallback
    '''
    proba=model.predict_proba(input_vector)[0]
    max_confidence=proba.max()

    #if confidence is low ask for more symptoms
    if max_confidence<0.30:
        retrun {
            'disease': None,
            'confidence':max_confidence,
            'top3':[],
            'description':None,
            'precautions':[]
        }

    top3_idx=proba.argsort()[-3:][::-1]
    top3=[
        (le.classes_[i],proba[i])
        for i in top3_idx
        if proba[i]>0.05
    ]
    best_disease=top3[0][0]
    best_confidence=top3[0][1]

    return {
        'disease': best_disease,
        'confidence': best_confidence,
        'top3':top3,
        'description': desc_dict.get(best_disease, "No disease available"),
        'precaution': get_precautions(best_disease)
    }

