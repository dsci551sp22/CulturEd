import os
import streamlit as st
import numpy as np
from PIL import Image

# Custom imports 
from multipage import MultiPage
from pages import countries, food, events, landmarks, quiz # import your pages here

# Create an instance of the app 
app = MultiPage()

# Add all your application here
app.add_page("Countries", countries.app)
app.add_page("Food", food.app)
app.add_page("Events", events.app)
app.add_page("Landmarks", landmarks.app)
app.add_page("Quiz", quiz.app)

# The main app
app.run()