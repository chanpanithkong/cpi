from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.menus import tbmenus
from schema.menusschema import MenusSchema

jwt = JWTManager(app)

class Menu(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,mid=None):
        try:  
            data = tbmenus.find_by_menuid(mid)
            schema = MenusSchema(many=False)
            _data = schema.dump(data)
            return {"menu":_data}
        except Exception as err:
            return {"msg":err} 


class MenusList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbmenus.query.all()
            schema = MenusSchema(many=True)
            _data = schema.dump(data)
            return {"menus":_data}
        except Exception as err:
            return {"msg":err} 
