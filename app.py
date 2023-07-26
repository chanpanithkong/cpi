from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from urllib.parse import quote
# from config.db import db, app, api

from models.menus import tbmenus

from controls.branches import Branch, BranchesList, IndexPage, APICreateBranch
from controls.categories import CreateCategory, CategoriesList, Category, CategoriesParent, CategoriesChildFromParent
from controls.measurement import Measurement, MeasurementList
from controls.menus import Menu, MenusList
from controls.products import APICreateProduct, Product, ProductsList
from controls.rolemenu import RoleMenu, RoleMenuList, RoleMenuParents, RoleMenuChilds, DeleteInsertRoleMenu
from controls.roles import Role, RoleList, RoleManagement
from controls.status import Status, StatusList
from controls.trans import Tran, TransList, InputterInsertTran, AuthorizerUpdateTran, InputterUpdateTran, CheckerUpdateTransaction, AuthorizerUpdateTransaction, InsertAllProductToTrans, UpdateTranByCategories, TransWithBatchWherePriceAndWeightIsEmpty, TransWithBatchCategoryWherePriceAndWeightIsEmpty, TransWithBatchCategory
from controls.batches import Batch, BatchesList, CreateBatch, CloseBatch, ReopenBatch
from controls.users import User, UsersList, UserLogin, ChangePasswordForUser, UpdateUserProfile
from pagecontrollers.pages import UpdateRoles,ViewUsers,ViewDeleteUsers, UpdateUsers, CreateUsers, CreateStatus, UpdateStatus, ViewStatus, AttachedRolePermission, CreatePermission, CreateRoles, CreateBatches, ViewBatches, UpdateBatches, Logout, UserLoginPage, LoginPage, HomePage, SubmittedTrans, AuthorizedTrans, CheckedTrans,BranchSession,BranchSessionDetails,SessionDuration,ViewBranches, CreateBranch, UpdateBranch, CheckedTransDetails, HistoryOfTrans, TransactionDetails, BeverageTobacco, Restaurant, ClothShoes, Shipping, Medicine, Housing
from pagecontrollers.usersetting import UserProfile, ChangePassword
from pagecontrollers.food import Rice, Ingredient, Meat, FishSeaFood, Fruit, Vegetables
from pagecontrollers.categoryproduct import ListProducts, CreateProducts, CreateCategories, UpdateProducts, UpdateCategories, ViewProducts, ViewCategories

from dbinfo import dbconfig
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
import logging
import os
from pprint import pprint
from datetime import datetime

# config file
app = Flask(__name__, template_folder='pages')
api = Api(app)

# log = logging.getLogger('werkzeug')
# log.disabled = True
    

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
# disable message error in internal system
# app.config['PROPAGATE_EXCEPTIONS'] = True

# MySQL closes it self the stale connections (8 hours of inactivity by default). You can set the pool recycle to solve this problem.
app.config["SQLALCHEMY_POOL_RECYCLE"] = 300

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbconfig.username + ':' + \
    dbconfig.password + '@' + dbconfig.url + ':' + \
    dbconfig.port + '/' + dbconfig.mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['CORS_HEADERS'] = 'Content-Type'

DEBUG = False

db = SQLAlchemy(app)

@app.route("/")
def index():
    if not session.get("userid"):
        return redirect("/login")
    else:
        return redirect("/dashboard")
    
# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST

# from flask_simple_crypt import SimpleCrypt

# cipher = SimpleCrypt()
# cipher.init_app(app)

# enc_data = cipher.encrypt("userprofile")
# print(enc_data)  # returns base64 encoded and encrypted data

# dec_data = cipher.decrypt(enc_data)
# print(dec_data)  # returns original data


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html')

######### webpage #########


api.add_resource(HomePage, "/dashboard")
# user settings
api.add_resource(UserProfile, "/userprofile")
api.add_resource(ChangePassword, "/changepassword")
api.add_resource(LoginPage, "/login/")
api.add_resource(Logout, "/logout")
api.add_resource(UserLoginPage, "/userloginpage")

# food
api.add_resource(Rice, "/rice")
api.add_resource(Ingredient, "/ingredients")
api.add_resource(Meat, "/meat")
api.add_resource(FishSeaFood, "/fishandseafood")
api.add_resource(Fruit, "/fruit")
api.add_resource(Vegetables, "/vegetables")
# beverage and tobacco
api.add_resource(BeverageTobacco, "/beveragestobacco")
# restaurant
api.add_resource(Restaurant, "/restaurant")
# clothes and shoes
api.add_resource(ClothShoes, "/clothesshoes")
# shipping
api.add_resource(Shipping, "/shipping")
# medecine
api.add_resource(Medicine, "/medicine")
# housing
api.add_resource(Housing, "/housing")

# submitted & authorized & checked trans
api.add_resource(SubmittedTrans, "/submittedtrans")
api.add_resource(AuthorizedTrans, "/authorizedtrans")
api.add_resource(CheckedTrans, "/checkedtrans")
api.add_resource(CheckedTransDetails, "/checkedtransdetail/<branchcode>")

# session
api.add_resource(BranchSession, "/branchsession")
api.add_resource(BranchSessionDetails, "/sessiondetails/<branchcode>/<page>")
api.add_resource(SessionDuration, "/sessionduration")

