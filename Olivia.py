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


# Configuración de la página
st.set_page_config(
    page_title='Olivia Academy',
    page_icon="🫒",
    layout='wide' )


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
        about_selection = st.sidebar.radio('', ['Intolerances and Allergies', "Introduction to our menu", 'Starters', 'Fresh from the oven', 'Fresh as a cucumber', 'From the stove to the plate', 'Desserts' ])
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
            st.subheader('# Celiac disease ')

        elif about_selection == 'Introduction to our menu':
            st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/productos.jpg" width="50%" alt="productos">
  <br>
</p>
''', unsafe_allow_html=True)
            st.markdown ('# Cheese')
            
            st.markdown('''
                     <p align="center">
  <img src="" width="30%" alt="Parmesano reggiano">
  <br>
</p>
''', unsafe_allow_html=True)
            st.markdown('## Mozzarella')
            st.markdown("####  The name ""mozzarella"" comes from the Italian verb ""mozzare,"" which means to cut, referring to how the cheese balls are manually cut at the end of the process. It encompasses a variety of fresh, soft, and elastic spun-curd cheeses, traditionally made from buffalo milk, but also commonly from cow's milk. ")
            data = {
    "Cheese": ["Mozzarella di Bufala", "Fior di Latte", "Burrata"],
    "Milk type": ["Buffalo", "Cow", "Cow or buffalo"],
    "Flavor": ["Intense, tangy", "Mild, milky", "Very mild and fresh"],
    "Texture": [
        "Creamy and elastic",
        "Firm and moist",
        "Firm outside, creamy inside"
    ],
    "Best use": [
        "Salads, gourmet pizzas",
        "Everyday cooking, pizzas",
        "Cold dishes, center of the plate"
    ]
}

                # Convert to DataFrame
            df = pd.DataFrame(data)

                # Title
            st.markdown("### Comparison of Mozzarella Types")

                # Display table
            st.table(df)
            moz1, moz2, moz3 = st.columns(3)
            with moz1:
                st.markdown('''
                     
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/mozarrela%20di%20buffala.jpg" width="50%" alt="Mozarrela di buffala.">
  <br>
</p>
''', unsafe_allow_html=True)
            with moz3:
                st.markdown('''
                     
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/mozzarella-burrata-recettes-tomates-confites-olives.jpeg" width="50%" alt="Mozarrela di burrata.">
  <br>
</p>
''', unsafe_allow_html=True)
            with moz2:
                st.markdown('''
                     
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/Fior-di-Latte-e1655353087386.jpeg" width="50%" alt="Mozarrela fior di late.">
  <br>
</p>
''', unsafe_allow_html=True)
                
                

            st.markdown('## Stracciatella')
            st.markdown("#### Stracciatella is a soft, creamy Italian cheese made from shredded fresh mozzarella mixed with cream. It has a delicate, milky flavor and a luxurious texture that's both stringy and smooth. Originating from the Puglia region in southern Italy, it's best known as the filling of burrata cheese. Stracciatella is typically served on its own with olive oil and bread, used as a topping on pizzas, or added to salads and cold pasta dishes. ")
            st.markdown('## "Grana" Cheese ')
            st.markdown("#### Grana cheeses are a family of hard, long-aged cheeses with a grainy texture (hence the name ""grana,"" which means grain in Italian). They are made primarily from partially skimmed cow's milk and have an intense, umami, and slightly salty flavor that intensifies with age. At Olivia we have two types, Grana Padano and Parmigiano Reggiano.")
            st.markdown("#### Parmigiano Reggiano, often called the ""King of Cheeses"", is a hard, aged cheese made from raw cow's milk. It has a crumbly, granular texture and a rich, savory flavor with nutty and umami notes that become more pronounced as it matures—typically between 12 and 36 months. Produced under strict DOP regulations in northern Italy (mainly in Emilia-Romagna), Parmigiano Reggiano is ideal grated over pasta, risottos, soups, or enjoyed in chunks with balsamic vinegar or cured meats.")
            st.markdown("#### Grana Padano is a hard, aged cow’s milk cheese similar to Parmigiano Reggiano but generally milder in flavor and less salty. It has a slightly grainy texture and is aged for a minimum of 9 months, with some versions reaching 20 months. Made in the Po Valley region of northern Italy, Grana Padano is protected by a DOP label but follows less strict production standards than Parmigiano. It’s a versatile cheese that can be grated, sliced, or eaten on its own, and it's often used as a more affordable alternative to Parmigiano Reggiano.")
            st.markdown("## Percorino Romano")
            st.markdown("#### Pecorino Romano is a hard, salty Italian cheese made from sheep’s milk. It has a sharp, tangy flavor and a crumbly texture, especially when aged beyond 8 months. Though associated with Rome, most Pecorino Romano is actually produced in Sardinia. It is an essential ingredient in classic Roman dishes such as carbonara, cacio e pepe, and amatriciana. Thanks to its bold taste and high salt content, it's best used grated to season pastas, soups, and roasted vegetables. ")
            st.markdown('# Meat section')
            st.markdown('## Prosciutto di Parma')
            st.markdown("###  ----- ")
            st.markdown ('## Mortadella di Bologna')
            st.markdown("###  ----- ")
            st.markdown('## Panceta')
            st.markdown("###  ----- ")
            st.markdown('## ´Ndjua')
            st.markdown("###  ----- ")
            st.markdown('# Sauces and condiments')
            st.markdown('## Gremolata')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('''
                     
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/Gremolada.jpg" width="50%" alt="Gremolata.">
  <br>
</p>
''', unsafe_allow_html=True)
                
            with col2:
                st.markdown("####  Gremolata is a fresh Italian mixture of finely chopped parsley, grated lemon zest and garlic. ")


            st.markdown('## Kampot-pepper')
            pepper1, pepper2, pepper3 = st.columns(3)
            with pepper1:
                st.markdown('''
                     
  <img src="https://raw.githubusercontent.com/Vicgutgam/Olivia/refs/heads/main/Im%C3%A1genes/Dried_red_Kampot_peppercorns.jpg" width="50%" alt="Gremolata.">
  <br>
</p>
''', unsafe_allow_html=True)
            with pepper2:
                st.markdown("#### It's a unique and versatile spice from Cambodia that can be used in a wide variety of dishes. Its unique flavor and aroma make it a popular ingredient in gourmet cooking, particularly in French and European dishes. ")
            


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




