from models.UserRole import UserRole
from models.UserFollower import UserFollower
from models.UserRating import UserRating
from models.pivot_tables import user_preferences
from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'),nullable=False)
    followers = db.relationship('UserFollower', backref='UserFollower', lazy=True)
    ratings = db.relationship('UserRating', backref='UserRating', lazy=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address 
        }
