from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.menus import tbmenus
from config.db import db

class MenusSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbmenus
        sqla_session = db.session
        load_instance = True

    menuid = auto_field()
    menu = auto_field()
    parentid = auto_field()
    functions = auto_field()
    details = auto_field()
    

