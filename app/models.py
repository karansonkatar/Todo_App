from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)    # Changed string to String
    status = db.Column(db.String(20), default="pending") # Changed string to String


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Changed 'name' to 'username' to match your login.html
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)