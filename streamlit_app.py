"""
Jack Liu 
First Streamlit App for Snowflake Badge 2 Data Builders Application Workshop
06/03/23
"""

import streamlit as st
import pandas
import requests
import snowflake.connector

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

#Add the requests python package library to request data from fruityvice API
st.header('Fruityvice Fruit Advice!')

#Create a fruit_choice text input to get user input on choice of fruit to display
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#Takes the json version of the API response and normalize it, then output it to the streamlit as a table with dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)



