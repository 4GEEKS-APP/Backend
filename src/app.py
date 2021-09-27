from logging import DEBUG
from flask import Flask, render_template
from flask_migrate import Migrate
from database import db
from routes.user_bp import user_bp
from config import Config


app = Flask(__name__)
app.url_map.slashes = False
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')


if __name__ == '__main__':
    app.run()