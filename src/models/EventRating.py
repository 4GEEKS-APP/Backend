import enum
from database import db
from sqlalchemy.dialects.mysql import JSON

class RatingRange(enum.Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

class EventRating(db.Model):
    __tablename__ = 'event_ratings'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    value = db.Column(db.Enum(RatingRange), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),nullable=False)
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