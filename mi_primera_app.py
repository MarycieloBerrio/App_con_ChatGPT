import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.write("Esta app fue elaborada por “Marycielo Berrio”.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Imprimir el mensaje de bienvenida
if nombre_usuario:
    mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje_bienvenida)
