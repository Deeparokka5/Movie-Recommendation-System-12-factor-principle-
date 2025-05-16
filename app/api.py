from fastapi import FastAPI
from app.recommend import Recommender
import config

app = FastAPI(title="Movie Recommender API", version="1.0")

recommender = Recommender(config.Config.MOVIE_DATA_PATH)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}

@app.get("/recommend/{title}")
def recommend(title: str):
    try:
        results = recommender.get_recommendations(title)
        return {"title": title, "recommendations": results}
    except KeyError:
        return {"error": f"Movie '{title}' not found in database."}