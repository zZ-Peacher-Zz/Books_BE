from flask_sqlalchemy import SQLAlchemy
from apps.db import db


class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Books(name = {self.name})"