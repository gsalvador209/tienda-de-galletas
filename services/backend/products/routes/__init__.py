from flask import Blueprint, request, jsonify, abort
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

@products_bp.route('/<init:id>', methods = ['PUT'])
def update_product(id):
    """
    Actualiza un producto existente.
    """
    product = Product.query.get(id)
    if not product:
        abort(404, description= f"El producto con id {id} no fue encontrado")
    
    data = request.get_json() or {}

    updatable_fields = ['name', 'description', 'price', 'stock', 'image_url']
    for field in updatable_fields:
        if field in data:
            setattr(product, field, data[field])
    
    db.session.commit()

    return jsonify(product.to_dict()), 200

@products_bp.route('/<int:id>', methods = ['DELETE'])
def delete_product(id):
    """
    Elimina un producto existente.
    """
    product = Product.query.get(id)
    if not product:
        abort(404, description= f"El producto con id {id} no fue encontrado")
    
    db.session.delete(product)

    db.session.commit()

    return '', 204



