# config_test.py
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///test_telecom.db'  # Use a separate database for tests
SQLALCHEMY_TRACK_MODIFICATIONS = False