from config.db import db

class tbproducts(db.Model):
    
    prodid = db.Column("prodid", db.Integer, primary_key = True)
    productcode = db.Column(db.String)
    nameen = db.Column(db.Integer)
    namekh = db.Column(db.String)
    inputtype = db.Column(db.String)
    catid = db.Column(db.Integer)
    details = db.Column(db.String)
    
    
    def __init__(self, prodid, productcode, nameen, namekh, inputtype, catid, details):
        self.prodid = prodid
        self.productcode = productcode
        self.nameen = nameen
        self.namekh = namekh
        self.inputtype = inputtype
        self.catid = catid
        self.details = details
        
        
    @classmethod
    def find_by_prodid(cls, prodid) -> "tbproducts":
        return cls.query.filter_by(prodid=prodid).first()
