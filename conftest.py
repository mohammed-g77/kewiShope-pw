import pytest
import json
import os

@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON file."""
    data_path = os.path.join(os.path.dirname(__file__), "data", "users.json")
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)

@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application."""
    return "https://kewi.ps"
