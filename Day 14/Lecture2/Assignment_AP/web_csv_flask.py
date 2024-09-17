from flask import Flask, redirect, render_template, url_for, request, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def handle_home():
    session['path'] = request.form['path']
    return redirect(url_for('summary'))


@app.route('/summary')
def summary():
    path = session.get('path')
    # path = "students.csv"
    print("CSV READ")
    print("Path: ", path)
    df = pd.read_csv(path)
    data = df.values
    print(data)
    return render_template('summary.html', path=path, data=data)


if __name__ == '__main__':
    app.run(port=5002)