# Branch
api.add_resource(ViewBranches, "/viewbranches")
api.add_resource(CreateBranch, "/createbranch")
api.add_resource(UpdateBranch, "/updatebranch/<branchcode>")

# historyoftrans
api.add_resource(HistoryOfTrans, "/historyoftrans/<page>")
api.add_resource(TransactionDetails, "/transactiondetails/<batchid>")

# products management
api.add_resource(CreateProducts, "/createproducts/<catid>")
api.add_resource(ListProducts, "/listproducts/<catid>")
api.add_resource(CreateCategories, "/createcategories")
api.add_resource(UpdateProducts, "/updateproducts/<catid>/<prodid>")
api.add_resource(UpdateCategories, "/updatecategories/<catid>")
api.add_resource(ViewProducts, "/viewproducts")
api.add_resource(ViewCategories, "/viewcategories")

# batches management
api.add_resource(CreateStatus, "/createstatus")
api.add_resource(UpdateStatus, "/updatestatus")
api.add_resource(ViewStatus, "/viewstatus")
# batches management
api.add_resource(UpdateRoles, "/updateroles/<roleid>")
api.add_resource(CreateRoles, "/createroles")
api.add_resource(CreatePermission, "/createpermission/<roleid>")
api.add_resource(AttachedRolePermission, "/attachedrolepermission")
# batches management
api.add_resource(CreateBatches, "/createbatch")
api.add_resource(ViewBatches, "/viewbatch")
api.add_resource(UpdateBatches, "/updatebatch")
# user management
api.add_resource(CreateUsers, "/createusers")
api.add_resource(ViewUsers, "/viewusers")
api.add_resource(ViewDeleteUsers, "/viewdeleteusers")
api.add_resource(UpdateUsers, "/updateusers/<userid>")


######## webservice #########
# api.add_resource(UpdateUserProfile, "/api/createuser")

# api.add_resource(IndexPage, "/api/")
api.add_resource(APICreateBranch, "/api/branch")
# api.add_resource(BranchesList, "/api/brancheslist")
api.add_resource(CreateCategory, "/api/createcategory")
# api.add_resource(Category, "/api/category/<catid>")
# api.add_resource(CategoriesList, "/api/categorieslist")
# api.add_resource(CategoriesParent, "/api/categoriesparent")
# api.add_resource(CategoriesChildFromParent,
#                  "/api/categorieschildfromparent/<parentid>")

# api.add_resource(Measurement, "/api/measurement/<mid>")
# api.add_resource(MeasurementList, "/api/measurementlist")

# api.add_resource(Menu, "/api/menu/<mid>")
# api.add_resource(MenusList, "/api/menuslist")

api.add_resource(APICreateProduct, "/api/createproduct")
# api.add_resource(Product, "/api/product/<pid>")
# api.add_resource(ProductsList, "/api/productslist")


api.add_resource(DeleteInsertRoleMenu, "/api/deleteinsertrolemenu")
# api.add_resource(RoleMenu, "/api/rolemenu/<roleid>")
# api.add_resource(RoleMenuList, "/api/rolemenulist")
# api.add_resource(RoleMenuParents, "/api/rolemenuparents/<roleid>")
# api.add_resource(RoleMenuChilds, "/api/rolemenuchilds/<roleid>/<parentid>")
api.add_resource(RoleManagement, "/api/rolemanagement")
# api.add_resource(Role, "/api/role/<roleid>")
# api.add_resource(RoleList, "/api/rolelist")

# api.add_resource(Status, "/api/status/<statusid>")
# api.add_resource(StatusList, "/api/statuslist")

# api.add_resource(Tran, "/api/tran/<tid>")
# api.add_resource(TransList, "/api/translist")
# api.add_resource(InputterInsertTran, "/api/inputterinserttran")
# api.add_resource(AuthorizerUpdateTran, "/api/authorizerupdatetran")
# api.add_resource(InputterUpdateTran, "/api/inputterupdatetran")

api.add_resource(InsertAllProductToTrans, "/api/insertallproducttotrans")
api.add_resource(UpdateTranByCategories, "/api/updatetranbycategories")
api.add_resource(AuthorizerUpdateTransaction, "/api/authorizetransactions")
api.add_resource(CheckerUpdateTransaction, "/api/checkerupdatetransactions")

# api.add_resource(TransWithBatchWherePriceAndWeightIsEmpty,
#                  "/api/transwithbatchwherepriceandweightisempty/<batchid>")
# api.add_resource(TransWithBatchCategory,
#                  "/api/transwithbatchcategory/<batchid>/<catid>")
# api.add_resource(TransWithBatchCategoryWherePriceAndWeightIsEmpty,
#                  "/api/transwithbatchcategorywherepriceandweightisempty/<batchid>/<catid>")

# api.add_resource(Batch, "/api/batch/<batchid>")
# api.add_resource(BatchesList, "/api/batcheslist")
api.add_resource(CreateBatch, "/api/createbatch")
api.add_resource(CloseBatch, "/api/closebatch")
api.add_resource(ReopenBatch, "/api/reopenbatch")

# api.add_resource(User, "/api/user/<userid>")
# api.add_resource(UsersList, "/api/userslist")
# api.add_resource(UserLogin, "/api/userlogin")
api.add_resource(ChangePasswordForUser, "/api/changepasswordforuser")
api.add_resource(UpdateUserProfile, "/api/updateuserprofile")


if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
