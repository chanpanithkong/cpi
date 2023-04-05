from config.db import db
from models.menus import tbmenus

class tbrolemenu(db.Model):

    roleid = db.Column("roleid", db.Integer, primary_key=True)
    menuid = db.Column("menuid", db.Integer, primary_key=True)
    details = db.Column(db.String)
    createby = db.Column(db.String)
    createdate = db.Column(db.DateTime)
    statusid = db.Column(db.Integer)

    def __init__(self, roleid=None, menuid=None, details=None, createby=None, createdate=None, statusid=None):
        self.roleid = roleid
        self.menuid = menuid
        self.details = details
        self.createby = createby
        self.createdate = createdate
        self.statusid = statusid

    @classmethod
    def find_by_roleid(cls, roleid) -> "tbrolemenu":
        return cls.query.filter_by(roleid=roleid).order_by(tbrolemenu.menuid).all()

    @classmethod
    def find_by_menuchild(cls, roleid, parentid) -> "tbrolemenu":
        filter = (tbrolemenu.roleid == roleid) & (tbmenus.parentid == parentid)
        data = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()
        return data
    
    @classmethod
    def find_by_menuparent(cls, roleid) -> "tbrolemenu":
        filter = (tbrolemenu.roleid == roleid) & (tbmenus.parentid == 0)
        data = db.session.query(tbrolemenu, tbmenus).filter(
            tbrolemenu.menuid == tbmenus.menuid).filter(filter).order_by(tbrolemenu.menuid).all()
        return data