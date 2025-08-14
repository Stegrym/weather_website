from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # main page
@app.route('/main')  # main page
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # False - когда выложу на сервер
