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
        token = request.headers.get('Authorization', None)
        # aquí validas el JWT con jose
        return f(*args, **kwargs)
    return decorated
