import os
from flask import Flask, request, json, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from dbinfo import dbconfig, dboracleconfig
import cx_Oracle
from flask_cors import CORS
import logging
from flask_session import Session

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)

api = Api(app)

log = logging.getLogger('werkzeug')
log.disabled = True
    
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
sess = Session(app)

#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
#disable message error in internal system
# app.config['PROPAGATE_EXCEPTIONS'] = True
#localdb

# MySQL closes it self the stale connections (8 hours of inactivity by default). You can set the pool recycle to solve this problem.
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 10
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = 10
# app.config["SQLALCHEMY_POOL_SIZE"] = 10


#oracle connection url 
# cx_Oracle.init_oracle_client(lib_dir=r"C:/instantclient_21_10")
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@' + cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string.format(
  username=dboracleconfig.username,
  password=dboracleconfig.password,
  hostname=dboracleconfig.url,
  port=dboracleconfig.port,
  service_name=dboracleconfig.db
)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbconfig.username + ':' + dbconfig.password + '@' + dbconfig.url + ':' + dbconfig.port + '/' + dbconfig.mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['CORS_HEADERS'] = 'Content-Type'
DEBUG = False

db = SQLAlchemy(app)

# CORS(app, resources={r"/*": {"origins": "*"}})
