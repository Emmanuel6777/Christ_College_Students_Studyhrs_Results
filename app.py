import streamlit as st
import joblib

model = joblib.load("student_studyhrs_withatt_model.pkl")

st.title("Student Pass/Fail Based on study Hours")

hours=st.number_input("Enter study hours",min_value=0.0,max_value=15.0,value=5.0)
attendance=st.number_input("Enter attendance hours",min_value=0.0,max_value=100.0,value=75.0)

input_data=pd.DataFrame({
  "StudyHours":[hours],
  "attendance":[attendance]
})
if st.button("Predict"):
  prediction = model.predict(input_data)
  prob=model.predict_proba(input_data)
  predictedpass=prob[0][1]
  if prediction[0]==1:
    st.success("PASS")
  else:
    st.error("FAIL")
  st.write("Pass Probablity:",predictedpass*100,"%")
                      
