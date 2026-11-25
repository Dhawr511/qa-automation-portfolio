import pytest
import requests

@pytest.fixture(scope="module")
def post_response(base_url, payload):
    return requests.post(base_url + "/posts", json=payload)

def test_post_code(post_response):
    assert post_response.status_code == 201

def test_post_payload(post_response, payload):
    response = post_response.json()


    assert response["title"] == payload["title"]
    assert response["body"] == payload["body"]

def test_post_has_id(post_response):
    assert "id" in post_response.json()
