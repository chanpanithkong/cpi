from config.db import db

class tbbranches(db.Model):
    
    branchcode = db.Column("branchcode", db.String, primary_key = True)
    nameen = db.Column(db.String)
    namekh = db.Column(db.String)
    address = db.Column(db.String)
    details = db.Column(db.String)
    
    
    def __init__(self, branchcode, nameen, namekh, address, details):
        self.branchcode = branchcode
        self.nameen = nameen
        self.namekh = namekh
        self.address = address
        self.details = details
        
        
    @classmethod
    def find_by_branchcode(cls, branchcode) -> "tbbranches":
        return cls.query.filter_by(branchcode=branchcode).first()
