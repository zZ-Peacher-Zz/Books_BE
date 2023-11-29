from apps.db import api
from apps.users.views import RegisterResource, LoginResource, AllUser
from flask import Blueprint
from flask_restful import Api, Resource

users_api = Blueprint('user_api', __name__)
api = Api(users_api)

api.add_resource(RegisterResource, "/users/register")
api.add_resource(LoginResource, "/users/login")
api.add_resource(AllUser, "/users")