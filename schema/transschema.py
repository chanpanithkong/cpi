from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.trans import tbtrans
from config.db import db

class TransSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbtrans
        sqla_session = db.session
        load_instance = True

    tid = auto_field()
    branchcode = auto_field()
    productid = auto_field()
    weight = auto_field()
    price   = auto_field()
    submitter   = auto_field()
    submitdate = auto_field()
    submitternote   = auto_field()
    authorizer  = auto_field()
    authorizedate = auto_field()
    authorizernote = auto_field()
    status  = auto_field()
    valuedate = auto_field()
    trandate = auto_field()
    countsubmitted  = auto_field()

