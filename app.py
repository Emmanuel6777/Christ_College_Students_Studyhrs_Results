import streamlit as st
import joblib

model = joblib.load("logistic_regression_Student__Studyhrs_Results_model.pkl")

st.title("Student Pass/Fail Based on study Hours")

hours=st.number_input("Enter study hours",min_value=0.0,max_value=15.0,value=5.0)

if st.button("Predict"):
  prediction = model.predict([[hours]])
  prob=model.predict_proba([[hours]])
  preditcedpass=prob[0][1]
  if prediction[0]==1:
    st.success("PASS")
  else:
    st.error("FAIL")
  st.write("Pass Probablity:",predictedpass*100,"%")
                      
