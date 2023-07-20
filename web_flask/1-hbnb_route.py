#!/usr/bin/python3
"""
This a script that starts a Flask web application.
It displays 'HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays greetings."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB."""
    return "HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

