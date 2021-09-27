import os
class Config:
    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Enable debug mode.
    DEBUG = True
    # Connect to the database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://asiz33:yonosoydelau1@localhost/4geeks_app'
    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = 'development'
