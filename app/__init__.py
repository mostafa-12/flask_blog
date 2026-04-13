from config import configs
from app.extensions import db, login_manager
from flask import Flask

def create_app():
    
    # inti app with its configurations
    app = Flask(__name__)
    app.config.from_object(configs["development"])
    # add extensions here 
    db.init_app(app)
    login_manager.init_app(app)
    
    # login manager with models configs 
    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    # init db with app context
    with app.app_context():
        db.create_all()
    
    # add blueprints here
    from app.main import main
    app.register_blueprint(main)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.services import services
    app.register_blueprint(services)
    
    # return the app instance
    return app