from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import app, db, request, json
from flask import session
from models.trans import tbtrans
from models.products import tbproducts
from models.categories import tbcategories
from models.batches import tbbatches
from models.users import tbusers

from schema.transschema import TransSchema
from sqlalchemy import func
from datetime import datetime
from config.userlogging import userlogging
from pprint import pprint

jwt = JWTManager(app)

class InsertAllProductToTrans(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)

            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if data['userrequest'] == "inserttranns" :
                
                batches = tbbatches.find_by_branchbatchopen(session.get('branchcode'))
                users = tbusers.find_by_userid(userid)
            
                for dt in data['data']:
            
                    trans = tbtrans.find_by_batchidprodid(batches.batchid, dt['prodid'])
                    if trans is not None:
                        
                        get_trandata = tbtrans.find_by_tid(trans.tid)
                        get_trandata.price = dt['price']
                        
                        get_trandata.submitternote = dt['note']
                        
                        #saved 12
                        #submitted 1
                        if data['msg'] == "submitted":
                            get_trandata.status = 1
                            userlogging.degbuglog(clientid, url, userid + " : submitted tran id " + str(trans.tid))
                        elif data['msg'] == "saved":
                            get_trandata.status = 12
                            userlogging.degbuglog(clientid, url, userid + " : saved tran id " + str(trans.tid))
                        
                        now = datetime.now()
                        currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                        
                        get_trandata.submitdate = currentdatetime
                        get_trandata.authorizedate = currentdatetime
                        get_trandata.checkerdate = currentdatetime
                        get_trandata.valuedate = currentdatetime
                        get_trandata.trandate = currentdatetime
                        get_trandata.countsubmitted = 0
                        
                        db.session.commit()       
                        
                    else:    
                        maxtid = db.session.query(func.max(tbtrans.tid)).scalar()
                        if maxtid is None:
                            maxtid = 1
                        else:
                            maxtid = maxtid + 1
                
                        get_trandata = tbtrans()
                        get_trandata.tid = maxtid
                
                        get_trandata.branchcode = users.branchcode
                        get_trandata.productid = dt['prodid']
                
                        get_trandata.weight = dt['weight']
                        get_trandata.price = dt['price']
                        get_trandata.submitter = userid
                        get_trandata.submitternote = dt['note']
                        get_trandata.authorizer = ""
                        get_trandata.authorizernote = ""
                        get_trandata.checker =  ""
                        get_trandata.checkernote = ""
                    
                        #saved 12
                        #submitted 1
                        if data['msg'] == "submitted":
                            get_trandata.status = 1
                            userlogging.degbuglog(clientid, url, userid + " : submitted tran id " + str(maxtid))
                        elif data['msg'] == "saved":
                            get_trandata.status = 12
                            userlogging.degbuglog(clientid, url, userid + " : saved tran id " + str(maxtid))
                            
                        now = datetime.now()
                        currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                    
                        get_trandata.submitdate = currentdatetime
                        get_trandata.authorizedate = currentdatetime
                        get_trandata.checkerdate = currentdatetime
                        get_trandata.valuedate = currentdatetime
                        get_trandata.trandate = currentdatetime
                        get_trandata.countsubmitted = 0
                        get_trandata.batchid = batches.batchid
                    
                        db.session.add(get_trandata)
                        db.session.commit()
                
                result = "insert all products of category"
                return {"msg": result}
            
            userlogging.degbuglog(clientid, url, userid + " : cannot insert products")
            return {"msg": "cannot insert products"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}
        

class InputterInsertTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            maxtid = db.session.query(func.max(tbtrans.tid)).scalar()

            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            if maxtid is None:
                maxtid = 1
            else:
                maxtid = maxtid + 1
            
            get_trandata = tbtrans()
            get_trandata.tid = maxtid
            get_trandata.branchcode = data['data']['branchcode']
            get_trandata.productid = data['data']['productid']
            get_trandata.weight = data['data']['weight']
            get_trandata.price = data['data']['price']
            get_trandata.submitter = data['data']['submitter']
            
            get_trandata.submitternote = data['data']['submitternote']
            # get_trandata.authorizer
            # get_trandata.authorizedate
            # get_trandata.authorizernote
            get_trandata.status = 1
            
            now = datetime.now()
            currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")

            get_trandata.submitdate = currentdatetime
            get_trandata.valuedate = currentdatetime
            get_trandata.trandate = currentdatetime
            get_trandata.countsubmitted = 0
            get_trandata.batchid = 1

            db.session.add(get_trandata)
            db.session.commit()
            result = "insert tid : " + str(maxtid)

            userlogging.degbuglog(clientid, url, userid + " : insert tid : " + str(maxtid))
            return {"msg": result}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}

class InputterUpdateTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            data = json.loads(request.data)
            tran_data = tbtrans.find_by_tid(data['data']['tid'])
            if (tran_data is not None):
                
                tran_data.productid = data['data']['productid']
                tran_data.weight = data['data']['weight']
                tran_data.price = data['data']['price']
                tran_data.submitter = data['data']['submitter']
                tran_data.branchcode = data['data']['branchcode']
                tran_data.submitternote = data['data']['submitternote']
                # get_trandata.authorizer
                # get_trandata.authorizedate
                # get_trandata.authorizernote
                tran_data.status = 1
                
                now = datetime.now()
                currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                tran_data.submitdate = currentdatetime
                tran_data.valuedate = currentdatetime
                tran_data.trandate = currentdatetime
                tran_data.countsubmitted = tran_data.countsubmitted + 1
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : update tid : " + str(tran_data.tid))
                result = "update tid : " + str(tran_data.tid)
                return {"msg": result}
            
            userlogging.degbuglog(clientid, url, userid + " : cannot update tid : " + data['data']['tid'])
            return {"msg": "there is no tid : " + data['data']['tid']}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}

class UpdateTranByCategories(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            data = json.loads(request.data)
            branchcode = session.get("branchcode")

            if len(data['data']) > 0:
                for dt in data['data']:
                    batch = tbbatches.find_by_branchbatchopen(branchcode)
                    
                    tran_data = tbtrans.find_by_prodbatchidnotsubmit(dt['prodid'], batch.batchid)[0]
                    
                    if (tran_data is not None):
                        # tran_data = tbtrans().update()
                        tran_data.weight = dt['weight']
                        tran_data.price = dt['price']
                        
                        # tran_data.submitter = data['data']['submitter']
                        # tran_data.branchcode = data['data']['branchcode']
                        tran_data.submitternote = dt['note']
                        # get_trandata.authorizer
                        # get_trandata.authorizedate
                        # get_trandata.authorizernote

                        if data['userrequest'] == 'save':
                            tran_data.status = 12
                        else:
                            tran_data.status = 1
                            
                        now = datetime.now()
                        currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                        tran_data.submitdate = currentdatetime
                        tran_data.valuedate = currentdatetime
                        tran_data.trandate = currentdatetime
                        # tran_data.countsubmitted = tran_data.countsubmitted + 1

                        db.session.commit()
                        userlogging.degbuglog(clientid, url, userid + " : update tid : " + str(tran_data.tid))

                return {"msg": "update list of data"}
            else:    
                userlogging.degbuglog(clientid, url, userid + " : there is no data")
                return {"msg": "there is no data"}
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}        


class CheckerUpdateTransaction(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            batch = tbbatches.find_by_branchbatchopen(data["branchcode"])

            if data['userrequest'] == 'acceptall':
                tran_data = tbtrans.findbybatchid(batch.batchid)
                for tran in tran_data:
                    if tran.status == 3:
                        tran.status = 13
                        db.session.commit()
                msg = "accept all"    
            else:
                
                msg = "reject"    
                
                for dt in data['data']:
                
                    tran_data = tbtrans.find_by_prodbatchidforchecker(dt['prodid'],batch.batchid)
                
                    if (tran_data is not None):
                
                        tran_data.checker = userid
                        now = datetime.now()
                        currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                
                        tran_data.checkerdate = currentdatetime
                        tran_data.checkernote = dt['checkernoted']
                
                        if data['userrequest'] == 'reject':
                            tran_data.status = 11
                            userlogging.degbuglog(clientid, url, userid + " : reject tid : " + str(tran_data.tid))
                            msg = "reject"
                        elif(data['userrequest'] == 'accept'):
                            tran_data.status = 13
                            userlogging.degbuglog(clientid, url, userid + " : accept tid : " + str(tran_data.tid))
                            msg = "accept"
                        
                        db.session.commit()

            return {"msg": msg}
            
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}


