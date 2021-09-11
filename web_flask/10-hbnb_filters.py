#!/usr/bin/python3
""" Module called 10-hbnb_filters """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def all_filters():
    """ This function use storage for fetching data from
        the storage engine: FileStorage or DBStorage.
        Data to filters in the page of the AirBnB clone.
        """
    is_state = storage.all(State).values()
    is_amenity = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=is_state, amenities=is_amenity)


@app.teardown_appcontext
def reset_session(exception):
    """ This function use the handler teardown_appcontext to
        close or otherwise deallocates the resource if it exists """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
