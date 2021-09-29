import enum
import datetime
from database import db
from sqlalchemy.dialects.mysql import JSON

class RatingCategories(enum.Enum):
    one = 1
    two = 2
    three = 3

class EventRating(db.Model):
    __tablename__ = 'event_ratings'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    category = db.Column(db.Enum(RatingCategories), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),nullable=False)
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'event_id': self.event_id,
            'value': self.value
        }
    def save(self):
        db.session.add(self)
        db.session.commit()