class AuthorizerUpdateTransaction(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            
            batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
            msg = "reject"    
            
            for dt in data['data']:
                
                tran_data = tbtrans.find_by_prodbatchid(dt['prodid'],batch.batchid)
                
                if (tran_data is not None):
                
                    tran_data.authorizer = userid
                    now = datetime.now()
                    currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                        
                    tran_data.authorizedate = currentdatetime
                    tran_data.authorizernote = dt['authorizernote']
    
                    if data['userrequest'] == 'reject':
                        tran_data.status = 10
                        userlogging.degbuglog(clientid, url, userid + " : reject tid : " + str(tran_data.tid))
                        msg = "reject"
                    elif(data['userrequest'] == 'authorize'):
                        tran_data.status = 3
                        userlogging.degbuglog(clientid, url, userid + " : authorize tid : " + str(tran_data.tid))
                        msg = "authorize"
                    
                    db.session.commit()

            return {"msg": msg}
            
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}

class AuthorizerUpdateTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            tran_data = tbtrans.find_by_tid(data['data']['tid'])
            if (tran_data is not None):
                tran_data.authorizer = data['data']['authorizer']

                now = datetime.now()
                currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")

                tran_data.authorizedate = currentdatetime
                tran_data.authorizernote = data['data']['authorizernote']
                tran_data.status = 3
                
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : authorize tid : " + str(tran_data.tid))
                result = "autherize tid : " + str(tran_data.tid)
                return {"msg": result}
            
            userlogging.degbuglog(clientid, url, userid + " : there is no tid : " + data['data']['tid'])
            return {"msg": "there is no tid : " + data['data']['tid']}
        
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}

class Tran(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, tid=None):
        try:
            data = tbtrans.find_by_tid(tid)
            schema = TransSchema(many=False)
            _data = schema.dump(data)
            return {"tran": _data}
        except Exception as err:
            return {"msg": err}


class TransList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbtrans.query.all()
            schema = TransSchema(many=True)
            _data = schema.dump(data)
            return {"trans": _data}
        except Exception as err:
            return {"msg": err}


class TransWithBatchWherePriceAndWeightIsEmpty(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, batchid=None):
        try:
            data = tbtrans.find_by_batchid(batchid)
            schema = TransSchema(many=True)
            _data = schema.dump(data)
            return {"tran": _data}
        except Exception as err:
            return {"msg": err}       
 
class TransWithBatchCategory(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, batchid=None, catid=None):
        try:
            filter = (tbtrans.batchid == batchid) & (tbcategories.catid == catid) 
            data = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).order_by(tbtrans.tid).all()
            pprint(data)
            
            json_data = []
            for dt in data:
               schema = TransSchema(many=False)
               _data = schema.dump(dt[0])
               json_data.append(_data)
               
            return {"tran": json_data}
        except Exception as err:
            return {"msg": err}       
 
class TransWithBatchCategoryWherePriceAndWeightIsEmpty(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, batchid=None, catid=None):
        try:
            filter = (tbtrans.batchid == batchid) & (tbcategories.catid == catid) & ((db.Column("price") == None) | (db.Column("weight") == None))
            data = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).order_by(tbtrans.tid).all()
            
            json_data = []
            for dt in data:
               schema = TransSchema(many=False)
               _data = schema.dump(dt[0])
               json_data.append(_data)
               
            return {"tran": json_data}
        except Exception as err:
            return {"msg": err}       
