#!/usr/bin/python3
"""
This a script that starts a Flask web application.
It displays n is a number ONLY if n is an integer.
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


@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """Displays C."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text):
    """Displays python."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays n is a number."""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True)
