from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from flask_cors import cross_origin
from config.db import app, request, json, jsonify
from models.users import tbusers
from schema.usersschema import UserSchema
from pprint import pprint
jwt = JWTManager(app)


class UserLogin(Resource):
    @classmethod
    # @jwt_required()
    @cross_origin()
    def post(cls):

        try:
            print(1)
            data = json.loads(request.data)
            print(data)
            userid = data['data']['userid']
            password = data['data']['password']
            user_data = tbusers.find_by_userid(userid)
            schema = UserSchema(many=False)
            _data = schema.dump(user_data)
            if user_data is not None:
                if _data['password'] == password:
                    return jsonify({"login": _data})
            return {"login": False}

        except Exception as err:
            return {"msg": err}


class User(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, userid=None):
        try:
            data = tbusers.find_by_userid(userid)
            schema = UserSchema(many=False)
            _data = schema.dump(data)
            return {"user": _data}
        except Exception as err:
            return {"msg": err}


class UsersList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbusers.query.all()
            schema = UserSchema(many=True)
            _data = schema.dump(data)
            return {"users": _data}
        except Exception as err:
            return {"msg": err}
