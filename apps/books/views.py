from flask_restful import Resource, marshal_with, fields, reqparse, abort
from apps.books.models import BookModel
from apps.db import db
from utils.args import *
from utils.helper_func import checking

class AllBooks(Resource):
    
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.String,
    }
    
    @marshal_with(resource_fields)
    def get(self):
        result = BookModel.query.all()
        return result
    
    @marshal_with(resource_fields)
    def post(self):
        args = book_put_args.parse_args()
        check_book = BookModel.query.filter_by(name = args["name"]).first()
        
        if check_book:
            abort(404, message = "Book already exist")
        new_book = BookModel(name = args["name"], price = args["price"])
        db.session.add(new_book)
        db.session.commit()
        return new_book, 201
    
class Books(Resource):
    
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.String
    }
    
    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id = book_id).first()
        checking(result, True, "Could not found book with that id...")
        return result
    
    @marshal_with(resource_fields)
    def patch(self, book_id):
        args = book_put_args.parse_args()
        book = BookModel.query.filter_by(id = book_id).first()

        checking(book, True, "Could not found book with that id...")
        if args["name"]:
            book.name = args["name"]
        if args["price"]:
            book.price = args["price"]
        db.session.commit()
        return book
         
    def delete(self, book_id):
        return f"Delete {book_id} successfully", 204
