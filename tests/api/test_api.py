import pytest
import requests

@pytest.fixture(scope="module")
def response(base_url):
    return requests.get(base_url +"/posts/1")

@pytest.fixture()
def data(response):
    return response.json()

@pytest.mark.parametrize("post_id", [1, 2, 3], ids=["post1", "post2", "post3"])
def test_post_exists(base_url, post_id):
    response = requests.get(base_url + f"/posts/{post_id}")

    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_get_post_status_code(response):
    assert response.status_code == 200


def test_check_content(data):
    assert data["userId"] == 1
    assert data["id"] == 1

def test_check_structure(data):
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_not_found(base_url):
    response_failed = requests.get(base_url+"/posts/99999")
    assert response_failed.status_code == 404