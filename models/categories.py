from config.db import db

class tbcategories(db.Model):
    
    catid = db.Column("catid", db.Integer, primary_key = True)
    catcode = db.Column(db.String)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    parentid = db.Column(db.Integer)
    details = db.Column(db.String)
        
    def __init__(self, catid=None, catcode=None, nameen=None, namekh=None, parentid=None, details=None):
        self.catid = catid
        self.catcode = catcode
        self.nameen = nameen
        self.namekh = namekh
        self.parentid = parentid
        self.details = details
        
    @classmethod
    def find_by_catid(cls, catid) -> "tbcategories":
        return cls.query.filter_by(catid=catid).first()
    
    @classmethod
    def find_by_parentid(cls, parentid) -> "tbcategories":
        return cls.query.filter_by(parentid=parentid).all()
    
    @classmethod
    def find_by_parent(cls) -> "tbcategories":
        return cls.query.filter_by(parentid=0).all()

    @classmethod
    def find_by_catidischild(cls, catid, parentid) -> "tbcategories":
        return cls.query.filter_by(catid=catid,parentid=parentid)

    @classmethod
    def find_by_countparentid(cls, parentid) -> "tbcategories":
        return cls.query.filter_by(parentid=parentid).count()
