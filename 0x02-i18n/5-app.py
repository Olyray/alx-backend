#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets a user from the users dict"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    current_user = get_user()
    if current_user:
        g.user = current_user


app.config.from_object(Config)


@app.route('/')
def index():
    """Renders the index template"""
    user = getattr(g, 'user', None)
    return render_template('5-index.html', user=user)


if __name__ == "__main__":
    app.run()
