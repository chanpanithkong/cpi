from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from urllib.parse import quote 
# from config.db import db, app, api

from controls.branches import Branch, BranchesList, IndexPage


# from pagecontrollers.index import IndexPage, LoginPage, CitizenTableList, CitizentDataEntry, CitizentDataEdit, CitizentAddData, CitizentUpdateData, CitizenTableListPrint


# config file
app = Flask(__name__,template_folder='pages')
api = Api(app)

#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
#disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True
#localdb
url = quote('localhost')
port =  quote('3306')
username = quote('root')
password =  quote('$Cambodia__089$')
mysqldb = quote('dbcpi')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + url + ':' + port + '/' + mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True

db = SQLAlchemy(app)

# @app.route("/")
# def index():
#     return "Hello World"

# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html')


api.add_resource(IndexPage, "/")
api.add_resource(Branch, "/branch/<branchcode>")
api.add_resource(BranchesList, "/brancheslist")



if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
