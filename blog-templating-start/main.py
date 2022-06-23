from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/post/<number>')
def get_blogs(number):
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    post = response.json()
    num = int(number)
    return render_template("post.html", post=post, num = num)


if __name__ == "__main__":
    app.run(debug=True)
