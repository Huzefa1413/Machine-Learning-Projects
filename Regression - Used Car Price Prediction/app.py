import streamlit as st
import joblib
import pandas as pd
import numpy as np

data = pd.read_csv('clean_used_car.csv')
ct = joblib.load('ColumnTransformer.pkl','rb')
regressor = joblib.load('RegressionModel.pkl')

def predict_price(prediction):
    prediction = ct.transform(prediction)
    prediction = prediction.toarray() if hasattr (prediction, 'toarray') else prediction
    return regressor.predict(prediction)[0]

st.title('Car Price Predictor')
brand = st.selectbox(
    'Select Your Car Company: ',
    sorted(data['brand'].unique()))
name = st.selectbox(
    'Select Your Car Name: ', sorted(data['description'][data['brand'] == brand].unique()))
model = st.selectbox(
    'Select Your Car Model: ',
    sorted(data['model_date'].unique()))
km = st.number_input('Enter Your Cars Km Driven: ',step=1,min_value=0)
fuel = st.selectbox(
    'Select Your Car Fuel Type: ',
    sorted(data['fuel_type'].unique()))
engine = st.selectbox(
    'Select Your Car Engine in cc: ',
    sorted(data['vehicle_engine'].unique()))
transmission = st.selectbox(
    'Select Your Car Transmission: ',
    sorted(data['vehicle_transmission'].unique()))

if st.button('Get Price'):
    price = predict_price([[brand, name, fuel, km, model, engine, transmission]])
    price = "PKR {:,.2f}".format(price)
    st.subheader('Price: ' + str(price))
