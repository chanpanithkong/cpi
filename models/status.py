from config.db import db

class tbstatus(db.Model):
    
    statusid = db.Column("statusid", db.Integer, primary_key = True)
    status = db.Column(db.String)
    details = db.Column(db.String)
    icon = db.Column(db.String)
    
    def __init__(self, statusid=None, status=None, details=None, icon=None):
        self.statusid = statusid
        self.status = status
        self.details = details
        self.icon = icon
        
        
    @classmethod
    def find_by_statusid(cls, statusid) -> "tbstatus":
        return cls.query.filter_by(statusid=statusid).first()
