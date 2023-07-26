from config.db import db

class tbbranches(db.Model):
    
    branchcode = db.Column("branchcode", db.String, primary_key = True)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    addressen = db.Column(db.String)
    addresskh = db.Column(db.String)
    weight = db.Column(db.Float)
    details = db.Column(db.String)
    
    
    def __init__(self, branchcode=None, nameen=None, namekh=None, addressen=None,addresskh=None,weight=None, details=None):
        self.branchcode = branchcode
        self.nameen = nameen
        self.namekh = namekh
        self.addressen = addressen
        self.addresskh = addresskh
        self.weight = weight
        self.details = details
        
        
    @classmethod
    def find_by_branchcode(cls, branchcode) -> "tbbranches":
        return cls.query.filter_by(branchcode=branchcode).first()

    @classmethod
    def getallbranches(cls, ) -> "tbbranches":
        return cls.query.all()
