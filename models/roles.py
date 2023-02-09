from config.db import db

class tbroles(db.Model):
    
    roleid = db.Column("roleid", db.Integer, primary_key = True)
    rolename = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, roleid, rolename, details):
        self.roleid = roleid
        self.rolename = rolename
        self.details = details
        
        
    @classmethod
    def find_by_roleid(cls, roleid) -> "tbroles":
        return cls.query.filter_by(roleid=roleid).first()
