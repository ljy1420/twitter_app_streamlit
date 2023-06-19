import streamlit as st
from PIL import Image
import requests

image = Image.open('Twitter_Logo.png')
st.image(image, width=125)
st.header('_:blue[Twitter]_ Personality Analyzing App :sunglasses:')

account_name = st.text_input('Enter a twitter account', '@elonmusk')

if st.button('Analyze'):
    with st.spinner('It takes a while to analyze...'):
        url = st.secrets.url
        params = {
                'account_name': account_name
        }
        res = requests.get(url, params=params).json()['result']
        st.write(res)
