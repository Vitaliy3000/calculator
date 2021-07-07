import sys
sys.path.append("./src")

from fastapi.testclient import TestClient
import pytest

from src.main import app


@pytest.fixture()
def client():
    return TestClient(app)
