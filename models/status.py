from config.db import db

class tbstatus(db.Model):
    
    statusid = db.Column("statusid", db.Integer, primary_key = True)
    status = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, statusid, status, details):
        self.statusid = statusid
        self.status = status
        self.details = details
        
        
    @classmethod
    def find_by_statusid(cls, statusid) -> "tbstatus":
        return cls.query.filter_by(statusid=statusid).first()
