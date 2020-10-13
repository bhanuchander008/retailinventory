from flask import Flask,request
from flask_cors import CORS
from config import *
from routes import *

CORS(app)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
