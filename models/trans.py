from config.db import db


class tbtrans(db.Model):

    tid = db.Column("tid", db.Integer, primary_key=True)
    branchcode = db.Column(db.String)
    productid = db.Column(db.Integer)
    weight = db.Column(db.Float)
    price = db.Column(db.Float)
    submitter = db.Column(db.String)
    submitdate = db.Column(db.DateTime)
    submitternote = db.Column(db.String)
    authorizer = db.Column(db.String)
    authorizedate = db.Column(db.DateTime)
    authorizernote = db.Column(db.String)
    status = db.Column(db.Integer)
    valuedate = db.Column(db.DateTime)
    trandate = db.Column(db.DateTime)
    countsubmitted = db.Column(db.Integer)
    batchid = db.Column(db.Integer)

    def __init__(self, tid=None, branchcode=None, productid=None, weight=None, price=None, submitter=None, submitdate=None, submitternote=None, authorizer=None, authorizedate=None, authorizernote=None, status=None, valuedate=None, trandate=None, countsubmitted=None, batchid=None):
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

    @classmethod
    def find_by_tid(cls, tid) -> "tbtrans":
        return cls.query.filter_by(tid=tid).first()
