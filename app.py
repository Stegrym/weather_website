from flask import Flask, render_template, request
from weather_logic import get_weather
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    # Это можно не прописывать
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static")


# app.config["SQLALCHEMY DATABASE_URI"] = 'sqlite:///city_data_base.db'  # sqlite можно поменять на POSTGRES

# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

@app.route('/', methods=['GET', 'POST'])  # http://localhost:5000/
# @app.route('/main')
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get('city')
        weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data)


# app.config['DEBUG'] = True
if __name__ == "__main__":
    app.run(debug=True)
