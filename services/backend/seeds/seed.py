# services/backend/seeds/seed.py

from app import create_app
from config.database import db
from models.product import Product

app = create_app()

with app.app_context():
    # Lista ampliada de productos de ejemplo
    sample_products = [
        {
            "name": "Chocolate Chip Classic",
            "description": "Galleta crujiente con trozos de chocolate semiamargo.",
            "price": 12.50,
            "stock": 120,
            "image_url": "https://example.com/images/choco_chip.jpg"
        },
        {
            "name": "Avena con Pasas",
            "description": "Galleta suave de avena integral con pasas jugosas.",
            "price": 10.00,
            "stock": 80,
            "image_url": "https://example.com/images/oat_raisin.jpg"
        },
        {
            "name": "Mantequilla de Maní",
            "description": "Galleta cremosa con auténtica mantequilla de maní.",
            "price": 13.75,
            "stock": 60,
            "image_url": "https://example.com/images/peanut_butter.jpg"
        },
        {
            "name": "Azucar Decorada",
            "description": "Galleta suave de azúcar con glaseado de colores.",
            "price": 9.99,
            "stock": 200,
            "image_url": "https://example.com/images/sugar_cookie.jpg"
        },
        {
            "name": "Doble Chocolate",
            "description": "Para los amantes del chocolate, masa y chips de chocolate.",
            "price": 14.00,
            "stock": 50,
            "image_url": "https://example.com/images/double_choco.jpg"
        },
        {
            "name": "Snickerdoodle",
            "description": "Galleta esponjosa con canela y azúcar moreno.",
            "price": 11.25,
            "stock": 90,
            "image_url": "https://example.com/images/snickerdoodle.jpg"
        },
        {
            "name": "Nuez de Macadamia",
            "description": "Galleta de vainilla con trozos de nuez de macadamia.",
            "price": 15.00,
            "stock": 40,
            "image_url": "https://example.com/images/macadamia.jpg"
        },
        {
            "name": "Gengibre Crujiente",
            "description": "Galleta de jengibre especiada y crujiente.",
            "price": 12.00,
            "stock": 70,
            "image_url": "https://example.com/images/ginger_snap.jpg"
        },
        {
            "name": "Shortbread Tradicional",
            "description": "Galleta fría de mantequilla típica de Escocia.",
            "price": 10.50,
            "stock": 100,
            "image_url": "https://example.com/images/shortbread.jpg"
        },
        {
            "name": "Limón y Semilla de Amapola",
            "description": "Galleta cítrica con ligero crujir de semillas.",
            "price": 12.75,
            "stock": 65,
            "image_url": "https://example.com/images/lemon_poppy.jpg"
        }
    ]

    # Solo inserta si la tabla está vacía
    if not Product.query.first():
        objs = [Product(**item) for item in sample_products]
        db.session.bulk_save_objects(objs)
        db.session.commit()
        print(f"🌱 Sembrados {len(objs)} productos de ejemplo.")
    else:
        print("🌱 La tabla products ya contiene datos, no se sembró nada.")
