from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.branches import tbbranches
from schema.branchesschema import BranchesSchema

jwt = JWTManager(app)

class Branch(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,branchcode=None):
        try:  
            data = tbbranches.find_by_branchcode(branchcode)
            schema = BranchesSchema(many=False)
            _data = schema.dump(data)
            return {"branch":_data}
        except Exception as err:
            return {"msg":err} 


class BranchesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbbranches.query.all()
            schema = BranchesSchema(many=True)
            _data = schema.dump(data)
            return {"branches":_data}
        except Exception as err:
            return {"msg":err} 

class IndexPage(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        return "<h1>hello world</h1>" 
