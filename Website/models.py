from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    Adhar = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(150))