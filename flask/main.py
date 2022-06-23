from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0,9)
# random_num = 6

def decoratorr(function):
    def warp():
        return "<b>"+function()+"</b>"
    return warp

@app.route("/")
@decoratorr
def helloworld():
    return f"<h1> Guess a number between 0 to 9 </h1>" \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
def find_num(number):
    if number > random_num:
        return "<h1>Too High</h1>"\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < random_num:
        return '<h1>Too low </h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return "<h1>You got it</h1>"\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

# @app.route(f'/{random_num}')
# def crt_number(random)

@app.route('/bye')
def bye():
    return "byeeee"

if __name__ == "__main__":
    app.run(debug=True)