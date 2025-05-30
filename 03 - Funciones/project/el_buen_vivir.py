import streamlit as st
import pandas as pd

def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto):
    subtotal = float(precio_producto) * float(cantidad_producto)
    nueva_fila = {'producto': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto, 'subtotal': subtotal}
    st.session_state.table_data = pd.concat([st.session_state.table_data, pd.DataFrame([nueva_fila])], ignore_index=True)

if 'table_data' not in st.session_state:
    st.session_state.table_data = pd.DataFrame(columns = ['producto', 'precio', 'cantidad', 'subtotal'])


st.title('Supermercado el Buen Vivir')

with st.form('producto_form'):
    producto_nombre = st.text_input('Introduce el nombre del producto')
    producto_precio = st.number_input('Introduce el precio del producto')
    producto_cantidad = st.number_input('Introduce la cantidad de productos')

    subtotal_boton = st.form_submit_button('Comprar producto')

if subtotal_boton:
    calcular_subtotal(producto_nombre, producto_precio, producto_cantidad)

st.dataframe(st.session_state.table_data)

if st.button('Calcular Total'):
    total = (st.session_state.table_data['precio'] * st.session_state.table_data['cantidad']).sum()

    st.subheader('El Precio Total')
    st.write('El precio total es: ' + str(total))