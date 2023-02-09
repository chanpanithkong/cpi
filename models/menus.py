from config.db import db

class tbmenus(db.Model):
    
    menuid = db.Column("menuid", db.Integer, primary_key = True)
    menu = db.Column(db.String)
    parentid = db.Column(db.Integer)
    functions = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, menuid, menu, parentid, functions, details):
        self.menuid = menuid
        self.menu = menu
        self.parentid = parentid
        self.functions = functions
        self.details = details
        
        
    @classmethod
    def find_by_menuid(cls, menuid) -> "tbmenus":
        return cls.query.filter_by(menuid=menuid).first()
