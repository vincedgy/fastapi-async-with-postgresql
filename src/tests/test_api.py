from src import __version__

import requests


def test_version():
    """Test version"""
    assert __version__ == '0.1.0'


def test_get_notes():
    """Request notes"""
    response = requests.get("http://localhost:5000/notes")
    assert response.status_code == 200
