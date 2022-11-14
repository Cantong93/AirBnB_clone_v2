#!/usr/bin/python3
<<<<<<< HEAD
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""
from flask import Flask

=======
"""Starts Flask web app:
    / - displays "Hello HBNB!"
    /hbnb - displays "HBNB"
"""


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
<<<<<<< HEAD
=======

>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
