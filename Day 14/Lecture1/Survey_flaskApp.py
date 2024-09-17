from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def show_home():
    return render_template('home1.html')


@app.route('/survey1')
def show_survey_page():
    return render_template('survey1.html')


@app.route('/survey1', methods=['POST'])
def handle_input():
    name = request.form['name']
    age = request.form['age']
    color = request.form['color']

    return redirect(url_for('show_result', name=name, age=age, color=color))


@app.route('/result1')
def show_result():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    color = request.args.get('color')
    return render_template("result1.html", name=name, age=age, color=color)


if __name__ == '__main__':
    app.run()




