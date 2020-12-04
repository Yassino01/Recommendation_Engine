import pandas as pd
import numpy as np
from movies import movies_genres,get_movie_id,get_movie_name,get_movie_year




def get_most_similar(movies,similarity, movie_name, year=None, top=10):
    
    index_movie = get_movie_id(movies, movie_name, year)
    best = similarity[index_movie].argsort()[::-1]
    return [(ind, get_movie_name(movies, ind), similarity[index_movie, ind]) for ind in best[:top]]

def get_recommendations(movies,ratings,user_id,similarity):
    
    top_movies = ratings[ratings['user_id'] == user_id].sort_values(by='rating', ascending=False).head(3)['movie_id']
    index=['movie_id', 'title', 'similarity']

    most_similars = []
    for top_movie in top_movies:
        most_similars += get_most_similar(movies,similarity, get_movie_name(movies, top_movie), get_movie_year(movies, top_movie))

    return pd.DataFrame(most_similars, columns=index).drop_duplicates().sort_values(by='similarity', ascending=False).head(5)


