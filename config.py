import os

class Config:
    MOVIE_DATA_PATH = os.getenv("MOVIE_DATA_PATH", "data/tmdb_5000_movies.csv")
    PORT = int(os.getenv("PORT", 8000))