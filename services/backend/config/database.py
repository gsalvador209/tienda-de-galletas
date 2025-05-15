from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy() # Inicializa la instancia de SQLAlchemy

def init_db(app):
    """
    Inicializa SQLAlchemy usando DATABASE_URI si existe o mySQL en cambio
    Esto para pooder hacer pruebas con una DB temporal
    """
    uri = os.getenv('DATABASE_URI')
    if uri and uri.startswith('sqlite:///'):
        # 1. Se extrae el path relativo tras 'sqlite:///'
        rel_path = uri.replace('sqlite:///', '')
        # 2. Se calcula carpeta base: services/backend
        base_dir = Path(__file__).resolve().parent.parent
        # 3. Se construye la ruta absoluta al fichero
        abs_db_path = (base_dir / rel_path).resolve()
        # 4. Reconstruye la URI con la ruta absoluta
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{abs_db_path}"
    else:
        # Conexión MySQL si no hay DATABASE_URI
        app.config['SQLALCHEMY_DATABASE_URI'] = uri

    print("»»» SQLALCHEMY_DATABASE_URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la extensión SQLAlchemy con la aplicación
    db.init_app(app)
