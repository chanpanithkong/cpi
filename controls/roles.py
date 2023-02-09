from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.roles import tbroles
from schema.rolesschema import RoleSchema

jwt = JWTManager(app)

class Role(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,roleid=None):
        try:  
            data = tbroles.find_by_roleid(roleid)
            schema = RoleSchema(many=False)
            _data = schema.dump(data)
            return {"role":_data}
        except Exception as err:
            return {"msg":err} 


class RoleList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbroles.query.all()
            schema = RoleSchema(many=True)
            _data = schema.dump(data)
            return {"roles":_data}
        except Exception as err:
            return {"msg":err} 
