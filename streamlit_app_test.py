import streamlit
streamlit.title('My hobby')
streamlit.header('Sports')
streamlit.text(('footbal,cricket....'))

streamlit.header('Breakfast Menu - 🥣 🥗 🐔 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruit_to_show)

# # my_fruit_list1 = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list1.index),['Avocado'])
# # streamlit.dataframe(my_fruit_list1)

# fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
# fruit_to_show=my_fruit_list.loc[fruits_selected]
# streamlit.dataframe(fruit_to_show)
