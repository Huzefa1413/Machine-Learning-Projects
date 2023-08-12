import streamlit as st
import pickle
import pandas as pd 

regressor = pickle.load(open('Regressor.pkl','rb'))
locations = pickle.load(open('Location.pkl','rb'))

def predict_house_price(data):
    return regressor.predict(data)

st.title('House Price Predictor')

location_name = st.selectbox('Location:',sorted(locations['Location'].unique()))
locations_index = locations[locations['Location'] == location_name].index[0]
location_id = locations['Location_ID'][locations_index]

col1,col2,col3 = st.columns(3)
with col1:
    number = st.number_input('Area Size:', step=1)
with col2:
    unit = st.selectbox('Area Unit:',options=['Marla','Kanal','Sq'])
    if unit == 'Marla':
        unit = 1
    elif unit == 'Kanal':
        unit = 0
    elif unit == 'Sq':
        unit = 2
with col3:
    rooms = st.number_input('Number of Rooms:', step=1)
if st.button('Get Price'):
    price = predict_house_price([[number,unit,rooms,location_id]])
    price = "PKR {:,.2f}".format(price[0])
    st.subheader('Price: ' + str(price))