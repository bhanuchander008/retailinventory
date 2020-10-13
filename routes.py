from flask import Flask
from flask_restful import Resource, Api
from config import *

api = Api(app)


from controllers.category_controller import GetAddCategory, GetUpdateCategory

api.add_resource(GetAddCategory, '/api/category')
api.add_resource(GetUpdateCategory, '/api/category/<int:id>')

from controllers.item_controller import GetAddItems, GetUpdateItems

# api.add_resource(GetAddItems, '/api/items')
api.add_resource(GetUpdateItems, '/api/items/<int:id>')
