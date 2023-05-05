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

from schema.usersschema import UserSchema

import datetime
from pprint import pprint
from sqlalchemy import func


class CreateUser(Resource):
    @classmethod
    def post(cls):
        try:
            print(1)
            msg = "fail"
            data = json.loads(request.data)
            print(1)
            if data['userrequest'] == "createuser":
                print(data['data'])
                print(1)
                usr = tbusers()
                print(1)
                usr.userid = data['data']['usrid']
                print(1)
                usr.password = data['data']['password']
                print(1)
                usr.roleid = data['data']['role']
                print(1)
                usr.username = data['data']['fname']
                print(1)
                usr.gender = data['data']['gender']
                print(1)
                usr.branchcode = data['data']['branch']
                print(1)
                usr.details = data['data']['detail']
                print(1)
                usr.email = data['data']['email']
                print(usr)
                print(1)
                db.session.add(usr)
                print(1)
                db.session.commit()
                print(1)
                msg = "create sucessfully"

            else:
                print("fail")

            return {"msg": msg}

        except Exception as err:
            return {"msg": err}
