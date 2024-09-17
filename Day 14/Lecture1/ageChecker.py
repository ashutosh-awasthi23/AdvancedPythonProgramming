from flask import Flask, render_template, request, redirect, url_for


# Step 1: Initialize Flask app
appLogin = Flask(__name__)
print(appLogin)


@appLogin.route('/')
def home():
    return render_template("home.html")


@appLogin.route('/agecheck')
def showage():
    return render_template("agecheck.html")


@appLogin.route('/agecheck', methods=['POST'])
def handle_age_check():
    age = request.form['age']
    print(age)
    return redirect(url_for('result', age=age))


@appLogin.route('/result')
def result():
    age = int(request.args.get('age'))  # Fetch age from query parameters
    if age >= 18:
        s = "Adult"
    else:
        s = "Minor"
    return render_template("result.html", s=s)


if __name__ == "__main__":
    appLogin.run()
