from wsgiref.util import request_uri

from flask import Flask, render_template, request, make_response, jsonify, url_for

# from logic import * #папка для функций

app = Flask(
    __name__,
    # Это можно не прописывать
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static")


@app.route('/')  # main page
@app.route('/main')  # main page
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
