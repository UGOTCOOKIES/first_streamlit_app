"""
Jack Liu 
First Streamlit App for Snowflake Badge 2 Data Builders Application Workshop
06/03/23
"""

import streamlit as st
import pandas
import requests

#Create the menu and display as text 
st.title('My Mom\'s New Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal \n🥗 Kale, Spinach & Rocket Soothie \n🐔 Hard-Boiled Free-Range Egg \n🥑🍞 Avocado Toast')
st.header('Fruit Smoothies')
st.text('🍌🥭Friendly Neighbourhood Banana Strawberry Smoothie')

#Use python pandas to read csv file and pull the data from csv into a strealit dataframe object to be displayed
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Add a pick list so users can pick which fruits to add
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page
st.dataframe(fruits_to_show)

#Add the requests python package library
st.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())


