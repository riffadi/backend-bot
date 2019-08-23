from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    born_date =db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    grup = db.relationship('Grup', backref='id', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Grup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Grup {}>'.format(self.name)    
