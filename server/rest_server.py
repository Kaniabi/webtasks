import os


# Flask configurations
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class DevelopmentConfig(BaseConfig):
    """
    Development configuration.

    Use a local sqlite database.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestingConfig(BaseConfig):
    """
    Testing configuration.

    Uses an in-memory database for fast access.
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """
    Production configuration.

    Uses a real database.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/webtasks'



def create_application(config):
    '''
    Creates the flask application and database.

    Using a function to avoid using global variables.

    :param BaseConfig config:
        One configuration object.

    :return tuple(Flask, SqlAlchemy):
        Returns the flask application and sql-alchemy database.
    '''
    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy
    from flask.ext.cors import CORS
    import flask.ext.restless

    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config)

    db = SQLAlchemy(app)

    # Define the Task model. The actual database is defined by the application configuration object
    # (SQLALCHEMY_DATABASE_URI).
    class Task(db.Model):

        __tablename__ = "tasks"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        task = db.Column(db.String(255), unique=True, nullable=False)
        done = db.Column(db.Boolean, nullable=False, default=False)

        def __init__(self, task, done=False, id=None):
            self.id = id
            self.task = task
            self.done = done

    # RESTless automatically creates the REST API based in a Model. Changes the defaults valus to match the required
    # API.
    restless_manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
    restless_manager.create_api(
        Task,
        methods=('GET', 'POST', 'DELETE', 'PATCH'),
        url_prefix='',
        collection_name='task',
        allow_delete_many=True
    )

    return app, db


if __name__ == '__main__':
    app, db = create_application(DevelopmentConfig)
    app.run()
