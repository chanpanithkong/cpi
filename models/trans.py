from config.db import db
from sqlalchemy import or_
from models.products import tbproducts
from models.categories import tbcategories


class tbtrans(db.Model):

    tid = db.Column("tid", db.Integer, primary_key=True)

    branchcode = db.Column(db.String, db.ForeignKey('tbbranches.branchcode'))
    # tbbranches = db.relationship("tbbranches")

    productid = db.Column(db.Integer, db.ForeignKey('tbproducts.prodid'))
    # tbproducts = db.relationship("tbproducts")

    weight = db.Column(db.Float)
    price = db.Column(db.Float)

    submitter = db.Column(db.String)
    submitdate = db.Column(db.DateTime)
    submitternote = db.Column(db.String)

    authorizer = db.Column(db.String)
    authorizedate = db.Column(db.DateTime)
    authorizernote = db.Column(db.String)

    checker = db.Column(db.String)
    checkerdate = db.Column(db.DateTime)
    checkernote = db.Column(db.String)

    status = db.Column(db.Integer, db.ForeignKey('tbstatus.statusid'))
    # tbstatus = db.relationship("tbstatus")

    valuedate = db.Column(db.DateTime)
    trandate = db.Column(db.DateTime)
    countsubmitted = db.Column(db.Integer)

    batchid = db.Column(db.Integer, db.ForeignKey('tbbatches.batchid'))
    # tbbatches = db.relationship("tbbatches")

    def __init__(self, tid=None, branchcode=None, productid=None, weight=None, price=None, submitter=None, submitdate=None, submitternote=None, authorizer=None, authorizedate=None, authorizernote=None, checker=None, checkerdate=None, checkernote=None, status=None, valuedate=None, trandate=None, countsubmitted=None, batchid=None):
        self.tid = tid
        self.branchcode = branchcode
        self.productid = productid
        self.weight = weight
        self.price = price
        self.submitter = submitter
        self.submitdate = submitdate
        self.submitternote = submitternote
        self.authorizer = authorizer
        self.authorizedate = authorizedate
        self.authorizernote = authorizernote
        
        self.checker = checker
        self.checkerdate = checkerdate
        self.checkernote = checkernote

        self.status = status
        self.valuedate = valuedate
        self.trandate = trandate
        self.countsubmitted = countsubmitted
        self.batchid = batchid
        # self.tbproducts = tbproducts
        # self.tbstatus = tbstatus
        # self.tbbranches = tbbranches
        # self.tbbatches = tbbatches

    @classmethod
    def find_by_tid(cls, tid) -> "tbtrans":
        return cls.query.filter_by(tid=tid).first()

    @classmethod
    def find_by_submitterbatchidprodid(cls, submitter, batchid, productid) -> "tbtrans":
        filters = (db.Column("submitter") == submitter) & (
            db.Column("batchid") == batchid) & (db.Column("productid") == productid)
        return cls.query.filter(filters).first()

    @classmethod
    def find_by_authorizecatbatchid(cls, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 1) | (tbtrans.status == 3) | (tbtrans.status == 10) | (tbtrans.status == 11))  & (tbtrans.batchid == batchid)
        return db.session.query( tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    
    @classmethod
    def find_by_checkebatchid(cls, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 3) | (tbtrans.status == 11) | (tbtrans.status == 13))  & (tbtrans.batchid == batchid)
        return db.session.query( tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    
    @classmethod
    def find_by_batchid(cls, batchid) -> "tbtrans":
        filters = (db.Column("status") == 7)  & (
            db.Column("batchid") == batchid)
        return cls.query.filter(filters).all()
    
    @classmethod
    def find_by_batchidnotaccept(cls, batchid) -> "tbtrans":
        filters = (db.Column("status") != 13)  & (
            db.Column("batchid") == batchid)
        return cls.query.filter(filters).all()

    
    @classmethod
    def find_by_catbatchidsubmit(cls,catid, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 1) | (tbtrans.status == 11))   & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    
    @classmethod
    def find_by_catbatchidachecked(cls,catid, batchid) -> "tbtrans":
        filters = (tbtrans.status == 13)  & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    

    @classmethod
    def find_by_catbatchidauthorize(cls,catid, batchid) -> "tbtrans":
        filters = (tbtrans.status == 3)  & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    


    @classmethod
    def find_by_catbatchid(cls,catid, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 1) | (tbtrans.status == 3))  & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    
    @classmethod
    def find_by_prodbatchid(cls,productid, batchid,) -> "tbtrans":
        filters = ((tbtrans.status == 1) | (tbtrans.status == 11))  & (tbtrans.batchid == batchid) & (tbproducts.prodid == productid)
        return db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(filters).first()
    
    @classmethod
    def find_by_prodbatchidforchecker(cls,productid, batchid,) -> "tbtrans":
        filters = ((tbtrans.status == 3) | (tbtrans.status == 13) | (tbtrans.status == 11))  & (tbtrans.batchid == batchid) & (tbproducts.prodid == productid)
        return db.session.query(tbtrans).filter(tbtrans.productid == tbproducts.prodid).filter(filters).first()
    
    @classmethod
    def find_by_prodbatchidnotsubmit(cls,productid, batchid,) -> "tbtrans":
        filters = (tbtrans.status != 1)  & (tbtrans.batchid == batchid) & (tbproducts.prodid == productid)
        return db.session.query(tbtrans, tbproducts).filter(tbtrans.productid == tbproducts.prodid).filter(filters).first()
    
    @classmethod
    def find_by_catbatchidrejectauthorize(cls,catid, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 3) | (tbtrans.status == 10))  & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    
    @classmethod
    def find_by_catbatchidrejectchecker(cls,catid, batchid) -> "tbtrans":
        filters = ((tbtrans.status == 11) | (tbtrans.status == 13))  & (tbtrans.batchid == batchid) & (tbcategories.catid == catid)
        return db.session.query(tbtrans, tbproducts, tbcategories).filter(tbtrans.productid == tbproducts.prodid).filter(tbproducts.catid == tbcategories.catid).filter(filters).all()
    