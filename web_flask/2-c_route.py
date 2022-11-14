#!/usr/bin/python3
"""Starts Flask web app:
    / - displays "Hello HBNB!"
    /hbnb - displays "HBNB"
    /c/<text> - display “C ” followed by the value of the text variable
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_message(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', '')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

