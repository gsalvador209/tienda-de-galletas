import os
from jose import jwt
from functools import wraps
from flask import request, jsonify

AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
API_AUDIENCE = os.getenv('AUTH0_AUDIENCE')
ALGORITHMS = ["RS256"]

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        #Bypass la autenticación
        if os.getenv("DISABLE_AUTH","false").lower() == "true":
            return f(*args, **kwargs)
        
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"msg": "Missing Authorization Header"}), 401

        token = auth_header.split()[1]
        
        #Payload (no se que sea eso)

        return f(*args, **kwargs)


    return decorated
