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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gwdfupqnufenzn:455fd768658c9af84671a7139ec3a81d920213dd9d2e9ce7e1067a51255896c1@ec2-100-24-169-249.compute-1.amazonaws.com:5432/d1o0u95058scop'
    ENV = 'production'
