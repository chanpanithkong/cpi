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

class Rice(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 2
        productlist = []

        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        submitdata = []
        trans = []
        disabled = ""
        isbutton = False
        if batch is not None:
            trans = tbtrans
            
            productlist = tbproducts

            filter = (tbtrans.status == 1) & (tbcategories.catid == category) & (tbtrans.batchid == batch.batchid)
            submitdata = db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
            isbutton = True    
            if len(submitdata) > 0:
                disabled = "disabled "

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled, submitdata=submitdata,isbutton=isbutton,category = category, task="rice"), 200, headers)


class Ingredient(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 3
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="ingredient"), 200, headers)


class Meat(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 4
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="meat"), 200, headers)


class FishSeaFood(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 5
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="fishandseafood"), 200, headers)


class Fruit(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 6
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="fruit"), 200, headers)


class Vegetables(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        category = 7
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist, trans=trans,batch=batch, disabled=disabled,isbutton=isbutton, task="vegetable"), 200, headers)
