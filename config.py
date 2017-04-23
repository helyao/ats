class Config(object):

    SECRET_KEY = 'yxD2z9Na'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True    # commit when @app.teardown
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # no signal when track object changed

    @staticmethod
    def init_app(app):
        pass

# Configuration for test - by Flask embeded Http-Server
class DebuggingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:welcome@localhost/ats'

# Configuration for development - on Ubuntu by Nginx + Gunicorn
class DevelopmentConfig(Config):
    pass

# Configuration for production - on Production Ubuntu Server by Nginx + Gunicorn
class ProductionConfig(Config):
    pass

config = {
    'debugging': DebuggingConfig,       # Native PC during Developing
    'development': DevelopmentConfig,   # Linux PC
    'product': ProductionConfig         # Production Server
}

RUN_LEVEL = 'debugging'