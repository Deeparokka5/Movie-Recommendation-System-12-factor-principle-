import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.df['overview'] = self.df['overview'].fillna('')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['overview'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        self.indices = pd.Series(self.df.index, index=self.df['title']).drop_duplicates()

    def get_recommendations(self, title, top_n=5):
        idx = self.indices[title]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        movie_indices = [i[0] for i in sim_scores[1:top_n+1]]
        return self.df[['title', 'overview']].iloc[movie_indices].to_dict('records')