from config.db import db

class tbmeasurement(db.Model):
    
    mid = db.Column("mid", db.Integer, primary_key = True)
    unit = db.Column(db.String)
    measurement = db.Column(db.Float)
    details = db.Column(db.String)
    
    
    def __init__(self, mid, unit, measurement, details):
        self.mid = mid
        self.unit = unit
        self.measurement = measurement
        self.details = details
        
        
    @classmethod
    def find_by_mid(cls, mid) -> "tbmeasurement":
        return cls.query.filter_by(mid=mid).first()
