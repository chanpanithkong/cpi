from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.categories import tbcategories
from config.db import db

class CategoriesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbcategories
        sqla_session = db.session
        load_instance = True

    catid = auto_field()
    catcode = auto_field()
    nameen = auto_field()
    namekh = auto_field()
    parentid = auto_field()
    details = auto_field()
    

