from src.database import db

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120))
    user = db.relationship('User', backref='user', lazy=True)
    def serialize(self):
        return{
            "id": self.id,
            "title": self.title
        }
    def save(self):
        db.session.add(self)
        db.session.commit()