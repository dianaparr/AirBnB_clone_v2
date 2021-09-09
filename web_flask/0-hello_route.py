#!/usr/bin/python3
""" Module called 0-hello_route """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_you():
    """ This function greets you when you
        are on the first page, root path """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
