"""
Jack Liu 
First Streamlit App for Snowflake Badge 2 Data Builders Application Workshop
06/03/23
"""

import streamlit as st
import pandas

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
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#Display the table on the page
st.dataframe(my_fruit_list)




