#!/usr/bin/env python3
""" Basic Flask app configuration """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuring babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/')
def index():
    """ Route to 1-index.html """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
