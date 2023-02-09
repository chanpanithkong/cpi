from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.measurement import tbmeasurement
from schema.measurementschema import MeasurementSchema

jwt = JWTManager(app)

class Measurement(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,mid=None):
        try:  
            data = tbmeasurement.find_by_mid(mid)
            schema = MeasurementSchema(many=False)
            _data = schema.dump(data)
            return {"measurement":_data}
        except Exception as err:
            return {"msg":err} 


class MeasurementList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbmeasurement.query.all()
            schema = MeasurementSchema(many=True)
            _data = schema.dump(data)
            return {"measurements":_data}
        except Exception as err:
            return {"msg":err} 
