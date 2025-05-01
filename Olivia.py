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

### Games
questions = [
    {
        "question": "What is the main grape used in red Bordeaux wines?",
        "options": ["Merlot", "Pinot Noir", "Zinfandel"],
        "answer": "Merlot"
    },
    {
        "question": "Which country is the largest producer of wine?",
        "options": ["France", "Italy", "Spain"],
        "answer": "Italy"
    },
    {
        "question": "What does 'terroir' refer to in wine?",
        "options": ["A wine's age", "The region’s environmental factors", "Fermentation method"],
        "answer": "The region’s environmental factors"
    },
    {
        "question": "Which of the following is a white grape variety?",
        "options": ["Chardonnay", "Cabernet Sauvignon", "Syrah"],
        "answer": "Chardonnay"
    },
    {
        "question": "What is rosé wine made from?",
        "options": ["White grapes only", "Red grapes with short skin contact", "Mixing red and white wines"],
        "answer": "Red grapes with short skin contact"
    },
    {
        "question": "Which region is famous for Chianti wine?",
        "options": ["Tuscany", "Bordeaux", "Rioja"],
        "answer": "Tuscany"
    },
    {
        "question": "What is the ideal temperature to serve red wine?",
        "options": ["8°C", "16–18°C", "25°C"],
        "answer": "16–18°C"
    },
    {
        "question": "Which wine is typically sweet?",
        "options": ["Port", "Cabernet Sauvignon", "Barolo"],
        "answer": "Port"
    },
    {
        "question": "Which country is known for Malbec wine?",
        "options": ["Argentina", "Germany", "Portugal"],
        "answer": "Argentina"
    },
    {
        "question": "Which of these wines is sparkling?",
        "options": ["Chablis", "Chianti", "Prosecco"],
        "answer": "Prosecco"
    },
    {
        "question": "What gives red wine its color?",
        "options": ["Grape juice", "Grape skins", "Barrel aging"],
        "answer": "Grape skins"
    },
    {
        "question": "Which wine is traditionally used in cooking coq au vin?",
        "options": ["White wine", "Red wine", "Rosé"],
        "answer": "Red wine"
    },
    {
        "question": "Which of the following is not a wine region in France?",
        "options": ["Champagne", "Napa Valley", "Burgundy"],
        "answer": "Napa Valley"
    },
    {
        "question": "What does 'vintage' mean in wine?",
        "options": ["Age of the barrel", "The year the grapes were harvested", "Type of grape used"],
        "answer": "The year the grapes were harvested"
    },
    {
        "question": "What does a sommelier do?",
        "options": ["Grows grapes", "Designs wine labels", "Selects and serves wine"],
        "answer": "Selects and serves wine"
    },
    {
        "question": "Which grape is used to make Rioja wine?",
        "options": ["Tempranillo", "Cabernet Franc", "Grenache"],
        "answer": "Tempranillo"
    },
    {
        "question": "Which wine is made in the Champagne region of France?",
        "options": ["Cava", "Prosecco", "Champagne"],
        "answer": "Champagne"
    },
    {
        "question": "Which of these wines is fortified?",
        "options": ["Sherry", "Beaujolais", "Moscato"],
        "answer": "Sherry"
    },
    {
        "question": "What is the main grape used in Barolo wine?",
        "options": ["Nebbiolo", "Sangiovese", "Zinfandel"],
        "answer": "Nebbiolo"
    },
    {
        "question": "What is the alcohol range of most table wines?",
        "options": ["5–7%", "8–15%", "16–20%"],
        "answer": "8–15%"
    }
]





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
    elif page == 'Something about Italy':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/Flag_of_Italy.svg.png" width="30%" alt="">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('What do you know about Italy?')
        st.markdown("#### Italy is one of the twenty-seven sovereign states that make up the European Union and one of the countries that has had the greatest influence on the development of Western European history, given that its capital, Rome, was the birthplace and development of the Roman Empire.")
        st.markdown("#### Its geography is highly diverse, both in terms of climate and relief, which favors the development of a wide variety of high-quality products. ")


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

### Tests?
    elif page == 'Test':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/wine.png" width="30%" alt="Wines TEST">
  <br>
</p>
''', unsafe_allow_html=True)
        st.title("🍷 Wine Quiz")



        for i, q in enumerate(questions, 1):
            st.subheader(f"Question {i}")
            user_answer = st.radio(q["question"], q["options"], key=i)
            if st.button(f"Submit Answer {i}", key=f"btn{i}"):
                if user_answer == q["answer"]:
                    st.success("Correct! 🎉")
                    score += 1
                else:
                    st.error(f"Incorrect. The correct answer is: {q['answer']}")

        st.markdown("---")
        st.header(f"Final Score: {score} / {len(questions)}")


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



## my side

    elif page == 'Hi, Víctor is here.':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/yo.jpg" width="30%" alt="My partner and I receiving the FLUPP of the month award.">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('Who Am I?')
        st.markdown("####  👨‍🏫Hi, my name is Victor and I work at Olivia Ramsalt in Bodø. I created this to facilitate the learning process in a new position at Olivia. I'm doing this because I enjoy working with computers (I'm a data analyst by training) and everything related to education (I was a history teacher in my home country before coming to Norway).")

        st.markdown('### Why did I create this?')
        st.markdown('#### I recently had a job interview and I had a bit of a hard time figuring out what my skills are or what projects I have created.')
        
        st.markdown('### Is there anything wrong or missing something?')
        st.markdown("#### I'm creating this website in my spare time, so it's not perfect, but I'd love for it to be. So, if you'd like, you can contact me by email, and together we can make this a better place. " \
        "vicgutgam@gmail.com.")




