""" This module stores and displays movie related info. """
import webbrowser

class Movie():
    """Class to store & display movie related info.

    Attributes:
        title(string)            Movies's title.
        storyline(string)        Movie's storyline.
        poster_image_url(string) URL of the movie's poster image.
        trailer_youtube_url      URL of the movie's youtube trailer.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Intitialize instance variables
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Play the movie's trailer. """
        webbrowser.open(self.trailer_youtube_url)
