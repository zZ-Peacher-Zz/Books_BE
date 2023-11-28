from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from model import BookModel, db, UserModel


#Config
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

#Create database
with app.app_context():
    db.create_all()


book_put_args = reqparse.RequestParser()
book_put_args.add_argument("name", type=str)
book_put_args.add_argument("price", type=str)

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("name", type=str)
book_update_args.add_argument("price", type=str)

user_register_post_args = reqparse.RequestParser()
user_register_post_args.add_argument("username", type=str)
user_register_post_args.add_argument("email", type=str)
user_register_post_args.add_argument("password", type=str)

user_login_post_args = reqparse.RequestParser()
user_login_post_args.add_argument("username", type=str)
user_login_post_args.add_argument("password", type=str)


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

class RegisterResource(Resource):
    
    def post(self):
        args = user_register_post_args.parse_args()
        username = args.get('username')
        password = args.get('password')
        
        print(username, password)

        if not username or not password:
            abort(400, message = 'Username and password are required')

        existing_user = UserModel.query.filter_by(username=username).first()
        
        if existing_user:
            abort(409, message = 'Username already exists')

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

api.add_resource(AllBooks, "/books")     
api.add_resource(Books, "/books/<int:book_id>")
api.add_resource(RegisterResource, "/users/register")
api.add_resource(LoginResource, "/users/login")

if __name__ == "__main__":
    app.run(debug=True)
        

