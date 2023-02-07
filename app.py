from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from urllib.parse import quote 
# from config.db import db, app, api


# from controls.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
# from controls.authorities import Authorities,AuthoritiesList,  AuthoritiesLogin
# from controls.citizens import Citizens,CitizensList,InsertCitizen,DeleteCitizen,UpdateCitizen,UpdateCitizenParty, CitizensByName, CitizensCountByParty
# from controls.communes import Communes,CommunesList
# from controls.districts import Districts,DistrictsList
# from controls.parties import Parties,PartiesList
# from controls.provinces import Provinces,ProvincesList
# from controls.roles import Role,RoleList
# from controls.userroles import UserRoles,UserRolesList
# from controls.villages import Villages,VillagesList

# from pagecontrollers.index import IndexPage, LoginPage, CitizenTableList, CitizentDataEntry, CitizentDataEdit, CitizentAddData, CitizentUpdateData, CitizenTableListPrint


# config file
app = Flask(__name__,template_folder='pages')
api = Api(app)

#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
#disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True
# mysql db connect
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$Cambodia__089$@localhost:3306/dbpartychecklist'

#localdb
url = quote('localhost')
port =  quote('3306')
username = quote('root')
password =  quote('$Cambodia__089$')
mysqldb = quote('dbpartychecklist')

# bongsithdb
# url = quote('13.230.198.156')
# port =  quote('3306')
# username = quote('phanith')
# password =  quote('@Phan1tH@')
# mysqldb = quote('phanith')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + url + ':' + port + '/' + mysqldb

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CLEARDB_DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True
db = SQLAlchemy(app)

# @app.route("/")
# def index():
#     return "Hello World"


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html')

# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST


# jwt token
# api.add_resource(WsUserLogin, "/wslogin")
# api.add_resource(WsTokenRefresh, "/wsrefresh")
# api.add_resource(WsUserLogout, "/wslogout")

# api.add_resource(IndexPage, "/")
# api.add_resource(LoginPage, "/login")
# api.add_resource(CitizenTableList, "/citizentablelist")
# api.add_resource(CitizenTableListPrint, "/citizentablelistprint")

# api.add_resource(CitizentDataEntry, "/citizendataentry")
# api.add_resource(CitizentAddData, "/citizenadddata")

# api.add_resource(CitizentDataEdit, "/citizendataedit/<cid>")
# api.add_resource(CitizentUpdateData, "/citizenupdatedata")




if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
