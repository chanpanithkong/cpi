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

    status = db.Column(db.Integer, db.ForeignKey('tbstatus.statusid'))
    # tbstatus = db.relationship("tbstatus")

    valuedate = db.Column(db.DateTime)
    trandate = db.Column(db.DateTime)
    countsubmitted = db.Column(db.Integer)

    batchid = db.Column(db.Integer, db.ForeignKey('tbbatches.batchid'))
    # tbbatches = db.relationship("tbbatches")

    def __init__(self, tid=None, branchcode=None, productid=None, weight=None, price=None, submitter=None, submitdate=None, submitternote=None, authorizer=None, authorizedate=None, authorizernote=None, status=None, valuedate=None, trandate=None, countsubmitted=None, batchid=None, tbproducts=None, tbstatus=None, tbbranches=None, tbbatches=None):
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
        self.status = status
        self.valuedate = valuedate
        self.trandate = trandate
        self.countsubmitted = countsubmitted
        self.batchid = batchid
        self.tbproducts = tbproducts
        self.tbstatus = tbstatus
        self.tbbranches = tbbranches
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
    def find_by_batchid(cls, batchid) -> "tbtrans":
        filters = (db.Column("status") == 1)  & (
            db.Column("batchid") == batchid)
        return cls.query.filter(filters).all()