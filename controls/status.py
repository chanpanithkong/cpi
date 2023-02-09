from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.status import tbstatus
from schema.statusschema import StatusSchema

jwt = JWTManager(app)

class Status(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,statusid=None):
        try:  
            data = tbstatus.find_by_statusid(statusid)
            schema = StatusSchema(many=False)
            _data = schema.dump(data)
            return {"status":_data}
        except Exception as err:
            return {"msg":err} 


class StatusList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbstatus.query.all()
            schema = StatusSchema(many=True)
            _data = schema.dump(data)
            return {"status":_data}
        except Exception as err:
            return {"msg":err} 
