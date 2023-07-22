#!/usr/bin/python3
"""
This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Displays an HTML page with a list of all State objects."""
    States = storage.all(State)
    return render_template("8-cities_by_states.html", States=States)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
