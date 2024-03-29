from config.db import db
from sqlalchemy import desc

class tbbatches(db.Model):
    
    batchid = db.Column("batchid", db.Integer, primary_key = True)
    batch = db.Column(db.String)
    detail = db.Column(db.String)
    createdate = db.Column(db.DateTime)
    createby = db.Column(db.String)
    branch = db.Column(db.String)
    statusid = db.Column(db.Integer)
    
    def __init__(self, batchid=None, batch=None, detail=None, createdate=None, createby=None, branch=None, statusid=None):
        self.batchid = batchid
        self.batch = batch
        self.detail = detail
        self.createdate = createdate
        self.createby = createby
        self.branch = branch
        self.statusid = statusid
        
    @classmethod
    def find_by_batchid(cls, batchid) -> "tbbatches":
        return cls.query.filter_by(batchid=batchid).first()
    
    @classmethod
    def find_by_createbyopen(cls, createby) -> "tbbatches":
        filters = (db.Column("createby") == createby) & (db.Column("statusid") == 9)
        return cls.query.filter(filters).first()

    @classmethod
    def find_by_branch(cls, branch) -> "tbbatches":
        filters = (db.Column("branch") == branch)
        return cls.query.filter(filters).first()
    @classmethod
    def find_by_branchbatchopenlist(cls, branch) -> "tbbatches":
        filters = (db.Column("branch") == branch) & (db.Column("statusid") == 9)
        return cls.query.filter(filters).order_by(desc(db.Column("batchid"))).all()
    
    @classmethod
    def find_by_batchopen(cls) -> "tbbatches":
        filters = (db.Column("statusid") == 9)
        return cls.query.filter(filters).all()
    @classmethod
    def find_by_branchbatchopen(cls, branch) -> "tbbatches":
        filters = (db.Column("branch") == branch) & (db.Column("statusid") == 9)
        return cls.query.filter(filters).order_by(desc(db.Column("batchid"))).first()
    @classmethod
    
    def find_by_branchidbatchopen(cls, batchid) -> "tbbatches":
        filters = (db.Column("batchid") == batchid) & (db.Column("statusid") == 9)
        return cls.query.filter(filters).first()
    @classmethod
    def find_by_branchidbatchclose(cls, batchid) -> "tbbatches":
        filters = (db.Column("batchid") == batchid) & (db.Column("statusid") == 8)
        return cls.query.filter(filters).first()

    @classmethod
    def find_by_branchbatchclose(cls, branch) -> "tbbatches":
        filters = (db.Column("branch") == branch) & (db.Column("statusid") == 8)
        return cls.query.filter(filters).order_by(desc(db.Column("batchid"))).first()