from flask import Flask, request, render_template, jsonify  # Import jsonify
import numpy as np
import pandas as pd
import pickle


# flask app
app = Flask(__name__)



sym_des = pd.read_csv("D:/utsav1/prediction/disease-prediction/data/symtoms_df.csv")
precautions = pd.read_csv("D:/utsav1/prediction/disease-prediction/data/precautions_df.csv")
workout = pd.read_csv("D:/utsav1/prediction/disease-prediction/data/workout_df.csv")
description = pd.read_csv("D:/utsav1/prediction/disease-prediction/data/description.csv")
medications = pd.read_csv('D:/utsav1/prediction/disease-prediction/data/medications.csv')
diets = pd.read_csv("D:/utsav1/prediction/disease-prediction/data/diets.csv")

# load model===========================================
svc = pickle.load(open('D:/utsav1/prediction/disease-prediction/model/svc.pkl','rb'))

def extract_symptoms(sentence):
    """
    Extract symptoms from the user input sentence.
    """
    extracted_symptoms = []
    for symptom in symptoms_dict.keys():
        if symptom.lower() in sentence.lower():
            extracted_symptoms.append(symptom)
    return extracted_symptoms


def helper(dis):
    # Fetch details with fallback for missing values
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc]) if not desc.empty else "Description not available."

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values] if not pre.empty else [["No precautions available."]]

    med = medications[medications['Disease'] == dis][['Medication_1', 'Medication_2', 'Medication_3', 'Medication_4', 'Medication_5']]
    med = [col for col in med.values] if not med.empty else ["No medications available."]

    die = diets[diets['Disease'] == dis][['Diet_1','Diet_2','Diet_3','Diet_4','Diet_5']]
    die = [col for col in die.values] if not die.empty else ["No diet recommendations available."]

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = wrkout.values[0] if not wrkout.empty else "No workout recommendations available."

    return desc, pre, med, die, wrkout



