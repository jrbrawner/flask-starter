"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_restful import Api, Resource

db = SQLAlchemy()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    api = Api(app)
    # Application Configuration
    app.config.from_object('config.Config')

    #authentication
    app.config['LOGIN_DISABLED'] = True

    # Initialize Plugins
    db.init_app(app)

    #Set up logging
    logging.basicConfig(filename='log.log',level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s : %(message)s', filemode='w+')
    
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


    with app.app_context():
        from .routes.app import HelloWorld, app_bp
        
        api.add_resource(HelloWorld, '/')

        # Register Blueprints
        app.register_blueprint(app_bp)
        
        # Create Database Models
        db.create_all()

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            pass

        return app