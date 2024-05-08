# tests/conftest.py
import pytest
from app import create_app, db
from app.models import Customer, Plan, Renewal
import os

@pytest.fixture
def test_app():
    # Set up Flask application with test configuration
    app = create_app()
    app.config.from_object('config_test')

    with app.app_context():
        # Drop all tables to ensure a clean slate
        db.drop_all()
        # Create all tables
        db.create_all()

    yield app  # Return the Flask app instance to be used in tests

    # Clean up after tests
    with app.app_context():
        db.drop_all()
