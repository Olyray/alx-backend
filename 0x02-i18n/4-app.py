#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """Chooses the appropriate language"""
    locale_argument = request.args.get('locale')
    if locale_argument and locale_argument in app.config['LANGUAGES']:
        return locale_argument
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index():
    """Renders the index template"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
