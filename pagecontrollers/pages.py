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
from sqlalchemy import func

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
        # batch = tbbatches.find_by_branch(session.get("branchcode"))

        user = tbusers.find_by_userid(session.get('userid'))


        sql = "select max(bat.batchid) maxid from tbbatches bat where bat.branch = '" + session.get('branchcode') + "'"
        batchresult = db.engine.execute(sql)

        batches = []
        for record in batchresult:
            batches.append(record)
        
        
        createdisable = ""
        reopendisable = ""
        closeddisable = ""

        

        if batches[0][0] is not None:
            
            if tbbatches.find_by_branchidbatchclose(batches[0][0]) is not None:
                createdisable = ""
                reopendisable = ""
                closeddisable = "disabled"
            
            elif tbbatches.find_by_branchidbatchopen(batches[0][0]) is not None:
                createdisable = "disabled"
                reopendisable = "disabled"
                closeddisable = ""
            
            else:
                print(4)
        else:
            createdisable = ""
            reopendisable = "disabled"
            closeddisable = "disabled"
            
            
        tbbat = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        sql = ""
        result = []
        transtatus = []
        if role.roleid == 3 or role.roleid == 2:
            sql = "select   t2.sts,   sum(cnt) procnt,  t2.status,   t2.details,   t2.icon,    count(t2.catid) catcnt from (	select t1.*,   sts.status,	   sts.details,	   sts.icon	from (	select cat.catid,   (case when trn.status is null then 7 else trn.status end) sts,   count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid   left join  tbtrans trn on pro.prodid = trn.productid	where trn.batchid = " + str(tbbat.batchid) + " or trn.batchid is null group by catid, sts ) t1 inner join tbstatus sts on t1.sts = sts.statusid where t1.sts = sts.statusid ) t2 group by t2.sts,  t2.status,  t2.details, t2.icon union select '10' sts, sum(procnt) procnt, 'Total' status, 'primary' details, 'bx bxl-firebase' icon, sum(catcnt) catcnt  from ( select   t2.sts,   sum(cnt) procnt,  t2.status,   t2.details,   t2.icon,    count(t2.catid) catcnt from (	select t1.*,   sts.status,	   sts.details,	   sts.icon	from (	select cat.catid,   (case when trn.status is null then 7 else trn.status end) sts,   count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid   left join  tbtrans trn on pro.prodid = trn.productid	where trn.batchid = " + str(tbbat.batchid) + " or trn.batchid is null group by catid, sts ) t1 inner join tbstatus sts on t1.sts = sts.statusid where t1.sts = sts.statusid ) t2 group by t2.sts,  t2.status,  t2.details, t2.icon ) t3"
        else:
            sql = "select '10' sts, sum(cntpro) cntpro, 'Total' status, 'primary' details, 'bx bxl-firebase' icon, sum(cntcat) cntcat from ( 	select sum(t1.cntpro) cntpro, count(t1.catid) cntcat from ( 	select count(pro.prodid) cntpro, cat.catid 	from tbcategories cat inner join tbproducts pro on pro.catid = cat.catid 	group by cat.catid 	) t1 ) t3"

        result = db.engine.execute(sql)
        for record in result:
            transtatus.append(record)

        
        

        return make_response(render_template('index.html', menus=menus, role=role,reopendisable=reopendisable,closeddisable=closeddisable, createdisable=createdisable, user=user, transtatus=transtatus, task="dashboard"), 200, headers)


class HistoryOfTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branchcode = session.get("branchcode")

        sql = "select trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status, count(trn.productid) cnt from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid where trn.branchcode = '"+ branchcode +"' and trn.authorizer is not null and trn.checker is not null group by trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status"
        result = db.engine.execute(sql)

        trans = []
        for record in result:
            trans.append(record)


        return make_response(render_template('index.html', menus=menus, role=role,trans=trans, task="historyoftrans"), 200, headers)


class BeverageTobacco(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 8
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="beveragetobacco"), 200, headers)


class Restaurant(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 9
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="restaurant"), 200, headers)



class ClothShoes(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 10
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="clothshoes"), 200, headers)



class Shipping(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 11
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="shipping"), 200, headers)

class Medicine(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 12
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="medicine"), 200, headers)



class Housing(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))

        category = 13
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

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton , task="housing"), 200, headers)


class SubmittedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        sql = ""
        record = []
        result = []
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        if batch is not None:
            
            sql = "select t1.*,  sts.status,  sts.details, sts.icon, men.functions	from ( select cat.catid,  cat.nameen,  (case when trn.status is null then 7 else trn.status end) sts,  count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid	where trn.batchid = " + str(batch.batchid) + " or trn.batchid is null group by catid,cat.nameen, sts ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid"
            result = db.engine.execute(sql)

        catlist = []
        for record in result:
            catlist.append(record)

        products = tbproducts

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

        # catlist = []
        trans = []
        sql = ""
        record = []
        result = []
        if batch is not None:
            # catlist = tbtrans.find_by_authorizecatbatchid(batch.batchid)
            trans = tbtrans
            sql = "select t1.*,  sts.status,  sts.details, sts.icon, men.functions	from ( select cat.catid,  cat.nameen,  (case when trn.status is null then 7 else trn.status end) sts,  count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid	where trn.batchid = " + str(batch.batchid) + " or trn.batchid is null group by catid,cat.nameen, sts ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid"
            result = db.engine.execute(sql)

        catlist = []
        for record in result:
            catlist.append(record)


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

        sql = "select t1.branchcode, t1.status, count(t1.status) as cnt, t1.statusname, t1.details from ( select trn.branchcode,trn.status,  pro.catid, count(pro.catid) as cnt, sts.status statusname, sts.details from tbtrans trn inner join tbstatus sts on sts.statusid = trn.status inner join tbproducts pro on trn.productid = pro.prodid  inner join tbbatches bat on bat.batchid = trn.batchid  where bat.statusid = 9  group by trn.branchcode,trn.status,  pro.catid ) as t1 group by t1.branchcode, t1.status order by t1.statusname "
        result = db.engine.execute(sql)

        transtatus = []
        for record in result:
            transtatus.append(record)

        return make_response(render_template('index.html', menus=menus, role=role, branches=branches, transtatus=transtatus, task="checkedtrans"), 200, headers)


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
        # catlist = []
        # if batch is not None:
        #     catlist = tbtrans.find_by_checkebatchid(batch.batchid)

        # trans = tbtrans
        print(batch)

        # catlist = []
        trans = []
        sql = ""
        record = []
        result = []
        if batch is not None:
            # catlist = tbtrans.find_by_authorizecatbatchid(batch.batchid)
            trans = tbtrans
            sql = "select t1.*,  sts.status,  sts.details, sts.icon, men.functions	from ( select cat.catid,  cat.nameen,  (case when trn.status is null then 7 else trn.status end) sts,  count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid	where trn.batchid = " + str(batch.batchid) + " or trn.batchid is null group by catid,cat.nameen, sts ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid"
            result = db.engine.execute(sql)

        catlist = []
        for record in result:
            catlist.append(record)

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans, branchcode=branchcode, task="checkedtransdetail"), 200, headers)


class CreateBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createbatch"), 200, headers)


class UpdateBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="updatebatch"), 200, headers)


class ViewBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="viewbatch"), 200, headers)


class CreateRoles(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createrole"), 200, headers)


class CreatePermission(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createpermission"), 200, headers)


class AttachedRolePermission(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="attachedrolepermission"), 200, headers)


class CreateStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="createstatus"), 200, headers)


class UpdateStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="updatestatus"), 200, headers)


class ViewStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        return make_response(render_template('index.html', menus=menus, role=role, task="viewstatus"), 200, headers)


class CreateUsers(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        testing = "Hello world!"

        return make_response(render_template('index.html', menus=menus, role=role, testing=testing, task="createusers"), 200, headers)


class UpdateUsers(Resource):
    @classmethod
    def get(cls, userid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        user = tbusers.find_by_userid(userid)

        return make_response(render_template('index.html', menus=menus, role=role, task="updateusers", user=user), 200, headers)


class ViewUsers(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        sql = 'select ROW_NUMBER() OVER(ORDER BY userid) as RN, usr.userid,usr.username,r.rolename,br.nameen,usr.email from tbusers usr left join tbbranches br on usr.branchcode=br.branchcode left join tbroles r on usr.roleid = r.roleid;'
        result = db.engine.execute(sql)

        user = []
        for record in result:
            user.append(record)
        print(user)

        return make_response(render_template('index.html', menus=menus, role=role, user=user, task="viewusers"), 200, headers)
