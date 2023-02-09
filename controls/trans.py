from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.trans import tbtrans
from schema.transschema import TransSchema

jwt = JWTManager(app)

class Tran(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,tid=None):
        try:  
            data = tbtrans.find_by_tid(tid)
            schema = TransSchema(many=False)
            _data = schema.dump(data)
            return {"tran":_data}
        except Exception as err:
            return {"msg":err} 


class TransList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbtrans.query.all()
            schema = TransSchema(many=True)
            _data = schema.dump(data)
            return {"trans":_data}
        except Exception as err:
            return {"msg":err} 
