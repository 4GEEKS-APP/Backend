import enum
from src.database import db

class RatingRange(enum.Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

class UserRating(db.Model):
    __tablename__ = 'user_ratings'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    value = db.Column(db.Enum(RatingRange), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    from_user_id = db.Column(db.Integer,nullable=False)