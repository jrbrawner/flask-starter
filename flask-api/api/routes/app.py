from flask import Flask, Blueprint
from flask_restful import Resource, Api

app_bp = Blueprint('app', __name__)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

