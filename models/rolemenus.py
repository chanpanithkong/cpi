from config.db import db

class tbrolemenu(db.Model):
    
    roleid = db.Column("roleid", db.Integer, primary_key = True)
    menuid = db.Column("menuid", db.Integer, primary_key = True)
    details = db.Column(db.String)
    createby = db.Column(db.String)
    createdate = db.Column(db.DateTime)
    statusid = db.Column(db.Integer)
    
    
    def __init__(self, roleid, menuid, details, createby, createdate, statusid):
        self.roleid = roleid
        self.menuid = menuid
        self.details = details
        self.createby = createby
        self.createdate = createdate
        self.statusid = statusid
        
        
    @classmethod
    def find_by_roleid(cls, roleid) -> "tbrolemenu":
        return cls.query.filter_by(roleid=roleid).order_by(tbrolemenu.menuid).all()

