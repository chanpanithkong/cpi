from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file, session

from models.rolemenus import tbrolemenu
from models.menus import tbmenus
from models.roles import tbroles
from models.users import tbusers
from models.products import tbproducts
from models.batches import tbbatches
from models.trans import tbtrans
from models.categories import tbcategories
from schema.usersschema import UserSchema

import datetime


class LoginPage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

class UserLoginPage(Resource):
    @classmethod
    def post(cls):
        headers = {'Content-Type': 'text/html'}

        userid = request.form.get('userid')
        password = request.form.get('password')
        try:
            user_data = tbusers.find_by_userid(userid)
            schema = UserSchema(many=False)
            _data = schema.dump(user_data)
            if user_data is not None:
                if _data['password'] == password:
                    session['userid'] = user_data.userid
                    session['roleid'] = user_data.roleid
                    session['username'] = user_data.username
                    session['branchcode'] = user_data.branchcode
                    session['details'] = user_data.details
                    return redirect("/")
            return make_response(render_template('login.html', data="Wrong userid and password !!!"), 200, headers)
        except Exception as err:
            return make_response(render_template('login.html', data=err), 200, headers)


class Logout(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        session.clear()
        return make_response(render_template('login.html'), 200, headers)   


class HomePage(Resource):
    @classmethod
    def get(cls):
        
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        
        user = tbusers.find_by_userid(session.get('userid'))

        batchdisabled = ""
        if batch.batchid is not None :
            batchtrans = tbtrans.find_by_batchid(batch.batchid)
            if len(batchtrans) > 0:
                batchdisabled = "disabled"
        
        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, role=role, batchdisabled=batchdisabled,user=user, task="dashboard"), 200, headers)


class SubmittedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, role=role, task="submittedtrans"), 200, headers)


class HistoryOfTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, task="historyoftrans"), 200, headers)


class BeverageTobacco(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 8
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="beveragetobacco"), 200, headers)


class Restaurant(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 9
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="restaurant"), 200, headers)


class ClothShoes(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 10
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="clothshoes"), 200, headers)

class Shipping(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 11
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="shipping"), 200, headers)


class Medicine(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 12
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="medicine"), 200, headers)


class Housing(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 13
        productlist = tbproducts.find_by_catid(category)

        batch = tbbatches.find_by_createbyopen(session.get("userid"))
        trans = tbtrans

        disabled = ""
        filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
        submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            
        if len(submitdata) > 0:
            disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, task="housing"), 200, headers)
