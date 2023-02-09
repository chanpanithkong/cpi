from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.users import tbusers
from schema.usersschema import UserSchema

jwt = JWTManager(app)

class User(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,userid=None):
        try:  
            data = tbusers.find_by_userid(userid)
            schema = UserSchema(many=False)
            _data = schema.dump(data)
            return {"user":_data}
        except Exception as err:
            return {"msg":err} 


class UsersList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbusers.query.all()
            schema = UserSchema(many=True)
            _data = schema.dump(data)
            return {"users":_data}
        except Exception as err:
            return {"msg":err} 
