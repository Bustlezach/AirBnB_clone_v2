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


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all State objects."""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<int:id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with a list of all State objects."""
    states = storage.all(State).get("State.{}".format(id))
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
