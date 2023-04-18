from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file, session 

from models.rolemenus import tbrolemenu
from models.users import tbusers
from models.roles import tbroles
from models.branches import tbbranches

class UserProfile(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        user = tbusers.find_by_userid(session.get('userid'))
        role = tbroles.find_by_roleid(session.get('roleid'))
        branch = tbbranches
        return make_response(render_template('index.html', menus=menus,  role=role, user=user, branch = branch, task="userprofile"), 200, headers)


class ChangePassword(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="changepassword"), 200, headers)
