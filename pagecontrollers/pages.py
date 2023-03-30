from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from flask_session import Session
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file, session

from models.rolemenus import tbrolemenu
from models.menus import tbmenus
from models.roles import tbroles
from models.users import tbusers
from models.products import tbproducts
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


        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, role=role, task="dashboard"), 200, headers)


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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="beveragetobacco"), 200, headers)


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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="restaurant"), 200, headers)


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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="clothshoes"), 200, headers)

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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="shipping"), 200, headers)


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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="medicine"), 200, headers)


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

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="housing"), 200, headers)
