import pickle
import numpy as np
import streamlit as st

#load save model 
model = pickle.load (open('Watermelon.sav','rb'))

#judul web
st.title('Prediksi Kualitas Semangka')

col1, col2, col3, =st.columns(3)

with col1:
    Num = st.number_input ('Nomer')
with col2:
    Color = st.number_input ('Warna')
with col3:
    Root = st.number_input ('Akar')
with col1:
    Sound = st.number_input ('Suara')
with col2:
    Texture = st.number_input ('Kualitas')
with col3:
    Belly_button = st.number_input ('Pusar')
with col1:
    Touch = st.number_input ('Menyentuh')
with col2:
    Density = st.number_input ('Kepadatan')
with col3:
    sugar_rate = st.number_input ('Tingkat Gula')

#code for prediction
watermelon_diagnosis =''

#membuat tombol prediction
if st.button('Prediksi Semangka'):
    watermelon_prediction = model.predict([[Num,Color,Root,Sound,Texture,Belly_button,Touch,Density,sugar_rate]])

    if (watermelon_prediction [0]==0):
        watermelon_diagnosis = 'Kualitas Semangka buruk'
    else : 
        watermelon_diagnosis = 'kualitas Semangka baik'

st.success (watermelon_diagnosis)

st.write ('SALSABIL ~ 191351087')

