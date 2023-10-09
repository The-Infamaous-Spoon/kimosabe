from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_email = db.Column(db.String(100), nullable = False, unique = True)
    user_tokens = db.Column(db.Integer)
    date_time = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id