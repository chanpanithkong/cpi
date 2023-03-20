from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json
from models.categories import tbcategories
from schema.categoriesschema import CategoriesSchema
from pprint import pprint
jwt = JWTManager(app)


class Category(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, catid=None):
        try:
            data = tbcategories.find_by_catid(catid)
            schema = CategoriesSchema(many=False)
            _data = schema.dump(data)
            return {"category": _data}
        except Exception as err:
            return {"msg": err}

class CategoriesChildFromParent(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            
            data = json.loads(request.data)
            if tbcategories.find_by_countparentid(data['data']['parentid']) > 0:
                data = tbcategories.find_by_parentid(data['data']['parentid'])
                schema = CategoriesSchema(many=True)
                _data = schema.dump(data)
                return {"categoris": _data}
            return {"No records"}
        except Exception as err:
            return {"msg": err}

class CategoriesParent(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcategories.query.all()
            parent = []
            for dt in data:
                if dt.parentid is None:
                    parent.append(dt)
            print(parent)
            schema = CategoriesSchema(many=True)
            _data = schema.dump(parent)
            return {"categories": _data}
        except Exception as err:
            return {"msg": err}


class CategoriesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcategories.query.all()
            schema = CategoriesSchema(many=True)
            _data = schema.dump(data)
            return {"categories": _data}
        except Exception as err:
            return {"msg": err}
