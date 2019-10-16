"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('settings.development.DevelopmentConfig')
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from api import routes
        from core.handlers.db_handler import init_logger

        # Create routes
        app.register_blueprint(routes.blueprint)

        # Create tables for our models
        db.create_all()

        # Initializing logger
        init_logger()

        return app
