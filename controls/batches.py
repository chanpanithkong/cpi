from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import app, request, json, db
from models.batches import tbbatches
from models.branches import tbbranches
from schema.batchesschema import BatchSchema
from config.userlogging import userlogging
from flask import session
from sqlalchemy import func
from datetime import datetime
from config.timestramp import convertdate
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
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if data['data'] == "reopenbatch":
                batch = tbbatches.find_by_branchbatchclose(session.get('branchcode'))
                if batch is not None:
                    batch.statusid = 9

                    db.session.commit()
                    result = "reopen batch"
                    userlogging.degbuglog(clientid, url, userid + " : reopen batch id " + str(batch.batchid))
                    return {"msg": result}
            return {"msg": "cannot reopen batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}
        
class CloseBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if data['data'] == "closebatch":
                batch = tbbatches.find_by_branchbatchopen(session.get('branchcode'))
                if batch is not None:
                    batch.statusid = 8
                    db.session.commit()
                    result = "close batch"
                    userlogging.degbuglog(clientid, url, userid + " : close batch id " + str(batch.batchid))
                    return {"msg": result}
                
            userlogging.degbuglog(clientid, url, userid + " : cannot create batch ")
            return {"msg": "cannot create batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}


class CreateBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if data['data'] == "createbatch":
                
                maxtid = db.session.query(func.max(tbbatches.batchid)).scalar()
                
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
                
                now = datetime.now()
                # currentdatetime = now.strftime("%Y-%m-%d %H:%M:%S")
                
                batchobject = tbbatches()
                batchobject.batchid = maxtid
                batchobject.batch = "batch" + str(maxtid)
                batchobject.detail = session.get('userid') + session.get('branchcode')
                batchobject.createdate = now
                batchobject.createby = session.get('userid')
                batchobject.branch = session.get('branchcode')
                batchobject.statusid = 9
                
                db.session.add(batchobject)
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : create batch id " + str(maxtid))
                result = {"batchid:": str(maxtid)}

                return {"msg": result}
            
            userlogging.degbuglog(clientid, url, userid + " : cannot create batch")
            return {"msg": "cannot create batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}


class OpenBatchForAllBranches(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if data['data'] == "openbatchforallbranches":
                msg = "success"
                batchopenlist = tbbatches.find_by_batchopen()
                if len(batchopenlist) > 0:
                    msg = "fail"
                else:
                    branches = tbbranches.query.all()
                    for branch in branches:
                        maxtid = db.session.query(func.max(tbbatches.batchid)).scalar()
                        
                        if maxtid is None:
                            maxtid = 1
                        else:
                            maxtid = maxtid + 1
                        
                        now = datetime.now()
                        # currentdatetime = now.strftime("%Y-%m-%d %H:%M:%S")
                        
                        batchobject = tbbatches()
                        batchobject.batchid = maxtid
                        batchobject.batch = "batch" + str(maxtid)
                        batchobject.detail = session.get('userid') + session.get('branchcode')
                        batchobject.createdate = now
                        batchobject.createby = session.get('userid')
                        batchobject.branch = branch.branchcode
                        batchobject.statusid = 9
                        
                        db.session.add(batchobject)
                        db.session.commit()

                        userlogging.degbuglog(clientid, url, userid + " : create batch id " + str(maxtid))
                    

                return {"msg": msg}
            
            userlogging.degbuglog(clientid, url, userid + " : cannot create batch")
            return {"msg": "cannot create batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}
        

class CloseBatchForAllBranches(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            
            if data['data'] == "closebatchforallbranches":
            
                branches = tbbranches.query.all()
                for branch in branches:
            
                    batch = tbbatches.find_by_branchbatchopen(branch.branchcode)
                    if batch is not None:
            
                        batch.statusid = 8
                        db.session.commit()
                        result = "close batch"
                        userlogging.degbuglog(clientid, url, userid + " : close batch id " + str(batch.batchid))
                        
                return {"msg": "success"}
                
            userlogging.degbuglog(clientid, url, userid + " : cannot create batch ")
            return {"msg": "cannot create batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}
        

class OpenAndCloseBatch(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            
            if data['userrequest'] == "openandclosebatch":
            
                branchcode = data['data']['branchcode']
                batchid = data['data']['batchid']
                batches = tbbatches.find_by_branchbatchopenlist(branchcode)
                for batch in batches:
                    if int(batch.batchid) != int(batchid):
                        batch.statusid = 8
                        db.session.commit()
                        
                        userlogging.degbuglog(clientid, url, userid + " : close batch id " + str(batch.batchid))
                
                
                batches = tbbatches.find_by_batchid(batchid) 
                if batches.statusid == 8:
                    batches.statusid = 9
                else:
                    batches.statusid = 8
                db.session.commit()
                
                return {"msg": "success"}
                
            userlogging.degbuglog(clientid, url, userid + " : cannot create batch ")
            return {"msg": "cannot create batch"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}