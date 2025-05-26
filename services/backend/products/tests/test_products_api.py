import os
import pytest
from app import create_app
from config.database import db
from models.product import Product
from models.product import ProductType

@pytest.fixture
def app():
    #Configuración de SQLite para pruebas y deshabilita el auth
    os.environ['DATABASE_URI'] = 'sqlite:///:memory:'
    os.environ['DISABLE_AUTH'] = 'true'

    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def seeded_products(app):
    #Inserción de dos productos pra GET, PUT y DELETE
    products = [
        Product(name = "Test A", type=ProductType.cupcake, description = "Desc A", price =1.0, stock = 10, image_url =  "urlA"),
        Product(name = "Test B", type=ProductType.galleta, description = "Desc B", price = 2.0, stock = 20, image_url = "urlB")
    ]

    #1.Se abre el contexto de la app
    with app.app_context():
        # 2. Se reconstrute el esquema de cero
        db.drop_all()
        db.create_all()
        # 3. Se añade y confirma
        db.session.add_all(products)
        db.session.commit()
        # 4. Se hace yield para que la sesion siga viva durante los tests
        yield products

        # 5. Cuando termina el yield se limpia la sesion
        db.session.remove()
        db.drop_all()

    return products

def test_get_products_empty(client):
    """ Checa si la db está vacía"""
    resp = client.get('/products/')
    assert resp.status_code == 200
    assert resp.get_json() == []

def test_get_products_with_data(client, seeded_products):
    """Obtiene los datos de los productos"""
    resp = client.get('/products/')
    data = resp.get_json()
    assert resp.status_code == 200 #Interrumpe si no hubo respuesta 200 del backend
    names = [p['name'] for p in data] # Descompone los nombres de los productos obtenidos
    #Se verifica que esten los que se están usando para testear
    assert "Test A" in names and "Test B" in names

def test_create_product(client):
    new_product = {
        "name" : "Cookie Test",
        "type" : ProductType.cupcake.value,
        "description" : "Deliciosamente a prueba",
        "price" : 333.33,
        "stock" : 777,
        "image_url" :"image"
    }

    resp = client.post("/products/", json = new_product)

    assert resp.status_code == 201 #Checa que se haya agregado correctamente
    created = resp.get_json()
    #Debe devolver el id asignado y los valores delcaraods originalmemte
    assert created['id'] is not None
    for key in new_product:
        assert created[key] == new_product[key]

def test_update_product(client, seeded_products):
    prod = seeded_products[1]
    update_data ={"price" : 0.99, "stock" : 0, "description" : "This product was updated"}
    resp = client.put(f"/products/{prod.id}", json = update_data)
    assert resp.status_code == 200
    updated = resp.get_json()
    assert updated['price'] == 0.99
    assert updated['stock'] == 0
    assert updated['description'] == "This product was updated"
    
    assert updated['name'] == prod.name

def test_update_nonexistent(client):
    resp = client.put('/products/9999', json={"name": "Nope"})
    assert resp.status_code == 404

def test_delete_product(client, seeded_products):
    prod = seeded_products[0]
    resp = client.delete(f'/products/{prod.id}')
    assert resp.status_code == 204

    #Probar que el get de error 404
    resp2 = client.get(f'/products/{prod.id}')
    assert resp2.status_code == 404

def test_delete_nonexisten(client):
    resp = client.delete('/products/9999')
    assert resp.status_code == 404