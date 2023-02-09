from config.db import db

class tbcategories(db.Model):
    
    catid = db.Column("catid", db.Integer, primary_key = True)
    catcode = db.Column(db.String)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    parentid = db.Column(db.Integer)
    details = db.Column(db.String)
    
    
    def __init__(self, catid, catcode, nameen, namekh, parentid, details):
        self.catid = catid
        self.catcode = catcode
        self.nameen = nameen
        self.namekh = namekh
        self.parentid = parentid
        self.details = details
        
        
    @classmethod
    def find_by_catid(cls, catid) -> "tbcategories":
        return cls.query.filter_by(catid=catid).first()
