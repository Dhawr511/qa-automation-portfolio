import pytest

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def payload():
    return {"title": "put i delete test", "body": "to jest test api", "userId": 1}