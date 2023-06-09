from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.users import tbusers
from config.db import db

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbusers
        sqla_session = db.session
        load_instance = True

    userid = auto_field()
    password = auto_field()
    key = auto_field()
    roleid = auto_field()
    username = auto_field()
    gender = auto_field()
    branchcode = auto_field()
    details = auto_field()
    position = auto_field()
    email = auto_field()
    status = auto_field()
    languages = auto_field()

