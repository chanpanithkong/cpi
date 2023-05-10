from config.db import db

class tbmenus(db.Model):
    
    menuid = db.Column("menuid", db.Integer, primary_key = True)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    parentid = db.Column(db.Integer)
    functions = db.Column(db.String)
    details = db.Column(db.String)
    icon = db.Column(db.String)
    iscat = db.Column(db.Integer)
    
    def __init__(self, menuid=None, nameen=None, namekh=None, parentid=None, functions=None, details=None, icon=None, iscat=None):
        self.menuid = menuid
        self.nameen = nameen
        self.namekh = namekh
        self.parentid = parentid
        self.functions = functions
        self.details = details
        self.icon = icon
        self.iscat = iscat
        
        
    @classmethod
    def find_by_menuid(cls, menuid) -> "tbmenus":
        return cls.query.filter_by(menuid=menuid).first()

    @classmethod
    def find_by_iscat(cls) -> "tbmenus":
        filters = (db.Column("iscat") != 0) & (db.Column("functions") != "None")
        return cls.query.filter(filters).all()
    
    @classmethod
    def find_by_parent(cls,parentid) -> "tbmenus":
        filters = (db.Column("parentid") == parentid)
        return cls.query.filter(filters).all()