from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app


@pytest.fixture
def client():
    return TestClient(app.app)


@pytest.fixture(autouse=True)
def restore_activities():
    original_activities = deepcopy(app.activities)
    yield
    app.activities.clear()
    app.activities.update(original_activities)