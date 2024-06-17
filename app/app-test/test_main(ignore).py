import os
import sys
import pytest
from pymongo import MongoClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.Backend.main import app

TEST_MONGO_URI = 'mongodb://mongo-service.mongo-namespace:27017/rc_recommunity'

@pytest.fixture
def client():
    app.testing = True
    app.config['MONGO_URI'] = TEST_MONGO_URI
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    # Set up the MongoDB test database connection
    client = MongoClient(TEST_MONGO_URI)
    db = client.get_database()
    users_collection = db.users
    
    yield
    users_collection.delete_many({})

def test_registration(client):
    registration_data = {
        'full_name': 'Test Guy',
        'email': 'Test@gmail.com',
        'password': '123',
        'DB': '01/01/2000'
    }
    print("Your Registration Data:", registration_data)

    response = client.post('/register', data=registration_data, content_type='application/x-www-form-urlencoded')

    # Print response status code and headers
    print("Registration Response Status Code:", response.status_code)
    print("Registration Response Headers:", response.headers)

    # Check if registration was successful
    assert response.status_code == 302  # Expecting a redirect status code
    assert response.headers['Location'] == '/login'  # Ensure it redirects to the relative login page

def test_registration_another_user(client):
    registration_data = {
        'users': 'Test2',
        'email': 'test2@gmail.com',
        'password': '123',
        'DB': '01/01/2000'
    }

    response = client.post('/register', data=registration_data)

    # Check if registration worked
    assert response.status_code == 302
    assert response.headers['Location'] == '/login' #moves to login page

    client = MongoClient(TEST_MONGO_URI)
    db = client.get_database()
    user = db.users.find_one({'email': 'anotheruser@example.com'})
    assert user is not None
    assert user['users'] == 'Another User'
    assert user['email'] == 'anotheruser@example.com'
    assert user['password'] == '123'
    assert user['DB'] == '01/01/2000'
