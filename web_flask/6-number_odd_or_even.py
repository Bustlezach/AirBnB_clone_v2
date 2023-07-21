#!/usr/bin/python3
"""
This a script that starts a Flask web application.
It renders the HTML page only if n is an integer:
H1 tag: “Number: n is even|odd”
"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays n is a number."""
    return render_template("5-number.html", n=n)
    

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays n is a number."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
