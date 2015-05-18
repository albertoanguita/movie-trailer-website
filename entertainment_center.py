# This module contains the definition of the movies that will be displayed
# in the website. There are 6 movies defined.

import fresh_tomatoes
import media


# This block of code fines the six movies for the web application
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter",
                        1995)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Cameron",
                     2009)
interstellar = media.Movie("Interstellar",
                           "Astronauts must find a planet for humanity to survive",
                           "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                           "Christopher Nolan",
                           2014)
fargo = media.Movie("Fargo",
                    "A man hires two criminals to kidnap his wife and receive her father's ransom",
                    "http://www.elpelicultista.com/wp-content/uploads/2014/08/fargo-poster.jpg",
                    "https://www.youtube.com/watch?v=EB4PmbfG4bw",
                    "Joel & Ethan Coen",
                    1996)
casino_royale = media.Movie("Casino Royale",
                            "James Bond plays poker against a terrorist",
                            "http://www.impawards.com/2006/posters/casino_royale_ver3.jpg",
                            "https://www.youtube.com/watch?v=36mnx8dBbGE",
                            "Martin Campbell",
                            2006)
memento = media.Movie("Memento",
                      "A man cannot remember more than a couple of minutes of his life",
                      "http://upload.wikimedia.org/wikipedia/bn/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0",
                      "Christopher Nolan",
                      2000)
movies = [toy_story, avatar, interstellar, fargo, casino_royale, memento]

# the defined list of movies is used to initialize the application and
# generate the website
fresh_tomatoes.open_movies_page(movies)