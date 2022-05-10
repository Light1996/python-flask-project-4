"""A simple flask web app"""
import os
from flask import Flask, render_template
from app.cli import create_database
from app.db import db
from app.db.models import User
import logging


def configure_logging():
    # register root logging
    logging.basicConfig(filename='noor.log', level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)


def create_app():

    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    configure_logging()
    app.logger.info('Application is running')
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    db_dir = "database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from app.authentications.authentications_blueprint import authentications_blueprints
    app.register_blueprint(authentications_blueprints)

    from app.dashboard.dashboard_blueprint import dashboard
    app.register_blueprint(dashboard)

    # add command function to cli commands
    app.cli.add_command(create_database)
    app.app_context().push()
    db.create_all()

    return app
