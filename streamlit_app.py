"""
Jack Liu 
First Streamlit App for Snowflake Badge 2 Data Builders Application Workshop
06/03/23
"""

import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#Create function
def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized
  
#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!') 
try: 
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)

except URLError as e:
  st.error()
  
#Query Snowflake
st.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()

#Add a button to load the fruit
if st.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     st.dataframe(my_data_rows)
     
#Allow the user to add a fruit to the list
def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
          return "Thanks for adding " + new_fruit
     
add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a Fruit to the List'):
     my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     st.text(back_from_function)