symptoms_dict = {'Itching': 0, 'Skin Rash': 1, 'Nodal Skin Eruptions': 2, 'Continuous Sneezing': 3, 'Shivering': 4, 'Chills': 5, 'Joint Pain': 6, 'Stomach Pain': 7, 'Acidity': 8, 'Ulcers On Tongue': 9, 'Muscle Wasting': 10, 'Vomiting': 11, 'Burning Micturition': 12, 'Spotting Urination': 13, 'Fatigue': 14, 'Weight Gain': 15, 'Anxiety': 16, 'Cold Hands And Feets': 17, 'Mood Swings': 18, 'Weight Loss': 19, 'Restlessness': 20, 'Lethargy': 21, 'Patches In Throat': 22, 'Irregular Sugar Level': 23, 'Cough': 24, 'High Fever': 25, 'Sunken Eyes': 26, 'Breathlessness': 27, 'Sweating': 28, 'Dehydration': 29, 'Indigestion': 30, 'Headache': 31, 'Yellowish Skin': 32, 'Dark Urine': 33, 'Nausea': 34, 'Loss Of Appetite': 35, 'Pain Behind The Eyes': 36, 'Back Pain': 37, 'Constipation': 38, 'Abdominal Pain': 39, 'Diarrhoea': 40, 'Mild Fever': 41, 'Yellow Urine': 42, 'Yellowing Of Eyes': 43, 'Acute Liver Failure': 44, 'Fluid Overload': 45, 'Swelling Of Stomach': 46, 'Swelled Lymph Nodes': 47, 'Malaise': 48, 'Blurred And Distorted Vision': 49, 'Phlegm': 50, 'Throat Irritation': 51, 'Redness Of Eyes': 52, 'Sinus Pressure': 53, 'Runny Nose': 54, 'Congestion': 55, 'Chest Pain': 56, 'Weakness In Limbs': 57, 'Fast Heart Rate': 58, 'Pain During Bowel Movements': 59, 'Pain In Anal Region': 60, 'Bloody Stool': 61, 'Irritation In Anus': 62, 'Neck Pain': 63, 'Dizziness': 64, 'Cramps': 65, 'Bruising': 66, 'Obesity': 67, 'Swollen Legs': 68, 'Swollen Blood Vessels': 69, 'Puffy Face And Eyes': 70, 'Enlarged Thyroid': 71, 'Brittle Nails': 72, 'Swollen Extremeties': 73, 'Excessive Hunger': 74, 'Extra Marital Contacts': 75, 'Drying And Tingling Lips': 76, 'Slurred Speech': 77, 'Knee Pain': 78, 'Hip Joint Pain': 79, 'Muscle Weakness': 80, 'Stiff Neck': 81, 'Swelling Joints': 82, 'Movement Stiffness': 83, 'Spinning Movements': 84, 'Loss Of Balance': 85, 'Unsteadiness': 86, 'Weakness Of One Body Side': 87, 'Loss Of Smell': 88, 'Bladder Discomfort': 89, 'Foul Smell Of Urine': 90, 'Continuous Feel Of Urine': 91, 'Passage Of Gases': 92, 'Internal Itching': 93, 'Toxic Look (Typhos)': 94, 'Depression': 95, 'Irritability': 96, 'Muscle Pain': 97, 'Altered Sensorium': 98, 'Red Spots Over Body': 99, 'Belly Pain': 100, 'Abnormal Menstruation': 101, 'Dischromic Patches': 102, 'Watering From Eyes': 103, 'Increased Appetite': 104, 'Polyuria': 105, 'Family History': 106, 'Mucoid Sputum': 107, 'Rusty Sputum': 108, 'Lack Of Concentration': 109, 'Visual Disturbances': 110, 'Receiving Blood Transfusion': 111, 'Receiving Unsterile Injections': 112, 'Coma': 113, 'Stomach Bleeding': 114, 'Distention Of Abdomen': 115, 'History Of Alcohol Consumption': 116, 'Fluid Overload.1': 117, 'Blood In Sputum': 118, 'Prominent Veins On Calf': 119, 'Palpitations': 120, 'Painful Walking': 121, 'Pus Filled Pimples': 122, 'Blackheads': 123, 'Scurring': 124, 'Skin Peeling': 125, 'Silver Like Dusting': 126, 'Small Dents In Nails': 127, 'Inflammatory Nails': 128, 'Blister': 129, 'Red Sore Around Nose': 130, 'Yellow Crust Ooze': 131}
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for symptom in patient_symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
    
    # Ensure input is 2D for model prediction
    input_vector = np.array([input_vector])
    print("Input vector for prediction:", input_vector)  # Debugging line
    
    predicted_index = svc.predict(input_vector)[0]
    print("Predicted index:", predicted_index)  # Debugging line
    
    predicted_disease = diseases_list.get(predicted_index, "Unknown Disease")
    print("Predicted disease:", predicted_disease)  # Debugging line
    
    return predicted_disease

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the symptoms from the form input
        symptoms_sentence = request.form.get('symptomsInput', '').strip()

        if not symptoms_sentence:
            message = "Please enter symptoms or a sentence describing your symptoms."
            return render_template('index.html', message=message)

        # Extract symptoms from the sentence
        extracted_symptoms = extract_symptoms(symptoms_sentence)

        if not extracted_symptoms:
            message = "No valid symptoms identified. Please describe your symptoms more clearly."
            return render_template('index.html', message=message)

        # Predict disease
        predicted_disease = get_predicted_value(extracted_symptoms)

        dis_des, precautions, medications, diets , workout= helper(predicted_disease)

        my_precautions = [precaution for precaution in precautions[0]]
        my_medications = [medications for medications in medications[0]]
        my_diets = [diets for diets in diets[0]]

        return render_template(
             "results.html",
            # 'index.html', 
            symptoms_sentence=symptoms_sentence,
            extracted_symptoms=", ".join(extracted_symptoms),
            predicted_disease=predicted_disease, 
            dis_des=dis_des, 
            my_precautions=my_precautions,
            my_medications=my_medications, 
            my_diets=my_diets,
            workout = workout
        )


# about view funtion and path
@app.route('/about')
def about():
    return render_template("about.html")
# contact view funtion and path
@app.route('/contact')
def contact():
    return render_template("contact.html")

# developer view funtion and path
@app.route('/developer')
def developer():
    return render_template("developer.html")

# about view funtion and path
@app.route('/blog')
def blog():
    return render_template("blog.html")


if __name__ == '__main__':

    app.run(debug=True)