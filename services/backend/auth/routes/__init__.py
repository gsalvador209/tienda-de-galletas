from flask import Blueprint, request, jsonify, abort
from config.auth0 import requires_auth
from models.user import User, db
from models.product import Product, db
from extensions import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods = ['POST'])
def register():
    data = request.get_json() or {}
    
    required_fields = ["email", "name", "password"]
    missing = [field for field in required_fields if field not in data]
    
    if missing:
        abort(400, description="Bad request")
    
    user = User.query.filter_by(email=data["email"]).first()
    
    if user:
        abort(409, description="El correo electrónico ya está en uso")
    
    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    new_user = User(
        password=hashed_pw, 
        email=data["email"], 
        name=data["name"],
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.to_dict()), 201

@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    
    required_fields = ["email", "password"]
    missing = [field for field in required_fields if field not in data]
    
    if missing:
        abort(400, description="Bad request")
        
    user = User.query.filter_by(email=data["email"]).first()
    
    if not user:
        abort(401, description="Credenciales inválidas")
        
    isPwValid = bcrypt.check_password_hash(user.password, data["password"])
    
    if not isPwValid:
        abort(401, description="Credenciales inválidas")

    user_session = {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
    
    return jsonify(user_session)

@auth_bp.route('/profile', methods = ['GET'])
@requires_auth
def profile():
    #Autenticacion exitosa
    return jsonify({'user':'datos de perfil'})