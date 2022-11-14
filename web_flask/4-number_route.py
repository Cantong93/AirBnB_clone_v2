#!/usr/bin/python3
<<<<<<< HEAD
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
    /python/<text> - display "Python is cool"
    /number/<n> - display n if integer
"""
from flask import Flask

=======
"""Return string when navigating to root dir"""
from flask import Flask


>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hbnb_route():
    """prints Hello HBNB"""
=======
def hello_holberton():
    """Return Hello HBNB"""
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
<<<<<<< HEAD
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display n if integer"""
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
def hello_hnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Route /c/<text> returns C message"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisbest(text="is cool"):
    """Route /python/(<text>) returns Python message"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def isint(n):
    """Route /number/<n> returns int status message"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
