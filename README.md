# QA Pytest practice     
Tests of sample odd even counter function and REST API tests

## What is tested
- Simple counter of odd and even numbers that takes list as argument
- REST API "https://jsonplaceholder.typicode.com"
- DELETE, PUT, POST, GET methods
- positive tests asserting correct response codes and body
- negative tests in operations on non-existing resources
- unit tests of counter function checking functionality with positive numbers, negative numbers and zeros

## Tech stack
- Python
- pytest
- pytest fixtures
- pytest parametrize
- requests

## How to run
- API tests require internet access
- open terminal in designated folder
```
# For Windows
git clone https://github.com/Dhawr511/qa-automation-portfolio
cd qa-automation-portfolio
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v


# For macOS / linux
git clone https://github.com/Dhawr511/qa-automation-portfolio
cd qa-automation-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Notes
JSONPlaceholder only simulates saving so it returns code 200 for DELETE method on non-existing resource. In real scenario it would return 204 or 404