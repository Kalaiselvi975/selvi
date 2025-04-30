import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# Title
st.title('🩺 Diabetes Prediction Web App')

# Sidebar title
st.sidebar.header('User Input Features')

# User input fields
pregnancies = st.sidebar.number_input('Pregnancies', min_value=0)
glucose = st.sidebar.number_input('Glucose Level', min_value=0)
blood_pressure = st.sidebar.number_input('Blood Pressure', min_value=0)
skin_thickness = st.sidebar.number_input('Skin Thickness', min_value=0)
insulin = st.sidebar.number_input('Insulin', min_value=0)
bmi = st.sidebar.number_input('BMI', min_value=0.0)
diabetes_pedigree = st.sidebar.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.sidebar.number_input('Age', min_value=0)

# Predict button
if st.sidebar.button('Predict'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(input_data)

    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.error('🚨 The person is Diabetic.')
    else:
        st.success('✅ The person is NOT Diabetic.')