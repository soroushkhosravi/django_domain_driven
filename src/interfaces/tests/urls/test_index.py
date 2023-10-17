"""Tests related to the index endpoint."""
from django.test import Client

def test_index_returns_expected_response(client):
    """Tests we can  get expected response from the index endpoint."""
    response = client.get("/src/index")
    assert response.status_code == 200
    assert response.content == b'<h1>This is passed foo value: bar.</h1>'