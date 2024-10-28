import pytest
import requests

# JSONPlaceholder API URL
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture
def sample_data():
    return {
        "title": "Sample Title",
        "body": "Sample body content",
        "userId": 1
    }


def test_get_request():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of posts


def test_post_request(sample_data):
    response = requests.post(BASE_URL, json=sample_data)
    assert response.status_code == 201  # 201 Created
    assert response.json().get("title") == sample_data["title"]


def test_put_request(sample_data):
    post_id = 1  # ID of the resource to update
    response = requests.put(f"{BASE_URL}/{post_id}", json=sample_data)
    assert response.status_code == 200
    assert response.json().get("title") == sample_data["title"]


def test_patch_request():
    post_id = 1  # ID of the resource to partially update
    partial_data = {"title": "Updated Title"}
    response = requests.patch(f"{BASE_URL}/{post_id}", json=partial_data)
    assert response.status_code == 200
    assert response.json().get("title") == "Updated Title"


def test_delete_request():
    post_id = 1  # ID of the resource to delete
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
