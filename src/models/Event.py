from database import db
from models.EventRating import EventRating
from models.EventImage import EventImage
from sqlalchemy.dialects.mysql import JSON

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    ratings = db.relationship('EventRating', backref='event_ratings', lazy=True)
    images = db.relationship('EventImage', backref='event_images', lazy=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    address = db.Column(db.String(200))
    
    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'title': self.title,
            'description': self.description
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
