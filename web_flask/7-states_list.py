#!/usr/bin/python3
""" Module called 7-states_list"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def all_states():
    """ This function use storage for fetching data from
        the storage engine: FileStorage or DBStorage """
    is_states = storage.all(State).values()
    return render_template('7-states_list.html', states=is_states)


@app.teardown_appcontext
def reset_session(exception):
    """ This function use the handler teardown_appcontext to
        close or otherwise deallocates the resource if it exists """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
