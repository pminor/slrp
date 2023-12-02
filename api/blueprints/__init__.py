from flask import Blueprint 

from .user import user
from .product import product
from .errors import errors

root = Blueprint('root', __name__, url_prefix='/api')

root.register_blueprint(user)
root.register_blueprint(product)
root.register_blueprint(errors)

@root.route('/mpesa')
def mpesa():
  return {'status':'ok'}
