from flask import Blueprint, request as req
from flask_restful import Api , Resource, fields, marshal_with

from api.dao import DaoProduct


product = Blueprint('product',__name__, url_prefix='/products')
api = Api(product)

json_product = {
    'id': fields.Integer,
    'name': fields.String
}

json_status = {
    'success': fields.Boolean,
    'errors': fields.List(fields.String)
}

json = {
    'status': fields.Nested(json_status),
    'product': fields.Nested(json_product, attribute='data')
}

json_list = {
    'status': fields.Nested(json_status),
    'data': fields.List(fields.Nested(json_product))
}

class Product(Resource):
    @marshal_with(json, envelope='response')
    def get(self,id):
        res = DaoProduct.find(id)
        return res

    #@marshal_with(res)
    def put(self,id):
        res = DaoProduct.update(id,req)
        return {'res': res} 

    #@marshal_with(res)
    def delete(self,id):
        res = DaoProduct.delete(id)
        return {'res': res} 

class ProductList(Resource):
    @marshal_with(json_list, envelope='response')
    def get(self):
        res = DaoProduct.read()
        return res 

    #@marshal_with(res)
    def post(self):
        name = req.json['name']
        res = DaoProduct.create(name)
        return {'res': res} 

api.add_resource(Product,'/<int:id>')
api.add_resource(ProductList,'','/') # trailing '/' or no traling '/'


















































# @product.route('/<string:name>/add') # POST
# def create(name):
#     res = DaoProduct.create(name)
#     return {'res': res}

# @product.route('/')
# def read():
#     res = DaoProduct.read()
#     return {'res': res}

# @product.route('/<int:id>')
# def find(id):
#     res = DaoProduct.find(id)
#     return {'res': res}

# @product.route('/<int:id>/edit/<string:name>') # PUT
# def update(id,name):
#     res = DaoProduct.update(id,name)
#     return {'res': res}

# @product.route('/<int:id>/delete')
# def delte(id):
#     res = DaoProduct.delete(id)
#     return {'res': res}