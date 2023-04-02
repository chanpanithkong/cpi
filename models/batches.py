from config.db import db

class tbbatches(db.Model):
    
    batchid = db.Column("batchid", db.Integer, primary_key = True)
    batch = db.Column(db.String)
    detail = db.Column(db.String)
    createdate = db.Column(db.DateTime)
    createby = db.Column(db.String)
    statusid = db.Column(db.Integer)
    
    def __init__(self, batchid=None, batch=None, detail=None, createdate=None, createby=None, statusid=None):
        self.batchid = batchid
        self.batch = batch
        self.detail = detail
        self.createdate = createdate
        self.createby = createby
        self.statusid = statusid
        
    @classmethod
    def find_by_batchid(cls, batchid) -> "tbbatches":
        return cls.query.filter_by(batchid=batchid).first()
    
    @classmethod
    def find_by_createbyopen(cls, createby) -> "tbbatches":
        filters = (db.Column("createby") == createby) & (db.Column("statusid") == 9)
        return cls.query.filter(filters).first()
