import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# construye tu URI igual que antes
DATABASE_URI = os.getenv("DATABASE_URI", "").strip() or (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

# instancia SQLAlchemy **sin** pasarle app
db = SQLAlchemy()

# Exporta Base para Alembic
Base = db.Model

def init_db(flask_app):
    """Crea todas las tablas definidas en los modelos."""
    with flask_app.app_context():
        flask_app.logger.info("Creando tablas en la base de datos…")
        db.create_all()
        flask_app.logger.info("Tablas creadas.")
