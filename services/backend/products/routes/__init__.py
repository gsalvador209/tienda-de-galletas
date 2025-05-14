from flask import Blueprint, request, jsonify
from models.product import Product, db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods= ['GET'])
def list_products():
    prods = Product.query.all()
    return jsonify([p.to_dict() for p in prods]) #Devuelve un arreglo JSON de todos


@products_bp.route('/', methods = ['POST']) #crea el producto
def create_product():
    data = request.json
    p = Product(**data)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict()), 201

#Poner el PUT y el DELETE