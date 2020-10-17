import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()





app = Flask(__name__)

app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://bhanu:bhanu@1015@localhost/retail"
db = SQLAlchemy(app)



app.config["SQLALCHEMY_ECHO"] = True

app.config['SECRET_KEY'] = '3b8d7b303173189153979542'



ma = Marshmallow(app)
db.init_app(app)

