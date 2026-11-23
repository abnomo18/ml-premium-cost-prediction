import streamlit as st
from prediction_helper import predict

st.title('Health Insurance Cost Predictor')

categorical_options = {
    'Gender' : ['Male', 'Female'],
    'Marital Status': ['Married', 'Unmarried'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking','Regular','Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': ['Diabetes','High blood pressure', 'No Disease','Diabetes & High blood pressure',
'Thyroid','Heart disease','High blood pressure & Heart disease', 'Diabetes & Thyroid','Diabetes & Heart disease'],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows for three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with row1[1]:
    number_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=20, step=1)
with row1[2]:
    income_lakhs = st.number_input("Income Lakhs", min_value=0, max_value=2000, step=1)

with row2[0]:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)
with row2[1]:
    insurance_plan = st.selectbox("Insurance Plan", options=categorical_options["Insurance Plan"])
with row2[2]:
    employment_status = st.selectbox('Employment Status', options=categorical_options["Employment Status"])

with row3[0]:
    gender = st.selectbox("Gender", options=categorical_options["Gender"])
with row3[1]:
    marital_status = st.selectbox("Marital Status", options=categorical_options["Marital Status"])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", options=categorical_options["BMI Category"])


with row4[0]:
    smoking_status = st.selectbox('Smoking Status', options=categorical_options["Smoking Status"])
with row4[1]:
    region = st.selectbox("Region", options=categorical_options["Region"])
with row4[2]:
    medical_history = st.selectbox('Medical History', options=categorical_options["Medical History"])



# Creating a dictionary for input values
input_dict = {
    'Age':age  ,
    'Number of Dependents':number_of_dependents ,
    'Income in Lakhs':income_lakhs ,
    'Genetical Risk':genetical_risk ,
    'Insurance Plan':insurance_plan,
    'Employment Status':employment_status ,
    'Gender':gender ,
    'Marital Status':marital_status ,
    'BMI Category':bmi_category ,
    'Smoking Status':smoking_status ,
    'Region':region ,
    'Medical History':medical_history ,
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium Cost: {prediction}")
