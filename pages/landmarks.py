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
    display = Image.open('static/landmarks/landmark_cover3.jpeg')
    col1, col2 = st.columns(2)
    col1.image(display, width = 350)
    col2.title('Landmarks')
    col2.write('"It is better to see something once than to hear about it a thousand times." - Chinese proverb')

    #local_css(os.path.join(here,"style.css"))
    st.write("Enter a country to see its landmarks.")
    location = st.text_input('Country','United States')

    if st.button('Search'):
        try:
            getCoords(location, 10, 3)
        except:
            st.write("Something went wrong")
        #    print("error")


def getCoords(country, numPlacesToCheck, maxPerPlace):
    # response = requests.get('https://countriesstats-8fc99-default-rtdb.firebaseio.com/forLandmarks/'+country+'.json')
    response = requests.get('https://dsci551-countriesdb-default-rtdb.firebaseio.com/forLandmarks/' + country + '.json')
    placeList = response.json()
    if (not placeList):
        st.write("Invalid country name.")
        return
    placeList = sorted(placeList, key = lambda x: x['population'], reverse=True)
    for i in placeList[:numPlacesToCheck+1]:
        #print('trying place ' + i['name'])
        lat = i['lat']
        lng = i['lng']
        basicSearch('Famous landmarks',lat,lng,maxPerPlace)
    response.text

def basicSearch(term, lat, lon,maxPerPlace):
    """ Returns the first 50 results for a search term and location from Yelp API """

    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    base_url = BASE_URL + "businesses/search"

    offset = 0
    limit = 50

    params = {'term': term,
          'latitude':lat,
          'longitude':lon,
          'radius':40000,
          'offset': offset,
          'sort_by':'review_count',
          'limit': limit}

    response = requests.get(base_url, headers=headers, params=params, timeout=5)
    json_res = json.loads(response.text)
    output_dict = json_res["businesses"]
    #st.write("Here are some landmarks related to " + term + ":")
    if (len(output_dict) == 0):
        b = 1
        #st.write("Nothing found!")
    else:
        showInterval(0,maxPerPlace,output_dict)

def showInterval(cur_index, interval, output_dict):
    """ Shows the first (interval) amount of results from the call to Yelp API """
    if (interval > len(output_dict)):
        interval = len(output_dict)
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
        col2.image(item['image_url'],use_column_width='auto')

    #st.write(output_dict)
