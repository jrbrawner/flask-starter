from flask import Flask, Blueprint

app_bp = Blueprint('app', __name__)

@app_bp.get('/')
def index():
    return {'hello': 'world'}

