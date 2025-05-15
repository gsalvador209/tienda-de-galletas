
from app import create_app
from config.database import db
from models.product import Product

app = create_app()

sample = [
    {"name":"Galleta Choco","description":"Deliciosa","price":12.5,"stock":100,"image_url" : ""},
    {"name":"Galleta Vainilla","description":"Clásica","price":10.0,"stock":80,"image_url" : ""},
]

with app.app_context():
    if not Product.query.first():
        objs = [Product(**item) for item in sample]
        db.session.bulk_save_objects(objs)
        db.session.commit()
        print("🌱 Semilla de products plantada")
    else:
        print("🌱 Ya existen products, no se sembró nada")
