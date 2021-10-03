from src.database import db

class EventImage(db.Model):
    __tablename__ = 'event_images'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    url= db.Column(db.String(350), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url
        }

    def save(self):
        db.session.add(self)
        db.session.commit()