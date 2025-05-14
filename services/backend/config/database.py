from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy() # Inicializa la instancia de SQLAlchemy

def init_db(app):
    """
    Inicializa SQLAlchemy usando DATABASE_URI si existe o mySQL en cambio
    Esto para pooder hacer pruebas con una DB temporal
    """
    database_uri = os.getenv('DATABASE_URI')
    if database_uri:
        # Pruebas con SQLite
        app.config['SQLAlCHEMY_DATABASE_URI'] = database_uri
    else:
        #Ya es la DB de Mirna
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
            f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )

    print("»»» SQLALCHEMY_DATABASE_URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la extensión SQLAlchemy con la aplicación
    db.init_app(app)
