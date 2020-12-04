import pandas as pd

def movies_genres():
    genre_cols = ["Animation", "Children's", 
           'Comedy', 'Adventure', 'Fantasy', 'Romance', 'Drama',
           'Action', 'Crime', 'Thriller', 'Horror', 'Sci-Fi', 'Documentary', 'War',
           'Musical', 'Mystery', 'Film-Noir', 'Western']

    genre_and_title_cols = ['title'] + genre_cols 
    return genre_and_title_cols 


def get_movie_id(movies :pd.DataFrame, title, year=None):
    #print((movies['title'] == title))
    res = movies[(movies['title'] == title)]
    if year:
        res = res[(res['year'] == year)]

    if len(res) > 1:
        print("Ambiguous: found")
        print(f"{res['title']} {res['year']}")
    elif len(res) == 0:
        print('not found')
    else:
        return res.index[0]

def get_movie_name(movies, index):
    return movies.iloc[index].title

def get_movie_year(movies, index):
    return movies.iloc[index].year

