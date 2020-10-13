from marshmallow import fields, Schema
from config import db, ma
from models.items import Items


class GetAddItemsSchema(ma.ModelSchema):
    class Meta:
        model = Items
        fields = ('id', "itemTitle", "categoryId",
                  "itemDescription", "itemPrice", "status", "createdAt", "updatedAt")
        include_relationships = True
        load_instance = True
        sqla_session = db.session


class GetItemsSchema(ma.ModelSchema):
    class Meta:
        model = Items
        fields = ('id', "itemTitle",
                  "itemDescription", "itemPrice")
        sqla_session = db.session
