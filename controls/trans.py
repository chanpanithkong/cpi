from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import app, db, request, json
from models.trans import tbtrans
from models.products import tbproducts
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
            productlist = tbproducts.query.all()
            for pl in productlist:

                
                maxtid = db.session.query(func.max(tbtrans.tid)).scalar()
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
                
                get_trandata = tbtrans()
                get_trandata.tid = maxtid
                get_trandata.branchcode = data['data']['branchcode']
                get_trandata.productid = pl.prodid
                # get_trandata.weight = data['data']['weight']
                # get_trandata.price = data['data']['price']
                get_trandata.submitter = data['data']['submitter']
                
                # get_trandata.submitternote = data['data']['submitternote']
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
                get_trandata.batchid = data['data']['batchid']

                db.session.add(get_trandata)
                db.session.commit()
            result = "insert all products with batch : " + str(data['data']['batchid'])
            return {"msg": result}
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
