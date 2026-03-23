import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def train_collaborative(movie_matrix):
    matrix_filled = movie_matrix.fillna(0)
    cosine_sim = cosine_similarity(matrix_filled.T)

    cosine_df = pd.DataFrame(cosine_sim,
                             index=movie_matrix.columns,
                             columns=movie_matrix.columns)

    pickle.dump(cosine_df, open('models/cosine.pkl', 'wb'))

    return cosine_df


def train_content(movies):
    cv = CountVectorizer(tokenizer=lambda x: x.split('|'))
    genre_matrix = cv.fit_transform(movies['genres'])

    genre_sim = cosine_similarity(genre_matrix)

    genre_df = pd.DataFrame(genre_sim,
                            index=movies['title'],
                            columns=movies['title'])

    pickle.dump(genre_df, open('models/genre.pkl', 'wb'))

    return genre_df