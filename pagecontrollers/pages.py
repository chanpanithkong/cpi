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
from models.branches import tbbranches

from schema.usersschema import UserSchema

import datetime
from pprint import pprint


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
    
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        
        user = tbusers.find_by_userid(session.get('userid'))

        batchdisabled = ""
        if batch is not None :
            batchtrans = tbtrans.find_by_batchid(batch.batchid)
            if len(batchtrans) > 0:
                batchdisabled = "disabled"
        
        return make_response(render_template('index.html', menus=menus, role=role, batchdisabled=batchdisabled,user=user, task="dashboard"), 200, headers)


class HistoryOfTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus,role=role, task="historyoftrans"), 200, headers)


class BeverageTobacco(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 8
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "
            
        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="beveragetobacco"), 200, headers)


class Restaurant(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 9
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, isbutton=isbutton, task="restaurant"), 200, headers)


class ClothShoes(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 10
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, isbutton=isbutton, task="clothshoes"), 200, headers)

class Shipping(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 11
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, isbutton=isbutton, task="shipping"), 200, headers)


class Medicine(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 12
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, isbutton=isbutton, task="medicine"), 200, headers)


class Housing(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 13
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            productlist = tbproducts.find_by_catid(category)
            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus,role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="housing"), 200, headers)


class SubmittedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        catlist = tbcategories.query.filter(tbcategories.catid != 1).all()
        
        products = tbproducts
        
        batch = []
        if batch is not None:
            batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
            
        trans = tbtrans

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans, task="submittedtrans"), 200, headers)


class AuthorizedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))
        
        
        products = tbproducts
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        
        catlist = []
        trans = []
        if batch is not None :
            catlist = tbtrans.find_by_authorizecatbatchid(batch.batchid)
            trans = tbtrans

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans, task="authorizedtrans"), 200, headers)
    
class CheckedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branches = tbbranches.getallbranches()

        return make_response(render_template('index.html', menus=menus, role=role, branches=branches, task="checkedtrans"), 200, headers)



class CheckedTransDetails(Resource):
    @classmethod
    def get(cls, branchcode):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))
        
        
        products = tbproducts
        batch = tbbatches.find_by_branchbatchopen(branchcode)
        catlist = []
        if batch is  not None :
            catlist = tbtrans.find_by_checkebatchid(batch.batchid)
        
        trans = tbtrans

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans, task="checkedtransdetail"), 200, headers)
