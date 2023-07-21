from config.db import db

class tbproducts(db.Model):
    
    prodid = db.Column("prodid", db.Integer, primary_key = True)
    productcode = db.Column(db.String)
    nameen = db.Column(db.Integer)
    namekh = db.Column(db.String)
    weight = db.Column(db.Float)
    baseprice = db.Column(db.Float)
    details = db.Column(db.String)
    catid = db.Column(db.Integer)
    unitkh = db.Column(db.String)
    uniten = db.Column(db.String)
    # tbcategories = db.relationship("tbcategories")
    
    
    def __init__(self, prodid = None, productcode = None, nameen = None, namekh = None, weight = None, baseprice =None, catid = None, details = None, tbcategories = None, unitkh = None, uniten = None):
        self.prodid = prodid
        self.productcode = productcode
        self.nameen = nameen
        self.namekh = namekh
        self.weight = weight
        self.baseprice = baseprice
        self.catid = catid
        self.details = details
        self.tbcategories = tbcategories
        self.uniten = uniten
        self.unitkh = unitkh
        
    @classmethod
    def find_by_prodid(cls, prodid) -> "tbproducts":
        return cls.query.filter_by(prodid=prodid).first()
    
    @classmethod
    def find_by_catid(cls, catid) -> "tbproducts":
        return cls.query.filter_by(catid=catid).all()

    @classmethod
    def find_by_catid(cls, catid) -> "tbproducts":
        return cls.query.filter_by(catid=catid).all()
    
    @classmethod
    def find_by_prodcode(cls, productcode) -> "tbproducts":
        return cls.query.filter_by(productcode=productcode).first()