# services/backend/seeds/seed.py

from app import create_app
from config.database import db
from models.product import Product

app = create_app()

with app.app_context():
    # Lista ampliada de productos de ejemplo
    sample_products = [
        {
            "name": "Cupcake Aleman",
            "description": "Delicioso y esponjoso cupcake de chocolate con un toque tradicional alemán. Perfecto para los amantes del sabor intenso y sofisticado.",
            "price": 80,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJhreqK4eTVn7Q32LeSvKAr0WMpwCBNJ8Tg6fx",
            "stock": 50
        },
        {
            "name": "Cupcake Ferrero",
            "description": "Un cupcake premium con todo el sabor del icónico Ferrero Rocher. Ideal para quienes disfrutan de un postre elegante y lleno de textura.",
            "price": 80,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJuiE4kiLt1LOJdIn7pGxXKDEVBwvqPeRj59ay",
            "stock": 50
        },
        {
            "name": "Cupcake Limon",
            "description": "Refrescante cupcake con sabor natural a limón. Su equilibrio entre dulzura y acidez lo convierte en una opción ligera y deliciosa.",
            "price": 70,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJhgK1nQTVn7Q32LeSvKAr0WMpwCBNJ8Tg6fxF",
            "stock": 50
        },
        {
            "name": "Cupcake Pistache",
            "description": "El sabor gourmet del pistache en una presentación irresistible. Un cupcake suave y aromático que conquista a los paladares más exigentes.",
            "price": 80,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJxIaKljHkB0vOgWVb68u473fhetryFCaLDwAJ",
            "stock": 50
        },
        {
            "name": "Cupcake Red Velvet",
            "description": "Clásico Red Velvet con un color vibrante y textura aterciopelada. Relleno y cubierto con un sutil frosting de queso crema y pedacitos de brownie.",
            "price": 80,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJsszIDTxmOCT72nLgBkJtNvucw63QAhSpVP9F",
            "stock": 50
        },
        {
            "name": "Cupcake Vainilla",
            "description": "El favorito de siempre. Cupcake suave y esponjoso con el delicado sabor de la vainilla natural. Perfecto para cualquier ocasión.",
            "price": 70,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJed5uvHrKwrmtHxdaFJqDkjfcyRXOgZAQ49EB",
            "stock": 50
        },
        {
            "name": "Cupcake Zanahoria",
            "description": "Cupcake casero con zanahoria rallada, nueces y especias. Una opción dulce y reconfortante con un toque saludable.",
            "price": 70,
            "type": "cupcake",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJmAYToPV2FlGJt73OkKRdrcgxsZvVpNQz1L4S",
            "stock": 50
        },
        {
            "name": "Galleta Birthday Cake",
            "description": "Celebra cada día como si fuera tu cumpleaños. Galleta suave con chispas de colores y sabor a pastel recién horneado.",
            "price": 55,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJF6wHdFmBQmzZjyVXkWlMuTKgN7H4w3ADeon2",
            "stock": 50
        },
        {
            "name": "Galleta Caramelo",
            "description": "Rica galleta con centro de caramelo suave. Una combinación de textura crujiente y relleno cremoso que encanta desde la primera mordida",
            "price": 65,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ2Etw7QUMhmyU4ZFQIYzaXxwAqo7OsCjT2Jip",
            "stock": 50
        },
        {
            "name": "Galleta Clasica",
            "description": "Nuestra receta tradicional. Una galleta simple, casera y deliciosa que nunca pasa de moda.",
            "price": 55,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJF6wHdFmBQmzZjyVXkWlMuTKgN7H4w3ADeon2",
            "stock": 50
        },
        {
            "name": "Galleta Cookies And Cream",
            "description": "Una irresistible mezcla de galleta crujiente y crema dulce. El clásico sabor de las galletas con leche, en una versión moderna.",
            "price": 65,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJT8V1VmFeXpZ0VndQysWbRwMr3zg8qJl7UYBG",
            "stock": 50
        },
        {
            "name": "Galleta Doble Chocolate",
            "description": "Hecha para verdaderos amantes del chocolate. Una explosión de sabor con chispas y masa de cacao puro.",
            "price": 69,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ9tLtgZ4ZvG02YokXQ3TCys16754wLpifcKbq",
            "stock": 50
        },
        {
            "name": "Galleta Gloria",
            "description": "Inspirada en el dulce mexicano tradicional. Esta galleta ofrece un sabor único, suave y lleno de tradición.",
            "price": 69,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJc17I2yv1Mg9ATxiRXkqCoYy38pZtna5wdIKF",
            "stock": 50
        },
        {
            "name": "Galleta Lotus",
            "description": "Galleta premium con pasta de Lotus Biscoff. Crujiente, caramelizada y con un toque especiado que enamora.",
            "price": 69,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJvNTbnGEFyALj20hBTYG6oJpKtwUuDmEcZ9fn",
            "stock": 50
        },
        {
            "name": "Galleta Nutella",
            "description": "Galleta rellena con abundante Nutella, ideal para los fanáticos del chocolate y la avellana. Cremosa por dentro, crocante por fuera.",
            "price": 69,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJBYsIzxhEJ9yA5kjLSoGwcNzD8utPOsenK3lx",
            "stock": 50
        },
        {
            "name": "Galleta Pistache",
            "description": "Galleta delicadamente elaborada con trozos de pistache natural. Su sabor suave y textura la hacen única.",
            "price": 65,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJr7O0xS8T9lQvPipB3eE7aMFJjq0tWz8Un1oH",
            "stock": 50
        },
        {
            "name": "Galleta Zanahoria",
            "description": "El sabor clásico de pastel de zanahoria en una galleta. Suave, especiada y con un toque casero inconfundible.",
            "price": 55,
            "type": "galleta",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJBWVqqzhEJ9yA5kjLSoGwcNzD8utPOsenK3lx",
            "stock": 50
        },
        {
            "name": "Pastel Chocolate",
            "description": "Pastel húmedo y esponjoso de chocolate, perfecto para los amantes del cacao. Ideal para celebrar o simplemente consentirse.",
            "price": 448,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ9yRYmh4ZvG02YokXQ3TCys16754wLpifcKbq",
            "stock": 50
        },
        {
            "name": "Pastel Frutos Rojos",
            "description": "Ligero y delicioso, con una mezcla de frutas rojas frescas. Una opción elegante para los que buscan un sabor afrutado y natural.",
            "price": 560,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJJYyPWWK7Ws0vQZKw1erdVgAh3qiUluNPjtF9",
            "stock": 50
        },
        {
            "name": "Pastel Guayaba",
            "description": "Sabor tradicional con un toque gourmet. El dulzor natural de la guayaba hace de este pastel una experiencia inolvidable.",
            "price": 519,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ8XDjeGFc6PuwxfTQ2F3mEK1WGCtpqaDhbAjv",
            "stock": 50
        },
        {
            "name": "Pastel Mostachon Fresa",
            "description": "Base crujiente con nueces, merengue y una capa generosa de fresas frescas. Un clásico mexicano reinventado.",
            "price": 420,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ5xnuEC0GpLWN6rgdyBIkVf7j9J8K0OncRA3b",
            "stock": 50
        },
        {
            "name": "Pastel Tortuga",
            "description": "Pastel con nueces, chocolate y caramelo, inspirado en el famoso dulce. Texturas y sabores que crean un bocado irresistible.",
            "price": 420,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJCDYV6haRD2xpYCMjg16l5yh7TLm9FBc8vzda",
            "stock": 50
        },
        {
            "name": "Pastel Tres Leches",
            "description": "Esponjoso pastel bañado en una mezcla de tres leches. Jugoso, dulce y perfecto para paladares que aman lo tradicional.",
            "price": 479,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJ846B1NFc6PuwxfTQ2F3mEK1WGCtpqaDhbAjv",
            "stock": 50
        },
        {
            "name": "Pastel Vainilla",
            "description": "Ligero, suave y con el delicado sabor de la vainilla. Perfecto como base para personalizar o disfrutar tal cual.",
            "price": 420,
            "type": "pastel",
            "imageUrl": "https://dzqckxx2le.ufs.sh/f/mXAqxtV2FlGJmMFX9CV2FlGJt73OkKRdrcgxsZvVpNQz1L4S",
            "stock": 50
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
