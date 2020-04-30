from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from flask_login import LoginManager
from corpe.config import Config

# Initiate object
db = SQLAlchemy()
# migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message = 'RA GACO COK!!'
login_manager.login_message_category = 'danger'

def create_app(config=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)
    # migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        # Admin.__table__.create(db.engine)
        # Initialize Global db
        # ss=db.create_all()
        # if ss:
        #     print("ISO")
        # else:
        #     print("RAISO")
        # from corpe import db, create_app
        # db.drop_all(app=create_app())
        # db.create_all(app=create_app())
        
        from corpe.predict.routes import predict_bp
        from corpe.admin.routes import admin_bp
        from corpe.main_routes import main_bp
        app.register_blueprint(predict_bp)
        app.register_blueprint(admin_bp)
        app.register_blueprint(main_bp)
        return app