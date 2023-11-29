from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from model import BookModel, db, UserModel, ActorModel
from utils.helper_func import checking
from utils.args import *

#Config
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

#Create database
with app.app_context():
    db.create_all()

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

class RegisterResource(Resource):
    
    def post(self):
        args = user_register_post_args.parse_args()
        username = args.get('username')
        password = args.get('password')
        
        print(username, password)

        if not username or not password:
            abort(400, message = 'Username and password are required')

        existing_user = UserModel.query.filter_by(username=username).first()
        checking(existing_user, False, 'Username already exists')
        
        new_user = UserModel(username=username)
        new_user.password = password
        if args['email']:
            new_user.email = args['email']
        
        db.session.add(new_user)
        db.session.commit()

        return make_response({'message': 'User registered successfully'}, 201)

class LoginResource(Resource):
    
    def post(self):
        args = user_login_post_args.parse_args()
        username = args.get('username')
        password = args.get('password')

        if not username or not password:
            abort(400, message = 'Username and password are required')

        user = UserModel.query.filter_by(username=username).first()
        if (not user) or (not user.verify_password(password)):
            abort(400, message = 'Invalid username or password')

        return make_response({'message': 'Login successful'}, 201)

class AllUser(Resource):
    
    user_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String
    }
    
    @marshal_with(user_fields)
    def get(self):
        all_user = UserModel.query.all()
        return all_user
        
class AllActor(Resource):
    
    actor_fields = {
        "id": fields.Integer,
        "name": fields.String
    }
    
    @marshal_with(actor_fields)
    def get(self):
        actor = ActorModel.query.all()
        return actor
    
    def post(self):
        args = actor_post_args.parse_args()
        actor = ActorModel.query.filter_by(name = args["name"]).first()
        
        if actor:
            abort(404, message = "Actor already exist")
            
        new_actor = ActorModel(name = args["name"])
        db.session.add(new_actor)
        db.session.commit()
        
        return make_response({'message': 'Actor created successfully'}, 201)
            
        

api.add_resource(AllBooks, "/books")     
api.add_resource(Books, "/books/<int:book_id>")
api.add_resource(RegisterResource, "/users/register")
api.add_resource(LoginResource, "/users/login")
api.add_resource(AllUser, "/users")
api.add_resource(AllActor, "/actors")

if __name__ == "__main__":
    app.run(debug=True)
        

