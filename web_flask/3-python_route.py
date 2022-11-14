#!/usr/bin/python3
"""Starts Flask web app"""


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
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/text>', strict_slashes=False)
def display_python(text="is cool"):
    """displays Python is cool"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
