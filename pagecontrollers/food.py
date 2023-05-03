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

from pprint import pprint

class Rice(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 2
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="rice"), 200, headers)


class Ingredient(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 3
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="ingredient"), 200, headers)


class Meat(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 4
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="meat"), 200, headers)

class FishSeaFood(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 5
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="fishandseafood"), 200, headers)

class Fruit(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 6
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="fruit"), 200, headers)


class Vegetables(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 7
        productlist = []
        submitdata = []
        disabled = "disabled"
        isbutton = False
        
        if batch is not None:
            if batch.statusid == 9:

                productlist = tbproducts.find_by_catid(category)

                filter = (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                dataexist = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()

                if len(dataexist) > 0: 

                    filter = ((tbtrans.status == 10) | (tbtrans.status == 12)) & (tbtrans.batchid == batch.batchid) & (tbcategories.catid == category)
                    submitdata = db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filter).all()
                    
                    isbutton = True    
                    if len(submitdata) > 0:
                        disabled = ""
                else:
                    isbutton = True    
                    disabled = ""

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="vegetable"), 200, headers)