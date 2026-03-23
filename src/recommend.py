def recommend_hybrid(movie_name, cosine_df, genre_df, w1=0.7, w2=0.3):
    if movie_name not in cosine_df.columns:
        return []

    collab = cosine_df[movie_name]
    content = genre_df[movie_name]

    hybrid = (w1 * collab) + (w2 * content)

    return hybrid.sort_values(ascending=False).iloc[1:11]