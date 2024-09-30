from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    
    placeid = db.Column(db.Text, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    geometry = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    rtype = db.Column(db.String(100), nullable=False)
    priceLevel = db.Column(db.Text, nullable=False)
    opeN = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f'Restaurant {self.name} and address {self.address}'

class History(db.Model):
    __tablename__ = 'history'
    
    placeid = db.Column(db.Text, primary_key=True)
    dateT = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    rtype = db.Column(db.String(100), nullable=False)
    geometry = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'History {self.name} and address {self.address}'