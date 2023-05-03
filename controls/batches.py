from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import app, request, json, db
from models.batches import tbbatches
from schema.batchesschema import BatchSchema

from flask import session
from sqlalchemy import func
from datetime import datetime
from pprint import pprint
jwt = JWTManager(app)


class Batch(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, batchid=None):
        try:
            data = tbbatches.find_by_batchid(batchid)
            schema = BatchSchema(many=False)
            _data = schema.dump(data)
            return {"batch": _data}
        except Exception as err:
            return {"msg": err}


class BatchesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbbatches.query.all()
            schema = BatchSchema(many=True)
            _data = schema.dump(data)
            return {"batches": _data}
        except Exception as err:
            return {"msg": err}


class ReopenBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            if data['data'] == "closebatch":
                batch = tbbatches.find_by_branchbatchclose(session.get('branchcode'))
                if batch is not None:
                    batch.statusid = 9

                    db.session.commit()
                    result = "no batch"
                result = "close batch"

                return {"msg": result}
            return {"msg": "cannot create batch"}
        except Exception as err:
            return {"msg": err}
        
class CloseBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            if data['data'] == "closebatch":
                batch = tbbatches.find_by_branchbatchopen(session.get('branchcode'))
                if batch is not None:
                    batch.statusid = 8

                    db.session.commit()
                    result = "no batch"
                result = "close batch"

                return {"msg": result}
            return {"msg": "cannot create batch"}
        except Exception as err:
            return {"msg": err}


class CreateBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            
            if data['data'] == "createbatch":
                
                maxtid = db.session.query(func.max(tbbatches.batchid)).scalar()
                
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
                
                now = datetime.now()
                currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                
                batchobject = tbbatches()
                batchobject.batchid = maxtid
                batchobject.batch = "batch" + str(maxtid)
                batchobject.detail = session.get('userid') + session.get('branchcode')
                batchobject.createdate = currentdatetime
                batchobject.createby = session.get('userid')
                batchobject.branch = session.get('branchcode')
                batchobject.statusid = 9
                
                db.session.add(batchobject)
                db.session.commit()
                result = {"batchid:": str(maxtid)}

                return {"msg": result}
            return {"msg": "cannot create batch"}
        except Exception as err:
            return {"msg": err}
