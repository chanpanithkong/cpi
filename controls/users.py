from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from flask_cors import cross_origin
from flask import session
from config.db import app, request, json, jsonify, db
from models.users import tbusers
from schema.usersschema import UserSchema
from pprint import pprint
jwt = JWTManager(app)


class ChangePasswordForUser(Resource):
    @classmethod
    # @jwt_required()
    @cross_origin()
    def post(cls):

        try:
            
            data = json.loads(request.data)
            
            if data['userrequest'] == 'change' :

                oldpassword = data['data']['oldpassword']
                confirmoldpassword = data['data']['confirmoldpassword']
                newpassword = data['data']['newpassword']

                if oldpassword == confirmoldpassword:

                    userid = session.get("userid")
                    user_data = tbusers.find_by_userid(userid)
                    if user_data.password == oldpassword:
                        user_data.password = newpassword
                    else:
                        return {"msg":"Cannot change password"}
                    
                    db.session.commit()
                    return {"msg":"Password changed"}
            
            return {"msg": "Cannot change password"}

        except Exception as err:
            return {"msg": err}

class UserLogin(Resource):
    @classmethod
    # @jwt_required()
    @cross_origin()
    def post(cls):

        try:
            
            data = json.loads(request.data)
            
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
