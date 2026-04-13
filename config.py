
class BaseConfig:
    """Base configuration."""
    
    SECRET_KEY = "very secret key"
    
    @staticmethod
    def init_app(app):
        pass
    
    
class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///DEV_db.sqlite3"

configs = {
    "base": BaseConfig,
    "development": DevelopmentConfig
}