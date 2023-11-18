from api import db
from api.model import Product

from pprint import pprint as pp

class DaoProduct:
    @classmethod
    def jsonify(cls,o):
       return {'id':o.id,'name':o.name}

    @classmethod
    def create(cls,name):
        errors = []

        try:
            product = Product(name=name)
            db.session.add(product)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append('Failed to create the product')

        return {'success': not errors, 'errors':errors}


    @classmethod
    def read(cls):
        errors = []
        products = []

        try:
            products = Product.query.all()            
        except:            
            errors.append('Failed to fetch the products')

        status = { 'success': not errors, 'errors':errors }

        return {'status': status, 'data':products}

    
    @classmethod
    def find(cls,id):
        errors = []
        product = None

        try:
            product = Product.query.get(id)
            if not product:
                raise Exception(f'The product with id {id} does not exist.') 
        except Exception as e:
            errors.append('Failed to find the product')
            errors.append(str(e))

        status = { 'success': not errors, 'errors':errors }

        return {'status': status, 'data':product}


    @classmethod
    def update(cls,id,req):
        errors = []

        try:
            data = req.json              
            if not data:
                raise Exception(f'The product update data was not provided.')

            product = Product.query.get(id)
            if not product:
                raise Exception(f'The product with id {id} does not exist.')

            product.name = data.get('name', product.name )

            product.verified = True 
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            errors.append('Failed to update the product')
            errors.append(str(e))

        return {'success': not errors, 'errors':errors}


    @classmethod
    def delete(cls,id):
        errors = []

        try:
            Product.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append('Failed to delete the product')

        return {'success': not errors, 'errors':errors}


