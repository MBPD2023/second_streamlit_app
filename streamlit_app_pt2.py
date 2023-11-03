#second streamlit app
import streamlit
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

streamlit.title("Zenas Amazing Athleisure Catalog")

