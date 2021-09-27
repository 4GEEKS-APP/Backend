import enum
from database import db

class RatingCategories(enum.Enum):
    one = 1
    two = 2
    three = 3

class UserRating(db.Model):
    __tablename__ = 'user_ratings'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    category = db.Column(db.Enum(RatingCategories))
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)