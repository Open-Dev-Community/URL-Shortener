from flask import Flask

from .extensions import db
from .routes import short_blp


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_pyfile(config_file)
    app.config['SESSION_COOKIE_SECURE'] = False
    # Initializing db
    db.init_app(app)
    # Import blueprint
    app.register_blueprint(short_blp)
    return app
