from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(10), unique = True)
    password = db.Column(db.String(16))

    def __init__(self, username, password):
        self.username = username
        self.password = password

