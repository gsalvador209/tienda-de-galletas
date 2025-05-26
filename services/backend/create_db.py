from config.database import engine, Base
import os
from sqlalchemy import text

# Importar todos los modelos
from models.user import User
from models.product import Product
from models.order import Order
from models.order_item import OrderItem

def run_migrations():
    # Si usas Alembic, aquí podrías hacer:
    # from alembic.config import Config
    # from alembic import command
    # alembic_cfg = Config("alembic.ini")
    # command.upgrade(alembic_cfg, "head")
    Base.metadata.create_all(bind=engine)

def run_seeds():
    dir_seeds = os.path.join(os.path.dirname(__file__), "..", "database", "seeds")
    for fname in ["users.sql", "products.sql", "orders.sql", "order_items.sql"]:
        path = os.path.abspath(os.path.join(dir_seeds, fname))
        with open(path) as f, engine.connect() as conn:
            conn.execute(text(f.read()))
    print("Seeds aplicados")

if __name__ == "__main__":
    run_migrations()
    run_seeds()
    print("Base de datos preparada.")
