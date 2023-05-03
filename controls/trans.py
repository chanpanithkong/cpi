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

from pprint import pprint

jwt = JWTManager(app)

class InsertAllProductToTrans(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            if data['userrequest'] == "inserttranns" :
                
                userid = session.get('userid')
                batches = tbbatches.find_by_branchbatchopen(session.get('branchcode'))
                users = tbusers.find_by_userid(userid)
            
                for dt in data['data']:
            
                    trans = tbtrans.find_by_batchidprodid(batches.batchid, dt['prodid'])
                    if trans is not None:
                        print(1)
                        get_trandata = tbtrans.find_by_tid(trans.tid)
                        get_trandata.price = dt['price']
                        print(1)
                        get_trandata.submitternote = dt['note']
                        print(1)
                        #saved 12
                        #submitted 1
                        if data['msg'] == "submitted":
                            get_trandata.status = 1
                        elif data['msg'] == "saved":
                            get_trandata.status = 12
                        print(1)    
                        now = datetime.now()
                        currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                        print(1)
                        get_trandata.submitdate = currentdatetime
                        get_trandata.authorizedate = currentdatetime
                        get_trandata.checkerdate = currentdatetime
                        get_trandata.valuedate = currentdatetime
                        get_trandata.trandate = currentdatetime
                        get_trandata.countsubmitted = 0
                        print(1)
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
                        elif data['msg'] == "saved":
                            get_trandata.status = 12
                            
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
            
            return {"msg": "cannot insert products"}
        except Exception as err:
            return {"msg": err}
        

class InputterInsertTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            maxtid = db.session.query(func.max(tbtrans.tid)).scalar()
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
            return {"msg": result}
        except Exception as err:
            return {"msg": err}

class InputterUpdateTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
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
                result = "insert tid : " + str(tran_data.tid)
                return {"msg": result}
            
            return {"msg": "there is no tid : " + data['data']['tid']}
        except Exception as err:
            return {"msg": err}

class UpdateTranByCategories(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            branchcode = session.get("branchcode")

            pprint(data)
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
                return {"msg": "update list of data"}
            else:    
                return {"msg": "there is no data"}
        except Exception as err:
            return {"msg": err}        


class CheckerUpdateTransaction(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            userid = session.get("userid")
            
            batch = tbbatches.find_by_branchbatchopen(data["branchcode"])
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
                    elif(data['userrequest'] == 'accept'):
                        tran_data.status = 13
                        msg = "accept"

                    db.session.commit()

            return {"msg": msg}
            
        except Exception as err:
            return {"msg": err}


class AuthorizerUpdateTransaction(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            
            data = json.loads(request.data)
            userid = session.get("userid")
            
            batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
            msg = "reject"    
            
            for dt in data['data']:
                print(dt['prodid'],batch.batchid)
                tran_data = tbtrans.find_by_prodbatchid(dt['prodid'],batch.batchid)
                print(tran_data)
                print(1)
                if (tran_data is not None):
                    print(1)
                    tran_data.authorizer = userid
                    now = datetime.now()
                    currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")
                    print(1)
                        
                    tran_data.authorizedate = currentdatetime
                    tran_data.authorizernote = dt['authorizernote']

                    print(1)
                    
                    if data['userrequest'] == 'reject':
                        tran_data.status = 10
                    elif(data['userrequest'] == 'authorize'):
                        tran_data.status = 3
                        msg = "authorize"
                        print(1)
                    
                    db.session.commit()

            return {"msg": msg}
            
        except Exception as err:
            return {"msg": err}

class AuthorizerUpdateTran(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = json.loads(request.data)
            tran_data = tbtrans.find_by_tid(data['data']['tid'])
            if (tran_data is not None):
                tran_data.authorizer = data['data']['authorizer']

                now = datetime.now()
                currentdatetime = now.strftime("%y-%m-%dT%H:%M:%S")

                tran_data.authorizedate = currentdatetime
                tran_data.authorizernote = data['data']['authorizernote']
                tran_data.status = 3
                # db.session.add(tran_data)
                db.session.commit()
                result = "autherize tid : " + str(tran_data.tid)
                return {"msg": result}
            return {"msg": "there is no tid : " + data['data']['tid']}
        except Exception as err:
            return {"msg": err}

# class UpdateCitizen(Resource):
#     @classmethod
#     # @jwt_required()
#     def post(cls):
#         try:
#             data = request.get_json()

#             citizen_data = tbcitizens.find_by_cid(data['data']['cid'])

#             if (citizen_data is not None):

#                 # get_statusdata = tbcitizens()
#                 # get_statusdata.cid = data['data']['cid']
#                 citizen_data.lastname = data['data']['lastname']
#                 citizen_data.middlename = data['data']['middlename']
#                 citizen_data.firstname = data['data']['firstname']
#                 citizen_data.gender = data['data']['gender']
#                 citizen_data.dob = data['data']['dob']
#                 citizen_data.placeofbirth = data['data']['placeofbirth']
#                 citizen_data.address = data['data']['address']
#                 citizen_data.electioncenter = data['data']['electioncenter']
#                 citizen_data.party = data['data']['party']
#                 citizen_data.updatedby = data['data']['updatedby']
#                 citizen_data.updateddate = data['data']['updateddate']

#                 db.session.commit()
#                 result = "update cid : " + data['data']['cid']
#                 return {"msg": result}
#             return {"msg": "there is no cid : " + data['data']['cid']}

#         except Exception as err:
#             return {"msg":err}

# class DeleteCitizen(Resource):
#     @classmethod
#     # @jwt_required()
#     def post(cls):
#         try:

#             data = request.get_json()
#             userid = data['data']['cid']
#             get_statusdata = tbcitizens.find_by_cid(userid)
#             db.session.delete(get_statusdata)
#             db.session.commit()
#             return {"msg":  "delete cid : "+data['data']['cid']}

#         except Exception as err:
#             return {"msg":err}


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

# class TransListDetails(Resource):
#     @classmethod
#     # @jwt_required()
#     def get(cls):
#         try:
#             # data = tbtrans.query.all()
            
#             data = db.session.query(tbtrans, tbbatches).join(tbbatches).all()
#             schema = TransSchema(many=True)
#             json_data = {}
#             for dt in data:
#                 _data = schema.dump(dt)
#                 json_data.append(_data)
#             return {"trans": json_data}
#         except Exception as err:
#             return {"msg": err}
