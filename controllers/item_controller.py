from flask import request,render_template
from flask_restful import Resource
from config import db,app
from models.items import Items
from schemas.item_schema import GetAddItemsSchema,GetItemsSchema


class GetAddItems(Resource):
    def __init__(self):
        pass
    # Items get call

    def get(self):
        try:
            obj = db.session.query(Items).order_by(Items.id).all()
            if obj:
                schema = GetAddItemsSchema(many=True)
                data = schema.dump(obj).data
                return ({"success": True, "data": data, "message": "Data fetched successfully"}, 200)
            else:
                return ({"success": False, "message": "No Item found"}, 200)
        except Exception as e:
            # Logger.create_error_log("getaddItems", str(e))
            return ({"success": False, "message": str(e)}, 500)

    # # Items post call
@app.route('/api/items', methods=['POST', 'GET'])
def Inventory():
    # try:
        if request.method == 'POST':
            request_json_data = request.form.to_dict(flat=True)
            print("cdcsd",request_json_data)
            request_json_data["categoryId"] = int(request_json_data["categoryId"])
            request_json_data["itemPrice"] = float(request_json_data["itemPrice"])
            
            checkname = db.session.query(Items).filter(
                Items.itemTitle == request_json_data["itemTitle"]).one_or_none()
            if checkname:
                return ({"success": False, "message": "Item title already exist"}, 200)
            schema = GetAddItemsSchema()
            obj = schema.load(
                request_json_data, session=db.session).data
            print(obj)
            db.session.add(obj)
            db.session.commit()

            return ({"success": True, "message": "Inventory Added successfully"}, 200)
        return render_template('firstpage.html',message = "inventory added succesfuly")
    # except Exception as e:
    #     # Logger.create_error_log("getaddItems", str(e))
    #     return ({"success": False, "message": str(e)}, 500)


@app.route('/',methods = ['get'])
def landPage():
    return render_template('index.html')
@app.route('/api/viewinventory',methods = ['get'])
def viewItems():
    return render_template('secondpage.html')

class GetUpdateItems(Resource):
    def __init__(self):
        pass

    # Items get call based on id
    def get(self, id):
        try:
            obj = Items.query.filter(Items.categoryId == id).all()
            if obj is not None:
                schema = GetItemsSchema(many=True)
                data = schema.dump(obj).data
                return ({"success": True, "data": data, "message": "Data fetched successfully"}, 200)
            else:
                return ({"success": False, "message": "No Item found"}, 200)
        except Exception as e:
            # Logger.create_error_log("getupdateItems", str(e))
            return ({"success": False, "message": str(e)}, 500)

    # Items update call

    def put(self, id):
        try:
            request_json_data = request.get_json()
            checkname = db.session.query(Items).filter(Items.itemTitle == request_json_data["itemTitle"], Items.id != id).one_or_none()
            if checkname:
                return ({"success": False, "message": "Item title already exist"}, 200)
            obj = db.session.query(Items).filter_by(id=id).update(request_json_data)
            if obj:
                db.session.commit()
                return ({"success": True, "message": "Item updated successfully"}, 200)
            else:
                return ({"success": False, "message": "No Item found"}, 200)
        except Exception as e:
            return ({"success": False, "message": str(e)}, 500)
