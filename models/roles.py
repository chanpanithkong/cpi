from config.db import db

class tbroles(db.Model):
    
    roleid = db.Column("roleid", db.Integer, primary_key = True)
    rolename = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, roleid=None, rolename=None, details=None):
        self.roleid = roleid
        self.rolename = rolename
        self.details = details
        
        
    @classmethod
    def find_by_roleid(cls, roleid) -> "tbroles":
        result = None
        if len(cls.query.filter_by(roleid=roleid).all()) > 0:
            result = cls.query.filter_by(roleid=roleid).first()
        return result
