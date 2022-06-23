from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    return render_template('index.html',year=now.year)

@app.route('/guess/<username>')
def guess(username):
    name = (username).title()
    inpt = {"name": name}

    response = requests.get(url='https://api.agify.io?', params=inpt)
    response2 = requests.get(url="https://api.genderize.io/?", params=inpt)

    age_data = response.json()["age"]
    gender_data = response2.json()['gender']

    return render_template("name_guess.html",name=name,gender_data=gender_data,age_data=age_data)

if __name__ == "__main__":
    app.run(debug=True)