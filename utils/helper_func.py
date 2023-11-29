from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with


def checking(params, status:bool, message):
    if bool(params) != status:
        abort(404, message = message)
        
    