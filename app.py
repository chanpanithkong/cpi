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
from controls.rolemenu import RoleMenu, RoleMenuList, RoleMenuParents, RoleMenuChilds
from controls.roles import Role, RoleList
from controls.status import Status, StatusList
from controls.trans import Tran, TransList, InputterInsertTran, AuthorizerUpdateTran, InputterUpdateTran, InsertAllProductToTrans, UpdateTranByCategories, TransWithBatchWherePriceAndWeightIsEmpty, TransWithBatchCategoryWherePriceAndWeightIsEmpty, TransWithBatchCategory
from controls.batches import Batch, BatchesList, CreateBatch
from controls.users import User, UsersList, UserLogin
from pagecontrollers.pages import LoginPage, HomePage
from pagecontrollers.usersetting import UserProfile, ChangePassword

from dbinfo import dbconfig
from flask_cors import CORS
from flask_migrate import Migrate

# config file
app = Flask(__name__, template_folder='pages')
api = Api(app)


# cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
# disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbconfig.username + ':' + \
    dbconfig.password + '@' + dbconfig.url + ':' + \
    dbconfig.port + '/' + dbconfig.mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

DEBUG = True

db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "*"}})

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

# webpage


api.add_resource(HomePage, "/")
# user settings
api.add_resource(UserProfile, "/userprofile")
api.add_resource(ChangePassword, "/changepassword")
api.add_resource(LoginPage, "/login/")
# food


# webservice

api.add_resource(IndexPage, "/api/")
api.add_resource(Branch, "/api/branch/<branchcode>")
api.add_resource(BranchesList, "/api/brancheslist")

api.add_resource(Category, "/api/category/<catid>")
api.add_resource(CategoriesList, "/api/categorieslist")
api.add_resource(CategoriesParent, "/api/categoriesparent")
api.add_resource(CategoriesChildFromParent,
                 "/api/categorieschildfromparent/<parentid>")

api.add_resource(Measurement, "/api/measurement/<mid>")
api.add_resource(MeasurementList, "/api/measurementlist")

api.add_resource(Menu, "/api/menu/<mid>")
api.add_resource(MenusList, "/api/menuslist")

api.add_resource(Product, "/api/product/<pid>")
api.add_resource(ProductsList, "/api/productslist")

api.add_resource(RoleMenu, "/api/rolemenu/<roleid>")
api.add_resource(RoleMenuList, "/api/rolemenulist")
api.add_resource(RoleMenuParents, "/api/rolemenuparents/<roleid>")
api.add_resource(RoleMenuChilds, "/api/rolemenuchilds/<roleid>/<parentid>")

api.add_resource(Role, "/api/role/<roleid>")
api.add_resource(RoleList, "/api/rolelist")

api.add_resource(Status, "/api/status/<statusid>")
api.add_resource(StatusList, "/api/statuslist")

api.add_resource(Tran, "/api/tran/<tid>")
api.add_resource(TransList, "/api/translist")
api.add_resource(InputterInsertTran, "/api/inputterinserttran")
api.add_resource(AuthorizerUpdateTran, "/api/authorizerupdatetran")
api.add_resource(InputterUpdateTran, "/api/inputterupdatetran")
api.add_resource(InsertAllProductToTrans, "/api/insertallproducttotrans")
api.add_resource(UpdateTranByCategories, "/api/updatetranbycategories")
api.add_resource(TransWithBatchWherePriceAndWeightIsEmpty,
                 "/api/transwithbatchwherepriceandweightisempty/<batchid>")
api.add_resource(TransWithBatchCategory,
                 "/api/transwithbatchcategory/<batchid>/<catid>")
api.add_resource(TransWithBatchCategoryWherePriceAndWeightIsEmpty,
                 "/api/transwithbatchcategorywherepriceandweightisempty/<batchid>/<catid>")

api.add_resource(Batch, "/api/batch/<batchid>")
api.add_resource(BatchesList, "/api/batcheslist")
api.add_resource(CreateBatch, "/api/createbatch")


api.add_resource(User, "/api/user/<userid>")
api.add_resource(UsersList, "/api/userslist")
api.add_resource(UserLogin, "/api/userlogin")

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
