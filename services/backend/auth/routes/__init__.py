from flask import Blueprint, request, jsonify
from config.auth0 import requires_auth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods = ['POST'])
def register():
    #Redirige a Auth0
    return jsonify({'msg':'registro OK'})

@auth_bp.route('/login', methods = ['POST'])
def login():
    #Inicia el flujo de OAuth
    return jsonify({'msg':'login OK'})

@auth_bp.route('/profile', methods = ['GET'])
@requires_auth
def profile():
    #Autenticacion exitosa
    return jsonify({'user':'datos de perfil'})