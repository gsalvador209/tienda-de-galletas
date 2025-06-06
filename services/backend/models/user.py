# services/backend/models/user.py

from datetime import datetime
from config.database import db

class User(db.Model):
    __tablename__ = 'users' # Tabla de usuarios “local”

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(50), default='user') #Pendiente si vale la pena porque aun no sabemos si haremos 2 vistas
    created_at = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }
