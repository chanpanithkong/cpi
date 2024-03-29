from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api, json
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
from config.cypertext import cypertext
from schema.usersschema import UserSchema
from sqlalchemy import func

from languages import lang

import datetime
from pprint import pprint
from sqlalchemy import func

from config.userlogging import userlogging

class LoginPage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)


class UserLoginPage(Resource):
    @classmethod
    def post(cls):

        try:

            headers = {'Content-Type': 'text/html'}
            cyper= cypertext()
            clientid = request.remote_addr
            url = request.base_url
            userid = request.form.get('userid')
            password = request.form.get('password')
        
            user_data = tbusers.find_by_userid(userid)
            if user_data is not None:
                if cyper.issame(password,user_data.key,user_data.password):
                    session['userid'] = user_data.userid
                    session['roleid'] = user_data.roleid
                    session['username'] = user_data.username
                    session['branchcode'] = user_data.branchcode
                    session['details'] = user_data.details
                    session['languages'] = user_data.languages
                    userlogging.degbuglog(clientid, url,userid + " : login")
                    return redirect("/dashboard")
                else:
                    userlogging.degbuglog(clientid, url,userid + " : is wrong password")
            else:
                userlogging.degbuglog(clientid, url,userid + " : is not exist")
            return make_response(render_template('login.html', data="Wrong userid and password !!!"), 200, headers)
            
        except Exception as err:
            # userlogging.degbuglog(clientid, url, err)
            db.session.rollback()
            raise
	        # return make_response(render_template('login.html', data=err), 200, headers)


class Logout(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        session.clear()
        db.session.close()
        return make_response(render_template('login.html'), 200, headers)


class HomePage(Resource):
    @classmethod
    def get(cls):
        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
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
            createdisable = ""
            reopendisable = "disabled"
            closeddisable = "disabled"
            
            
        tbbat = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        
        # sql = "select '10' sts, sum(cntpro) cntpro, 'Total' status, 'primary' details, 'bx bxl-firebase' icon, sum(cntcat) cntcat from ( 	select sum(t1.cntpro) cntpro, count(t1.catid) cntcat from ( 	select count(pro.prodid) cntpro, cat.catid 	from tbcategories cat inner join tbproducts pro on pro.catid = cat.catid 	group by cat.catid 	) t1 ) t3"
        sql = " select '10' sts, t3.procnt procnt, 'Total' status, 'primary' details, 'bx bxl-firebase' icon, (select count(*) from tbcategories cat where cat.parentid = 0) catcnt from ( select   t2.sts,   sum(cnt) procnt,  t2.status,   t2.details,   t2.icon,    count(t2.catid) catcnt  from (	select t1.*,   sts.status,	   sts.details,	   sts.icon	from (	select cat.catid,    '10'  sts,    count(pro.prodid) cnt from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid group by cat.catid, '10' ) t1 inner join tbstatus sts on t1.sts = sts.statusid where t1.sts = sts.statusid ) t2 group by t2.sts,  t2.status,  t2.details, t2.icon ) t3 "
                
        result = []
        transtatus = []
        
        if tbbat is not None :
            if role.roleid == 3 or role.roleid == 4:
                sql = " select '10' sts, "\
                      " (select count(pro.prodid) from tbproducts pro) procnt, "\
                      " 'Total' status, 'primary' details, 'bx bxl-firebase' icon, "\
                      " (select count(cat.catid) from tbcategories cat where cat.parentid = 0) catcnt "\
                      " from ( select   t2.sts,   "\
                      "         sum(cnt) procnt,  "\
                      "         t2.status,   "\
                      "         t2.details,   "\
                      "         t2.icon,    "\
                      "         count(t2.catid) catcnt  "\
                      " from (	select t1.*,   "\
                      "                  sts.status,	   "\
                      "                   sts.details,	   "\
                      "                   sts.icon	"\
                      "           from (	select cat.catid,    "\
                      "                           '10'  sts,    "\
                      "                           count(pro.prodid) cnt "\
                      "                   from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid where cat.parentid = 0 group by cat.catid, '10' "\
                      "                   ) t1 inner join tbstatus sts on t1.sts = sts.statusid where t1.sts = sts.statusid "\
                      "           ) t2 group by t2.sts,  t2.status,  t2.details, t2.icon ) t3 "
                    
                    # pending status but it is not correct yet
                    #   " union "
                      
            else:
                sql = " select '10' sts, "\
                      "  sum(procnt) procnt, "\
                      "  'Total' status, 'primary' details, "\
                      "  'bx bxl-firebase' icon, "\
                      "  7 catcnt "\
                      " from ( select   t2.sts,   "\
                      "              sum(cnt) procnt,  "\
                      "              t2.status,   "\
                      "              t2.details,   "\
                      "              t2.icon,    "\
                      "              count(t2.catid) catcnt  "\
                      "  from (  select t1.*,   "\
                      "                  sts.status,     "\
                      "                  sts.details,     "\
                      "                  sts.icon  "\
                      "          from (  select cat.catid,    "\
                      "                          '10'  sts,    "\
                      "                          count(pro.prodid) cnt "\
                      "                  from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid group by cat.catid, '10' "\
                      "                  ) t1 inner join tbstatus sts on t1.sts = sts.statusid where t1.sts = sts.statusid "\
                      "          ) t2 group by t2.sts,  t2.status,  t2.details, t2.icon "\
                      "  ) t3 "
                      
                
        result = db.engine.execute(sql)
        for record in result:
            transtatus.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')

        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access Dashboard")
        
        return make_response(render_template('index.html', menus=menus, role=role,reopendisable=reopendisable,closeddisable=closeddisable, createdisable=createdisable, user=user, transtatus=transtatus,languages=languages,locals=locals, task="dashboard",main=""), 200, headers)


class HistoryOfTrans(Resource):
    @classmethod
    def get(cls, page):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branchcode = session.get("branchcode")

        page = int(page)
        if page <= 1:
            page = 1

        limitpage = 10
        rowdisplay = (page-1) * limitpage

        sql = " select trn.branchcode, "\
              " trn.submitter, "\
              " trn.authorizer, "\
              " trn.checker, "\
              " sts.status, "\
              " count(trn.productid) cnt, "\
              " to_date(trn.submitdate) checkdate, "\
              " trn.batchid  "\
              " from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid "\
              " group by trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status,to_date(trn.submitdate), trn.batchid "\
              " order by trn.batchid desc "\
              " OFFSET " + str(rowdisplay) +" ROWS FETCH NEXT " + str(limitpage) + " ROWS ONLY"
        sqlcount = " select count(t1.batchid) cnt "\
                   " from ( select trn.batchid from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid "\
                   " group by trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status,to_date(trn.checkerdate), trn.batchid) t1 "
        if role.roleid == 3 or role.roleid == 4:
            sql = " select trn.branchcode, "\
                  " trn.submitter, "\
                  " trn.authorizer, "\
                  " trn.checker, "\
                  " sts.status, "\
                  " count(trn.productid) cnt, "\
                  " to_date(trn.submitdate) checkdate, "\
                  " trn.batchid "\
                  " from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid  "\
                  " where trn.branchcode = '"+ branchcode +"' "\
                  " group by trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status,to_date(trn.submitdate), trn.batchid "\
                  " OFFSET " + str(rowdisplay) +" ROWS FETCH NEXT " + str(limitpage) + " ROWS ONLY"

            sqlcount = " select count(t1.batchid) cnt "\
                       " from ( select trn.batchid from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid  "\
                       " where trn.branchcode = '"+ branchcode +"' "\
                       " group by trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status,to_date(trn.checkerdate), trn.batchid) t1 "
            # sql = "select trn.branchcode, trn.submitter, trn.authorizer, trn.checker, sts.status, 10 cnt, date(trn.checkerdate) checkdate from tbtrans trn inner join tbstatus sts on trn.status = sts.statusid where trn.branchcode = '001' limit " + str(rowdisplay) + "," + str(limitpage) 
        
        resultcount = db.engine.execute(sqlcount) 
        result = db.engine.execute(sql) 

        pagelist = []        
        for rowcount in resultcount:
            for i in range(0,rowcount[0],limitpage):
                pagelist.append(int(i/limitpage)+1)

        
        trans = []
        for record in result:
            trans.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access HistoryOfTrans")

        return make_response(render_template('index.html', menus=menus, role=role,trans=trans,pagelist=pagelist,page=page,languages=languages,locals=locals, task="historyoftrans",main=""), 200, headers)


class TransactionDetails(Resource):
    @classmethod
    def get(cls, batchid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        branchcode = session.get("branchcode")
        batchid = int(batchid)

        sql = "select  cat.nameen catnameen, cat.namekh catnamekh, trn.productid, pro.nameen pronameen,pro.namekh pronamekh, pro.uniten,pro.unitkh, trn.price, trn.weight, trn.submitter, trn.submitdate, sts.status, trn.branchcode,trn.authorizer, trn.authorizedate, trn.checker, trn.checkerdate from tbtrans trn inner join tbproducts pro on pro.prodid = trn.productid inner join tbcategories cat on cat.catid = pro.catid inner join tbstatus sts on trn.status = sts.statusid  where trn.batchid = " + str(batchid) + " order by prodid "
                      
        result = db.engine.execute(sql) 

        trans = []
        for record in result:
            trans.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        return make_response(render_template('index.html', menus=menus, role=role,batchid=batchid,trans=trans,languages=languages,locals=locals, task="transactiondetails",main=""), 200, headers)


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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access BeverageTobacco")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton, languages=languages, locals=locals , task="beveragestobacco",main=""), 200, headers)


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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')

        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access Restaurant")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton,languages=languages,locals=locals , task="restaurant",main=""), 200, headers)



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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access ClothShoes")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton, languages=languages, locals=locals , task="clothesshoes",main=""), 200, headers)



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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access Shipping")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton, languages=languages, locals=locals , task="shipping",main=""), 200, headers)

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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access Medicine")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton, languages=languages, locals=locals , task="medicine",main=""), 200, headers)



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

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access Housing")

        return make_response(render_template('index.html', menus=menus, role=role, productlist=productlist,tbtrans=tbtrans,batch=batch, disabled=disabled, isbutton=isbutton, languages=languages, locals=locals , task="housing",main=""), 200, headers)


class SubmittedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        sql = ""
        
        result = []
        result1 = []
        batch = tbbatches.find_by_branchbatchopen(session.get("branchcode"))
        if batch is not None:
            
            sql = ("	select t1.catid,  " +
                  "	t1.nameen, " +
                  "	sta.statusid,  "  + 
                  "	t1.procnt,  "  +
                  "	sta.status,   "  +
                  "	sta.details,  "  +
                  "	sta.icon,  "  +
                  "	t1.functions, "  +
                  "	t1.namekh, "  +
                  "	(select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, "\
                  "	(select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh  "\
                  "	from ( select cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7 sts ,   " +
                  "	        count(pro.prodid) procnt, " +
                  "	        men.functions  " +
                  "	from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  " +
                  "	inner join tbmenus men on cat.catid = men.iscat  group by cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7, " +
                  "	        men.functions 	" +
                  "	) t1 inner join tbstatus sta on t1.sts = sta.statusid " )
            
            result = db.engine.execute(sql)

            sql1 = (" select t1.catid, " +
                   "  t1.nameen, " +
                   "  t1.sts, " +
                   "  t1.cnt,  " +
                   "  sts.status,  " +
                   "  sts.details, " +
                   "  sts.icon, " +
                   "  men.functions, " +
                   "  t1.namekh, " +
                   "  (select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, " +
                   "  (select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh	" +
                   "  from ( select  cat.catid,  cat.nameen,cat.namekh, " +
                   "          (case when trn.status is null then 7 else trn.status end) sts, " +  
                   "          count(pro.prodid) cnt " +
                   "  from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid " +	
                   "  where trn.batchid = " + str(batch.batchid) + " group by cat.catid, cat.nameen, cat.namekh, (case when trn.status is null then 7 else trn.status end) " +
                   "  ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid" )

            result1 = db.engine.execute(sql1)

        catlist1 = []
        catlist2 = []
        for record in result:
            catlist1.append(record)

        for record in result1:
            catlist2.append(record)

        catlist = []
        for data1 in catlist1:
            data = []
            for data2 in catlist2:
                if data1[0] == data2[0]:
                    data.append(data2)
            if len(data) > 0:
                catlist.append(data[0])
            else:
                catlist.append(data1)
            
        products = tbproducts
        trans = tbtrans
        category = tbcategories

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access SubmittedTrans")

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist,category=category, products=products, batch=batch, trans=trans,languages=languages,locals=locals, task="submittedtrans",main=""), 200, headers)


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
        result1 = []
        
        if batch is not None:
            # catlist = tbtrans.find_by_authorizecatbatchid(batch.batchid)
            trans = tbtrans

            sql = ("	select t1.catid,  " +
                  "	t1.nameen, " +
                  "	sta.statusid,  "  + 
                  "	t1.procnt,  "  +
                  "	sta.status,   "  +
                  "	sta.details,  "  +
                  "	sta.icon,  "  +
                  "	t1.functions, "  +
                  "	t1.namekh, "  +
                  "	(select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, "\
                  "	(select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh  "\
                  "	from ( select cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7 sts ,   " +
                  "	        count(pro.prodid) procnt, " +
                  "	        men.functions  " +
                  "	from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  " +
                  "	inner join tbmenus men on cat.catid = men.iscat  group by cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7, " +
                  "	        men.functions 	" +
                  "	) t1 inner join tbstatus sta on t1.sts = sta.statusid " )
            
            result = db.engine.execute(sql)

            sql1 = (" select t1.catid, " +
                   "  t1.nameen, " +
                   "  t1.sts, " +
                   "  t1.cnt,  " +
                   "  sts.status,  " +
                   "  sts.details, " +
                   "  sts.icon, " +
                   "  men.functions, " +
                   "  t1.namekh, " +
                   "  (select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, " +
                   "  (select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh	" +
                   "  from ( select  cat.catid,  cat.nameen,cat.namekh, " +
                   "          (case when trn.status is null then 7 else trn.status end) sts, " +  
                   "          count(pro.prodid) cnt " +
                   "  from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid " +	
                   "  where trn.batchid = " + str(batch.batchid) + " group by cat.catid, cat.nameen, cat.namekh, (case when trn.status is null then 7 else trn.status end) " +
                   "  ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid" )

            result1 = db.engine.execute(sql1)

        catlist1 = []
        catlist2 = []
        for record in result:
            catlist1.append(record)

        for record in result1:
            catlist2.append(record)

        catlist = []
        for data1 in catlist1:
            data = []
            for data2 in catlist2:
                if data1[0] == data2[0]:
                    data.append(data2)
            if len(data) > 0:
                catlist.append(data[0])
            else:
                catlist.append(data1)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 


        userlogging.degbuglog(clientid, url, userid + " : access AuthorizedTrans")

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans,languages=languages,locals=locals, task="authorizedtrans",main=""), 200, headers)


