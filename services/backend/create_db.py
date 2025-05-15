from app import create_app
from config.database import db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tablas creadas correctamente")