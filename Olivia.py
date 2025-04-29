#Olivia
## Para arracan streamlit hay que escribir en la terminal : streamlit run Olivia.py


import streamlit as st
import pandas as pd
import numpy as np
import base64
import os
from PIL import Image

#El request me va a ayudar a importar el archivo de la URL y así permitirme descargarme el archivo una vez pulse el botón
import requests





# Pasos para conseguir el botón de descarga del CV:
    # 1º Crear una referencia del la url
    
link_cv = 'https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/CV%20Victor%20Guti%C3%A9rrez.png'

    # 2º Crear el botón de descarga en la zona deseada.

    #3º Configurar el botón 

response = requests.get(link_cv)
pdf_data = response.content



# Configuración de la página
st.set_page_config(
    page_title='Olivia_training',
    page_icon="",
    layout='wide', )


# Imagen para el fondo de pantalla

def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )
        
add_bg_from_local('fondo.jpg')

## Imágenes desde la carpeta
imagen1 = Image.open("C:/Users/Usuario/Desktop/Olivia/italianrestaurant.png")

### sidebar

top_sidebar_placeholder = st.sidebar.empty()
top_sidebar_placeholder.markdown('''
<p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/portada.jpg?token=GHSAT0AAAAAACXPZG5MLQWWR4XXNVGV4HDUZXVVP2A" width="100%" alt="Akkurat">
  <br>
</p>
''', unsafe_allow_html=True)
st.sidebar.title('Index')


page = st.sidebar.radio('', ['What is Olivia?', 'Something about Italy', 'The wines', 'Our food', 'Test', 'Hi, Víctor is here.'])
about_selection = ''



with st.spinner('Un attimo per favore'):
      

### What is Olivia ?
    if page == 'What is Olivia?':
        st.image(imagen, caption="imagen1", use_column_width=True)
        st.subheader('What is Olivia?')
        st.markdown("#### The origins of Oliva")

        st.markdown('### Olivia´s family')
        st.markdown('#### All restaurants and how they are organized (jobs - promotion requirements).')


### Something about Italy?
    elif page == 'Something about Italy?':
        st.markdown('''
                     <p align="center">
  <img src="https://www.mensjournal.com/.image/t_share/MTk3MDg4ODkwMDM5OTAzMzE1/promo_amalfi_gettyimages_aleh-varnishcha.jpg" width="30%" alt="Italia TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('What do you know about Italy?')
        st.markdown("####  History, culture, Geography, etc. ")


### Something about Italy?
    elif page == 'Something about Italy?':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/jeg.jpeg?token=GHSAT0AAAAAACXPZG5NORLLY6HD74Z7A7IYZXVVNTA" width="30%" alt="Italia TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('What do you know about Italy?')
        st.markdown("####  History, culture, Geography, etc. ")


### The wines?
    elif page == 'The wines?':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/jeg.jpeg?token=GHSAT0AAAAAACXPZG5NORLLY6HD74Z7A7IYZXVVNTA" width="30%" alt="Wines TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('How to become a wine expert?')
        st.markdown("##  sommelier course ")
        st.markdown("##  A brief introduction to what you should know about wines. ")
        st.markdown("##  What wines do we have? ")
