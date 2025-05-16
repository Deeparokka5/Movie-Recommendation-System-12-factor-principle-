# 🎬 Movie Recommendation System

A simple movie recommendation system built using **FastAPI**, **Streamlit**, and **content-based filtering** using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata ).

This app gives content-based recommendations for movies by analyzing titles, overviews, and keywords using **TF-IDF** and **cosine similarity**.

---

## Features

- RESTful API via FastAPI with Swagger UI
- Web UI using Streamlit
- Content-based recommendations
- Unit tested with `pytest`
- Configurable via `.env` environment variables
- Containerized with Docker
- Includes pre-commit hooks for code formatting (`black`, `flake8`)

---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Deeparokka5/movie-recommender.git 
cd movie-recommender
```

###  How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Backend
```bash
uvicorn app.api:app --reload
```

### Start Streamlit frontend
```bash
streamlit run streamlit/ui.py
```

### Build and run docker 
```bash
docker build -t movie-recommender .
docker run -p 8000:8000 movie-recommender
```

### Tests
```bash
pytest tests/test_api.py -v```
```

![image](https://github.com/user-attachments/assets/186389b0-d29e-4470-bc95-77deb2030390)
![image](https://github.com/user-attachments/assets/c8464f1a-8c56-45c3-b107-57113b0f03da)
![image](https://github.com/user-attachments/assets/97a1b671-9f7d-44da-a9c9-bc0e02f7709b)


