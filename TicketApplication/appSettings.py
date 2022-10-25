from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


api = Api(app)
app.config["JWT_SECRET_KEY"] = 'uTl1oNk7wk'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("db_url")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/organizationmanagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
