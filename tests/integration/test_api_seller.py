from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_seller_by_product_id_success():
    response = client.get("/sellers/by-product/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "seller123"
    assert "products" in data
