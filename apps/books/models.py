from apps.db import db
from apps.actors.models import ActorModel

class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    actor = db.relationship('ActorModel', backref=db.backref('books'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor_model.id'))

    def __repr__(self):
        return f"Books(name = {self.name})"