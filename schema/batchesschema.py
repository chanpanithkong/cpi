from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.batches import tbbatches
from config.db import db


class BatchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbbatches
        sqla_session = db.session
        load_instance = True

    batchid = auto_field()
    batch = auto_field()
    detail = auto_field()
    createdate = auto_field()
    createby = auto_field()
    branch = auto_field()
    statusid = auto_field()
