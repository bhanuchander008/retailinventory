import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()





app = Flask(__name__)

app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

cur_dir = os.getcwd()

# selecting app environment
if os.getenv("ENV") == "test":
    db_url = "sqlite:////"+cur_dir+"/temp/test.db"
    port = 5000
    host = "0.0.0.0"

elif os.getenv("ENV") == "development":
    db_url = "sqlite:////"+cur_dir+"/temp/development.db"
    port = 5000
    host = "0.0.0.0"
    
elif os.getenv("ENV") == "demo":
    db_url = "sqlite:////"+cur_dir+"/temp/demo.db"
    port = 5000
    host = "0.0.0.0"

elif os.getenv("ENV") == "production":
    db_url = 'sqlite:////"+cur_dir+"/temp/production.db'
    port = 5000
    host = "0.0.0.0"
    

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config['SECRET_KEY'] = '3b8d7b303173189153979542'



ma = Marshmallow(app)
db.init_app(app)

