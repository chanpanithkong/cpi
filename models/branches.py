from config.db import db

class tbbranches(db.Model):
    
    branchcode = db.Column("branchcode", db.String, primary_key = True)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    addressen = db.Column(db.String)
    addresskh = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, branchcode, nameen, namekh, addressen,addresskh, details):
        self.branchcode = branchcode
        self.nameen = nameen
        self.namekh = namekh
        self.addressen = addressen
        self.addresskh = addresskh
        self.details = details
        
        
    @classmethod
    def find_by_branchcode(cls, branchcode) -> "tbbranches":
        return cls.query.filter_by(branchcode=branchcode).first()

    @classmethod
    def getallbranches(cls, ) -> "tbbranches":
        return cls.query.all()
