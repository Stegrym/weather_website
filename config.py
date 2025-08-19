import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit(".env не найден")
else:
    load_dotenv()

API_key= os.getenv("OPENWEATHER_KEY")