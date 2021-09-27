from database import db
from models.EventRating import EventRating

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    #media = db.Column(db.PickleType)
    rating_id = db.Column(db.Integer, db.ForeignKey('event_ratings.id'),nullable=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    address = db.Column(db.String(200))