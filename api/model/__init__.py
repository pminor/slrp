from .user import User 
from .product import Product

from api import admin, db 
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))