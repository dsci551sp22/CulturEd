import streamlit as st
import requests, json
from serpapi import GoogleSearch
from PIL import Image

API_KEY = "12f7ff6ffdb37b954364f9e9150dcfa50c25ce1072ab8c9c833ce9e0ac5d71f4"

def app():
     # Title of the main page
    display = Image.open('static/culture5.jpeg')
    col1, col2 = st.columns(2)
    col1.image(display, width = 350)
    col2.title('CulturEd')
    col2.write('An educational platform built to inform the public on various cultures through food and local events')

    st.title("Events")

    term = st.text_input('Cultural Event', "Enter event")
    location = st.text_input('Current Location', 'Los Angeles, CA')

    if st.button('Search'):
        search(term, location)

def search(term, location):
    params = {
        "engine": "google_events",
        "q": term + ' events',
        "location": location,
        "api_key": API_KEY
    }

    search = GoogleSearch(params) 
    results = search.get_dict()
    events_results = results['events_results']
    st.write('Here are some events related to ' + term + ' :')
    showInterval(0,5,events_results)


def showInterval(cur_index, interval, output_dict):
    """ Shows the first (interval) amount of results from the call to Yelp API """
    for i in range(cur_index, interval):
        try:
            item = output_dict[i]
        except: 
            break

        col1, col2 = st.columns(2)

        col1.header(item['title'])
        col1.write(item['date']['start_date'])
        col1.write(item['date']['when'])
        col1.write(item['address'][0])
        col1.write(item['address'][1])
        col2.image(item['thumbnail'],use_column_width='auto')