import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()  # carga .env de services/backend

from config.database import db, init_db, DATABASE_URI
from products.routes import products_bp
from users.routes    import users_bp
from auth.routes import auth_bp
from extensions import bcrypt

def create_app():
    app = Flask(__name__)

    # 1) Configuración de SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 2) Registra la extensión
    db.init_app(app)

    # 3) Otras extensiones
    bcrypt.init_app(app)
    if os.getenv("ENABLE_CORS", "true").lower() == "true":
        CORS(app, origins=[os.getenv("FRONTEND_URL")])

    # 4) Crea tablas pero **no** si ya existen
    init_db(app)

    # 5) Blueprints
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(auth_bp,     url_prefix="/auth")
    app.register_blueprint(users_bp,    url_prefix="/users")

    @app.route("/")
    def health():
        return {"status": "OK"}

    return app

# Exportar la instancia de flask para uvicorn
app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
