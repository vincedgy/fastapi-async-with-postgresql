from src import __version__

import requests


def test_version():
    """Test version"""
    assert __version__ == '0.1.0'


def test_create_note():
    """Request to create one note"""
    response = requests.post("http://localhost:5000/notes", json={"text": "test", "completed": "false"})
    assert response.status_code == 200


def test_known_note():
    """Request  one note"""
    response = requests.get("http://localhost:5000/notes/1")
    assert response.status_code == 200


def test_get_all_notes():
    """Request notes"""
    response = requests.get("http://localhost:5000/notes/all")
    assert response.status_code == 200


def test_update_note():
    """Request to update one note"""
    response = requests.put("http://localhost:5000/notes/1", json={"text": "test", "completed": "false"})
    assert response.status_code == 200


def test_get_notes():
    """Request notes"""
    response = requests.get("http://localhost:5000/notes")
    assert response.status_code == 200


def test_get_notes_with_pagination():
    """Request notes"""
    response = requests.get("http://localhost:5000/notes?take=5")
    print(response.json())
    assert response.status_code == 200


def test_delete_note():
    """Request to delete one note"""
    response = requests.delete("http://localhost:5000/notes/1")
    assert response.status_code == 200


def test_unknown_note():
    """Request  one note"""
    response = requests.get("http://localhost:5000/notes/1")
    assert response.status_code == 404


def test_create_another_note():
    """Request to create another note"""
    response = requests.post("http://localhost:5000/notes", json={"text": "Another test", "completed": "true"})
    assert response.status_code == 200


def test_get_one_note():
    """Request one note"""
    response = requests.get("http://localhost:5000/notes/2")
    assert response.status_code == 200
