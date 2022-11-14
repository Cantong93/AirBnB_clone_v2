#!/usr/bin/python3
<<<<<<< HEAD
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask

=======
"""Starts Flask web app"""


from flask import Flask


>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hbnb_route():
    """prints Hello HBNB"""
=======
def hello_route():
    """Displays Hello HBNB!"""
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """prints HBNB"""
=======
    """Displays HBNB"""
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
<<<<<<< HEAD
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
=======
def c_message(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', '')
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
<<<<<<< HEAD
=======

>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
