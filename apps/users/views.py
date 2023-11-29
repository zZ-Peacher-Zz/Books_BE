from flask_restful import Resource, abort, fields, marshal_with
from utils.args import *
from utils.helper_func import checking
from apps.users.models import UserModel
from flask import make_response
from apps.db import db



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
 