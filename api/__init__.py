import os 

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin 
from datetime import datetime

from config import config_options

db = SQLAlchemy()
admin = Admin()

def create_app(config_name=os.environ.get('CONFIG_NAME')):
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://salesdb:salespwd@localhost:5432/salesdb'
    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://salesdb:salespwd@localhost:5432/salesdb'
    # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://hisuser:hispwd@localhost/hisdb'
    app.config.from_object( config_options[config_name] )

    db.init_app(app)
    admin.init_app(app)

    # avoid cycle when user bp imports user dao which imports user model which imports db which is in this same file
    # imported below the db creation
    from .blueprints import root # user, product, errors
    app.register_blueprint(root)
    # app.register_blueprint(user)
    # app.register_blueprint(product)
    # app.register_blueprint(errors)

    return app





