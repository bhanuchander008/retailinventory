import datetime
from config import db


class Category(db.Model):
    __tablename__ = "category"

    """
    Represents category 

    field id: Primary key
    type id: Integer

    """
    id = db.Column(db.Integer, primary_key=True)
    categoryTitle = db.Column(db.Enum('Hats','Shirts','Pants','Shoes'), nullable=False, unique=True)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updatedAt =  db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())

