
from apps.db import db

class ActorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self) -> str:
        return f"Actor name is {self.name}"

