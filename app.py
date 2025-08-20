from flask import Flask, render_template, request
from weather_logic import get_weather
from models import db, City
from config import config


def create_app(config_name="develop"):
    """Создание фабрики приложения"""

    app = Flask(
        __name__,
        # Это можно не прописывать
        instance_relative_config=False,
        template_folder="templates",
        static_folder="static")

    # Настройка конфига
    app.config.from_object(config[config_name])

    # Инициализируем базу
    db.init_app(app)
    # Создание колонок
    with app.app_context():
        db.create_all()

    @app.route('/', methods=['GET', 'POST'])  # http://localhost:5000/
    # @app.route('/main')
    def index():
        weather_data = None
        if request.method == "POST":
            city = request.form.get('city')
            weather_data = get_weather(city)
        return render_template("index.html", weather=weather_data)

    return app


if __name__ == "__main__":
    app = create_app('develop')  # Используем конфигурацию для разработки
    app.run(debug=app.config['DEBUG'])
