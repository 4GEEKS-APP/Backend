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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost:5432/4geeks_app'
    ENV = 'development'

class ProdConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dituydduiddtko:2ab223e8d8342f5f1043b73fecf99cf51ba230d4ded250423d98940296f31b6d@ec2-34-199-209-37.compute-1.amazonaws.com:5432/d51vgatsd8peb8'
    ENV = 'production'
