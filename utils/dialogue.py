import random

GREETINGS = [
    "Hello. I am MedBot, your personal healthcare companion. Please describe your symptoms and I will do my best to help you.",
    "Hi there. I am MedBot. Tell me how you are feeling and I will analyse your symptoms.",
    "Hello! I am MedBot. On a scale of 1 to 10, how would you rate your discomfort? Or simply describe your symptoms.",
]

SCANNING = [
    "Analysing your symptoms...",
    "Running diagnostic scan...",
    "Processing your symptoms...",
]

def greeting():
    return random.choice(GREETINGS)

def bulid_response(result, detected_symptoms, severity_level, severity_emoji):
    disease= result['disease']
    confidence=result['confidence']
    description= result['description']
    precaution= result['precaution']
    top3= result['top3']

    response= f""" **Scan complete.**
    
    Based on your symptoms, my diagnosis is:
    🏥**{disease}**
    📊Confidence:{confidence:.0%}
    {severity_emoji} Severity: **{severity_level}**
    
    **About this condition:**
    {description}
    """
    if len(top3)>1:
        response+="**Other possibilities:**\n"
        for d,p in top3[1:]:
            if p>0.08:
                response+=f"->{d}:{p:.0%}\n"
        response+="\n"

    response+="**Recommended precaution:**\n"
    for i,precaution in enumerate(precaution[:4],1):
        response+=f"{i}.{precaution}\n"
    response+="""
        ⚠️**Disclaimer:** I am not a substitute
        for professional medical advice. Please
        consult a doctor if symptoms parsist
        or worsen.
        
        Are you satisfied with your care?🤗"""
    return response

def no_symptoms_reponse():
    return """ I could not detect specific symptoms
    from your description.
    
    Could you be more specific? For example:
    > "I have fever and body ache"
    > "I feel nauseous with headache"
    > "I have skin rash and itching"
    
    The more detail you provide, the better
    I can help you."""