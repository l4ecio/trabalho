import pytest

def test_create_user(client):
    response = client.post("/users", json={"name": "João", "email": "joao@email.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "João"
    assert data["email"] == "joao@email.com"

@pytest.mark.parametrize("name,email", [
    ("Maria", "maria@email.com"),
    ("Carlos", "carlos@email.com"),
])
def test_create_multiple_users(client, name, email):
    response = client.post("/users", json={"name": name, "email": email})
    assert response.status_code == 201
    assert response.json()["email"] == email

def test_get_users(client):
    client.post("/users", json={"name": "Aline", "email": "aline@email.com"})
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 1

@pytest.mark.skip(reason="Validação de e-mail inválido ainda não implementada")
def test_create_user_invalid_email(client):
    response = client.post("/users", json={"name": "Test", "email": "invalid-email"})
    assert response.status_code == 422