import enum
from database import db

class RatingCategories(enum.Enum):
    one = 1
    two = 2
    three = 3

class EventRating(db.Model):
    __tablename__ = 'event_ratings'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    category = db.Column(db.Enum(RatingCategories))
    event = db.relationship('Event', backref='events', lazy=True)
    #votes = db.Column(db.PickleType)