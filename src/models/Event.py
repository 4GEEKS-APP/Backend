from src.database import db
from src.models.EventRating import EventRating
from src.models.EventImage import EventImage
from src.models.EventComment import EventComment
from src.models.pivot_tables import event_participants
from sqlalchemy.dialects.mysql import JSON

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    address = db.Column(db.String(200))
    gender = db.Column(db.String(200), nullable=False)
    level = db.Column(db.String(200), nullable=False)
    max_members= db.Column(db.Integer, nullable=False)
    thumbnail = db.Column(db.String(350), nullable=False)

    ratings = db.relationship('EventRating', backref='event_ratings', lazy=True)
    images = db.relationship('EventImage', backref='event_images', lazy=True)
    comments = db.relationship('EventComment', backref='event_comments', lazy=True)
    participants = db.relationship('User', secondary=event_participants)


    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'date_start': self.date_start,
            'title': self.title,
            'description': self.description,
            'creator_id': self.creator_id,
            'images': list(map(lambda image: image.serialize(), self.images)),
            'participants': list(map(lambda user: user.simple(), self.participants)),
            'comments': list(map(lambda comment: comment.serialize(), self.comments)),
            'max_members': self.max_members,
            'thumbnail': self.thumbnail,
            'level': self.level,
            'gender': self.gender,
            'category': self.category.serialize()
        }
    def simple(self):
        return {
            'id': self.id,
            'date_start': self.date_start,
            'title': self.title,
            'description': self.description,
            'creator_id': self.creator_id,
            'participants': list(map(lambda user: user.tiny(), self.participants)),
            'max_members': self.max_members,
            'thumbnail': self.thumbnail,
            'level': self.level,
            'gender': self.gender,
            'category': self.category.serialize()
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
