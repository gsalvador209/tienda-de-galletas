# Fabricador de la app
from dotenv import load_dotenv
load_dotenv()


from flask import Flask
from config.database import init_db
from products.routes import products_bp
from auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env() #Lee variables que empiezan con FLASK
    init_db(app)

    #Registro de blueprints
    app.register_blueprint(products_bp, url_prefix = '/products')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def health():
        return {'status', 'OK'}
    
    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=5000)