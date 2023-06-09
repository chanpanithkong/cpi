from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.status import tbstatus
from config.db import db

class StatusSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbstatus
        sqla_session = db.session
        load_instance = True

    statusid = auto_field()
    statusen = auto_field()
    statuskh = auto_field()
    details = auto_field()
    icon = auto_field()
    

