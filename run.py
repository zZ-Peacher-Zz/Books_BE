from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from apps.actors.models import ActorModel
from apps.books.models import BookModel
from apps.users.models import UserModel
from apps.db import db, api
from utils.args import *
from utils.helper_func import checking
from apps.actors.urls import actor_api
from apps.users.urls import users_api
from apps.books.urls import book_api

#Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

app.register_blueprint(actor_api, url_prefix ='/')
app.register_blueprint(users_api, url_prefix ='/')
app.register_blueprint(book_api, url_prefix ='/')


#Create database
# with app.app_context():
#     db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)