#!/usr/bin/python3
""" Module called 1-hbnb_route """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_you():
    """ This function greets you when you
        are on the first page, root path """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show_string():
    """ This function show the string when stay
        into the path /hbnb """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
