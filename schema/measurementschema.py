from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.measurement import tbmeasurement
from config.db import db

class MeasurementSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbmeasurement
        sqla_session = db.session
        load_instance = True

    mid = auto_field()
    unit = auto_field()
    measurement = auto_field()
    details = auto_field()
    

