from config.db import db


class tbusers(db.Model):

    userid = db.Column("userid", db.String, primary_key=True)
    password = db.Column(db.String)
    key = db.Column(db.String)
    roleid = db.Column(db.Integer)
    username = db.Column(db.String)
    gender = db.Column(db.String)
    branchcode = db.Column(db.String)
    details = db.Column(db.String)
    position = db.Column(db.String)
    email = db.Column(db.String)
    status = db.Column(db.Integer)
    phonenumber = db.Column(db.String)
    telegram = db.Column(db.String)
    languages = db.Column(db.String)

    def __init__(self, userid=None, password=None, key=None, roleid=None, username=None, gender=None, branchcode=None, details=None,position=None, email=None, status=None,phonenumber = None, telegram = None, languages = None):
        self.userid = userid
        self.password = password
        self.key = key
        self.roleid = roleid
        self.username = username
        self.gender = gender
        self.branchcode = branchcode
        self.details = details
        self.position = position
        self.email = email
        self.status = status
        self.phonenumber = phonenumber
        self.telegram = telegram
        self.languages = languages


    @classmethod
    def find_by_userid(cls, userid) -> "tbusers":
        return cls.query.filter_by(userid=userid).first()
