from flask_restful import reqparse

user_register_post_args = reqparse.RequestParser()
user_register_post_args.add_argument("username", type=str)
user_register_post_args.add_argument("email", type=str)
user_register_post_args.add_argument("password", type=str)

user_login_post_args = reqparse.RequestParser()
user_login_post_args.add_argument("username", type=str)
user_login_post_args.add_argument("password", type=str)