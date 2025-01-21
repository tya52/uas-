import streamlit as st
import pickle
import numpy as np


with open('model_uas.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Prediksi Charges Asuransi")
st.write("Nama: Hadiid Fadli Marbun | NIM: 2021230054053")

age = st.number_input("Usia", min_value=0, max_value=100)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0)
children = st.number_input("Jumlah Anak", min_value=0, max_value=10)
smoker = st.selectbox("Perokok?", ["no", "yes"])
region = st.selectbox("Wilayah", ["northeast", "northwest", "southeast", "southwest"])


smoker = 1 if smoker == "yes" else 0
region_mapping = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region = region_mapping[region]


if st.button("Submit"):
    input_data = np.array([[age, bmi, children, smoker, region]])
    prediction = model.predict(input_data)
    st.success(f"Prediksi Biaya Asuransi: ${prediction[0]:.2f}")
