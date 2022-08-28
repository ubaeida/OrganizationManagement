from flask import Flask, request, jsonify, make_response, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
# from DBRepository.DBConnector import DBConnector
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/org'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
