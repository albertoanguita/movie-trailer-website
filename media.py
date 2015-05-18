# This module defines the class for a movie

import webbrowser

class Movie():
    """This class provides a way to store movie related information.

    Two new instance variables have been added to the class, with respect to
    those shown in the videos: director and release_year. The formed stores the
    movie director, while the latter stores the year in which the movie was
    released.
    """

    # This class variable is commented, since it is not used accross the project
    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster, trailer, director, year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.director = director
        self.release_year = year

    def show_trailer(self):
        """Opens the trailer page."""

        webbrowser.open(self.trailer_youtube_url)