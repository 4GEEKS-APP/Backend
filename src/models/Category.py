from src.database import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, nullable=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(150), nullable=False)

    event_category = db.relationship('Event', backref='category', lazy=True)

    def serialize(self):
        return{
            'title': self.title,
            'description': self.description,
            'id': self.id
        }