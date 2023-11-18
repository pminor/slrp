from flask import Blueprint 

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    return {'code':404,'message':'route not found'}