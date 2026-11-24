import requests
import pytest

@pytest.mark.parametrize("post_id", [0, -1, 99999, "abc"], ids=["zero", "negative", "non_existent", "wrong_type"])
def test_get_invalid_post(base_url, post_id):
    response = requests.get(base_url + f"/posts/{post_id}")
    assert response.status_code == 404


def test_non_existent_put(base_url, payload):
    response = requests.put(base_url + "/posts/99999", json=payload)
    assert response.status_code == 404

def test_non_existent_delete(base_url):
    response = requests.delete(base_url + "/posts/99999")
    assert response.status_code == 200
    # testowe api zwraca 200 ale prawdziwe zwróciłoby 404 albo 204