from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.rolemenus import tbrolemenu
from models.menus import tbmenus
from schema.rolemenuschema import RoleMenuSchema
from schema.menusschema import MenusSchema

from pprint import pprint
jwt = JWTManager(app)


class RoleMenu(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, roleid=None):
        try:
            data = tbrolemenu.find_by_roleid(roleid)
            schema = RoleMenuSchema(many=True)
            _data = schema.dump(data)
            return {"rolemenu": _data}
        except Exception as err:
            return {"msg": err}


class RoleMenuList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbrolemenu.query.all()
            schema = RoleMenuSchema(many=True)
            _data = schema.dump(data)
            return {"rolemenus": _data}
        except Exception as err:
            return {"msg": err}


class RoleMenuParents(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, roleid=None):
        try:

            filter = (tbrolemenu.roleid == roleid) & (tbmenus.parentid == 0)
            data = db.session.query(tbrolemenu, tbmenus).filter(
                tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

            rolemenu = []
            menu = []
            for dt in data:
                schemarolemenu = RoleMenuSchema(many=False)
                schemamenu = MenusSchema(many=False)

                datarolemenu = schemarolemenu.dump(dt[0])
                datamenu = schemamenu.dump(dt[1])

                rolemenu.append(datarolemenu)
                menu.append(datamenu)

            # schema = RoleMenuSchema(many=True)
            # _data = schema.dump(data)
            return {"rolemenus": rolemenu, "menus": menu}
        except Exception as err:
            return {"msg": err}

class RoleMenuChilds(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, roleid=None, parentid=None):
        try:

            filter = (tbrolemenu.roleid == roleid) & (tbmenus.parentid == parentid)
            data = db.session.query(tbrolemenu, tbmenus).filter(
                tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

            rolemenu = []
            menu = []
            for dt in data:
                schemarolemenu = RoleMenuSchema(many=False)
                schemamenu = MenusSchema(many=False)

                datarolemenu = schemarolemenu.dump(dt[0])
                datamenu = schemamenu.dump(dt[1])

                rolemenu.append(datarolemenu)
                menu.append(datamenu)

            # schema = RoleMenuSchema(many=True)
            # _data = schema.dump(data)
            return {"rolemenus": rolemenu, "menus": menu}
        except Exception as err:
            return {"msg": err}
