from flask import Flask

app = Flask(__name__)


@app.route('/main_page')
def main_page():
    return "I am WORK!!!"


if __name__ == "__main__":
    app.run(debug=True)
