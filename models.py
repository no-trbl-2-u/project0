from app import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String)
    email = db.Column(db.String(25))


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    name = db.Column(db.String(20))
    level = db.Column(db.Integer)
    race = db.Column(db.String(20))
    _class = db.Column(db.String(20))
    current_xp = db.Column(db.Integer)
