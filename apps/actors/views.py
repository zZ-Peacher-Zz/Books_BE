from flask_restful import Resource, fields, marshal_with, abort
from flask import make_response
from apps.actors.models import ActorModel
from utils.args import *
from utils.helper_func import checking
from apps.db import db


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
 