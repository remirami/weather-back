import pytest
from hello import hello

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_home_page(client):
    "Test the home page"
    response = client.get('/')
    assert response.status_code == 200