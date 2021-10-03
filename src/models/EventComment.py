from src.database import db

class EventComment(db.Model):
    __tablename__ = 'event_comments'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    body= db.Column(db.String(350), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'body': self.body,
            'user': self.user.tiny()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()