#!/usr/bin/python3
<<<<<<< HEAD
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
=======
"""Starts Flask web app that displays "Hello HBNB!"
>>>>>>> 052ab6c5e78d1867e6f9815110ae00acbabf44f0
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
