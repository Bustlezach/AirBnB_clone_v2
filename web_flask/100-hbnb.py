#!/usr/bin/python3

"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays an HTML page with a list of all State objects."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnbs.html", states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_appcontext(exc):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
