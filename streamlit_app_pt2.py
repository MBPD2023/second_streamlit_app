#second streamlit app
import streamlit
import pandas as pd
import snowflake.connector


streamlit.title("Zenas Amazing Athleisure Catalog")

#connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#Turn Data into Dataframe
df = pd.DataFrame(my_catalog

#write df into page to check
streamlit.write(df)
