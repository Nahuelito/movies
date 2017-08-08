import webbrowser


class Movie():
    """This is the documentation of Movie Class.
       It describes a Movie"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """It initializes the movie title, storyline,
           poster image and Youtube trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens up the YouTube link on the browser"""
        webbrowser.open(self.trailer_youtube_url)
