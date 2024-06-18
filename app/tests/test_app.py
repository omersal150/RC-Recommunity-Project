import sys
import os
import pytest
from flask import session  # Import the session object
from Backend.main import app, mongo  # Import the Flask app and MongoDB connection object

# Add the 'app' directory to the system path
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
sys.path.append(app_path)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = "mongodb://localhost:27017/test_rc_recommunity"
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database and collections
            mongo.db.users.drop()
            mongo.db.recyclable_items.drop()
            yield client
            
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_register_and_login(client):
    # Test registration
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful' in response.data

    # Test login
    response = client.post('/login', data={
        'username_or_email': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome' in response.data
    assert 'username' in session
    assert session['username'] == 'testuser'

def test_add_model(client):
    # First, register and log in
    client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    client.post('/login', data={
        'username_or_email': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Test adding a model
    response = client.post('/add_model', data={
        'media_link': 'http://example.com',
        'model_name': 'Test Model',
        'manufacture': 'Test Manufacture',
        'year_of_release': '2023',
        'description': 'Test Description',
        'pros_cons': 'Test Pros and Cons',
        'image_url_1': 'http://example.com/image1.jpg',
        'image_url_2': 'http://example.com/image2.jpg',
        'image_url_3': 'http://example.com/image3.jpg'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Model added successfully!' in response.data

def test_logout(client):
    client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    client.post('/login', data={
        'username_or_email': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Test logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert 'username' not in session
