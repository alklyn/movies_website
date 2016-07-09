import webbrowser

class Movie():
    """
    Class to store & display movie related info
    """
    pass

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
        webbrowser.open(self.trailer_youtube_url)
