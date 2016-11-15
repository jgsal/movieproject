import tmdbsimple as tmdb

tmdb.API_KEY = '350a49206a5b6ce33466613951bb2e88'


def movie_call(movie_id):
    '''Get Movie Data from API'''
    movieselect = tmdb.Movies(movie_id)
    append_trailers = {'append_to_response': 'trailers'}
    movie_info = (movieselect.info(**append_trailers)
                  .get('trailers').get('youtube'))
    first_trailer = movie_info[0].get('source')
    poster_src = movieselect.poster_path
    youtube_url = 'https://www.youtube.com/watch?v=' + first_trailer
    poster_url = 'http://image.tmdb.org/t/p/w185' + poster_src
    return movieselect.title, movieselect.overview, poster_url, youtube_url
