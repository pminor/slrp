from api import db
from api.model import User

from pprint import pprint as pp

class DaoUser:
    @classmethod
    def jsonify(cls,o):
       return {'id':o.id,'name':o.name,'age':o.age}

    @classmethod
    def create(cls,name,age):
        errors = []

        try:
            user = User(name=name,age=age)
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append('Failed to create the user')

        return {'success': not errors, 'errors':errors}


    @classmethod
    def read(cls):
        errors = []
        users = []

        try:
            users = User.query.all()
        except:            
            errors.append('Failed to fetch the users')

        return {'success': not errors, 'errors':errors,'data':users}

    @classmethod
    def find(cls,id):
        errors = []
        user = None

        try:
            user = User.query.get(id)
            if not user:
                raise Exception(f'The user with id {id} does not exist.') 
        except Exception as e:
            errors.append('Failed to find the user')
            errors.append(str(e))

        return {'success': not errors, 'errors':errors,'data':user} #  UserResponse(not errors, errors, user) #


    @classmethod
    def update(cls,id,req):
        errors = []

        try:
            data = req.json
            if not data:
                raise Exception(f'The user update data was not provided.')

            user = User.query.get(id)
            if not user:
                raise Exception(f'The user with id {id} does not exist.') 
            
            user.name = data.get('name', user.name)
            user.age = data.get('age', user.age)

            # User.query.filter_by(id=id).update(user) # failed to update
            # db.session.add(user) # alternative
            user.verified = True
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            errors.append('Failed to update the user')
            errors.append(str(e))

        return {'success': not errors, 'errors':errors}


    @classmethod
    def delete(cls,id):
        errors = []

        try:
            User.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append('Failed to delete the user')

        return {'success': not errors, 'errors':errors}

