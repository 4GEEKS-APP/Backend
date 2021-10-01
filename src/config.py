import os
class Config:
    SECRET_KEY = os.urandom(32)
    JWT_SECRET_KEY = 'Shhhhhhhhhh!'
    DEBUG = True
    # Connect to the database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://asiz33:yonosoydelau1@localhost/4geeks_app_v2'

    # SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:pwd@localhost:/4geeks_app_v2'

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = 'development'

class DevConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://asiz33:yonosoydelau1@localhost/4geeks_app_v2'
    ENV = 'development'

class ProdConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:pwd@localhost:/4geeks_app_v2'
    ENV = 'production'
