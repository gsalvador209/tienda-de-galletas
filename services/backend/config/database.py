import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#-------------------------------------------
# Carga de variables de entorno
#-------------------------------------------
DATABASE_URI = os.getenv("DATABASE_URI","").strip()

# Credenciales MySQL
DB_USER = os.getenv("DB_USER", "")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "")

#-------------------------------------------
# Construcción de URI
#-------------------------------------------
#
#Inicializa SQLAlchemy usando DATABASE_URI si existe o mySQL en cambio
#Esto para poder hacer pruebas con una DB temporal

if DATABASE_URI and DATABASE_URI.startswith('sqlite:///'):
    #Modo desarrollo o pruebas con SQLITE
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
else:
    #Modo producción o Docker con mySQL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}"
        f"@{DB_HOST}/{DB_NAME}"
    )

#-------------------------------------------
# Configuración de Flask y SQLAlchemy
#-------------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Base para Alembic y así usará metadata de modelos
Base = db.Model


#-------------------------------------------
# Funciones de inicialización
#-------------------------------------------
def init_app(flask_app: Flask):
    """
    Inicializa la extensión SQLAlchyemy en la app de Flask
    Esta función debe ser utilizada en la app principal
    """
    db.init_app(flask_app)

def create_db_and_seed():
    """
    Para entornos de Docker / Producción: crea 
    todas las tablas y carga los seeds
    """
    with app.app_context():
        db.create_all()
        #Llamar a las seed

        
# -------------------------------------------------
# Ejecución directa
# -------------------------------------------------
if __name__ == "__main__":
    print("Usando URI:", SQLALCHEMY_DATABASE_URI)
    create_db_and_seed()
    print("Base de datos creada y seeds aplicados (si los tienes).")
