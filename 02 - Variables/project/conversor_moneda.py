# Programa para convertir de dolares a euros

import streamlit as st

st.title('Conversor de Dolares a Euros')

dolares = st.number_input('Introduce la cantidad de dolares')

euros = dolares * 1.14

st.button('Procesar', on_click=print(f'{dolares} Dolares son {euros} Euros'))