class SessionDuration(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))
        
        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]


        userlogging.degbuglog(clientid, url, userid + " : access Session")

        return make_response(render_template('index.html', menus=menus, role=role, languages=languages, locals=locals, task="sessionduration",main="session"), 200, headers)

class BranchSessionDetails(Resource):
    @classmethod
    def get(cls, branchcode, page):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        page = int(page)
        if page <= 1:
            page = 1

        limitpage = 10
        rowdisplay = (page-1) * limitpage

        sql = " SELECT * FROM tbbatches bat where bat.branch = "+ branchcode +" order by bat.batchid desc "\
              " OFFSET " + str(rowdisplay) +" ROWS FETCH NEXT " + str(limitpage) + " ROWS ONLY"
        sqlcount = "SELECT count(*) FROM tbbatches bat where bat.branch = " + branchcode + " order by bat.batchid desc" 
       
        resultcount = db.engine.execute(sqlcount) 
        result = db.engine.execute(sql) 

        pagelist = []        
        for rowcount in resultcount:
            for i in range(0,rowcount[0],limitpage):
                pagelist.append(int(i/limitpage)+1)

        
        trans = []
        for record in result:
            trans.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access HistoryOfTrans")

        return make_response(render_template('index.html', menus=menus, role=role,trans=trans,branchcode=branchcode,pagelist=pagelist,page=page,languages=languages,locals=locals, task="sessiondetails",main="session"), 200, headers)


