from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.branches import tbbranches
from config.db import db

class BranchesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbbranches
        sqla_session = db.session
        load_instance = True

    branchcode = auto_field()
    nameen = auto_field()
    namekh = auto_field()
    address = auto_field()
    details = auto_field()
    

