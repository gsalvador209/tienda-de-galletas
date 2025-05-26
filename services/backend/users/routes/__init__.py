# services/backend/users/routes/__init__.py

"""
Blueprint 'users_bp' — CRUD de usuarios.
Rutas:
  GET    /users/           -> Listar usuarios
  GET    /users/<int:id>/  -> Obtener usuario por ID
  POST   /users/           -> Crear un usuario nuevo
  PUT    /users/<int:id>/  -> Actualizar un usuario existente
  DELETE /users/<int:id>/  -> Eliminar un usuario
"""

from flask import Blueprint, request, jsonify, abort
from werkzeug.security import generate_password_hash
from datetime import datetime

from config.database import db
from models.user import User

# Creamos el blueprint, desactivando strict_slashes para aceptar /users y /users/
users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def list_users():
    """
    GET /users/
    Recupera todos los usuarios.
    """
    users = User.query.all()
    # Serializamos manualmente para no exponer atributos internos
    data = [{
        "id":         u.id,
        "email":      u.email,
        "name":       u.name,
        "role":       u.role,
        "created_at": u.created_at.isoformat()
    } for u in users]
    return jsonify(data), 200

@users_bp.route("/<int:user_id>/", methods=["GET"])
def get_user(user_id):
    """
    GET /users/<id>/
    Recupera un solo usuario o 404 si no existe.
    """
    u = User.query.get_or_404(user_id)
    return jsonify({
        "id":         u.id,
        "email":      u.email,
        "name":       u.name,
        "role":       u.role,
        "created_at": u.created_at.isoformat()
    }), 200

@users_bp.route("/", methods=["POST"])
def create_user():
    """
    POST /users/
    Crea un usuario nuevo. Espera JSON con 'email','password','name','role'.
    """
    data = request.get_json() or {}
    # Validación mínima de campos requeridos
    for field in ("email", "password", "name", "role"):
        if field not in data:
            abort(400, description=f"Falta campo requerido '{field}'")

    # Hasheamos contraseña y creamos instancia
    hashed = generate_password_hash(data["password"])
    new_user = User(
        email      = data["email"],
        password   = hashed,
        name       = data["name"],
        role       = data["role"],
        created_at = datetime.now(datetime.timezone.utc)
    )
    db.session.add(new_user)
    db.session.commit()

    # Devolvemos la representación mínima
    return jsonify({
        "id":         new_user.id,
        "email":      new_user.email,
        "name":       new_user.name,
        "role":       new_user.role,
        "created_at": new_user.created_at.isoformat()
    }), 201

@users_bp.route("/<int:user_id>/", methods=["PUT"])
def update_user(user_id):
    """
    PUT /users/<id>/
    Actualiza un usuario. Se pueden enviar 'email','password','name','role'.
    """
    u = User.query.get_or_404(user_id)
    data = request.get_json() or {}

    # Actualizamos solo los campos presentes
    if "email" in data:
        u.email = data["email"]
    if "name" in data:
        u.name = data["name"]
    if "role" in data:
        u.role = data["role"]
    if "password" in data:
        u.password = generate_password_hash(data["password"])

    db.session.commit()
    return jsonify({
        "id":         u.id,
        "email":      u.email,
        "name":       u.name,
        "role":       u.role,
        "created_at": u.created_at.isoformat()
    }), 200

@users_bp.route("/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    """
    DELETE /users/<id>/
    Elimina un usuario o retorna 404 si no existe.
    """
    u = User.query.get_or_404(user_id)
    db.session.delete(u)
    db.session.commit()
    # 204 No Content es semánticamente correcto para borrados
    return "", 204
