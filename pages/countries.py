import streamlit as st
import pandas as pd
import json
import requests
import os
import sys
import re
import glob
from PIL import Image

from pages.events import search
from pages.food import basicSearch

COUNTRIES = [None, 'Italy','France','United States of America','United Kingdom','Japan','Spain','South Korea'
                 ,'Switzerland','Germany','Sweden','China','United Arab Emirates','Brazil','Canada'
                 ,'Singapore','Australia','Greece','Netherlands','New Zealand','Mexico', 'Denmark'
                 ,'Thailand','Norway','Finland','India','Belgium','Austria','Russia','Turkey'
                 ,'Portugal','Ireland','Egypt','Qatar','Argentina','Saudi Arabia','Morocco'
                 ,'Costa Rica','Malaysia','Israel','Indonesia','South Africa','Philippines','Colombia'
                 ,'Croatia','Poland','Dominican Republic','Peru','Sri Lanka','Vietnam','Chile'
                 ,'Jordan','Panama','Kenya','Tunisia','Romania','Czech Republic','Hungary'
                 ,'Cambodia','Oman','Ecuador']

SEARCH_TERMS = {'Italy':'italian','France':'french','United States of America':'american','United Kingdom':'british','Japan':'japanese','Spain':'spanish','South Korea':'korean'
                 ,'Switzerland':'swiss','Germany':'german','Sweden':'swedish','China':'chinese','United Arab Emirates':'arab','Brazil':'brazilian','Canada':'canadian'
                 ,'Singapore':'singaporean','Australia':'austrailian','Greece':'greek','Netherlands':'dutch','New Zealand':'new zealand','Mexico':'mexican', 'Denmark':'danish'
                 ,'Thailand':'thai','Norway':'norwegian','Finland':'finnish','India':'indian','Belgium':'belgian','Austria':'austrian','Russia':'russian','Turkey':'turkish'
                 ,'Portugal':'portugese','Ireland':'irish','Egypt':'egyptian','Qatar':'qatari','Argentina':'argentinian','Saudi Arabia':'arabic','Morocco':'moroccan'
                 ,'Costa Rica':'costa rican','Malaysia':'malaysian','Israel':'israeli','Indonesia':'indonesian','South Africa':'south african','Philippines':'filipino'
                 ,'Colombia':'colombian','Croatia':'croatian','Poland':'polish','Dominican Republic':'dominican','Peru':'peruvian','Sri Lanka':'sri lankan','Vietnam':'vietnamese'
                 ,'Chile':'chilean','Jordan':'jordanian','Panama':'panamanian','Kenya':'kenyan','Tunisia':'tunisian','Romania':'romanian','Czech Republic':'czech','Hungary':'hungarian'
                 ,'Cambodia':'cambodian','Oman':'omani','Ecuador':'ecuadorian'}

@st.cache

def get_country_data(country):
    country = country.replace(" ", "")
    response = requests.get('https://dsci551-countriesdb-default-rtdb.firebaseio.com/'+country+'.json')
    response.text
    return response.json()

def countries_blurb(country):
    r1 = get_country_data(country)
    for key, value in r1.items():
        if key == 'Country Description':
            blurb = value
    return blurb

def countries_capital(country):
    r1 = get_country_data(country)
    for key, value in r1.items():
        if key == 'Capital':
            capital = value
    return capital
    
def countries_slogan(country):
    r1 = get_country_data(country)
    for key, value in r1.items():
        if key == 'Tourism Slogan':
            slogan = ('Tourism Slogan: '+value)
    return slogan    

def countries_population(country):
    r1 = get_country_data(country)
    for key, value in r1.items():
        if key == 'Population':
            population = value
    return population 

# displays country's blurb and "Tell Me More" button 
# button here is functional and will simply add "Food" and "Events" section to page
def display_country(country):
    st.subheader(countries_slogan(country))
    col1, col2 = st.columns([1,2])
    with col1:
        flag = Image.open('static/flags/' + country + '.png')
        rflag = flag.resize((250,150))
        st.image(rflag)
          
    with col2:
        st.markdown(countries_blurb(country))
        bt = st.button('Tell Me More About ' + country)
    if bt:
        st.header('National Dishes')
        food_images = glob.glob('static/dishes/' + country.replace(" ", "") + '*')
        for food_image in food_images:
            with open(food_image,"rb") as file:
                img = Image.open(file)
                rimg = img.resize((300,200)) #make all images the same size
                st.image(rimg)
                food_name = os.path.basename(food_image) #extract name frim image name
                dish_name = re.search('-(.*).jpeg',food_name)
                st.markdown(dish_name.group(1))
                st.write(' ')
                
        st.header('Restaurants')
        # basicSearch(SEARCH_TERMS[country] + ' food', 'Los Angeles, CA')
        st.header('Events')
        # search(SEARCH_TERMS[country] + ' events', 'Los Angeles, CA')

def app():
    # Title of the main page
    display = Image.open('static/Logo.png')
    col1, col2 = st.columns(2)
    col1.image(display, width = 350)
    col2.title('CulturEd')
    col2.write('An educational platform built to inform the public on various cultures through food and local events')
    
    st.title('Countries')

    country = st.selectbox(
        'Select a country', 
        options=COUNTRIES,
    )

    if country:
        display_country(country)
    else:
        for c in COUNTRIES[1:]:
            col1, col2, col3 = st.columns([2,5,1])
            
            with col1: 
                st.image('static/flags/'+c+'.png', output_format='JPEG')

            with col2:
                st.write(countries_blurb(c) + " **To learn more about {}, use the dropdown menu.**".format(c))
                st.markdown('')

            with col3: 
                st.markdown('Capital: ' + countries_capital(c))
                st.markdown('Population: ' + countries_population(c))
