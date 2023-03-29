from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file

from models.rolemenus import tbrolemenu
from models.menus import tbmenus


import datetime


class LoginPage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)


class HomePage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="dashboard"), 200, headers)


class SubmittedTrans(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="submittedtrans"), 200, headers)


class HistoryOfTrans(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="historyoftrans"), 200, headers)


class BeverageTobacco(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="beveragetobacco"), 200, headers)


class Restaurant(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="restaurant"), 200, headers)


class ClothShoes(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="clothshoes"), 200, headers)


class Shipping(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="shipping"), 200, headers)


class Medicine(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="medicine"), 200, headers)


class Housing(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        # role id = 1 is static
        filter = (tbrolemenu.roleid == 3) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()

        menuchilds = tbrolemenu

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, task="housing"), 200, headers)
