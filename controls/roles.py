from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json
from models.roles import tbroles
from schema.rolesschema import RoleSchema
from sqlalchemy import func

jwt = JWTManager(app)


class RoleManagement(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:  
            msg = ""
            data = json.loads(request.data)
            
            if data['userrequest'] == 'createrole':
            
                rolename = data['data']['rolename']
                details = data['data']['details']
            
                maxtid = db.session.query(func.max(tbroles.roleid)).scalar()
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
            
                role_data = tbroles()

                role_data.roleid = maxtid
                role_data.rolename = rolename
                role_data.details = details
                db.session.add(role_data)
            
                db.session.commit()
            
                msg = "Role created successfully"
            elif data['userrequest'] == 'updaterole':
                
                roleid = data['data']['roleid']
                rolename = data['data']['rolename']
                details = data['data']['details']

                role_data = tbroles.find_by_roleid(roleid)
                
                if role_data is not None:
                
                    role_data.rolename = rolename
                    role_data.details = details

                    db.session.commit()

                    msg = "Role updated successfully"
                else:
                    msg = "Cannot upatet role"

            return {"msg":msg}

        except Exception as err:
            return {"msg":err} 

class Role(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,roleid=None):
        try:  
            data = tbroles.find_by_roleid(roleid)
            schema = RoleSchema(many=False)
            _data = schema.dump(data)
            return {"role":_data}
        except Exception as err:
            return {"msg":err} 


class RoleList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbroles.query.all()
            schema = RoleSchema(many=True)
            _data = schema.dump(data)
            return {"roles":_data}
        except Exception as err:
            return {"msg":err} 
