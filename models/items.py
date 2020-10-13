import datetime
from config import db


class Items(db.Model):
    __tablename__ = "items"

    """
    Represents items 

    field id: Primary key
    type id: Integer

    """
    
    id = db.Column(db.Integer, primary_key=True)
    itemTitle = db.Column(db.String(220), nullable=False)
    categoryId = db.Column( db.ForeignKey('category.id'), nullable=False)
    itemDescription = db.Column(db.Text, nullable=True)
    itemPrice = db.Column(db.Float(precision=2), nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updatedAt =  db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())