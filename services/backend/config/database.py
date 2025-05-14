from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy() # Inicializa la instancia de SQLAlchemy

def init_db(app):
    """
    Inicializa la base de datos con la aplicación Flask.
    """
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        f"mysql+pymysql:://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_NAME')}/{os.getenv('DB_NAME')}"
        )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la extensión SQLAlchemy con la aplicación
    db.init_app(app)
