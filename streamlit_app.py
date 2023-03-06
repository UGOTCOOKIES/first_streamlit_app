"""
Jack Liu 
First Streamlit App for Snowflake Badge 2 Data Builders Application Workshop
06/03/23
"""

import streamlit as st
import pandas

st.title('My Mom\'s New Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal \n🥗 Kale, Spinach & Rocket Soothie \n🐔 Hard-Boiled Free-Range Egg \n🥑🍞 Avocado Toast')
st.header('Fruit Smoothies')
st.text('🍌🥭Friendly Neighbourhood Banana Strawberry Smoothie')
        
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
