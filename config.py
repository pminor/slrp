import os 

class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://hisuser:hispwd@localhost/hisdb'
    SECRET_KEY='secret_key_required_by_flask_admin'

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://hisuser2:hispwd2@localhost:3307/hisdb2'
    
class Production(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

config_options = {
    'development': DevConfig,
    'production': Production
}