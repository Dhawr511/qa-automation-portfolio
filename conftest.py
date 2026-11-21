import pytest
import requests


@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def response(base_url):
    requests.get(base_url + "/posts/1")
    return response