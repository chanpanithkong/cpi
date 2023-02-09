from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.products import tbproducts
from config.db import db

class ProductsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbproducts
        sqla_session = db.session
        load_instance = True

    prodid = auto_field()
    productcode = auto_field()
    nameen = auto_field()
    namekh = auto_field()
    inputtype = auto_field()
    catid = auto_field()
    details = auto_field()
    

