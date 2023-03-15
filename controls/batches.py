from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import app, request, json
from models.batches import tbbatches
from schema.batchesschema import BatchSchema

jwt = JWTManager(app)

class Batch(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,batchid=None):
        try:  
            data = tbbatches.find_by_batchid(batchid)
            schema = BatchSchema(many=False)
            _data = schema.dump(data)
            return {"batch":_data}
        except Exception as err:
            return {"msg":err} 


class BatchesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbbatches.query.all()
            schema = BatchSchema(many=True)
            _data = schema.dump(data)
            return {"batches":_data}
        except Exception as err:
            return {"msg":err} 
