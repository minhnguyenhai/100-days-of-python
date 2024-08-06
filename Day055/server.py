import random
from flask import Flask

app = Flask(__name__)

correct_number = random.randint(0, 9)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="HOME PAGE">'


@app.route('/<int:guessing_number>'):
def check_number(guessing_number):
    if guessing_number < correct_number:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="TOO LOW">'
    elif guessing_number > correct_number:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="TOO HIGH">'
    else:
        return '<h1 style="color: red;">You found!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="CORRECT">'

if __name__ =='__main__':
    app.run(debug=True)
