import streamlit as st
from PIL import Image
import requests, json
import os

here = os.path.dirname(os.path.abspath(__file__))

API_KEY = "MtZilmOxg6XQK4tnYjfqOD4fCBy2VD6ts1BGgXrI7AbSjVy7OFBr4PpwTAh7fjRq8g_kPRQ7vD9ZMh_5n5H8Ow2lYifj38dt8QFoHT9-f7SCICDLclY1ctXvAGYYYnYx"
BASE_URL = "https://api.yelp.com/v3/"

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def app():
    # Title of the main page
    display = Image.open('static/landing_food.jpeg')
    col1, col2 = st.columns(2)
    col1.image(display, width = 350)
    col2.title('Food IS Culture')
    col2.write('You have to taste a culture to understand it - Deborah Carter')

    #local_css(os.path.join(here,"style.css"))

    term = st.text_input('Cuisine type','food')
    location = st.text_input('Current location','Los Angeles, CA')

    if st.button('Search'):
        #try:
        basicSearch(term, location)
        print("Success")
        #except:
        #    st.write("Something went wrong")
        #    print("error")

    st.header("Explore Different Common Types of Food Near You:")
    dist_location = st.text_input('Search location','Los Angeles, CA')
    if st.button('Get Results'):
        distributionSearch(dist_location)
        print("Success")

def basicSearch(term, location):
    """ Returns the first 50 results for a search term and location from Yelp API """

    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    base_url = BASE_URL + "businesses/search"

    offset = 0
    limit = 50

    params = {'term': term, 
          'location': location,
          'offset': offset,
          'limit': limit}

    response = requests.get(base_url, headers=headers, params=params, timeout=5)
    json_res = json.loads(response.text)
    output_dict = json_res["businesses"]
    st.write("Here are some restaurants related to " + term + ":")
    showInterval(0,5,output_dict)

def showInterval(cur_index, interval, output_dict):
    """ Shows the first (interval) amount of results from the call to Yelp API """
    for i in range(cur_index, interval):
        item = output_dict[i]

        col1, col2 = st.columns(2)

        col1.header(item['name'])
        category_string = ''
        for alias in item['categories']:
            category_string += alias['title'] + ', '
        category_string = category_string[:-2]
        col1.write(category_string)
        loc_string = ''
        for loc in item['location']['display_address']:
            loc_string += loc + ', '
        col1.write(loc_string)    
        col1.write("Rating: " + str(item.get('rating','N/A')))
        
        col1.write("Price is: " + item.get('price','N/A'))
        col2.image(item['image_url'],use_column_width='auto')

    #st.write(output_dict)


def distributionSearch(location):
    """ Returns the distribution of restaurant categories in a give location from Yelp API """
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    base_url = BASE_URL + "businesses/search"

    # iterate through in batches of 50 for 1000 total
    category_dict = {}

    for i in range(0,10):
        print(i)
        offset = 50*i
        params = {'term': "food", 
          'location': location,
          'offset':offset,
          'limit': 50}
    
        response = requests.get(base_url, headers=headers, params=params, timeout=5)
        json_res = json.loads(response.text)
        output_dict = json_res["businesses"]
        restaurant_categories = [x['categories'] for x in output_dict]
        #print(restaurant_categories)

        for restaurant in restaurant_categories:
            if restaurant:
                first_title = restaurant[0]['title']
                if first_title in category_dict:
                    category_dict[first_title] += 1
                else:
                    category_dict[first_title] = 1
    
    dict_view = [(v,k) for k,v in category_dict.items()]
    dict_view.sort(reverse=True)
    #for (v,k) in dict_view:
    #    st.write("%s: %d" %(k,v))
    numToList = 4
    lst = []
    while (numToList > 0):
        for (v, k) in dict_view:
            lst.append(k)
            numToList -= 1

    st.write("The most common common types of food in " + location + " are " + lst[0] + ", " + lst[1] + ", " + lst[2] + ", and " + lst[3] + ".")