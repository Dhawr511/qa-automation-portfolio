import pytest
import requests




@pytest.fixture(scope="module")
def put_response(base_url, payload):
    return requests.put(base_url + "/posts/1", json=payload)

@pytest.fixture(scope="module")
def delete_response(base_url, payload):
    return requests.delete(base_url + "/posts/1")

def test_put_returns_200(put_response, payload):

    assert put_response.status_code == 200

def test_put_return_equals_payload(put_response, payload):
    data = put_response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == 1

def test_delete_returns_200(delete_response):
    assert delete_response.status_code == 200
def test_delete_returns_empty_body(delete_response):
    assert delete_response.json() == {}