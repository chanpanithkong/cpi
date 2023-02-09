from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.rolemenus import tbrolemenu
from config.db import db

class RoleMenuSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbrolemenu
        sqla_session = db.session
        load_instance = True

    roleid = auto_field()
    menuid = auto_field()
    details = auto_field()
    createby = auto_field()
    createdate = auto_field()
    statusid = auto_field()
    

