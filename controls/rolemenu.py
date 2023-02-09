from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.rolemenus import tbrolemenu
from schema.rolemenuschema import RoleMenuSchema

jwt = JWTManager(app)

class RoleMenu(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,roleid=None):
        try:  
            data = tbrolemenu.find_by_roleid(roleid)
            schema = RoleMenuSchema(many=False)
            _data = schema.dump(data)
            return {"rolemenu":_data}
        except Exception as err:
            return {"msg":err} 


class RoleMenuList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbrolemenu.query.all()
            schema = RoleMenuSchema(many=True)
            _data = schema.dump(data)
            return {"rolemenus":_data}
        except Exception as err:
            return {"msg":err} 
