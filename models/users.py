from config.db import db

class tbusers(db.Model):
    
    userid = db.Column("userid", db.String, primary_key = True)
    password = db.Column(db.String)
    roleid = db.Column(db.Integer)
    username = db.Column(db.String)
    gender = db.Column(db.String)
    branchcode = db.Column(db.String)
    details = db.Column(db.String)
    email = db.Column(db.String)
    
    def __init__(self, userid, password, roleid, username, gender, branchcode, details, email):
        self.userid = userid
        self.password = password
        self.roleid = roleid
        self.username = username
        self.gender = gender
        self.branchcode = branchcode
        self.details = details
        self.email = email
        
        
    @classmethod
    def find_by_userid(cls, userid) -> "tbusers":
        return cls.query.filter_by(userid=userid).first()
