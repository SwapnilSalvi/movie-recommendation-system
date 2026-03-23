import streamlit as st
import pandas as pd
import pickle
from src.recommend import recommend_hybrid

movies = pd.read_csv('data/movies.csv')

cosine_df = pickle.load(open('models/cosine.pkl', 'rb'))
genre_df = pickle.load(open('models/genre.pkl', 'rb'))

st.title("🎬 Movie Recommendation System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    results = recommend_hybrid(selected_movie, cosine_df, genre_df)

    st.subheader("Top Recommendations:")
    for movie in results.index:
        st.write(movie)