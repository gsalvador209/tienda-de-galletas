# Al ejecutar alembic init migrations se crea este archivo, pero
# yo lo midifiqué para tome la fábrica ya definida

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Python importa la app y config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

#Se carga .env para el URI de la database
from dotenv import load_dotenv
load_dotenv()

#Importa la fábrica y el objeto db para que alembic serpa comparar
from app import create_app
from config.database import db

# Carga la configuración de alembic.ini y ajusta el log
config = context.config
fileConfig(config.config_file_name)

# Crea la app y saca la URI real
flask_app = create_app()
config.set_main_option('sqlalchemy.url', flask_app.config['SQLALCHEMY_DATABASE_URI'])

# Metadata de todos los modelos para autogenerarse
target_metadata = db.metadata

def run_migrations_offline():
    """Corre migraciones sin conexión a BD. (Genera SQL)"""
    url=config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata = target_metadata, literal_binds = True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Corre migraciones conectándose a la BD"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix = 'sqlalchemy.', #Nótese el punto al final
        poolclass = pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection = connection, target_metadata = target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


