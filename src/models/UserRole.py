from database import db

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    user = db.relationship('User', backref='user', lazy=True)