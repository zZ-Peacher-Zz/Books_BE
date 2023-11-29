from flask_restful import reqparse

book_put_args = reqparse.RequestParser()
book_put_args.add_argument("name", type=str)
book_put_args.add_argument("price", type=str)

book_post_args = reqparse.RequestParser()
book_post_args.add_argument("name", type=str)
book_post_args.add_argument("price", type=str)


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

actor_post_args = reqparse.RequestParser()
actor_post_args.add_argument("name", type=str)