import os, sys
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

# Ajusta el path para poder importar tu app y tu config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Carga variables de .env (en services/backend/.env)
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Importa tu Base metadata desde config/database.py
from config.database import Base

# Configuración de logging
config = context.config
fileConfig(config.config_file_name)

# Inyecta la URL si no está en alembic.ini
db_url = os.getenv("DATABASE_URI") or (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
config.set_main_option("sqlalchemy.url", db_url)

# Metadata para autogenerate
target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata,
        literal_binds=True, dialect_opts={"paramstyle": "named"}
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    from sqlalchemy import engine_from_config
    from sqlalchemy.pool import NullPool
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=NullPool
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
