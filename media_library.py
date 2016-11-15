# Import files must be in same folder
import fresh_tomatoes
import media
import tmdb_api

# Movie Class Instances
# Array for Top 6 Favorite Movies
movie_array = []
# Favorite movie list and Loop to gather movie information and store in array
movie_list = {2907, 127585, 140607, 10681, 31417, 153}
for x in movie_list:
    movie = tmdb_api.movie_call(x)
    movieitems = media.Movie(movie[0].encode('utf8'), movie[1].encode('utf8'),
                             movie[2].encode('utf8'), movie[3].encode('utf8'))
    movie_array.append(movieitems)

movies = [movie_array[5], movie_array[4], movie_array[3], movie_array[2],
          movie_array[1], movie_array[0]]
fresh_tomatoes.open_movies_page(movies)
