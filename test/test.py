import pytest
from fastapi.testclient import TestClient
from app.api import app
from config import Config
from app.recommend import Recommender

# Initialize test client
client = TestClient(app)

# Ensure recommender loads dataset
@pytest.fixture(scope="module")
def recommender():
    return Recommender(Config.MOVIE_DATA_PATH)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_recommend_existing_movie(recommender):
    sample_title = recommender.df.iloc[0]['title']
    response = client.get(f"/recommend/{sample_title}")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "recommendations" in data
    assert len(data["recommendations"]) > 0

def test_recommend_nonexistent_movie():
    response = client.get("/recommend/ThisMovieDoesNotExist12345")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data