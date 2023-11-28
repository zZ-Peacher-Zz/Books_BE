
from flask_restful import Api, Resource, reqparse


book_put_args = reqparse.RequestParser()
book_put_args.add_argument("name", type=str)
book_put_args.add_argument("price", type=str)

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("name", type=str)
book_update_args.add_argument("price", type=str)