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
    page_title='Olivia Academy',
    page_icon="",
    layout='wide', )


# Imagen para el fondo de pantalla



### sidebar

top_sidebar_placeholder = st.sidebar.empty()
top_sidebar_placeholder.markdown('''
<p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/fondo.jpg" width="100%" alt="Olivia">
  <br>
</p>
''', unsafe_allow_html=True)
st.sidebar.title('Index')


page = st.sidebar.radio('', ['What is Olivia?', 'Something about Italy', 'The wines', 'Our food', 'Test', 'Hi, Víctor is here.'])
about_selection = ''



with st.spinner('Un attimo per favore'):
      

### What is Olivia ?
    if page == 'What is Olivia?':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/fondo.jpg" width="30%" alt="">
  <br>
</p>
''', unsafe_allow_html=True)
        st.markdown('''
                     <p align="center">
  <img src="" width="30%" alt="Nærmere Italia kommer du ikke">
  <br>
</p>
''', unsafe_allow_html=True)
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


### The wines?
    elif page == 'The wines':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/wine.png" width="30%" alt="Wines TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('# How to become a wine expert?')
        st.markdown("###  sommelier course ")
        st.markdown("### A brief introduction to what you should know about wines. ")
        st.markdown("###  What wines do we have? ")


### The Food
    elif page == 'Our food':
        about_selection = st.sidebar.radio('', ['Intolerances and Allergies', 'Starters', 'Fresh from the oven', 'Fresh as a cucumber', 'From the stove to the plate', 'Desserts' ])
        if about_selection == 'Intolerances and Allergies':
            st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/allergy.jpg" width="30%" alt="Wines TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('# Intolerances')
        st.markdown("###  ----- ")
        st.subheader('# Allergies')
        st.markdown("### -------. ")
        st.subheader('# Others')



