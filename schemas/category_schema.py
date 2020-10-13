from marshmallow import fields, Schema
from config import db, ma
from models.category import Category

class GetAddCategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        fields = ('id', "categoryTitle")
        sqla_session = db.session
