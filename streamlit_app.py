import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
##streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))
#streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
	#streamlit.text(fruityvice_response.json())
	# take json version and normalize it 
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	# ouput on the screen as table
	return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:

	fruit_choice = streamlit.text_input('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit to get information.")
	else:
		#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
		##streamlit.text(fruityvice_response.json())
		## take json version and normalize it 
		#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
		## ouput on the screen as table
		back_from_function = get_fruityvice_data(fruit_choice)
		streamlit.dataframe(back_from_function)

except URLError as e:
	streamlit.error()


streamlit.write('The user entered ', fruit_choice)


#import requests



#streamlit.stop()

#import snowflake.connector


streamlit.header("View Our Fruit List - Add Your Favorites:")
def get_fruits_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("select * from fruit_load_list")
		return my_cur.fetchall()

if streamlit.button('Get Fruit List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruits_load_list()
	my_cnx.close()
	streamlit.dataframe(my_data_rows)
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#my_data_row = my_cur.fetchall()
#my_data_row_dup = my_data_row 
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)
	
def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
		my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+ new_fruit +"')")
		my_cnx.close()
	return "Thanks for adding " + new_fruit


add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button('Add a Fruit to the List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	back_from_function = insert_row_snowflake(add_my_fruit)
	streamlit.text(back_from_function)

streamlit.stop()



streamlit.text("What fruit would you like to add?")

add_my_fruit = streamlit.text_input('jackfruit')
my_data_row_dup = my_data_row.append(add_my_fruit)
streamlit.write('The user entered ', add_my_fruit)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
streamlit.dataframe(my_data_row_dup)

#fruit_added = streamlit.text_input('jackfruit')
#my_data_row_dup = my_data_row.append(fruit_added)
#streamlit.write('The user entered ', fruit_added)
#streamlit.dataframe(my_data_row_dup)
#fruits_added = streamlit.multiselect("Pick some fruits:", list(my_data_row.index), ['jackfruit'])
#fruits_to_show = my_fruit_list.loc[fruits_added]
#streamlit.dataframe(fruits_to_show)
#my_cur.execute("insert into fruit_load_list values ('" + add_my_fruit + "')")
