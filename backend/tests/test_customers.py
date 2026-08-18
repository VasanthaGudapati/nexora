from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_create_customer():
    """Test creating a customer successfully with valid data."""
    payload = {
        "name": "Alice Smith",
        "email": "alice@example.com"
    }
    response = client.post("/api/v1/customers", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Alice Smith"
    assert data["email"] == "alice@example.com"


def test_get_customers():
    """Test retrieving the list of customers."""
    response = client.get("/api/v1/customers")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_create_multiple_customers():
    """Test creating multiple customers and verify unique generated IDs."""
    payload_1 = {
        "name": "Charlie Brown",
        "email": "charlie@example.com"
    }
    payload_2 = {
        "name": "Diana Prince",
        "email": "diana@example.com"
    }

    response_1 = client.post("/api/v1/customers", json=payload_1)
    response_2 = client.post("/api/v1/customers", json=payload_2)

    assert response_1.status_code == 201
    assert response_2.status_code == 201

    cust_1 = response_1.json()
    cust_2 = response_2.json()

    assert cust_1["id"] != cust_2["id"]
    assert cust_2["id"] > cust_1["id"]
    assert cust_1["name"] == "Charlie Brown"
    assert cust_2["name"] == "Diana Prince"


def test_create_customer_missing_email():
    """Test validation failure when the required email field is missing."""
    payload = {
        "name": "Invalid Customer"
    }
    response = client.post("/api/v1/customers", json=payload)
    assert response.status_code == 422


def test_create_customer_invalid_email_type():
    """Test validation failure when email has an invalid data type."""
    payload = {
        "name": "Invalid Customer",
        "email": None
    }
    response = client.post("/api/v1/customers", json=payload)
    assert response.status_code == 422
