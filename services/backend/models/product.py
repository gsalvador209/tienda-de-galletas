#Modelo de lo que sería un producto

from datetime import datetime
from config.database import db
from sqlalchemy import Enum
import enum

class ProductType(enum.Enum):
    cupcake = "cupcake"
    galleta = "galleta"
    pastel = "pastel"
    
class Product(db.Model):
    __tablename__ = 'products' #Nombre de la tabla en MySQL

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False) 
    type = db.Column(Enum(ProductType, name="producttype"), nullable = False)
    description = db.Column(db.Text, nullable=True)         # Descripción opcional
    price = db.Column(db.Numeric(10, 2), nullable=False)    # Precio con 2 decimales
    stock = db.Column(db.Integer, default=0)                # Cantidad en inventario
    image_url = db.Column(db.String(),nullable=True)        # Imagen de referencia
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(),
        onupdate=datetime.now()
    )

    def to_dict(self):
        """Convierte el modelo a un dict para jsonify."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type.value,
            'description': self.description,
            'price': float(self.price),
            'stock': self.stock,
            'image_url' : self.image_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }