from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json, session
from models.branches import tbbranches
from schema.branchesschema import BranchesSchema
from config.userlogging import userlogging
from sqlalchemy import func

jwt = JWTManager(app)


class APICreateBranch(Resource):
    @classmethod
    def post(cls):
        try:
            msg = "fail"
            data = json.loads(request.data)
            
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            
            if data['userrequest'] == "createbranch":
            
                branch = tbbranches()
                branch.branchcode = data['data']['branchcode']
                branch.nameen = data['data']['nameen']
                branch.namekh = data['data']['namekh']
                branch.addressen = data['data']['addressen']
                branch.addresskh = data['data']['addresskh']
                branch.weight = data['data']['weight']
                branch.details = data['data']['details']
            
                db.session.add(branch)
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : create product id " + branch.branchcode)
                msg = "create sucessfully"
            
            elif data['userrequest'] == "updatebranch":
                
                branch = tbbranches.find_by_branchcode(data['data']['branchcode'])
                branch.nameen = data['data']['nameen']
                branch.namekh = data['data']['namekh']
                branch.addressen = data['data']['addressen']
                branch.addresskh = data['data']['addresskh']
                branch.weight = data['data']['weight']
                branch.details = data['data']['details']
                
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : update branchcode " + branch.branchcode)
                msg = "update sucessfully"

            elif data['userrequest'] == "deletebranch":
                
                branch = tbbranches.find_by_branchcode(data['data']['branchcode'])
                db.session.delete(branch)
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : delete branchcode " + branch.branchcode)
                msg = "delete sucessfully"

            return {"category": msg}
        
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}


class Branch(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,branchcode=None):
        try:  
            data = tbbranches.find_by_branchcode(branchcode)
            schema = BranchesSchema(many=False)
            _data = schema.dump(data)
            return {"branch":_data}
        except Exception as err:
            return {"msg":err} 


class BranchesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbbranches.query.all()
            schema = BranchesSchema(many=True)
            _data = schema.dump(data)
            return {"branches":_data}
        except Exception as err:
            return {"msg":err} 

class IndexPage(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        return "<h1>hello world</h1>" 
