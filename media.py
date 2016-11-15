import webbrowser
# style guide class name should be first initial capital


class Movie():
    # documentation for class movie
    """This class provides a way to store movie related information"""
    # constant variables should be ALL CAPS
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''Memory Storage for Movie Data'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''Function for Viewing Trailer'''
        webbrowser.open(self.trailer_youtube_url)
