#!/usr/bin/python3
""" Module called 2-c_route """
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


@app.route("/c/<text>", strict_slashes=False)
def show_text_replace(text):
    """ This function show the string started in “C ”
        followed by the value of the text variable """
    text_replace = text.replace('_', ' ')
    return "C {}".format(text_replace)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
