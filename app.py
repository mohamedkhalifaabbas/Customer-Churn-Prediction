import streamlit as st
import requests

st.title("Customer Churn Prediction 🚀")
st.write("Enter customer details to predict whether they are likely to churn or stay with the bank.")


CreditScore = st.number_input("Credit Score", min_value=300, max_value=850, value=619)
Geography = st.selectbox("Geography ", ['France', 'Spain', 'Germany'])
Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.number_input("Age", min_value=18, max_value=100, value=42)
Tenure = st.number_input("Tenure (Years with bank)", min_value=0, max_value=10, value=2)
Balance = st.number_input("Balance", min_value=0.0, value=0.0)
NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=10, value=1)
HasCrCard = st.selectbox("Has Credit Card (0=No, 1=Yes)", [0, 1])
IsActiveMember = st.selectbox("Is Active Member (0=No, 1=Yes)", [0, 1])
EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, value=101348.88)


# Predict button
if st.button("Predict"):
    features = {
    "features": [CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]
    }

    url = "http://127.0.0.1:5000/predict" 
    response = requests.post(url, json=features)
  
    if response.status_code == 200:
        response_data = response.json()
        prediction = response_data.get("prediction")

        if prediction == 0:
            st.success("✅ The customer is likely to **stay** with the bank")
        else:
            st.error("❌ The customer is likely to **churn**")
    else:
        st.error(f"API Error: {response.status_code}")

