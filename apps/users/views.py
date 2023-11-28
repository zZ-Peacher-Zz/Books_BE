from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import UserModel, db
from request_args import user_login_post_args, user_register_post_args
from flask import make_response




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
