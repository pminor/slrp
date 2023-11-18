from flask import Blueprint, request as req
from flask_restful import Api , Resource, fields, marshal_with
from pprint import pprint as pp

from api.dao import DaoUser


user = Blueprint('user',__name__, url_prefix='/users')
api = Api(user)

json_user = {
     'id': fields.Integer,
     'name': fields.String,
     'age': fields.Integer
}

# json_nest_props_option = {
#     'success': fields.Boolean,
#     'errors': fields.List(fields.String),
#     'data':{
#         'id': fields.Integer(attribute='data.id'),
#         'name': fields.String(attribute='data.name'),
#         'age': fields.Integer(attribute='data.age')
#     }
# }

json = {
    'success': fields.Boolean,
    'errors': fields.List(fields.String),
    'user': fields.Nested(json_user,attribute='data') # if keys differ, specify the attribute name
}

json_list = { 
    'success': fields.Boolean,
    'errors': fields.List(fields.String),
    'data': fields.List(fields.Nested(json_user)) 
}

class User(Resource):
    @marshal_with(json, envelope='response')
    def get(self,id):
        res = DaoUser.find(id)
        return res #{'response': res} 

    #@marshal_with(res)
    def put(self,id):      
        res = DaoUser.update(id,req)
        return {'response': res} 

    #@marshal_with(res)
    def delete(self,id):
        res = DaoUser.delete(id)
        return {'response': res} 

class UserList(Resource):
    @marshal_with(json_list, envelope='response')
    def get(self):
        res = DaoUser.read()
        return res #{'response': res} 

    #@marshal_with(res)
    def post(self):
        name = req.json['name']
        res = DaoUser.create(name,35)
        return {'response': res} 

api.add_resource(User,'/<int:id>')
api.add_resource(UserList,'/')














# @user.route('/',methods=['POST']) # POST
# def create():
#     name = req.json['name']
#     res = DaoUser.create(name,35)
#     return {'response': res}

# @user.route('/')
# def read():
#     res = DaoUser.read()
#     return {'response': res}

# @user.route('/<int:id>')
# def find(id):
#     res = DaoUser.find(id)
#     return {'response': res}

# @user.route('/<int:id>/edit/<string:name>') # PUT
# def update(id,name):
#     res = DaoUser.update(id,name)
#     return {'response': res}

# @user.route('/<int:id>/delete')
# def delte(id):
#     res = DaoUser.delete(id)
#     return {'response': res}