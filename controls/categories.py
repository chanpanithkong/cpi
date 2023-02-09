from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.categories import tbcategories
from schema.categoriesschema import CategoriesSchema

jwt = JWTManager(app)

class Category(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,catid=None):
        try:  
            data = tbcategories.find_by_catid(catid)
            schema = CategoriesSchema(many=False)
            _data = schema.dump(data)
            return {"category":_data}
        except Exception as err:
            return {"msg":err} 


class CategoriesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcategories.query.all()
            schema = CategoriesSchema(many=True)
            _data = schema.dump(data)
            return {"categories":_data}
        except Exception as err:
            return {"msg":err} 
