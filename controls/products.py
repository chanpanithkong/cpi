from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.products import tbproducts
from schema.productsschema import ProductsSchema

jwt = JWTManager(app)

class Product(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,pid=None):
        try:  
            data = tbproducts.find_by_prodid(pid)
            schema = ProductsSchema(many=False)
            _data = schema.dump(data)
            return {"product":_data}
        except Exception as err:
            return {"msg":err} 


class ProductsList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbproducts.query.all()
            schema = ProductsSchema(many=True)
            _data = schema.dump(data)
            return {"products":_data}
        except Exception as err:
            return {"msg":err} 
