from config.db import db

class tbstatus(db.Model):
    
    statusid = db.Column("statusid", db.Integer, primary_key = True)
    statusen = db.Column(db.String)
    statuskh = db.Column(db.String)
    details = db.Column(db.String)
    icon = db.Column(db.String)
    
    def __init__(self, statusid=None, statusen=None,statuskh=None, details=None, icon=None):
        self.statusid = statusid
        self.statusen = statusen
        self.statuskh = statuskh
        self.details = details
        self.icon = icon
        
        
    @classmethod
    def find_by_statusid(cls, statusid) -> "tbstatus":
        return cls.query.filter_by(statusid=statusid).first()
