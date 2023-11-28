
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import BookModel, db
from request_args import book_put_args, book_update_args


class AllBooks(Resource):
    
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.String
    }
    @marshal_with(resource_fields)
    def get(self):
        result = BookModel.query.all()
        return result
    


class Books(Resource):
    
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.String
    }
    
    
    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id = book_id).first()
        if not result:
            abort(404, message="Could not found book with that id...")
        
        return result
    
    @marshal_with(resource_fields)
    def put(self, book_id):
        args = book_put_args.parse_args()
        result = BookModel.query.filter_by(id = book_id).first()
        
        if result:
            abort(404, message="book id taken...")
        
        book = BookModel(id = book_id, name = args["name"], price = args["price"])
        
        db.session.add(book)
        db.session.commit()
        return book, 201
    
    @marshal_with(resource_fields)
    def patch(self, book_id):
        args = book_put_args.parse_args()
        book = BookModel.query.filter_by(id = book_id).first()
        
        if not book:
            abort(404, message="Could not found book with that id...")
        
        if args["name"]:
            book.name = args["name"]
        if args["price"]:
            book.price = args["price"]
            
        
        db.session.commit()
        return book       
    
    def delete(self, book_id):
        return f"Delete {book_id} successfully", 204