class UpdateBranch(Resource):
    @classmethod
    def get(cls, branchcode):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branch = tbbranches.find_by_branchcode(branchcode)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]


        userlogging.degbuglog(clientid, url, userid + " : access Session")

        return make_response(render_template('index.html', menus=menus, role=role, languages=languages, locals=locals,branch=branch, task="updatebranch",main="branchmanagement"), 200, headers)


class CreateBranch(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]


        userlogging.degbuglog(clientid, url, userid + " : access Session")

        return make_response(render_template('index.html', menus=menus, role=role, languages=languages, locals=locals, task="createbranch",main="branchmanagement"), 200, headers)


class ViewBranches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu
        
        role = tbroles.find_by_roleid(session.get('roleid'))

        branches = tbbranches.query.all()

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]


        userlogging.degbuglog(clientid, url, userid + " : access Session")

        return make_response(render_template('index.html', menus=menus,  role=role, languages=languages, locals=locals,branches=branches, task="viewbranches",main="branchmanagement"), 200, headers)


class BranchSession(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branches = tbbranches.getallbranches()

        batch = tbbatches

        sql = "select t1.branchcode, "\
              " t1.status, "\
              " count(t1.status) as cnt, "\
              " t1.statusname, "\
              " t1.details "\
              " from ( select trn.branchcode, "\
              "           trn.status,  "\
              "           pro.catid, "\
              "           count(pro.catid) as cnt, "\
              "           sts.status statusname, "\
              "           sts.details "\
              "       from tbtrans trn inner join tbstatus sts on sts.statusid = trn.status "\
              "                       inner join tbproducts pro on trn.productid = pro.prodid  "\
              "                       inner join tbbatches bat on bat.batchid = trn.batchid  "\
              "       where bat.statusid = 9 and sts.statusid in (3,11,13) group by trn.branchcode,trn.status,  pro.catid, sts.status ,  sts.details "\
              "   ) t1 group by t1.branchcode, t1.status, t1.statusname, t1.details  order by t1.statusname "
        result = db.engine.execute(sql)

        transtatus = []
        for record in result:
            transtatus.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]


        userlogging.degbuglog(clientid, url, userid + " : access Session")

        return make_response(render_template('index.html', menus=menus, role=role,batch=batch, branches=branches, transtatus=transtatus,languages=languages, locals=locals, task="branchsession",main="session"), 200, headers)


