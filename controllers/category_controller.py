from flask import request
from flask_restful import Resource
from config import db
from models.category import Category
from schemas.category_schema import GetAddCategorySchema


class GetAddCategory(Resource):
    def __init__(self):
        pass
    # Category get call

    def get(self):
        try:
            obj = db.session.query(Category).order_by(Category.id).all()
            if obj:
                schema = GetAddCategorySchema(many=True)
                data = schema.dump(obj).data
                return ({"success": True, "data": data, "message": "Data fetched successfully"}, 200)
            else:
                return ({"success": False, "message": "No category found"}, 200)
        except Exception as e:
            return ({"success":False, "message":str(e)},500)

    # Category post call
    def post(self):
        try:
            request_json_data = request.get_json()
            checkname = db.session.query(Category).filter(Category.categoryTitle == request_json_data["categoryTitle"]).one_or_none()
            if checkname:
                Logger.create_warning_log("getaddCategory", "Category title already exist")
                return ({"success": False, "message": "Category title already exist"}, 200)
            schema = GetAddCategorySchema()
            obj = schema.load(
                request_json_data, session=db.session).data
            db.session.add(obj)
            db.session.commit()
            return ({"success": True, "message": "Category Added successfully"}, 200)
        except Exception as e:
            return ({"success": False, "message": str(e)}, 500)


class GetUpdateCategory(Resource):
    def __init__(self):
        pass

    # Category get call based on id
    def get(self, id):
        try:
            obj = Category.query.filter(Category.id == id).one_or_none()
            if obj is not None:
                schema = GetAddCategorySchema()
                data = schema.dump(obj).data
                return ({"success": True, "data": data, "message": "Data fetched successfully"},200)
            else:
                return ({"success": False, "message": "No category found"}, 200)
        except Exception as e:
            return ({"success": False, "message": str(e)}, 500)



    # Category update call

    def put(self, id):
        try:
            request_json_data= request.get_json()
            checkname = db.session.query(Category).filter(Category.categoryTitle == request_json_data["categoryTitle"], Category.id != id).one_or_none()
            if checkname:
                Logger.create_warning_log("getupdateCategory", "Category title already exist")
                return ({"success": False, "message": "Category title already exist"}, 200)
            obj = db.session.query(Category).filter_by(id = id).update(request_json_data)
            if obj:
                db.session.commit()
                return ({"success":True,"message":"Category updated successfully"}, 200)
            else:
                return ({"success":False, "message":"No category found"}, 200)
        except Exception as e:
            return ({"success":False, "message":str(e)}, 500)


