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

class Rice(Resource):
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

        category = 2
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="rice"), 200, headers)


class Ingredient(Resource):
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

        category = 3
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="ingredient"), 200, headers)


class Meat(Resource):
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

        category = 4
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="meat"), 200, headers)


class FishSeaFood(Resource):
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

        category = 5
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="fishandseafood"), 200, headers)


class Fruit(Resource):
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

        category = 6
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="fruit"), 200, headers)


class Vegetables(Resource):
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

        category = 7
        productlist = tbproducts.find_by_catid(category)

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds,role=role, productlist=productlist, task="vegetable"), 200, headers)
