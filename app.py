from flask import Flask, render_template, request
from routes import IndexView
from logic.weather import get_weather
from models import db
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

	# маршруты

	app.add_url_rule('/', view_func=IndexView.as_view('index'))

	return app


if __name__ == "__main__":
	app = create_app('develop')  # Используем конфигурацию для разработки
	app.run(debug=app.config['DEBUG'])
