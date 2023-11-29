from apps.db import api
from apps.books.views import AllBooks, Books
from flask import Blueprint
from flask_restful import Api

book_api = Blueprint('book_api', __name__)
api = Api(book_api)

api.add_resource(AllBooks, "/books")     
api.add_resource(Books, "/books/<int:book_id>")