from apps.db import api
from apps.actors.views import AllActor
from flask import Blueprint
from flask_restful import Api

actor_api = Blueprint('actor_api', __name__)
api = Api(actor_api)

api.add_resource(AllActor, "/actors")