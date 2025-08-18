from flask import Flask, render_template, request, make_response, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from logic import * #папка для функций


app = Flask(
    __name__,
    # Это можно не прописывать
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static")

app.config["SQLALCHEMY DATABASE_URI"] = 'sqlite:///city_data_base.db'  # sqlite можно поменять на POSTGRES

@app.route('/')  # http://localhost:5000/
@app.route('/main')
def index():
    return render_template("index.html")


# Это тёмная магия!!!
@app.route("/give_number", methods=["GET"])
def get_random_number():
    if request.method != 'GET':
        return make_response("request=", 400)
    headers = {"Content-Type": "aplication/json"}
    return make_response('It_WORKED!', 200, headers)


if __name__ == "__main__":
    app.run(debug=True)  # False - когда выложу на сервер
