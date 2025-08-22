from flask import render_template, request
from flask.views import MethodView
from logic.weather import get_weather


class IndexView(MethodView):
	def get(self):
		return render_template("index.html", weather=None)

	def post(self):
		city = request.form.get('city')
		weather_data = get_weather(city)
		return render_template("index.html", weather=weather_data)
