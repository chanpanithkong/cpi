from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from urllib.parse import quote 
# from config.db import db, app, api

from controls.branches import Branch, BranchesList, IndexPage
from controls.categories import CategoriesList, Category, CategoriesParent, CategoriesChildFromParent
from controls.measurement import Measurement, MeasurementList
from controls.menus import Menu, MenusList
from controls.products import Product, ProductsList
from controls.rolemenu import RoleMenu, RoleMenuList
from controls.roles import Role, RoleList
from controls.status import Status, StatusList
from controls.trans import Tran, TransList, InputterInsertTran, AuthorizerUpdateTran, InputterUpdateTran, InsertAllProductToTrans, UpdateTranByCategories, TransWithBatchWherePriceAndWeightIsEmpty, TransWithBatchCategoryWherePriceAndWeightIsEmpty, TransWithBatchCategory
from controls.batches import Batch, BatchesList, CreateBatch
from controls.users import User, UsersList, UserLogin
# from pagecontrollers.index import IndexPage, LoginPage, CitizenTableList, CitizentDataEntry, CitizentDataEdit, CitizentAddData, CitizentUpdateData, CitizenTableListPrint
from dbinfo import dbconfig
from flask_cors import CORS
from flask_migrate import Migrate

# config file
app = Flask(__name__,template_folder='pages')
CORS(app) 
api = Api(app)

#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
#disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbconfig.username + ':' + dbconfig.password + '@' + dbconfig.url + ':' + dbconfig.port + '/' + dbconfig.mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True

db = SQLAlchemy(app)

# @app.route("/")
# def index():
#     return "Hello World"

# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html')


api.add_resource(IndexPage, "/")
api.add_resource(Branch, "/branch/<branchcode>")
api.add_resource(BranchesList, "/brancheslist")

api.add_resource(Category, "/category/<catid>")
api.add_resource(CategoriesList, "/categorieslist")
api.add_resource(CategoriesParent, "/categoriesparent")
api.add_resource(CategoriesChildFromParent, "/categorieschildfromparent/<parentid>")

api.add_resource(Measurement, "/measurement/<mid>")
api.add_resource(MeasurementList, "/measurementlist")

api.add_resource(Menu, "/menu/<mid>")
api.add_resource(MenusList, "/menuslist")

api.add_resource(Product, "/product/<pid>")
api.add_resource(ProductsList, "/productslist")

api.add_resource(RoleMenu, "/rolemenu/<roleid>")
api.add_resource(RoleMenuList, "/rolemenulist")

api.add_resource(Role, "/role/<roleid>")
api.add_resource(RoleList, "/rolelist")

api.add_resource(Status, "/status/<statusid>")
api.add_resource(StatusList, "/statuslist")

api.add_resource(Tran, "/tran/<tid>")
api.add_resource(TransList, "/translist")
api.add_resource(InputterInsertTran, "/inputterinserttran")
api.add_resource(AuthorizerUpdateTran, "/authorizerupdatetran")
api.add_resource(InputterUpdateTran, "/inputterupdatetran")
api.add_resource(InsertAllProductToTrans, "/insertallproducttotrans")
api.add_resource(UpdateTranByCategories, "/updatetranbycategories")
api.add_resource(TransWithBatchWherePriceAndWeightIsEmpty, "/transwithbatchwherepriceandweightisempty/<batchid>")
api.add_resource(TransWithBatchCategory, "/transwithbatchcategory/<batchid>/<catid>")
api.add_resource(TransWithBatchCategoryWherePriceAndWeightIsEmpty, "/transwithbatchcategorywherepriceandweightisempty/<batchid>/<catid>")

api.add_resource(Batch, "/batch/<batchid>")
api.add_resource(BatchesList, "/batcheslist")
api.add_resource(CreateBatch, "/createbatch")


api.add_resource(User, "/user/<userid>")
api.add_resource(UsersList, "/userslist")
api.add_resource(UserLogin, "/userlogin")

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
