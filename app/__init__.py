from flask import Flask
from config import configs
from app.extensions import db, login_manager

def create_app():
    
    # inti app with its configurations
    app = Flask(__name__)
    app.config.from_object(configs["development"])
    # add extensions here 
    db.init_app(app)
    login_manager.init_app(app)
    # add blueprints here
    from app.main import main
    app.register_blueprint(main)
    from app.auth import auth
    app.register_blueprint(auth)
    
    
    # return the app instance
    return app