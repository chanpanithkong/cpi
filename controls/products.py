from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json, session
from models.products import tbproducts
from schema.productsschema import ProductsSchema
from pprint import pprint
from config.userlogging import userlogging
from sqlalchemy import func


jwt = JWTManager(app)



class APICreateProduct(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            msg = "fail"
            data = json.loads(request.data)
            
            clientid = request.remote_addr
            url = request.base_url
            userid = session.get('userid')
            
            if data['userrequest'] == "createproduct":
            
                maxtid = db.session.query(func.max(tbproducts.prodid)).scalar()
                if maxtid is None:
                    maxtid = 1
                else:
                    maxtid = maxtid + 1
                cat = tbproducts()
                cat.prodid = maxtid
                cat.productcode = data['data']['productcode']
                cat.nameen = data['data']['nameen']
                cat.namekh = data['data']['namekh']
                cat.weight = data['data']['weight']
                cat.catid = data['data']['catid']
                cat.details = data['data']['details']
            
                db.session.add(cat)
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : create product id " + str(maxtid))
                msg = "create sucessfully"
            
            elif data['userrequest'] == "updateproduct":
                
                cat = tbproducts.find_by_prodid(data['data']['prodid'])
                cat.productcode = data['data']['productcode']
                cat.nameen = data['data']['nameen']
                cat.namekh = data['data']['namekh']
                cat.weight = data['data']['weight']
                cat.catid = data['data']['catid']
                cat.details = data['data']['details']
                
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : update product id " + str(cat.prodid))
                msg = "update sucessfully"

            elif data['userrequest'] == "deleteproduct":
                
                cat = tbproducts.find_by_prodid(data['data'])
                db.session.delete(cat)
                db.session.commit()

                userlogging.degbuglog(clientid, url, userid + " : update product id " + str(cat.prodid))
                msg = "delete sucessfully"

            return {"category": msg}
        
        except Exception as err:
            userlogging.degbuglog(clientid, url, err)
            return {"msg": err}
        

class Product(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,pid=None):
        try:  
            data = tbproducts.find_by_prodid(pid)
            schema = ProductsSchema(many=False)
            _data = schema.dump(data)
            return {"product":_data}
        except Exception as err:
            return {"msg":err} 


class ProductsList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbproducts.query.all()
            schema = ProductsSchema(many=True)
            _data = schema.dump(data)
            return {"products":_data}
        except Exception as err:
            return {"msg":err} 
