import random
from flask import Flask
app = Flask(__name__)

answer = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/ZssqBe3IYrssyrtMtT" width="480" height="266" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/nfl-sports-football-sport-ZssqBe3IYrssyrtMtT">via GIPHY</a></p>'


@app.route('/<int:number>')
def guess(number):
    if number > answer:
        return f"<h2 style='color: red'>{number} is too high</h2>"
    elif number < answer:
        return f"<h2 style='color: blue'>{number} is too low</h2>"
    else:
        return f"<h2>{number} is just right</h2>"


if __name__ == '__main__':
    app.run(debug=True)
