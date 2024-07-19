import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_home_page(client):
    "Test the home page"
    response = client.get('/')
    assert response.status_code == 200