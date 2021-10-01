from logging import DEBUG
from flask import Flask, render_template
from flask_migrate import Migrate
from src.database import db
from src.routes.user_bp import user_bp
from src.routes.event_bp import event_bp
from src.config import DevConfig
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
app.url_map.slashes = False
app.config.from_object(DevConfig)
db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)



app.register_blueprint(user_bp, url_prefix='/users')
#Rutas de eventos
app.register_blueprint(event_bp, url_prefix='/events')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()