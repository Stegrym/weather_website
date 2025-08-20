import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit(".env не найден")
else:
    load_dotenv()


class Config:
    # SQlite
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///city_data_base.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower()

    # weather_key
    OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")


class Develop(Config):
    DEBUG = True


class Product(Config):
    DEBUG = False


config = {"develop": Develop, "product": Product}
