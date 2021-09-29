from models.UserRole import UserRole
from models.UserRating import UserRating
from models.pivot_tables import user_preferences, user_followers
from database import db
from flask import jsonify

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    avatar_url = db.Column(db.String(400))
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'),nullable=False)
    ratings = db.relationship('UserRating', backref='UserRating', lazy=True)

    followers = db.relationship("User",
                            secondary=user_followers,
                            primaryjoin=id==user_followers.c.user_id,
                            secondaryjoin=id==user_followers.c.follower_id,backref="user_followers")
    
    following = db.relationship("User",
                            secondary=user_followers,
                            primaryjoin=id==user_followers.c.follower_id,
                            secondaryjoin=id==user_followers.c.user_id,backref="user_following")

    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'followers': list(map(lambda user: user.simple(), self.followers)),
            'following': list(map(lambda user: user.simple(), self.following)),
            'avatar_url': self.avatar_url
        }
    def simple(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'avatar_url': self.avatar_url
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
