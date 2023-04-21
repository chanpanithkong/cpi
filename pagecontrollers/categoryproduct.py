from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file, session

from models.rolemenus import tbrolemenu
from models.categories import tbcategories
from models.roles import tbroles

class CreateProducts(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createproducts"), 200, headers)
    
class CreateCategories(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createcategories"), 200, headers)
    
class UpdateProducts(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="updateproducts"), 200, headers)
    
class UpdateCategories(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="updatecategories"), 200, headers)
    
class ViewProducts(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        categories = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role,categories=categories, task="viewproducts"), 200, headers)
    
class ViewCategories(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        categories = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role, categories=categories, task="viewcategories"), 200, headers)