from flask import Flask
app = Flask(__name__)


@app.route("/")  # This route will handle request to the root URL
def homePage(debug=True):
    return "Welcome to the HomePage!"


if __name__ == "__main__":
    app.run()


