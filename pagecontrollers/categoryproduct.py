from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from flask import make_response, render_template, redirect, send_file, session

from models.rolemenus import tbrolemenu
from models.categories import tbcategories
from models.products import tbproducts
from models.roles import tbroles

from pprint import pprint


class ListProducts(Resource):
    @classmethod
    def get(cls, catid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        products = tbproducts.find_by_catid(catid)

        category = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role, products=products, category=category, catid=catid, task="listproducts",main="product"), 200, headers)


class CreateProducts(Resource):
    @classmethod
    def get(cls, catid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        category = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role, catid=catid, category=category, task="createproducts",main="product"), 200, headers)


class CreateCategories(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        category = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role, category=category, task="createcategories",main="product"), 200, headers)


class UpdateProducts(Resource):
    @classmethod
    def get(cls, catid, prodid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        print(catid, prodid)

        category = tbcategories
        product = tbproducts

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, category=category, catid=catid, product=product, prodid=prodid, task="updateproducts",main="product"), 200, headers)


class UpdateCategories(Resource):
    @classmethod
    def get(cls, catid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        category = tbcategories.find_by_catid(catid)

        return make_response(render_template('index.html', menus=menus, role=role, category=category, task="updatecategories",main="product"), 200, headers)


class ViewProducts(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        categories = tbcategories

        return make_response(render_template('index.html', menus=menus, role=role, categories=categories, task="viewproducts",main="product"), 200, headers)


class ViewCategories(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        categories = tbcategories
        return make_response(render_template('index.html', menus=menus, role=role, categories=categories, task="viewcategories",main="product"), 200, headers)
