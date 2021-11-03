import os
class Config:
    SECRET_KEY = os.urandom(32)
    JWT_SECRET_KEY = 'Shhhhhhhhhh!'
    DEBUG = True
    # Connect to the database
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://asiz33:yonosoydelau1@localhost/4geeks_app_v2'

    # SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://root:root@localhost:5432/4geeks_app_v2'

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = 'development'

class DevConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oonxjewfaaypft:9788124e93c50d4ed715556650c86e1ccb0c8b2458445473a2f2c0bc15709ce7@ec2-44-196-96-149.compute-1.amazonaws.com:5432/ddd7sqjbmkab0b'
    ENV = 'development'

class ProdConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oonxjewfaaypft:9788124e93c50d4ed715556650c86e1ccb0c8b2458445473a2f2c0bc15709ce7@ec2-44-196-96-149.compute-1.amazonaws.com:5432/ddd7sqjbmkab0b'
    ENV = 'production'
