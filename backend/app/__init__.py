# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from flask_cors import CORS  # Import Flask-CORS

db = SQLAlchemy()
migrate = None  # Placeholder for Flask-Migrate instance


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../telecom.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Allow requests from your React frontend
    CORS(app, origins="http://localhost:3000")

    db.init_app(app)

    # Initialize Flask-Migrate with Flask app and SQLAlchemy database
    global migrate
    migrate = Migrate(app, db)

    with app.app_context():
        from .routes import bp
        db.create_all()  # Create the tables if they don't exist
        app.register_blueprint(bp)

    return app
