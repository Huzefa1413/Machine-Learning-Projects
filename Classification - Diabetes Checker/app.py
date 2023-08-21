import streamlit as st
import pickle


sc = pickle.load(open("Scaler.pkl", "rb"))
classifier = pickle.load(open("Classifier.pkl", "rb"))


st.title("Diabetes Checker")

col1, col2 = st.columns(2)

with col1:
    inp1 = st.number_input("Number of times pregnant:", step=1, min_value=0)
with col2:
    inp2 = st.number_input(
        "Plasma glucose concentration a 2 hours in an oral glucose tolerance test:",
        step=1,
        min_value=0,
    )


col1, col2 = st.columns(2)

with col1:
    inp3 = st.number_input("Diastolic blood pressure (mm Hg):", step=1, min_value=0)
with col2:
    inp4 = st.number_input("Triceps skin fold thickness (mm):", step=1, min_value=0)


col1, col2 = st.columns(2)

with col1:
    inp5 = st.number_input("2-Hour serum insulin (mu U/ml):", step=1, min_value=0)
with col2:
    inp6 = st.number_input(
        "Body mass index (weight in kg/(height in m)^2):",step=0.1, value= 0.0 , min_value=0.0
    )

col1, col2 = st.columns(2)

with col1:
    inp7 = st.number_input("Diabetes pedigree function:", step=0.1, value= 0.0 , min_value=0.0)
with col2:
    inp8 = st.number_input("Age (years):", step=1, min_value=0)

if st.button("Check Diabetes"):
    prediction = classifier.predict(
        sc.transform([[inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8]])
    )
    if prediction[0] == 1:
        text = "Patient has diabetes"
    else:
        text = "The patient doesn't have diabetes"
    st.subheader(text)