class CheckedTrans(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}
        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        branches = tbbranches.getallbranches()

        sql = "select t1.branchcode, "\
              " t1.status, "\
              " count(t1.status) as cnt, "\
              " t1.statusname, "\
              " t1.details "\
              " from ( select trn.branchcode, "\
              "           trn.status,  "\
              "           pro.catid, "\
              "           count(pro.catid) as cnt, "\
              "           sts.status statusname, "\
              "           sts.details "\
              "       from tbtrans trn inner join tbstatus sts on sts.statusid = trn.status "\
              "                       inner join tbproducts pro on trn.productid = pro.prodid  "\
              "                       inner join tbbatches bat on bat.batchid = trn.batchid  "\
              "       where bat.statusid = 9 and sts.statusid in (3,11,13) group by trn.branchcode,trn.status,  pro.catid, sts.status ,  sts.details "\
              "   ) t1 group by t1.branchcode, t1.status, t1.statusname, t1.details  order by t1.statusname "
        
        result = db.engine.execute(sql)

        transtatus = []
        for record in result:
            transtatus.append(record)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        pprint(transtatus)

        userlogging.degbuglog(clientid, url, userid + " : access CheckedTrans")

        return make_response(render_template('index.html', menus=menus, role=role, branches=branches, transtatus=transtatus,languages=languages, locals=locals, task="checkedtrans",main=""), 200, headers)


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
        
        # catlist = []
        trans = []
        sql = ""
        record = []
        result = []
        result1 = []
        if batch is not None:
            # catlist = tbtrans.find_by_authorizecatbatchid(batch.batchid)
            trans = tbtrans
            sql = ("	select t1.catid,  " +
                  "	t1.nameen, " +
                  "	sta.statusid,  "  + 
                  "	t1.procnt,  "  +
                  "	sta.status,   "  +
                  "	sta.details,  "  +
                  "	sta.icon,  "  +
                  "	t1.functions, "  +
                  "	t1.namekh, "  +
                  "	(select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, "\
                  "	(select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh  "\
                  "	from ( select cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7 sts ,   " +
                  "	        count(pro.prodid) procnt, " +
                  "	        men.functions  " +
                  "	from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  " +
                  "	inner join tbmenus men on cat.catid = men.iscat  group by cat.catid,  " +
                  "	        cat.nameen, " +
                  "	        cat.namekh, " +
                  "	        7, " +
                  "	        men.functions 	" +
                  "	) t1 inner join tbstatus sta on t1.sts = sta.statusid " )
            
            result = db.engine.execute(sql)

            sql1 = (" select t1.catid, " +
                   "  t1.nameen, " +
                   "  t1.sts, " +
                   "  t1.cnt,  " +
                   "  sts.status,  " +
                   "  sts.details, " +
                   "  sts.icon, " +
                   "  men.functions, " +
                   "  t1.namekh, " +
                   "  (select  cat.nameen parenten from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parenten, " +
                   "  (select  cat.namekh parentkh from tbcategories cat where cat.catid  = ( select cat.parentid from tbcategories cat where cat.parentid != 0 and cat.catid = t1.catid)) parentkh	" +
                   "  from ( select  cat.catid,  cat.nameen,cat.namekh, " +
                   "          (case when trn.status is null then 7 else trn.status end) sts, " +  
                   "          count(pro.prodid) cnt " +
                   "  from tbcategories cat inner join tbproducts pro on cat.catid = pro.catid  left join  tbtrans trn on pro.prodid = trn.productid " +	
                   "  where trn.batchid = " + str(batch.batchid) + " group by cat.catid, cat.nameen, cat.namekh, (case when trn.status is null then 7 else trn.status end) " +
                   "  ) t1 inner join tbstatus sts on t1.sts = sts.statusid inner join tbmenus men on t1.catid = men.iscat where t1.sts = sts.statusid order by t1.catid" )

            result1 = db.engine.execute(sql1)

        catlist1 = []
        catlist2 = []
        for record in result:
            catlist1.append(record)

        for record in result1:
            catlist2.append(record)

        catlist = []
        for data1 in catlist1:
            data = []
            for data2 in catlist2:
                if data1[0] == data2[0]:
                    data.append(data2)
            if len(data) > 0:
                catlist.append(data[0])
            else:
                catlist.append(data1)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages]

        userlogging.degbuglog(clientid, url, userid + " : access CheckedTransDetails")

        return make_response(render_template('index.html', menus=menus, role=role, catlist=catlist, products=products, batch=batch, trans=trans, branchcode=branchcode,languages=languages,locals=locals, task="checkedtransdetail",main=""), 200, headers)


class CreateBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu

        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access CreateBatches")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="createbatch",main=""), 200, headers)


class UpdateBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access UpdateBatches")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="updatebatch",main=""), 200, headers)


class ViewBatches(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access ViewBatches")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="viewbatch",main=""), 200, headers)


class UpdateRoles(Resource):
    @classmethod
    def get(cls,roleid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        tb_role = tbroles.find_by_roleid(roleid)

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access UpdateRoles")

        return make_response(render_template('index.html', menus=menus, role=role,tb_role=tb_role,languages= languages, locals=locals, task="updateroles",main="role"), 200, headers)




class CreateRoles(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access CreateRoles")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="createroles",main="role"), 200, headers)


class CreatePermission(Resource):
    @classmethod
    def get(cls,roleid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        # batch = tbbatches.find_by_branchbatchopen("001")

        sql = ""
        record = []
        result = []
        # if batch is not None:
        sql = "select * from tbmenus men where men.parentid = 0"
        result = db.engine.execute(sql)

        menulist = []
        for record in result:
            menulist.append(record)

        tb_role = tbroles.find_by_roleid(roleid)
        tb_menus = tbmenus
        
        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access CreatePermission")

        return make_response(render_template('index.html', menus=menus, role=role,tb_role=tb_role,menulist=menulist,tb_menus= tb_menus,languages=languages,locals=locals,  task="createpermission",main="role"), 200, headers)


class AttachedRolePermission(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        tb_roles = tbroles

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access AttachedRolePermission")

        return make_response(render_template('index.html', menus=menus, role=role,tb_role=tb_roles,languages=languages,locals=locals, task="attachedrolepermission",main="role"), 200, headers)


class CreateStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access CreateStatus")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="createstatus",main=""), 200, headers)


class UpdateStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access UpdateStatus")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="updatestatus",main=""), 200, headers)


class ViewStatus(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access ViewStatus")

        return make_response(render_template('index.html', menus=menus, role=role,languages=languages,locals=locals, task="viewstatus",main=""), 200, headers)


class CreateUsers(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        tb_roles = tbroles
        tb_branches = tbbranches

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access CreateUsers")

        return make_response(render_template('index.html', menus=menus, role=role, tb_roles=tb_roles, tb_branches=tb_branches,languages=languages,locals=locals, task="createusers",main="users"), 200, headers)


class UpdateUsers(Resource):
    @classmethod
    def get(cls, userid):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        filters = (tbusers.userid == userid)
        user = db.session.query(tbusers,tbroles, tbbranches).filter(tbusers.roleid == tbroles.roleid).filter(tbusers.branchcode == tbbranches.branchcode).filter(filters).all()
        tb_roles = tbroles
        tb_branches = tbbranches

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access UpdateUsers")

        return make_response(render_template('index.html', menus=menus, role=role,tb_roles=tb_roles, tb_branches=tb_branches, user=user,languages=languages,locals=locals, task="updateusers",main="users"), 200, headers)


class ViewUsers(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        user = db.session.query(tbusers,tbroles, tbbranches).filter(tbusers.roleid == tbroles.roleid).filter(tbusers.branchcode == tbbranches.branchcode).filter(tbusers.status == 5).all()

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 


        userlogging.degbuglog(clientid, url, userid + " : access ViewUsers")

        return make_response(render_template('index.html', menus=menus, role=role, user=user,languages=languages,locals=locals, task="viewusers",main="users"), 200, headers)
    

class ViewDeleteUsers(Resource):
    @classmethod
    def get(cls):

        if not session.get("userid"):
            return redirect("/login")

        headers = {'Content-Type': 'text/html'}

        menus = tbrolemenu
        role = tbroles.find_by_roleid(session.get('roleid'))
        user = db.session.query(tbusers,tbroles, tbbranches).filter(tbusers.roleid == tbroles.roleid).filter(tbusers.branchcode == tbbranches.branchcode).filter(tbusers.status == 6).all()

        clientid = request.remote_addr
        url = request.base_url
        userid = session.get('userid')
        languages = session.get('languages')
        locals = lang[languages] 

        userlogging.degbuglog(clientid, url, userid + " : access ViewUsers")

        return make_response(render_template('index.html', menus=menus, role=role, user=user,languages=languages,locals=locals, task="viewdeleteusers",main="users"), 200, headers)