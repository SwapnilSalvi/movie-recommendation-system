def create_matrix(data):
    movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
    return movie_matrix