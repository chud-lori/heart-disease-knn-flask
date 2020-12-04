"""
initiation file for the app
this file invoked from setup.py outstide
this represent the corpe/ directory
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from flask_login import LoginManager
from corpe.config import Config
# Import routes
from corpe.predict.routes import predict_bp
from corpe.admin.routes import admin_bp
from corpe.main_routes import main_bp


# Initiate object
db = SQLAlchemy()
# migrate = Migrate()
bcrypt = Bcrypt()
# Set up login to auth admin
login_manager = LoginManager()
# Set view for login and message if error auth
login_manager.login_view = 'admin.login'
login_manager.login_message = 'RA GACO BRUH!!'
login_manager.login_message_category = 'danger'


def create_app(config=Config):
    """
    end point of the app
    """
    # Initiate flask object and its config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    # Initiate db to app
    db.init_app(app)
    # migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # run route from the app context
    with app.app_context():
        app.register_blueprint(predict_bp)
        app.register_blueprint(admin_bp)
        app.register_blueprint(main_bp)
        return app
