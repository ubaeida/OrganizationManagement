from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = 'uTl1oNk7wk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/organizationmanagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
