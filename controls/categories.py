from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json, session
from models.categories import tbcategories
from models.products import tbproducts
from schema.categoriesschema import CategoriesSchema
from pprint import pprint
from config.userlogging import userlogging

from sqlalchemy import func

jwt = JWTManager(app)


class CreateCategory(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:

            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')

            msg = "fail"
            data = json.loads(request.data)

            if data['userrequest'] == "createcategory":
                maxtid = db.session.query(
                    func.max(tbcategories.catid)).scalar()
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
                cat = tbcategories()
                cat.catid = maxtid
                cat.catcode = data['data']['catcode']
                cat.nameen = data['data']['nameen']
                cat.namekh = data['data']['namekh']
                cat.parentid = data['data']['parentid']
                cat.details = data['data']['details']
                db.session.add(cat)
                db.session.commit()
                msg = "create sucessfully"
                userlogging.degbuglog(clientid, url, userid + " create category id " + maxtid)

            elif data['userrequest'] == "updatecategory":

                cat = tbcategories.find_by_catid(data['data']['catid'])
                cat.catcode = data['data']['catcode']
                cat.nameen = data['data']['nameen']
                cat.namekh = data['data']['namekh']
                cat.parentid = data['data']['parentid']
                cat.details = data['data']['details']

                db.session.commit()
                msg = "update sucessfully"
                userlogging.degbuglog(clientid, url, userid + " update category id " + data['data']['catid'])

            elif data['userrequest'] == "deletecategory":

                prod = tbproducts.find_by_catid(data['data'])
                
                if len(prod) > 0:
                    msg = "This category has products, Please delete products first"
                    userlogging.degbuglog(clientid, url, userid + " delete category id but " + msg)
                else:
                    cat = tbcategories.find_by_catid(data['data'])
                    db.session.delete(cat)
                    db.session.commit()
                    msg = "delete sucessfully"
                    userlogging.degbuglog(clientid, url, userid + " delete category id " + cat.catid)

            return {"msg": msg}

        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}


class Category(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, catid=None):
        try:
            data = tbcategories.find_by_catid(catid)
            schema = CategoriesSchema(many=False)
            _data = schema.dump(data)
            return {"category": _data}
        except Exception as err:
            return {"msg": err}


class CategoriesChildFromParent(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, parentid=None):
        try:

            data = tbcategories.find_by_parentid(parentid)
            schema = CategoriesSchema(many=True)
            _data = schema.dump(data)
            return {"categoris": _data}

        except Exception as err:
            return {"msg": err}


class CategoriesParent(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcategories.query.all()
            parent = []
            for dt in data:
                if dt.parentid is None:
                    parent.append(dt)
            print(parent)
            schema = CategoriesSchema(many=True)
            _data = schema.dump(parent)
            return {"categories": _data}
        except Exception as err:
            return {"msg": err}


class CategoriesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcategories.query.all()
            schema = CategoriesSchema(many=True)
            _data = schema.dump(data)
            return {"categories": _data}
        except Exception as err:
            return {"msg": err}
