import os
from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from urllib.parse import quote 
from flask_cors import CORS
# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)
CORS(app) 
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
