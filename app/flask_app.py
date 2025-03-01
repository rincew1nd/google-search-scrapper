from flask import Flask
from app.flask_routes import register_routes

def create_app(google_searcher):
    # Create a new Flask app and specify the templates folder location.
    app = Flask(__name__, template_folder='templates')
    # Register all the routes and pass in the google_searcher instance.
    register_routes(app, google_searcher)
    return app