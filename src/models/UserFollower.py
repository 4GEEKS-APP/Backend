from database import db

class UserFollower(db.Model):
    __tablename__ = 'user_followers'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)