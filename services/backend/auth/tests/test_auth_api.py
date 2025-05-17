import os
import pytest
from app import create_app
from extensions import bcrypt
from config.database import db
from models.user import User

TEST_USER_PASSWORD = 'test123'

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
def seeded_users(app):
    #Inserción de dos usuarios
    pw = bcrypt.generate_password_hash(TEST_USER_PASSWORD).decode("utf-8")
    users = [
      User(password=pw, email="test@mail.com", name="Juan"),
      User(password=pw, email="test2@mail.com", name="Ale")
    ]

    #1.Se abre el contexto de la app
    with app.app_context():
        # 2. Se reconstrute el esquema de cero
        db.drop_all()
        db.create_all()
        # 3. Se añade y confirma
        db.session.add_all(users)
        db.session.commit()
        # 4. Se hace yield para que la sesion siga viva durante los tests
        yield users

        # 5. Cuando termina el yield se limpia la sesion
        db.session.remove()
        db.drop_all()

    return users
  
  
def test_login_success(client, seeded_users):
  user = seeded_users[0].to_dict()
  login_payload = {
    "email": user["email"],
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/login', json=login_payload)
  assert res.status_code == 200
  
  res_json = res.get_json()
  assert res_json["id"] == user["id"]
  assert res_json["name"] == user["name"]
  assert res_json["email"] == user["email"]

def test_login_failed_wrong_pw(client, seeded_users):
  user = seeded_users[0].to_dict()
  login_payload = {
    "email": user["email"],
    "password": "test1234"
  }
  res = client.post('/auth/login', json=login_payload)
  assert res.status_code == 401
  
def test_login_failed_nonexistent_email(client):
  login_payload = {
    "email": "wrong@test.com",
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/login', json=login_payload)
  assert res.status_code == 401
  
def test_login_failed_bad_request_email(client):
  login_payload = {
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/login', json=login_payload)
  assert res.status_code == 400
  
def test_login_failed_bad_request_pw(client):
  login_payload = {
    "email": "wrong@test.com",
  }
  res = client.post('/auth/login', json=login_payload)
  assert res.status_code == 400
  
def test_register_success(client):
  test_name = "Manuel"
  test_email = "test3@mail.com"
  register_payload = {
    "name": test_name,
    "email": test_email,
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/register', json=register_payload)
  assert res.status_code == 201
  
  res_json = res.get_json()
  assert res_json["name"] == test_name
  assert res_json["email"] == test_email
  
def test_register_failed_email_collision(client, seeded_users):
  test_name = "Manuel"
  test_email = "test@mail.com"
  register_payload = {
    "name": test_name,
    "email": test_email,
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/register', json=register_payload)
  assert res.status_code == 409
  
  
def test_register_failed_bad_request_name(client):
  test_email = "test@mail.com"
  register_payload = {
    "email": test_email,
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/register', json=register_payload)
  assert res.status_code == 400
  
    
def test_register_failed_bad_request_email(client):
  test_name = "Manuel"
  register_payload = {
    "name": test_name,
    "password": TEST_USER_PASSWORD
  }
  res = client.post('/auth/register', json=register_payload)
  assert res.status_code == 400
  
def test_register_failed_bad_request_pw(client):
  test_name = "Manuel"
  test_email = "test@mail.com"
  register_payload = {
    "name": test_name,
    "email": test_email,
  }
  res = client.post('/auth/register', json=register_payload)
  assert res.status_code == 400