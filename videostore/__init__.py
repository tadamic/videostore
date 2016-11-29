from flask import Flask
from .settings import environments
from .db import db
from flask.ext.sqlalchemy import SQLAlchemy


def create_app(config_environment):
    app = Flask('videostore')

    config_object = environments[config_environment]()
    app.config.from_object(config_object)

    db.init_app(app)

    return app
