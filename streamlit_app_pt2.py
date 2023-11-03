#second streamlit app
import streamlit
import pandas as pd
import snowflake.connector
#import requests as rq
#from urllib.error import URLError

streamlit.title("Zenas Amazing Athleisure Catalog")

#connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor

my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()

streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

