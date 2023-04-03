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

class UserProfile(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}

        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()
        menuchilds = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))
        
        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, role=role, task="userprofile"), 200, headers)


class ChangePassword(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}

        filter = (tbrolemenu.roleid == session.get('roleid')) & (tbmenus.parentid == 0)
        menus = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()
        menuchilds = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, menuchilds=menuchilds, role=role, task="changepassword"), 200, headers)
