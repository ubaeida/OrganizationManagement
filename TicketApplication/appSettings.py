from flask import Flask, request, jsonify, make_response, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/organizationmanagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
