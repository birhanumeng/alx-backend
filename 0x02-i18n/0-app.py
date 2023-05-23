#!/usr/bin/env python3
""" Basic Flask app configuration. """

from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='')
from os import getenv


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
        Return: 0-index.html
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
